# Rinse fm XBMC Plugin
# Developer: @TheYid009
# Support: www.xbmchub.com or @TheYid009
# Disclaimer: @TheYid009 dose not own or publish the content delivered by the plugin
# streams and content is owned by Rinse fm

import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import re, string, sys, os
from TheYid.common.addon import Addon
from TheYid.common.net import Net

addon_id = 'plugin.audio.rinsefmplayer'
plugin = xbmcaddon.Addon(id=addon_id)
DB = os.path.join(xbmc.translatePath("special://database"), 'rinsefmplayer.db')
BASE_URL = 'http://rinse.fm/'
net = Net()
addon = Addon('plugin.audio.rinsefmplayer', sys.argv)
mode = addon.queries['mode']
url = addon.queries.get('url', None)
content = addon.queries.get('content', None)
listitem = addon.queries.get('listitem', None)
text = addon.queries.get('text', None)

############################################################################### Get links #############################################################################################

def GetLinks(url):
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<option value="(.+?)">(.+?)</option>').findall(content)
        listitem = GetMediaInfo(content)
        for url, name in match:
                addon.add_directory({'mode': 'GetLinks2', 'url': url, 'listitem': listitem}, {'title':  name.strip()}, img = 'http://2.bp.blogspot.com/-0enPTd9lXMY/TePPr-IU1xI/AAAAAAAABoo/ZL8QxQSk96w/s400/RINSE.png', fanart = 'http://crackmagazine.net/wp-content/uploads/2013/01/rinse_fm_wallpaper_by_peants-d4cinr4.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks2(url, text):
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<div class="listen icon">\s*?<a href="(.+?)" class=".+?" data-airtime=".+?" data-air-day="(.+?)" data-artist="(.+?)" data-img-src=".+?">.+?</a>').findall(content)
        listitem = GetMediaInfo(content)
        for url, date, show in match:
                addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem, 'text':  show + ' - ' + date }, {'title': show + ' - ' + date }, img = 'http://2.bp.blogspot.com/-0enPTd9lXMY/TePPr-IU1xI/AAAAAAAABoo/ZL8QxQSk96w/s400/RINSE.png', fanart = 'http://welikemusic.info/wp-content/uploads/2013/06/amit-dj-krust-rinse-fm-podcast-13-02-2013.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

##\s*?##

################################################################################ ListItem #################################################################################

def GetMediaInfo(html):
        listitem = xbmcgui.ListItem()
        match = re.search('og:title" content="(.+?) \((.+?)\)', html)
        if match:
                print match.group(1) + ' : '  + match.group(2)
                listitem.setInfo('video', {'Title': match.group(1), 'Year': int(match.group(2)) } )
        return listitem

################################################################################# menus ####################################################################################################

def MainMenu():   
        addon_handle = int(sys.argv[1]) 
        xbmcplugin.setContent(addon_handle, 'audio')
        url = 'http://podcast.dgen.net:8000/rinseradio'
        li = xbmcgui.ListItem('[COLOR powderblue][B]Rinse FM[/B][/COLOR] [COLOR lime] (((LIVE))) [/COLOR]', iconImage='http://s16.postimg.org/kdlyi29j9/icon.png', thumbnailImage= 'http://s16.postimg.org/kdlyi29j9/icon.png')
        li.setProperty('fanart_image', 'http://s29.postimg.org/rsd7ep7gn/fanart.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
        addon.add_directory({'mode': 'GetLinks', 'url': BASE_URL + '/podcasts/'}, {'title':  '[COLOR powderblue][B]Past Shows & Podcasts[/B][/COLOR]'}, img = 'http://s16.postimg.org/kdlyi29j9/icon.png', fanart = 'http://s29.postimg.org/rsd7ep7gn/fanart.jpg')
        xbmcplugin.endOfDirectory(addon_handle)

############################################################################# Play Video #####################################################################################

def PlayVideo(url, listitem, text):
        addon_handle = int(sys.argv[1])
        xbmcplugin.setContent(addon_handle, 'audio')
        li = xbmcgui.ListItem('[COLOR dodgerblue][B]PLAY [/B][/COLOR] ' + text , thumbnailImage= 'http://2.bp.blogspot.com/-0enPTd9lXMY/TePPr-IU1xI/AAAAAAAABoo/ZL8QxQSk96w/s400/RINSE.png')
        li.setProperty('fanart_image', 'http://fc00.deviantart.net/fs71/f/2013/091/6/7/my_forest_of_contrast_topped_of_by_a_rinse_fm_logo_by_cyrax_apex-d602ggy.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
        xbmcplugin.endOfDirectory(addon_handle)

################################################################################# mode #########################################################################################

if mode == 'main': 
	MainMenu()
elif mode == 'GetLinks':
	GetLinks(url)
elif mode == 'GetLinks2':
	GetLinks2(url, text)
elif mode == 'PlayVideo':
	PlayVideo(url, listitem, text)	
