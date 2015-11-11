
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import urllib, urllib2
import re, string, sys, os
import urlresolver
from TheYid.common.addon import Addon
from TheYid.common.net import Net
from htmlentitydefs import name2codepoint as n2cp
import HTMLParser

addon_id = 'plugin.video.RapidBit'
plugin = xbmcaddon.Addon(id=addon_id)
DB = os.path.join(xbmc.translatePath("special://database"), 'RapidBit.db')
BASE_URL = 'http://rapidbit.net/'
net = Net()
addon = Addon('plugin.video.RapidBit', sys.argv)

###### PATHS ###########
AddonPath = addon.get_path()
IconPath = AddonPath + "/icons/"
FanartPath = AddonPath + "/icons/"

##### Queries ##########
mode = addon.queries['mode']
url = addon.queries.get('url', None)
content = addon.queries.get('content', None)
query = addon.queries.get('query', None)
startPage = addon.queries.get('startPage', None)
numOfPages = addon.queries.get('numOfPages', None)
listitem = addon.queries.get('listitem', None)
urlList = addon.queries.get('urlList', None)
section = addon.queries.get('section', None)
img = addon.queries.get('img', None)

################################################################################# Titles #################################################################################

def GetTitles(section, url, startPage= '1', numOfPages= '1'): # Get Movie & tv show Titles
    try:
        print 'oneclickwatch get Movie Titles Menu %s' % url
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content
                match = re.compile('itemprop="headline"><a href="(.+?)" title=".+?">(.+?)</a></h2>.+? src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl, 'img': img}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png') 
                addon.add_directory({'mode': 'GetTitles', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img= 'http://www.megatoner.si/media/mw_promobox/icon/open-left.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site mite be down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

##############################################################################\s*?# Get links #############################################################################################

def GetLinks(section, url, img):
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<a href="(.+?)"').findall(content)
        match2 = re.compile('<a href="http://sh.st/st/.+?/(.+?)">.+?</a><br />').findall(content)
        match1 = re.compile('<meta name="description" content="Download and (.+?)"/>').findall(content)
        match3 = re.compile('width=".+?" height=".+?" /></p>\s*?<p>(.+?)</p>').findall(content)
        listitem = GetMediaInfo(content)
        for name in match1:
                addon.add_directory({'listitem': listitem}, {'title': '[COLOR pink][B](' + name + ')[/B][/COLOR]' }, img= img, fanart=FanartPath + 'fanart.png')
        for name in match3:
                addon.add_directory({'listitem': listitem}, {'title': '[COLOR blue][B](' + name + ')[/B][/COLOR]' }, img= img, fanart=FanartPath + 'fanart.png')
        for url in match:
                host = GetDomain(url)
                if 'Unknown' in host:
                                continue
                r = re.search('\.rar[(?:\.html|\.htm)]*', url, re.IGNORECASE)
                if r:
                        continue
                if urlresolver.HostedMediaFile(url= url):
                        title = url.rpartition('/')
                        title = title[2].replace('.html', '')
                        title = title.replace('.htm', '')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title': host + ' : ' + title }, img= img, fanart=FanartPath + 'fanart.png')
        for url in match2:
                url = 'http://' + url
                host = GetDomain(url)
                if 'Unknown' in host:
                                continue
                r = re.search('\.rar[(?:\.html|\.htm)]*', url, re.IGNORECASE)
                if r:
                        continue
                if urlresolver.HostedMediaFile(url= url):
                        title = url.rpartition('/')
                        title = title[2].replace('.html', '')
                        title = title.replace('.htm', '')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title': host + ' : ' + title }, img= img, fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

############################################################################# Play Video #####################################################################################

def PlayVideo(url, listitem):
    try:
        print 'in PlayVideo %s' % url
        stream_url = urlresolver.HostedMediaFile(url).resolve()
        xbmc.Player().play(stream_url)
        addon.add_directory({'mode': 'help'}, {'title':  '[COLOR slategray][B]^^^ Press back ^^^[/B] [/COLOR]'},'','')
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

###################################################################### menus ####################################################################################################

def MainMenu():    #homescreen
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/tv-shows/',
                             'startPage': '1', 'numOfPages': '2'}, {'title':  '[COLOR blue][B]Latest Tv episodes[/B] [/COLOR]>>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/movies/',
                             'startPage': '1', 'numOfPages': '2'}, {'title':  '[COLOR blue][B]Latest Movies[/B] [/COLOR]>>'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')

        addon.add_directory({'mode': 'GetSearchQuery1'},  {'title':  '[COLOR green][B]Search[/B][/COLOR]'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'ResolverSettings'}, {'title':  '[COLOR red]Resolver Settings[/COLOR]'}, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.png')  
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

######################################################################## search #################################################################################################

def GetSearchQuery1():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search1(query)
	else:
                return
def Search1(query):
    try:
        url = 'http://rapidbit.net/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('itemprop="headline"><a href="(.+?)" title=".+?">(.+?)</a></h2>.+? src="(.+?)"', re.DOTALL).findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title}, img=img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry OneClickWatch search is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")

#################################################################################################################################################################################

if mode == 'main': 
	MainMenu()
elif mode == 'HelpMenu':
        HelpMenu()
elif mode == 'GetTitles': 
	GetTitles(section, url, startPage, numOfPages)
elif mode == 'GetLinks':
	GetLinks(section, url, img)
elif mode == 'GetSearchQuery1':
	GetSearchQuery1()
elif mode == 'Search1':
	Search1(query)
elif mode == 'PlayVideo':
	PlayVideo(url, listitem)	
elif mode == 'ResolverSettings':
        urlresolver.display_settings()
xbmcplugin.endOfDirectory(int(sys.argv[1]))