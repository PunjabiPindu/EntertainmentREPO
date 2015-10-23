import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import urllib, urllib2
import re, string, sys, os
import urlresolver
from TheYid.common.addon import Addon
from TheYid.common.net import Net
from htmlentitydefs import name2codepoint as n2cp
import HTMLParser

addon_id = 'plugin.video.tardis'
plugin = xbmcaddon.Addon(id=addon_id)
DB = os.path.join(xbmc.translatePath("special://database"), 'tardis.db')
BASE_URL = 'http://www.voirfilms.org/'
net = Net()
addon = Addon('plugin.video.tardis', sys.argv)

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
text = addon.queries.get('text', None)
img = addon.queries.get('img', None)
##.replace('', '')## \s*? ##
################################################################################# Titles #################################################################################

def GetTitles(url, text, img):
    try:
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('''<div class="unepetitesaisons">\s*?<a href="(.+?)" title="(.+?)">\s*?<div class="saisonimage">\s*?<img src="(.+?)" title=".+?">''').findall(content)
        for url, name, img in match:
                addon.add_directory({'mode': 'GetTitles1', 'url': url, 'listitem': listitem, 'text': name.strip().replace('saison', 'Season'), 'img': img}, {'title': name.strip().replace('saison', 'Season')}, img= 'http://www.voirfilms.org/' + img, fanart= 'https://ladygeekgirl.files.wordpress.com/2015/01/all13doctors.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
    except:
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetTitles1(url, text, img):
    try:
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('''class="description132"><a class=".+?" title="(.+?)" href="(.+?)">.+?</a>''').findall(content)
        for name, url in match:
                addon.add_directory({'mode': 'GetLinks', 'url': 'http://www.voirfilms.org/' + url, 'listitem': listitem, 'text': name.strip().replace('saison', 'Season').replace('VOSTFR', '').replace(',', '').replace('VF', '')}, {'title': name.strip().replace('saison', 'Season').replace('VOSTFR', '').replace(',', '').replace('VF', '')}, img=IconPath + 'icon.png',  fanart= 'https://ladygeekgirl.files.wordpress.com/2015/01/all13doctors.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
    except:
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks(section, url):
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<a href="(.+?)" target="filmPlayer"').findall(content)
        match1 = re.compile('<a href="https://uptostream.com/iframe/(.+?)" target="filmPlayer"').findall(content)
        listitem = GetMediaInfo(content)
        for url in match1:
                addon.add_directory({'mode': 'GetLinks1', 'url': 'http://uptobox.com/' + url, 'listitem': listitem}, {'title':  'UpToStream : direct link'}, img= 'https://uptostream.com/images/logo.png', fanart=FanartPath + 'fanart.jpg')
        for url in match:
                url = url.replace('iframe/', '') 
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        addon.add_directory({'mode': 'PlayVideo1', 'url': url, 'listitem': listitem}, {'title':  host }, img=IconPath + 'icon.png', fanart=FanartPath + 'fanart.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks1(section, url):
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('Streaming link: <a href="(.+?)" class="blue_link">.+?</a>').findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                addon.add_directory({'mode': 'GetLinks2', 'url': url, 'listitem': listitem}, {'title':  'load stream' + ' : ' + url}, img= 'https://uptostream.com/images/logo.png', fanart=FanartPath + 'fanart.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks2(section, url):
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile("<source src='(.+?)' type='.+?' data-res='(.+?)'").findall(content)
        listitem = GetMediaInfo(content)
        for url, name in match:
                addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title': name }, img= 'https://uptostream.com/images/logo.png', fanart=FanartPath + 'fanart.jpg')
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

def PlayVideo(url, listitem):
        addon_handle = int(sys.argv[1])
        xbmcplugin.setContent(addon_handle, 'video')
        li = xbmcgui.ListItem('[COLOR dodgerblue][B]PLAY STREAM[/B][/COLOR]  >> ', iconImage='http://orig14.deviantart.net/240f/f/2012/178/a/d/satin_alloy_tardis_icon___jaku_style_by_chaoticbuddhist-d550pp0.png', thumbnailImage= 'http://orig14.deviantart.net/240f/f/2012/178/a/d/satin_alloy_tardis_icon___jaku_style_by_chaoticbuddhist-d550pp0.png')
        li.setProperty('fanart_image', 'http://orig10.deviantart.net/266a/f/2010/107/7/b/daleks_from_the_darkness_by_gift_of_the_goddess.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
        xbmcplugin.endOfDirectory(addon_handle)

def PlayVideo1(url, listitem):
    try:
        print 'in PlayVideo %s' % text
        stream_url = urlresolver.HostedMediaFile(url).resolve()
        xbmc.Player().play(stream_url)
        addon.add_directory({'mode': 'help'}, {'title':  '[COLOR slategray][B]^^^ Press back ^^^[/B] [/COLOR]'}, img=img, fanart= 'http://orig10.deviantart.net/266a/f/2010/107/7/b/daleks_from_the_darkness_by_gift_of_the_goddess.jpg')
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

def MainMenu():    #homescreenserie
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/serie/doctor-who-1963.htm'}, {'title':  '[COLOR blue][B]Doctor Who 1963[/B] [/COLOR]>>'}, img= 'http://cdn.marketplaceimages.windowsphone.com/v8/images/4ae46d2f-2c2c-4686-8122-573f4b7a9973?imageType=ws_icon_large', fanart= 'http://i.imgur.com/VaMfWZw.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/serie/doctor-who-2005.htm'}, {'title':  '[COLOR blue][B]Doctor Who 2005[/B] [/COLOR]>>'}, img= 'http://cdn.marketplaceimages.windowsphone.com/v8/images/4ae46d2f-2c2c-4686-8122-573f4b7a9973?imageType=ws_icon_large', fanart= 'http://i.imgur.com/VaMfWZw.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))


#################################################################################################################################################################################

if mode == 'main': 
	MainMenu()
elif mode == 'GetTitles': 
	GetTitles(url, text, img)
elif mode == 'GetTitles1': 
	GetTitles1(url, text, img)
elif mode == 'GetTitles2': 
	GetTitles2(url, text)
elif mode == 'GetLinks':
	GetLinks(section, url)
elif mode == 'GetLinks1':
	GetLinks1(section, url)
elif mode == 'GetLinks2':
	GetLinks2(section, url)
elif mode == 'PlayVideo':
	PlayVideo(url, listitem, text)
elif mode == 'PlayVideo1':
	PlayVideo1(url, listitem)	
xbmcplugin.endOfDirectory(int(sys.argv[1]))