import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import urllib, urllib2
import re, string, sys, os
import urlresolver
from TheYid.common.addon import Addon
from TheYid.common.net import Net
from htmlentitydefs import name2codepoint as n2cp
import HTMLParser

addon_id = 'plugin.video.ts80k'
plugin = xbmcaddon.Addon(id=addon_id)
DB = os.path.join(xbmc.translatePath("special://database"), 'ts80k.db')
BASE_URL = 'http://tvonline.tw/'
net = Net()
addon = Addon('plugin.video.ts80k', sys.argv)

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
def GetTitles(url, text, img):
    try:
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile("<h3><a href='http://tvonline.tw/(.+?)' title='.+?'>(.+?)</a></h3> <ul><li>\s*?<a href='http://tvonline.tw/.+?' title='.+?'>").findall(content)
        for url, name in match:
                addon.add_directory({'mode': 'GetTitles1', 'url': 'http://tvonline.tw/' + url, 'listitem': listitem, 'text': name.strip(), 'img' : img}, {'title': name.strip()}, img= img, fanart=FanartPath + 'fanart.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
    except:
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetTitles1(url, text, img):
    try:
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile("<li><a href='http://tvonline.tw/(.+?)' title='Wtach.+?online'><strong>(.+?)</strong>(.+?)</a></li>").findall(content)
        for url, name, name1 in match:
                addon.add_directory({'mode': 'GetLinks', 'url': 'http://tvonline.tw/' + url, 'listitem': listitem, 'text': name.strip(), 'img' : img}, {'title': name.strip() + ' ' + name1}, img= img, fanart=FanartPath + 'fanart.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
    except:
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks(section, url, text, img):
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile("'(http://.+?)'").findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem, 'img' : img}, {'title':  host }, img= img, fanart=FanartPath + 'fanart.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))


def PlayVideo(url, listitem, img):
    try:
        print 'in PlayVideo %s' % text
        stream_url = urlresolver.HostedMediaFile(url).resolve()
        xbmc.Player().play(stream_url)
        addon.add_directory({'mode': 'help'}, {'title':  '[COLOR slategray][B]^^^ Press back ^^^[/B] [/COLOR]'}, img=img, fanart=FanartPath + 'fanart.jpg')
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

def MainMenu(url, img, text):    #homescreenserie
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/the-a-team-1983/', 'img' : 'http://travelblog.portfoliocollection.com/images/A-Team-Movie-Poster.jpg'}, {'title':  '[COLOR blue][B]The A-Team (1983)[/B] [/COLOR]>>'}, img= 'http://travelblog.portfoliocollection.com/images/A-Team-Movie-Poster.jpg', fanart= 'https://adameastondotcom.files.wordpress.com/2014/05/a-team.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/airwolf-1984/', 'img' : 'http://ecx.images-amazon.com/images/I/910i7M-sOgL._SL1500_.jpg'}, {'title':  '[COLOR blue][B]Airwolf (1984)[/B] [/COLOR]>>'}, img= 'http://ecx.images-amazon.com/images/I/910i7M-sOgL._SL1500_.jpg', fanart= 'https://mindreels.files.wordpress.com/2015/03/airwolf2.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/knight-rider-1982/', 'img' : 'https://upload.wikimedia.org/wikipedia/en/b/b5/Knight_Rider_season_1_DVD.png'}, {'title':  '[COLOR blue][B]Knight Rider (1982)[/B] [/COLOR]>>'}, img= 'https://upload.wikimedia.org/wikipedia/en/b/b5/Knight_Rider_season_1_DVD.png', fanart= 'https://lh3.ggpht.com/iQltD9YoehRbIbFdleRN1TE9Se7EZihXSH_Y36NVcB74tvyOIuT59hRMbXB7MDZhwr-sGQ=w1264')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/blue-thunder-1984/', 'img' : 'http://ecx.images-amazon.com/images/I/51MTG3B61CL.jpg'}, {'title':  '[COLOR blue][B]Blue Thunder (1984)[/B] [/COLOR]>>'}, img= 'http://ecx.images-amazon.com/images/I/51MTG3B61CL.jpg', fanart= 'http://spinoff.comicbookresources.com/wp-content/uploads/2015/03/blue-thunder.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/street-hawk-1985/', 'img' : 'http://www.scifi-movies.com/images/contenu/data/0003380/affiche-tonnerre-mecanique-street-hawk-1985-1.jpg'}, {'title':  '[COLOR blue][B]Street Hawk (1985)[/B] [/COLOR]>>'}, img= 'http://www.scifi-movies.com/images/contenu/data/0003380/affiche-tonnerre-mecanique-street-hawk-1985-1.jpg', fanart= 'http://www.streethawkonline.com/Wallpapers/StreetHawk_02_800x600.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/red-dwarf-1988/', 'img' : 'http://ecx.images-amazon.com/images/I/41-8sKNcXnL.jpg'}, {'title':  '[COLOR blue][B]Red Dwarf (1988)[/B] [/COLOR]>>'}, img= 'http://ecx.images-amazon.com/images/I/41-8sKNcXnL.jpg', fanart= 'http://static.comicvine.com/uploads/original/11/113883/4012095-7578756264-biRLb.jpg')

        xbmcplugin.endOfDirectory(int(sys.argv[1]))


#################################################################################################################################################################################

if mode == 'main': 
	MainMenu(url, img, text)
elif mode == 'GetTitles': 
	GetTitles(url, text, img)
elif mode == 'GetTitles1': 
	GetTitles1(url, text, img)
elif mode == 'GetLinks':
	GetLinks(section, url, text, img)
elif mode == 'PlayVideo':
	PlayVideo(url, listitem, img)
xbmcplugin.endOfDirectory(int(sys.argv[1]))