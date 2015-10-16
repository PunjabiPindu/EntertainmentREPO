# Kool London KODI Plugin
# Developer: @TheYid009
# Support: Twitter : @TheYid009
# Disclaimer: @TheYid009 dose not own or publish the content delivered by the plugin
# streams and content is owned by Kool London

import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import re, string, sys, os
from TheYid.common.addon import Addon
from TheYid.common.net import Net

addon_id = 'plugin.audio.koollondon'
plugin = xbmcaddon.Addon(id=addon_id)
DB = os.path.join(xbmc.translatePath("special://database"), 'koollondon.db')
BASE_URL = 'http://koollondon.varsitycloud.co/'
net = Net()
addon = Addon('plugin.audio.koollondon', sys.argv)
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
	match = re.compile('<div class="file-item-container" name="(.+?)" data=".+?" aid=".+?" ondblclick="(.+?)">').findall(content)
	listitem = GetMediaInfo(content)
	for name, url in match:
		url = url.replace("', function(){LandingPageSetup();});", '')
		url = url.replace("Spinner();$('#FileList').load('", '')
		addon.add_directory({'mode': 'GetLinks2', 'url': 'http://koollondon.varsitycloud.co/' + url, 'listitem': listitem}, {'title':  name.strip()}, img = 'http://s30.postimg.org/5r870dash/icon.png', fanart = 'http://s0.hulkshare.com/song_images/original/1/b/a/1ba96478934405ef5a9a2528947804ec.jpg?dd=1388552400')
	setView('menu', 'menu-view')
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks2(url, text):
	print 'GETLINKS FROM URL: '+url
	html = net.http_GET(url).content
	listitem = GetMediaInfo(html)
	content = html
	match = re.compile('<div class="file-item-container" name="(.+?)" data="(.+?)" aid="(.+?)" rel=".+?" rev="topMiddle">').findall(content)
	match2 = re.compile('<div class="file-item-container" name="(.+?)" data=".+?" aid=".+?" ondblclick="(.+?)">').findall(content)
	match1 = re.compile('<a class="" href="/.+?/.+?.+?=(.+?)&(.+?)" onclick=".+?">Next</a>').findall(content)
	listitem = GetMediaInfo(content)
	for name, url, url1 in match:
		addon.add_directory({'mode': 'PlayVideo', 'text' : name, 'url': 'http://koollondon.varsitycloud.co/IO/DownloadSharedFile?NodeID=' + url + '&AID=' + url1, 'listitem': listitem}, {'title': name}, img = 'http://s30.postimg.org/5r870dash/icon.png', fanart = 'http://s0.hulkshare.com/song_images/original/1/b/a/1ba96478934405ef5a9a2528947804ec.jpg?dd=1388552400')
	for name, url in match2:
		url = url.replace("', function(){LandingPageSetup();});", '')
		url = url.replace("Spinner();$('#FileList').load('", '')
		addon.add_directory({'mode': 'GetLinks2', 'url': 'http://koollondon.varsitycloud.co/' + url, 'listitem': listitem}, {'title':  name.strip()}, img = 'http://s30.postimg.org/5r870dash/icon.png', fanart = 'http://s0.hulkshare.com/song_images/original/1/b/a/1ba96478934405ef5a9a2528947804ec.jpg?dd=1388552400')
	for url, url1 in match1:
		url1 = url1.replace('amp;pageNo=', 'pageNo=')
		url1 = url1.replace('&amp;viewMode=1', '&viewMode=1')
		addon.add_directory({'mode': 'GetLinks2', 'url': 'http://koollondon.varsitycloud.co/files/FileList/' + url + '?fileId=' + url + '&' + url1, 'listitem': listitem}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img= 'https://raw.githubusercontent.com/MrEntertainment/EntertainmentREPO/master/plugin.video.allinone/icons/nextpage1.png', fanart = 'http://s0.hulkshare.com/song_images/original/1/b/a/1ba96478934405ef5a9a2528947804ec.jpg?dd=1388552400')
	setView('menu', 'menu-view')
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
	url = 'http://uk1-pn.webcast-server.net:8698'
	li = xbmcgui.ListItem('[COLOR dodgerblue][B]Kool London  [/B][/COLOR] [COLOR red][B][I](Live)[/B][/I][/COLOR]  [COLOR yellow][B] >>[/B][/COLOR] >>    [COLOR lime](Stream 1)[/COLOR]', iconImage='http://s30.postimg.org/5r870dash/icon.png', thumbnailImage= 'http://s30.postimg.org/5r870dash/icon.png')
	li.setProperty('fanart_image', 'http://koollondon.com/images/stories/kool-timetable-june-2015.png')
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

	addon_handle = int(sys.argv[1])
	xbmcplugin.setContent(addon_handle, 'video')
	url = 'rtmp://w10.streamgb.com:1935/kool/kool'
	li = xbmcgui.ListItem('[COLOR dodgerblue][B]Kool London  [/B][/COLOR] [COLOR red][B][I](Live)[/B][/I][/COLOR]  [COLOR yellow][B] >>[/B][/COLOR] >>    [COLOR lime](Webcam 1)[/COLOR]', iconImage='http://s30.postimg.org/5r870dash/icon.png', thumbnailImage= 'http://s30.postimg.org/5r870dash/icon.png')
	li.setProperty('fanart_image', 'http://koollondon.com/images/stories/kool-timetable-june-2015.png')
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

	addon.add_directory({'mode': 'GetLinks', 'url': BASE_URL + '/'}, {'title':  '[COLOR powderblue][B]Kool London Archives[/B][/COLOR]  [COLOR yellow][B] >>[/B][/COLOR] >>'}, img = 'http://s30.postimg.org/5r870dash/icon.png', fanart = 'http://s0.hulkshare.com/song_images/original/1/b/a/1ba96478934405ef5a9a2528947804ec.jpg?dd=1388552400')

	xbmcplugin.setContent(addon_handle, 'audio')
	url = 'https://archive.org/download/koollondon/koollondon.m3u'
	li = xbmcgui.ListItem('[COLOR mediumturquoise][B]Kool FM 94.5 Archives[/COLOR][/B]  [COLOR yellow][B] >>[/B][/COLOR] >>', iconImage='http://s30.postimg.org/5r870dash/icon.png', thumbnailImage='http://s30.postimg.org/5r870dash/icon.png')
	li.setProperty('fanart_image', 'http://s0.hulkshare.com/song_images/original/1/b/a/1ba96478934405ef5a9a2528947804ec.jpg?dd=1388552400')
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

	xbmcplugin.setContent(addon_handle, 'audio')
	url = 'http://uk1-pn.mixstream.net/8698.asx'
	li = xbmcgui.ListItem('Text: 07943 813 011. Twitter: @koollondon, Koollondon.com - Internet Radio Station The Mecca of Drum n Bass, Jungle & Hardcore, 11 times winner of Drum & Bass Awards', iconImage='http://s30.postimg.org/5r870dash/icon.png', thumbnailImage= 'http://s30.postimg.org/5r870dash/icon.png')
	li.setProperty('fanart_image', 'http://s2.postimg.org/4jtfmw5qx/fanart2.jpg')
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
	setView('menu', 'menu-view')
	xbmcplugin.endOfDirectory(addon_handle)

############################################################################# Play Video #####################################################################################

def PlayVideo(url, listitem, text):
	addon_handle = int(sys.argv[1])
	xbmcplugin.setContent(addon_handle, 'audio')
	li = xbmcgui.ListItem('[COLOR dodgerblue][B]PLAY [/B][/COLOR]' + text, thumbnailImage= 'http://s30.postimg.org/5r870dash/icon.png')
	li.setProperty('fanart_image', 'http://koollondon.com/images/stories/kool-timetable-june-2015.png')
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
	setView('menu', 'menu-view')
	xbmcplugin.endOfDirectory(addon_handle)

############################################################################# set views #####################################################################################

def setView(content, viewType):
	if content:
		xbmcplugin.setContent(int(sys.argv[1]), content)
	if addon.get_setting('auto-view') == 'true':
		xbmc.executebuiltin("Container.SetViewMode(%s)" % addon.get_setting(viewType) )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_UNSORTED )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_LABEL )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_VIDEO_RATING )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_DATE )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_PROGRAM_COUNT )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_VIDEO_RUNTIME )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_GENRE )

################################################################################# mode #########################################################################################

if mode == 'main': 
	MainMenu()
elif mode == 'GetLinks':
	GetLinks(url)
elif mode == 'GetLinks2':
	GetLinks2(url, text)
elif mode == 'PlayVideo':
	PlayVideo(url, listitem, text)	
