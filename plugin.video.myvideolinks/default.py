import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import re, string, sys, os
import urlresolver
import HTMLParser
from TheYid.common.addon import Addon
from TheYid.common.net import Net

addon_id = 'plugin.video.myvideolinks'
plugin = xbmcaddon.Addon(id=addon_id)
DB = os.path.join(xbmc.translatePath("special://database"), 'myvideolinks.db')
net = Net()
addon = Addon('plugin.video.myvideolinks', sys.argv)
BASE_URL = 'http://new.myvideolinks.xyz/'
AddonPath = addon.get_path()
IconPath = AddonPath + "/icons/"
FanartPath = AddonPath + "/icons/"
mode = addon.queries['mode']
url = addon.queries.get('url', None)
content = addon.queries.get('content', None)
query = addon.queries.get('query', None)
startPage = addon.queries.get('startPage', None)
numOfPages = addon.queries.get('numOfPages', None)
listitem = addon.queries.get('listitem', None)
urlList = addon.queries.get('urlList', None)
section = addon.queries.get('section', None)


def GetTitles(section, url, startPage= '1', numOfPages= '1'): 
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/page/' + startPage + '/'
                        html = net.http_GET(pageUrl).content                      
                match = re.compile('<div class="habangbuhay">\s*?<a href="(.+?)" rel=".+?" title=".+?"> <img src="(.+?)"  title="(.+?)" class=".+?" alt=".+?" /></a>', re.DOTALL).findall(html)
                for movieUrl, img, name in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')      
                addon.add_directory({'mode': 'GetTitles', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')        
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetTitles1(section, url, startPage= '1', numOfPages= '1'): 
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/page/' + startPage + '/'
                        html = net.http_GET(pageUrl).content                      
                match = re.compile('<div class="habangbuhay">\s*?<a href="(.+?)" rel="bookmark" title=".+?"> <img src="(.+?)" title="(.+?)" class=".+?" alt=".+?" /></a>', re.DOTALL).findall(html)
                for movieUrl, img, name in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')      
                addon.add_directory({'mode': 'GetTitles1', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')        
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks(section, url): 
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match2 = re.compile('<p><a href=".+?" rel=".+?">.+?</a></p>\s*?<p>.+?</p>\s*?<p>(.+?)</p>').findall(content)
        match = re.compile('<li><a href="(.+?)">.+?</a></li>').findall(content)
        match1 = re.compile('<li><a href="http://uploadrocket.net/(.+?)">.+?</a></li>').findall(content)
        listitem = GetMediaInfo(content)
        for name in match2:
                addon.add_directory({'mode': 'GetLinks1', 'url': url, 'listitem': listitem}, {'title':  '[B][COLOR lawngreen]' + name + '[/B][/COLOR]'}, img= 'http://www.64ouncegames.com/blog/wp-content/uploads/2013/09/PlotTwist.png', fanart=FanartPath + 'fanart.png')
        for url in match1:
                addon.add_directory({'mode': 'GetLinks1', 'url': 'http://uploadrocket.net/' + url, 'listitem': listitem}, {'title': url}, img=IconPath + 'vids.png', fanart=FanartPath + 'fanart.png')
        for url in match:
                host = GetDomain(url)
                if 'Unknown' in host:
                                continue
                print '*****************************' + host + ' : ' + url
                if urlresolver.HostedMediaFile(url= url):
                        print 'in GetLinks if loop'
                        title = url.rpartition('/')
                        title = title[2].replace('.html', '')
                        title = title.replace('.htm', '')
                        host = host.replace('youtube.com','[COLOR lime]Movie Trailer[/COLOR]')
                        host = host.replace('youtu.be','[COLOR lime]Movie Trailer[/COLOR]')
                        host = host.replace('.net','')
                        host = host.replace('.com','')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))



def GetLinks1(url):                                            
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<a class="dlbutton_green" href="(.+?)" target="_blank"><span>.+?</span></a>').findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                addon.add_directory({'mode': 'GetLinks2', 'url': url, 'listitem': listitem}, {'title':  url}, img=IconPath + 'watch.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks2(url):                                            
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match1 = re.compile('<a href="http://uploadrocket.net/directdownload.html/(.+?)" target="_blank">').findall(content)
        listitem = GetMediaInfo(content)
        for url in match1:
                addon.add_directory({'mode': 'GetLinks2a', 'url': 'http://uploadrocket.net/directdownload.html/' + url, 'listitem': listitem}, {'title':  'load stream - ' + url}, img=IconPath + 'watch.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks2a(url):                                            
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match1 = re.compile('<a href="http://(.+?)" onclick=').findall(content)
        listitem = GetMediaInfo(content)
        for url in match1:
                addon.add_directory({'mode': 'PlayVideo1', 'url': 'http://' + url, 'listitem': listitem}, {'title':  'load stream - ' + url}, img=IconPath + 'watch.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def PlayVideo(url, listitem):
    try:
        print 'in PlayVideo %s' % url
        stream_url = urlresolver.HostedMediaFile(url).resolve()
        xbmc.Player().play(stream_url)
        addon.add_directory({'mode': 'help'}, {'title':  '[COLOR slategray][B]^ Press back ^[/B] [/COLOR]'},'','')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry Link may have been removed ![/B][/COLOR],[COLOR lime][B]Please try a different link/host !![/B][/COLOR],7000,"")")

def PlayVideo1(url, listitem):
        addon_handle = int(sys.argv[1])
        xbmcplugin.setContent(addon_handle, 'video')
        li = xbmcgui.ListItem('[COLOR dodgerblue][B]PLAY STREAM[/B][/COLOR]  >> ', iconImage='http://maps.synthicity.com/activemaps/images/button_black_play.png', thumbnailImage= 'http://maps.synthicity.com/activemaps/images/button_black_play.png')
        li.setProperty('fanart_image', 'https://raw.githubusercontent.com/TheYid/My-Repo/master/repository.TheYid/fanart.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
        xbmcplugin.endOfDirectory(addon_handle)

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

def MainMenu():   
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/allmovies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue]Latest Movies added [/COLOR]>>'}, img=IconPath + 'newmovies1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'releaseMenu'}, {'title':  '[COLOR blue]Movie by year & release group [/COLOR]>>'}, img=IconPath + 'date1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GenreMenu'}, {'title':  '[COLOR blue]Movies & Tv shows by genre [/COLOR]>>'}, img=IconPath + 'mg1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/tv-shows/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue]Latest Tv shows added [/COLOR]>>'}, img=IconPath + 'newtvs1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery9'},  {'title':  '[COLOR green]Movie Search[/COLOR]'}, img=IconPath + 'searchse1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'ResolverSettings'}, {'title':  '[COLOR red]Resolver Settings[/COLOR]'}, img=IconPath + 'resolvere1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def releaseMenu():  
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/allmovies/2015release/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]2015 [/COLOR]>>'}, img=IconPath + 'date1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/allmovies/2014release/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]2014 [/COLOR]>>'}, img=IconPath + 'date1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/allmovies/2013older/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]2013 and older [/COLOR]>>'}, img=IconPath + 'date1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/allmovies/3dmovies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]3D movies [/COLOR]>>'}, img=IconPath + 'date1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/allmovies/bdrips/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]BDRip [/COLOR]>>'}, img=IconPath + 'date1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/allmovies/blurays/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]BluRay [/COLOR]>>'}, img=IconPath + 'date1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/allmovies/dvdrip-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]DVDRip [/COLOR]>>'}, img=IconPath + 'date1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/uncategorized/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Uncategorized [/COLOR]>>'}, img=IconPath + 'date1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GenreMenu():  
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/allmovies/3dmovies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]3D >>[/COLOR]'}, img=IconPath + '3d11.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL + '/tag/family-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Family >>[/COLOR]'}, img=IconPath + 'fam1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL + '/tag/animation-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Animation >>[/COLOR]'}, img=IconPath + 'an1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL + '/tag/actionmovies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Action >>[/COLOR]'}, img=IconPath + 'ac1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL + '/tag/adventure-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Adventure >>[/COLOR]'}, img=IconPath + 'ad1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL + '/tag/biography-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Biography >>[/COLOR]'}, img=IconPath + 'bm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL + '/tag/comedy-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Comedy >>[/COLOR]'}, img=IconPath + 'coms.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL + '/tag/documentary-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Documentary >>[/COLOR]'}, img=IconPath + 'doc11.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL + '/tag/fantasy-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Fantasy >>[/COLOR]'}, img=IconPath + 'fan1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL + '/tag/horror-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Horror >>[/COLOR]'}, img=IconPath + 'ho1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL + '/tag/sci-fi-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Sci-fi >>[/COLOR]'}, img=IconPath + 'sci1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL + '/tag/mystery-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Mystery >>[/COLOR]'}, img=IconPath + 'ms1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL + '/tag/music-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Music >>[/COLOR]'}, img=IconPath + 'mus1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL + '/tag/war-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]War >>[/COLOR]'}, img=IconPath + 'war1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL + '/tag/western-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Western >>[/COLOR]'}, img=IconPath + 'west1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetSearchQuery9():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search9(query)
	else:
                return
def Search9(query):
        url = 'http://movies.myvideolinks.xyz/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<div class="habangbuhay">\s*?<a href="(.+?)" rel="bookmark" title=".+?"> <img src="(.+?)" title="(.+?)" class=".+?" alt=".+?" /></a>', re.DOTALL).findall(html)
        for url, img, title in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title}, img = img , fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

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

if mode == 'main': 
	MainMenu()
elif mode == 'HelpMenu':
        HelpMenu()
elif mode == 'GenreMenu':
        GenreMenu()
elif mode == 'releaseMenu':
        releaseMenu()
elif mode == 'GetTitles': 
	GetTitles(section, url, startPage, numOfPages)
elif mode == 'GetTitles1': 
	GetTitles1(section, url, startPage, numOfPages)
elif mode == 'GetLinks':
	GetLinks(section, url)
elif mode == 'GetLinks1':
	GetLinks1(url)
elif mode == 'GetLinks2':
	GetLinks2(url)
elif mode == 'GetLinks2a':
	GetLinks2a(url)
elif mode == 'GetSearchQuery9':
	GetSearchQuery9()
elif mode == 'Search9':
	Search9(query)
elif mode == 'PlayVideo':
	PlayVideo(url, listitem)
elif mode == 'PlayVideo1':
	PlayVideo1(url, listitem)	
elif mode == 'ResolverSettings':
        urlresolver.display_settings()
xbmcplugin.endOfDirectory(int(sys.argv[1]))