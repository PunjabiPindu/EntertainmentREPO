import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import urllib, urllib2
import re, string, sys, os
import urlresolver
from TheYid.common.addon import Addon
from TheYid.common.net import Net
from htmlentitydefs import name2codepoint as n2cp
import HTMLParser

addon_id = 'plugin.video.oneclickwatch'
plugin = xbmcaddon.Addon(id=addon_id)
DB = os.path.join(xbmc.translatePath("special://database"), 'oneclickwatch.db')
BASE_URL = 'http://oneclickwatch.ws/'
BASE_URL1 = 'http://rlsseries.com/'
BASE_URL2 = 'http://www.rls-dl.com/'
BASE_URL4 = 'http://www.tvguide.com/'
BASE_URL5 = 'http://www.moviefone.com/'
BASE_URL6 = 'http://www.pogdesign.co.uk/'
net = Net()
addon = Addon('plugin.video.oneclickwatch', sys.argv)

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

################################################################################# Titles OCW #################################################################################

def GetTitles(section, url, startPage= '1', numOfPages= '1'):
    try:
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
                match = re.compile('<h2 class="title"><a href="(.+?)" title=".+?">(.+?)<.+? src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.jpg') 
                addon.add_directory({'mode': 'GetTitles', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage.png', fanart=FanartPath + 'fanart.jpg')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site mite be down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------- TV Calendar index ----------------------------------------------------------------------------------------------------#

def GetTitles6(section, url, startPage= '1', numOfPages= '1'):
    try:
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
                match = re.compile('<strong><a href=".(.+?)" title="(.+?)"><span class=".+?">.+?</span> <span class=".+?">.+?</span><span class=".+?">.+?</span>', re.DOTALL).findall(html)
                for movieUrl, name in match:
                        addon.add_directory({'mode': 'GetTitles6a', 'section': section, 'url': 'http://www.pogdesign.co.uk/cat/' + movieUrl }, {'title': '[B]' + name + '[/B]'}, img= 'https://briantudor.files.wordpress.com/2010/12/tv-icon1.png',  fanart=FanartPath + 'fanart.jpg') 
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site mite be down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetTitles6a(query, section): 
        pageUrl = url
        html = net.http_GET(pageUrl).content                     
        match = re.compile('<div class="contbox ovbox" style=" background-image: url(.+?);">\s*?<h4><a href=".+?">(.+?)<span>.+?</span></a></h4>\s*?<h5><a href=".+?">(.+?)<span>(.+?)/span></a></h5>\s*?<div class=".+?">.+?<a href=".+?">.+?</a></div> \s*?<ul class=".+?">\s*?<li><strong>.+?</strong>(.+?)</li>',re.DOTALL).findall(html)
        for img, name1, query, name, time in match:
                addon.add_directory({'mode': 'Search1', 'section': section, 'query': name1 + name.replace(' 1,', '01').replace(' 2,', '02').replace(' 3,', '03').replace(' 4,', '04').replace(' 5,', '05').replace(' 6,', '06').replace(' 7,', '07').replace(' 8,', '08').replace(' 9,', '09').replace(' 1<', '01').replace(' 2<', '02').replace(' 3<', '03').replace(' 4<', '04').replace(' 5<', '05').replace(' 6<', '06').replace(' 7<', '07').replace(' 8<', '08').replace(' 9<', '09').replace('Season', 's').replace('Episode', 'e').replace(',', '').replace('-', '').replace(' ', '')}, {'title': '[COLOR blue][B]' + name1 +'[/B][/COLOR]' + ' - ' + '[COLOR lime]' + query + '[/COLOR]' + ' - ' + '[COLOR pink][I]' + name.replace('<', ' ') + '[/I][/COLOR]' + ' - ' + time}, img= 'http://www.pogdesign.co.uk/' + img.replace('(', '').replace(')', ''),  fanart=FanartPath + 'fanart.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------- moviefone movie index ---------------------------------------------------------------------------------#

def GetTitles5(query):
    try:
        pageUrl = url
        html = net.http_GET(pageUrl).content                     
        match = re.compile('<img name="replace-image" rel=".+?" id=".+?" class=".+?" src=".+?" data-src="(.+?)" alt="(.+?)"/>',re.DOTALL).findall(html)
        for img, query in match:
                addon.add_directory({'mode': 'Search2', 'query': query}, {'title':  query}, img= img, fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------- tvguide movie index ----------------------------------------------------------------------------------------------------#

def GetTitles4(query):
    try:
        pageUrl = url
        html = net.http_GET(pageUrl).content                     
        match = re.compile('<span class="show-card show-card-small">\s*?<img src="(.+?)" class=".+?" alt=".+?" title="(.+?)" srcset=".+?" width=".+?" height=".+?" />',re.DOTALL).findall(html)
        for img, query in match:
                addon.add_directory({'mode': 'Search2', 'query': query}, {'title':  query}, img= img.replace('100x133.png', '1000x339.png').replace('100x133.jpg', '1000x339.jpg'), fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------- rls-dl tv index ----------------------------------------------------------------------------------------------------#

def GetTitles3(query, startPage= '1', numOfPages= '1'): 
    try:
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
                match = re.compile('<div class="thumbn"><img src="(.+?)" alt="(.+?)" /></div>', re.DOTALL).findall(html)
                for img, query in match:
                        addon.add_directory({'mode': 'Search1', 'section': section, 'query': query}, {'title':  query}, img= img, fanart= 'http://www.blazevideo.com/blog/wp-content/uploads/tv-shows-montage.jpg')
                addon.add_directory({'mode': 'GetTitles1', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage.png', fanart= 'http://www.blazevideo.com/blog/wp-content/uploads/tv-shows-montage.jpg') 
        setView('tvshows', 'tvshows-view')   
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site mite be down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------- rlsseries tv index ----------------------------------------------------------------------------------------------------#

def GetTitles2(section, url, startPage= '1', numOfPages= '1'):
    try:
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
                match = re.compile('<option class="level-0" value=".+?">(.+?)</option>', re.DOTALL).findall(html)
                for movieUrl in match:
                        addon.add_directory({'mode': 'GetTitles1', 'section': section, 'url': 'http://rlsseries.com/category/' + movieUrl.replace(' ', '-') + '/'}, {'title': movieUrl}, img= 'https://briantudor.files.wordpress.com/2010/12/tv-icon1.png', fanart= 'http://www.blazevideo.com/blog/wp-content/uploads/tv-shows-montage.jpg') 
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site mite be down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetTitles1(query, section): 
        pageUrl = url
        html = net.http_GET(pageUrl).content                     
        match = re.compile('<span class="gotocomments"><a href=".+?">.+?</a></span>\s*?</div>\s*?<div class="clear"></div>\s*?<div class="entry">\s*?<p><img class=".+?" src="(.+?)" alt=".+?" width=".+?" height=".+?" /><br />.+?<strong>(.+?)</strong>.+?<br />',re.DOTALL).findall(html)
        for img, query in match:
                addon.add_directory({'mode': 'Search1', 'section': section, 'query': query}, {'title':  query}, img= img, fanart= 'http://www.blazevideo.com/blog/wp-content/uploads/tv-shows-montage.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------- index search tv ----------------------------------------------------------------------------------------------------#

def Search1(query):
    try:
        url = 'http://oneclickwatch.ws/' + query + '/'
        url = url.replace(' ', '-')
        print url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match1 = re.compile('<h2 class="title">(.+?)</h2>.+?.+?src="(.+?)"', re.DOTALL).findall(html)
        match = re.compile('<a href="(.+?)" rel="nofollow"', re.DOTALL).findall(html)
        match2 = re.compile('href="(http://uptobox.com/.+?)"').findall(content)
        match3 = re.compile('<meta name="description" itemprop="description" content="(.+?)" />').findall(content)
        for name, img in match1:
                addon.add_directory({'mode': 'PlayVideo1', 'url': url, 'listitem': listitem}, {'title': '[COLOR pink][B](' + name + ')[/B][/COLOR]' }, img= img, fanart=FanartPath + 'fanart.jpg')
        for name in match3:
                addon.add_directory({'mode': 'PlayVideo1', 'url': url, 'listitem': listitem}, {'title': '[COLOR blue][B]' + name.replace('http://www.tvguide.com/', '').replace('http://www.tvrage.com/', '').replace('/', ' ').replace(';', ' ').replace('-', ' ').replace('tvshows', ' ').replace('_', ' ') + '[/B][/COLOR]' }, img= 'https://briantudor.files.wordpress.com/2010/12/tv-icon1.png', fanart=FanartPath + 'fanart.jpg')
        for url in match2:
                addon.add_directory({'mode': 'GetLinks1', 'url':  url, 'listitem': listitem}, {'title':  'UpToStream : direct link'}, img= 'https://uptostream.com/images/logo.png', fanart=FanartPath + 'fanart.jpg')
        for url in match:
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host.replace('oneclickwatch.ws', 'Streamimg links below') }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.jpg')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]No Links in OCW [/B][/COLOR],[COLOR blue][B]Trying rlsseries[/B][/COLOR],7000,"")")
    try:
        url = 'http://rlsseries.com/' + query + '/'
        url = url.replace(' ', '-')
        print url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('href="(.+?)">.+?</a>', re.DOTALL).findall(html)
        for url in match:
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host + ' - ' + ' rlsseries'}, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.jpg')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]No Links in rlsseries [/B][/COLOR],[COLOR blue][B]Trying watchseries-onlines[/B][/COLOR],7000,"")")
    try:
        url = 'http://watchseries-onlines.ch/' + query + '/'
        url = url.replace(' ', '-')
        print url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<div class="play-btn text-center"><a href="(.+?)" target="_blank" rel="nofollow">.+?</a></div>', re.DOTALL).findall(html)
        for url in match:
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host + ' - ' + ' WSO'}, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.jpg')
    except:
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))


#---------------------------------------------------------------------------- index search movies ----------------------------------------------------------------------------------------------------#

def Search2(query):
    try:
        url = 'http://oneclickwatch.ws/' + query + '/'
        url = url.replace(' ', '-')
        print url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match1 = re.compile('<h2 class="title">(.+?)</h2>.+?.+?src="(.+?)"', re.DOTALL).findall(html)
        match = re.compile('<a href="(.+?)" rel="nofollow"', re.DOTALL).findall(html)
        match2 = re.compile('href="(http://uptobox.com/.+?)"').findall(content)
        match3 = re.compile('<meta name="description" itemprop="description" content="(.+?)" />').findall(content)
        for name, img in match1:
                addon.add_directory({'mode': 'PlayVideo1', 'url': url, 'listitem': listitem}, {'title': '[COLOR pink][B](' + name + ')[/B][/COLOR]' }, img= img, fanart=FanartPath + 'fanart.jpg')
        for name in match3:
                addon.add_directory({'mode': 'PlayVideo1', 'url': url, 'listitem': listitem}, {'title': '[COLOR blue][B]' + '(OCW) ' + name.replace('http://www.tvguide.com/', '').replace('http://www.tvrage.com/', '').replace('/', ' ').replace(';', ' ').replace('-', ' ').replace('tvshows', ' ').replace('_', ' ') + '[/B][/COLOR]' }, img= 'https://briantudor.files.wordpress.com/2010/12/tv-icon1.png', fanart=FanartPath + 'fanart.jpg')
        for url in match2:
                addon.add_directory({'mode': 'GetLinks1', 'url':  url, 'listitem': listitem}, {'title':  'UpToStream : direct link'}, img= 'https://uptostream.com/images/logo.png', fanart=FanartPath + 'fanart.jpg')
        for url in match:
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host.replace('oneclickwatch.ws', 'Streamimg links below') }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.jpg')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]No Links in OCW [/B][/COLOR],[COLOR blue][B]Trying rlsseries[/B][/COLOR],7000,"")")
    try:
        url = 'http://300mbmovies4u.com/hollywood-movie/' + query + '/'
        url = url.replace(' ', '-')
        print url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match3 = re.compile('content="width=device-width, initial-scale=1.0"/><title>(.+?)</title>', re.DOTALL).findall(html)
        match2 = re.compile('href="(http://uptobox.com/.+?)"').findall(content)
        match = re.compile('href="(.+?)"').findall(content)
        for name in match3:
                addon.add_directory({'mode': 'PlayVideo1', 'url': url, 'listitem': listitem}, {'title': '[COLOR blue][B]' + name.replace('300mbmovies4u.com', '(300mbmovies4u.com)  ') + '[/B][/COLOR]' }, img= 'https://briantudor.files.wordpress.com/2010/12/tv-icon1.png', fanart=FanartPath + 'fanart.jpg')
        for url in match2:
                addon.add_directory({'mode': 'GetLinks1', 'url':  url, 'listitem': listitem}, {'title':  'UpToStream : direct link'}, img= 'https://uptostream.com/images/logo.png', fanart=FanartPath + 'fanart.jpg')
        for url in match:
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.jpg')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]No Links in 300mbmovies4u [/B][/COLOR],[COLOR blue][B]Trying rlsseries[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

##.replace('/', ' ')## \s*? ##
############################################################################### Get links #############################################################################################

def GetLinks(section, url):
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<a href="(.+?)" rel="nofollow" target="_blank">.+?</a><br />').findall(content)
        match1 = re.compile('href="(http://uptobox.com/.+?)"').findall(content)
        listitem = GetMediaInfo(content)
        for url in match1:
                addon.add_directory({'mode': 'GetLinks1', 'url':  url, 'listitem': listitem}, {'title':  'UpToStream : direct link'}, img= 'https://uptostream.com/images/logo.png', fanart=FanartPath + 'fanart.jpg')
        for url in match:
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks1(section, url):
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('Streaming link: <a href="(.+?)" class="blue_link">.+?</a>').findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                addon.add_directory({'mode': 'GetLinks1a', 'url': url, 'listitem': listitem}, {'title':  'load stream' + ' : ' + url}, img= 'https://uptostream.com/images/logo.png', fanart=FanartPath + 'fanart.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks1a(section, url):
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile("<source src='(.+?)' type='.+?' data-res='(.+?)'").findall(content)
        listitem = GetMediaInfo(content)
        for url, name in match:
                addon.add_directory({'mode': 'PlayVideo1', 'url': url, 'listitem': listitem}, {'title': name }, img= 'https://uptostream.com/images/logo.png', fanart=FanartPath + 'fanart.jpg')
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

def PlayVideo1(url, listitem):
        addon_handle = int(sys.argv[1])
        xbmcplugin.setContent(addon_handle, 'video')
        li = xbmcgui.ListItem('[COLOR dodgerblue][B]PLAY STREAM[/B][/COLOR]  >> ', iconImage='https://lh5.googleusercontent.com/-p2h0tx7Trgs/Uzu-3kxzKuI/AAAAAAAAOsU/sVJKqxSMY-4/s319/watch2.jpg', thumbnailImage= 'http://s29.postimg.org/8z8jd5x5j/logo1.png')
        li.setProperty('fanart_image', 'http://i.ytimg.com/vi/a-lCl3ZuZrE/maxresdefault.jpg')
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

###################################################################### menus ####################################################################################################

def MainMenu():    #homescreen
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]OCW Latest Added Movies[/B] [/COLOR]>>'}, img=IconPath + 'movies1.png', fanart=FanartPath + 'fanart.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/tv-shows/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]OCW Latest Added Episodes[/B] [/COLOR]>>'}, img=IconPath + 'tv2.png', fanart=FanartPath + 'fanart.jpg')
        addon.add_directory({'mode': 'GetTitles6', 'section': 'ALL', 'url': BASE_URL6 + '/cat/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orchid][B]TV Calendar [/B][/COLOR]'}, img=IconPath + 'indexs.png', fanart=FanartPath + 'fanart.jpg')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL1 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR greenyellow][B]TV Index Search[/B] (A-Z)[/COLOR]'}, img=IconPath + 'indexs.png', fanart=FanartPath + 'fanart.jpg')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL2 + '/category/tv-shows/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR greenyellow][B]TV Index Search[/B] (Episodes)[/COLOR]'}, img=IconPath + 'indexs.png', fanart=FanartPath + 'fanart.jpg')
        addon.add_directory({'mode': 'GetTitles4', 'url': BASE_URL4 + '/movies/'}, {'title':  '[COLOR greenyellow][B]Movies Index Search[/B] (Top Movies)[/COLOR]'}, img=IconPath + 'indexs.png', fanart=FanartPath + 'fanart.jpg')
        addon.add_directory({'mode': 'GetTitles5', 'url': BASE_URL5 + '/new-movie-releases'}, {'title':  '[COLOR greenyellow][B]Movies Index Search[/B] (Box Office)[/COLOR]'}, img=IconPath + 'indexs.png', fanart=FanartPath + 'fanart.jpg')
        addon.add_directory({'mode': 'GetSearchQuery'},  {'title':  '[COLOR green][B]OCW[/B] Search (google)[/COLOR]'}, img=IconPath + 'searchs1.png', fanart=FanartPath + 'fanart.jpg')
        addon.add_directory({'mode': 'ResolverSettings'}, {'title':  '[COLOR red]Resolver Settings[/COLOR]'}, img=IconPath + 'resolver1.png', fanart=FanartPath + 'fanart.jpg') 
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

######################################################################## search google #################################################################################################

def GetSearchQuery():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search(query)
	else:
                return  
def Search(query):
        url = 'http://www.google.com/search?q=site:oneclickwatch.ws ' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h3 class="r"><a href="(.+?)".+?onmousedown=".+?">(.+?)</a>').findall(html)
        for url, title in match:
                title = title.replace('<b>...</b>', '').replace('<em>', '').replace('</em>', '')
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title})
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

########################################################################################################################################################################

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



#################################################################################################################################################################################

if mode == 'main': 
	MainMenu()
elif mode == 'HelpMenu':
        HelpMenu()
elif mode == 'GetTitles': 
	GetTitles(section, url, startPage, numOfPages)
elif mode == 'GetTitles1': 
	GetTitles1(query, section)
elif mode == 'GetTitles2': 
	GetTitles2(section, url, startPage, numOfPages)
elif mode == 'GetTitles3': 
	GetTitles3(query, startPage, numOfPages)
elif mode == 'GetTitles4': 
	GetTitles4(query)
elif mode == 'GetTitles5': 
	GetTitles5(query)
elif mode == 'GetTitles6': 
	GetTitles6(section, url, startPage, numOfPages)
elif mode == 'GetTitles6a': 
	GetTitles6a(query, section)
elif mode == 'GetLinks':
	GetLinks(section, url)
elif mode == 'GetLinks1':
	GetLinks1(section, url)
elif mode == 'GetLinks1a':
	GetLinks1a(section, url)
elif mode == 'GetSearchQuery':
	GetSearchQuery()
elif mode == 'Search':
	Search(query)
elif mode == 'Search1':
	Search1(query)
elif mode == 'Search2':
	Search2(query)
elif mode == 'PlayVideo':
	PlayVideo(url, listitem)
elif mode == 'PlayVideo1':
	PlayVideo1(url, listitem)	
elif mode == 'ResolverSettings':
        urlresolver.display_settings()
xbmcplugin.endOfDirectory(int(sys.argv[1]))