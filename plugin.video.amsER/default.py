import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import urllib, urllib2
import re, string, sys, os
import urlresolver
from TheYid.common.addon import Addon
from TheYid.common.net import Net
from htmlentitydefs import name2codepoint as n2cp
import HTMLParser

addon_id = 'plugin.video.amsER'
plugin = xbmcaddon.Addon(id=addon_id)
DB = os.path.join(xbmc.translatePath("special://database"), 'amsER.db')
BASE_URL = 'http://www.all-movies-stream.com/'
net = Net()
addon = Addon('plugin.video.amsER', sys.argv)

###### PATHS ###########
AddonPath = addon.get_path()
IconPath = AddonPath + "/icons/"
FanartPath = AddonPath + "/icons/"

##### Queries ##########
mode = addon.queries['mode']
url = addon.queries.get('url', None)
content = addon.queries.get('content', None)
query = addon.queries.get('query', None)
listitem = addon.queries.get('listitem', None)
urlList = addon.queries.get('urlList', None)
section = addon.queries.get('section', None)
text = addon.queries.get('text', None)
img = addon.queries.get('img', None)
#\s*?#
################################################################################# Titles #################################################################################

def GetTitles(url, text):
    try:
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<li><a href="(.+?)" class="rightsidemenu genrefilma">(.+?)</a></li>').findall(content)
        for url, name in match:
                addon.add_directory({'mode': 'GetTitles1', 'url': 'http://www.all-movies-stream.com/' + url, 'listitem': listitem, 'text': name.strip()}, {'title': name.strip()}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
    except:
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetTitles1(url, text, img):
    try:
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('''<a href="/film/(.+?)" title="(.+?)stream - movie stream">\s*?<img src="(.+?)"''').findall(content)
        match1 = re.compile('''<li class="cursorpointer" onclick="window.location = '.+?'"><a href="(.+?)">&raquo;</a></li>''').findall(content)
        for url, name, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': 'http://www.all-movies-stream.com/film/' + url, 'listitem': listitem, 'text': name.strip(), 'img': img}, {'title': name.strip()}, img= img, fanart=FanartPath + 'fanart.jpg')
        for url in match1:
                addon.add_directory({'mode': 'GetTitles1', 'url': 'http://www.all-movies-stream.com' + url, 'listitem': listitem, 'text': url}, {'title': 'Next Page...'}, img= 'http://raumatiroadsurgery.co.nz/img/arrow.png', fanart=FanartPath + 'fanart.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
    except:
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))


def GetLinks(section, url, text, img):
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<iframe src="(.+?)"').findall(content)
        match1 = re.compile('<IFRAME SRC="(.+?)"').findall(content)
        match2 = re.compile('<iframe src="(http://uptostream.com/iframe/.+?)"').findall(content)
        listitem = GetMediaInfo(content)
        for url in match2:
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        addon.add_directory({'mode': 'PlayVideo', 'url': url.replace('http://uptostream.com/iframe/', 'http://uptobox.com/'), 'listitem': listitem}, {'title': 'uptobox.com' }, img= img, fanart=FanartPath + 'fanart.jpg')
        for url in match + match1:
                url = url.replace('/iframe/', '/')
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host }, img= img, fanart=FanartPath + 'fanart.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))


def PlayVideo(url, listitem):
    try:
        print 'in PlayVideo %s' % text
        stream_url = urlresolver.HostedMediaFile(url).resolve()
        xbmc.Player().play(stream_url)
        addon.add_directory({'mode': 'help'}, {'title':  '[COLOR slategray][B]^^^ Press back ^^^[/B] [/COLOR]'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.jpg')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry Link may have been removed ![/B][/COLOR],[COLOR lime][B]Please try a different link/host !![/B][/COLOR],7000,"")")

def GetDomain(url):
        tmp = re.compile('//(.+?)/').findall(url)
        domain = 'Unknown'
        if len(tmp) > 0 :
            domain = tmp[0].replace('www.', '')
        return domain

def GetMediaInfo(html):
        listitem = xbmcgui.ListItem()
        match = re.search('og:title" content="(.+?) \((.+?)\)', html)
        if match:
                print match.group(1) + ' : '  + match.group(2)
                listitem.setInfo('video', {'Title': match.group(1), 'Year': int(match.group(2)) } )
        return listitem


def GetSearchQuery():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green][B]Search tv shows[/B][/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search(query)
	else:
                return

        
def Search(query):
        url = 'http://www.all-movies-stream.com/s/' + query + '-stream-p1.html'
        print url
        html = net.http_GET(url).content
        match = re.compile('''<li class="imgborder">\s*?<h2 class="widget-title" onclick="window.location = '(.+?)'">(.+?)</h2>\s*?<a href=".+?" title=".+?">\s*?<img src="(.+?)" alt=".+?" title=".+?" class="scale-with-grid"/>''').findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url':'http://www.all-movies-stream.com' +  url}, {'title':  title}, img= img, fanart=FanartPath + 'fanart.jpg')
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

###################################################################### menus ####################################################################################################

def MainMenu(url, text):    #homescreenserie
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/'}, {'title':  '[COLOR blue][B]Genres[/B] [/COLOR]>>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.jpg')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL + '/categorie/2/movie-on-stream-stream-p1.html'}, {'title':  '[COLOR blue][B]Just Added[/B] [/COLOR]>>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.jpg')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL + '/categorie/8/movies-2015-stream-stream-p1.html'}, {'title':  '[COLOR blue][B]Latest [/B] [/COLOR]>>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.jpg')

        addon.add_directory({'mode': 'GetSearchQuery'},  {'title':  '[B][COLOR green]Search[/B][/COLOR] >>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#################################################################################################################################################################################

if mode == 'main': 
	MainMenu(url, text)
elif mode == 'GetTitles': 
	GetTitles(url, text)
elif mode == 'GetTitles1': 
	GetTitles1(url, text, img)
elif mode == 'GetLinks':
	GetLinks(section, url, text, img)
elif mode == 'PlayVideo':
	PlayVideo(url, listitem)
elif mode == 'GetSearchQuery':
	GetSearchQuery()
elif mode == 'Search':
	Search(query)
xbmcplugin.endOfDirectory(int(sys.argv[1]))