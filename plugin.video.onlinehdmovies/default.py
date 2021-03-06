import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import re, string, sys, os
import urlresolver
import HTMLParser
from TheYid.common.addon import Addon
from TheYid.common.net import Net

addon_id = 'plugin.video.onlinehdmovies'
plugin = xbmcaddon.Addon(id=addon_id)
DB = os.path.join(xbmc.translatePath("special://database"), 'onlinehdmovies.db')
net = Net()
addon = Addon('plugin.video.onlinehdmovies', sys.argv)
BASE_URL = 'http://onlinehdmovies.org/'
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
                        pageUrl = url + '/page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content                      
                match = re.compile('<div class="item">\s*?<h2>(.+?)</h2>\s*?<div class="peli">\s*?<img src="(.+?)" alt=".+?" />\s*?<a href="(.+?)"', re.DOTALL).findall(html)
                for name, img, movieUrl in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart= 'http://images.forwallpaper.com/files/thumbs/preview/64/646017__cinema_p.jpg')      
                addon.add_directory({'mode': 'GetTitles', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart= 'http://images.forwallpaper.com/files/thumbs/preview/64/646017__cinema_p.jpg')
        setView('tvshows', 'tvshows-view')        
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks(section, url):
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<div id=".+?"><IFRAME SRC="(.+?)" FRAMEBORDER=.+? MARGINWIDTH=.+? MARGINHEIGHT=.+? SCROLLING=.+? WIDTH=.+? HEIGHT=.+?></IFRAME></div>').findall(content)
        match1 = re.compile('<center><a style=".+?" href="(.+?)" target="_blank">').findall(content)
        match2 = re.compile('<center><a href="(https://openload.io.+?)" target="_blank"><strong><span style=".+?">.+?</span></strong></a></center>').findall(content)
        match3 = re.compile('<p>(.+?)<A HREF=".+?">.+?</A></p>').findall(content)
        listitem = GetMediaInfo(content)
        for name in match3:
                addon.add_directory({'mode': 'GetLinks1', 'url':  url, 'listitem': listitem}, {'title': '[COLOR lawngreen][B]' + name  + '[/B][/COLOR]'}, img= 'http://onlinehdmovies.org/wp-content/uploads/2015/01/logo.png', fanart= 'http://imgprix.com/web/wallpapers/private-cinema-room/2560x1600.jpg')
        for url in match + match1:
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        host = host.replace('embed.','')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host }, img=IconPath + 'play.png', fanart= 'http://imgprix.com/web/wallpapers/private-cinema-room/2560x1600.jpg')
        for url in match2:
                addon.add_directory({'mode': 'GetLinks1', 'url':  url, 'listitem': listitem}, {'title':  'Direct Link - ' + url}, img= 'https://openload.io/assets/img/logo-alpha.png', fanart= 'http://imgprix.com/web/wallpapers/private-cinema-room/2560x1600.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks1(url):                                            
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match1 = re.compile('<span style="display:none;" id=".+?"><a href="(.+?)"').findall(content)
        listitem = GetMediaInfo(content)
        for url in match1:
                addon.add_directory({'mode': 'PlayVideo1', 'url': url, 'listitem': listitem}, {'title':  'Load Stream'}, img=IconPath + 'watch.png', fanart= 'http://www.htbackdrops.org/v2/albums/userpics/10097/orig_oefg_kino_im_kesselhaus.jpg')
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
        li.setProperty('fanart_image', 'http://www.htbackdrops.org/v2/albums/userpics/10097/orig_oefg_kino_im_kesselhaus.jpg')
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
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue]Latest Movies added [/COLOR]>>'}, img=IconPath + 'newmovies.png', fanart= 'http://www.htbackdrops.org/v2/albums/userpics/10097/orig_oefg_kino_im_kesselhaus.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/hd-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue]HD Movies [/COLOR]>>'}, img=IconPath + 'hdmovies.png', fanart= 'http://www.htbackdrops.org/v2/albums/userpics/10097/orig_oefg_kino_im_kesselhaus.jpg') 
        addon.add_directory({'mode': 'releaseMenu'}, {'title':  '[COLOR blue]Movies by year [/COLOR]>>'}, img=IconPath + 'date.png', fanart= 'http://www.htbackdrops.org/v2/albums/userpics/10097/orig_oefg_kino_im_kesselhaus.jpg')
        addon.add_directory({'mode': 'GenreMenu'}, {'title':  '[COLOR blue]Movies by genre [/COLOR]>>'}, img=IconPath + 'mg1.png', fanart= 'http://www.htbackdrops.org/v2/albums/userpics/10097/orig_oefg_kino_im_kesselhaus.jpg')
        addon.add_directory({'mode': 'GetSearchQuery9'},  {'title':  '[COLOR green]Movie Search[/COLOR]'}, img=IconPath + 'search11.png', fanart= 'http://www.htbackdrops.org/v2/albums/userpics/10097/orig_oefg_kino_im_kesselhaus.jpg')
        addon.add_directory({'mode': 'ResolverSettings'}, {'title':  '[COLOR red]Resolver Settings[/COLOR]'}, img=IconPath + 'resolvere.png', fanart= 'http://www.htbackdrops.org/v2/albums/userpics/10097/orig_oefg_kino_im_kesselhaus.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def releaseMenu():  
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/fecha-estreno/2015',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]2015 [/COLOR] >>'}, img=IconPath + 'date.png', fanart= 'http://www.h3dwallpapers.com/wp-content/uploads/2014/08/Mobile_wallpapers_hd_3d-5.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/fecha-estreno/2014',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]2014 [/COLOR] >>'}, img=IconPath + 'date.png', fanart= 'http://www.h3dwallpapers.com/wp-content/uploads/2014/08/Mobile_wallpapers_hd_3d-5.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/fecha-estreno/2013',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]2013 [/COLOR] >>'}, img=IconPath + 'date.png', fanart= 'http://www.h3dwallpapers.com/wp-content/uploads/2014/08/Mobile_wallpapers_hd_3d-5.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/fecha-estreno/2012',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]2012 [/COLOR] >>'}, img=IconPath + 'date.png', fanart= 'http://www.h3dwallpapers.com/wp-content/uploads/2014/08/Mobile_wallpapers_hd_3d-5.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/fecha-estreno/2011',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]2011 [/COLOR] >>'}, img=IconPath + 'date.png', fanart= 'http://www.h3dwallpapers.com/wp-content/uploads/2014/08/Mobile_wallpapers_hd_3d-5.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/fecha-estreno/2010',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]2010 [/COLOR] >>'}, img=IconPath + 'date.png', fanart= 'http://www.h3dwallpapers.com/wp-content/uploads/2014/08/Mobile_wallpapers_hd_3d-5.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/fecha-estreno/2009',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]2009 [/COLOR] >>'}, img=IconPath + 'date.png', fanart= 'http://www.h3dwallpapers.com/wp-content/uploads/2014/08/Mobile_wallpapers_hd_3d-5.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/fecha-estreno/2008',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]2008 [/COLOR] >>'}, img=IconPath + 'date.png', fanart= 'http://www.h3dwallpapers.com/wp-content/uploads/2014/08/Mobile_wallpapers_hd_3d-5.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/fecha-estreno/2007',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]2007 [/COLOR] >>'}, img=IconPath + 'date.png', fanart= 'http://www.h3dwallpapers.com/wp-content/uploads/2014/08/Mobile_wallpapers_hd_3d-5.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/fecha-estreno/2006',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]2006 [/COLOR] >>'}, img=IconPath + 'date.png', fanart= 'http://www.h3dwallpapers.com/wp-content/uploads/2014/08/Mobile_wallpapers_hd_3d-5.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/fecha-estreno/2005',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]2005 [/COLOR] >>'}, img=IconPath + 'date.png', fanart= 'http://www.h3dwallpapers.com/wp-content/uploads/2014/08/Mobile_wallpapers_hd_3d-5.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/fecha-estreno/2004',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]2004 [/COLOR] >>'}, img=IconPath + 'date.png', fanart= 'http://www.h3dwallpapers.com/wp-content/uploads/2014/08/Mobile_wallpapers_hd_3d-5.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/fecha-estreno/2003',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]2003 [/COLOR] >>'}, img=IconPath + 'date.png', fanart= 'http://www.h3dwallpapers.com/wp-content/uploads/2014/08/Mobile_wallpapers_hd_3d-5.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/fecha-estreno/2002',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]2002 [/COLOR] >>'}, img=IconPath + 'date.png', fanart= 'http://www.h3dwallpapers.com/wp-content/uploads/2014/08/Mobile_wallpapers_hd_3d-5.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/fecha-estreno/2001',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]2001 [/COLOR] >>'}, img=IconPath + 'date.png', fanart= 'http://www.h3dwallpapers.com/wp-content/uploads/2014/08/Mobile_wallpapers_hd_3d-5.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/fecha-estreno/2000',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]2000 [/COLOR] >>'}, img=IconPath + 'date.png', fanart= 'http://www.h3dwallpapers.com/wp-content/uploads/2014/08/Mobile_wallpapers_hd_3d-5.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/fecha-estreno/1999',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]1999 [/COLOR] >>'}, img=IconPath + 'date.png', fanart= 'http://www.h3dwallpapers.com/wp-content/uploads/2014/08/Mobile_wallpapers_hd_3d-5.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/fecha-estreno/1998',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]1998 [/COLOR] >>'}, img=IconPath + 'date.png', fanart= 'http://www.h3dwallpapers.com/wp-content/uploads/2014/08/Mobile_wallpapers_hd_3d-5.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/fecha-estreno/1997',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]1997 [/COLOR] >>'}, img=IconPath + 'date.png', fanart= 'http://www.h3dwallpapers.com/wp-content/uploads/2014/08/Mobile_wallpapers_hd_3d-5.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/fecha-estreno/1996',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]1996 [/COLOR] >>'}, img=IconPath + 'date.png', fanart= 'http://www.h3dwallpapers.com/wp-content/uploads/2014/08/Mobile_wallpapers_hd_3d-5.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GenreMenu(): 
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/action-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Action [/COLOR] >>'}, img=IconPath + 'Action.png', fanart= 'http://www.hdesktops.com/wp-content/uploads/2013/12/purple-3d-abstract-wallpaper-desktop-background-171.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/adventure-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Adventure [/COLOR] >>'}, img=IconPath + 'Adventure.png', fanart= 'http://www.hdesktops.com/wp-content/uploads/2013/12/purple-3d-abstract-wallpaper-desktop-background-171.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/animation-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Animation [/COLOR] >>'}, img=IconPath + 'Animation.png', fanart= 'http://www.hdesktops.com/wp-content/uploads/2013/12/purple-3d-abstract-wallpaper-desktop-background-171.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/biography-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Biography [/COLOR] >>'}, img=IconPath + 'Bipgraphy.png', fanart= 'http://www.hdesktops.com/wp-content/uploads/2013/12/purple-3d-abstract-wallpaper-desktop-background-171.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/comedy-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Comedy [/COLOR] >>'}, img=IconPath + 'Comedy.png', fanart= 'http://www.hdesktops.com/wp-content/uploads/2013/12/purple-3d-abstract-wallpaper-desktop-background-171.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/crime-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Crime [/COLOR] >>'}, img=IconPath + 'Crime.png', fanart= 'http://www.hdesktops.com/wp-content/uploads/2013/12/purple-3d-abstract-wallpaper-desktop-background-171.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/documentary-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Documentary [/COLOR] >>'}, img=IconPath + 'Documentary.png', fanart= 'http://www.hdesktops.com/wp-content/uploads/2013/12/purple-3d-abstract-wallpaper-desktop-background-171.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/drama-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Drama [/COLOR] >>'}, img=IconPath + 'Drama.png', fanart= 'http://www.hdesktops.com/wp-content/uploads/2013/12/purple-3d-abstract-wallpaper-desktop-background-171.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/fantasy-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Fantasy [/COLOR] >>'}, img=IconPath + 'Fantasy.png', fanart= 'http://www.hdesktops.com/wp-content/uploads/2013/12/purple-3d-abstract-wallpaper-desktop-background-171.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/history-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]History [/COLOR] >>'}, img=IconPath + 'History.png', fanart= 'http://www.hdesktops.com/wp-content/uploads/2013/12/purple-3d-abstract-wallpaper-desktop-background-171.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/horror-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Horror [/COLOR] >>'}, img=IconPath + 'Horror.png', fanart= 'http://www.hdesktops.com/wp-content/uploads/2013/12/purple-3d-abstract-wallpaper-desktop-background-171.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/music-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Music [/COLOR] >>'}, img=IconPath + 'Music.png', fanart= 'http://www.hdesktops.com/wp-content/uploads/2013/12/purple-3d-abstract-wallpaper-desktop-background-171.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/musical-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Musical [/COLOR] >>'}, img=IconPath + 'Musical.png', fanart= 'http://www.hdesktops.com/wp-content/uploads/2013/12/purple-3d-abstract-wallpaper-desktop-background-171.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/mystery-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Mystery [/COLOR] >>'}, img=IconPath + 'Mystery.png', fanart= 'http://www.hdesktops.com/wp-content/uploads/2013/12/purple-3d-abstract-wallpaper-desktop-background-171.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/oscar-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Oscar Movies [/COLOR] >>'}, img=IconPath + 'Favourites.png', fanart= 'http://www.hdesktops.com/wp-content/uploads/2013/12/purple-3d-abstract-wallpaper-desktop-background-171.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/romance-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Romance [/COLOR] >>'}, img=IconPath + 'Romantic.png', fanart= 'http://www.hdesktops.com/wp-content/uploads/2013/12/purple-3d-abstract-wallpaper-desktop-background-171.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/sci-fi-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Sci-fi [/COLOR] >>'}, img=IconPath + 'Sience Fiction.png', fanart= 'http://www.hdesktops.com/wp-content/uploads/2013/12/purple-3d-abstract-wallpaper-desktop-background-171.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/short-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Short Movies [/COLOR] >>'}, img=IconPath + 'Other.png', fanart= 'http://www.hdesktops.com/wp-content/uploads/2013/12/purple-3d-abstract-wallpaper-desktop-background-171.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/sport-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Sport [/COLOR] >>'}, img=IconPath + 'Sport.png', fanart= 'http://www.hdesktops.com/wp-content/uploads/2013/12/purple-3d-abstract-wallpaper-desktop-background-171.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/thriller-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Thriller [/COLOR] >>'}, img=IconPath + 'Thriller.png', fanart= 'http://www.hdesktops.com/wp-content/uploads/2013/12/purple-3d-abstract-wallpaper-desktop-background-171.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/war-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]War [/COLOR] >>'}, img=IconPath + 'War.png', fanart= 'http://www.hdesktops.com/wp-content/uploads/2013/12/purple-3d-abstract-wallpaper-desktop-background-171.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/western-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Western [/COLOR] >>'}, img=IconPath + 'Western.png', fanart= 'http://www.hdesktops.com/wp-content/uploads/2013/12/purple-3d-abstract-wallpaper-desktop-background-171.jpg')

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
        url = 'http://onlinehdmovies.org/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<div class="imagen">\s*?<a href="(.+?)"><img src="(.+?)" alt="(.+?)" /></a>', re.DOTALL).findall(html)
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
elif mode == 'GetLinks':
	GetLinks(section, url)
elif mode == 'GetLinks1':
	GetLinks1(url)
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