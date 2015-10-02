
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
BASE_URL1 = 'http://www.rls-dl.com/'
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
                        req = urllib2.Request(url)
                        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3 Gecko/2008092417 Firefox/3.0.3')
                        response = urllib2.urlopen(req)
                        link=lemon.read()
                        response.close()
                match = re.compile('<h2 class="title"><a href="(.+?)" title=".+?">(.+?)<.+? src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png') 
                addon.add_directory({'mode': 'GetTitles', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'next.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site mite be down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------- rls-dl search ----------------------------------------------------------------------------------------------------#

def GetTitles1(query, startPage= '1', numOfPages= '1'): 
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
                addon.add_directory({'mode': 'GetTitles1', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'next.png', fanart= 'http://www.blazevideo.com/blog/wp-content/uploads/tv-shows-montage.jpg')
        setView('tvshows', 'tvshows-view')       
    except:
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

############################################################################### Get links #############################################################################################

def GetLinks(section, url):
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<a href="(.+?)" rel="nofollow" target="_blank">.+?</a><br />').findall(content)
        match1 = re.compile('href="(http://uptobox.com/.+?)"').findall(content)
        listitem = GetMediaInfo(content)
        for url in match1:
                addon.add_directory({'mode': 'GetLinks1', 'url':  url, 'listitem': listitem}, {'title':  'UpToStream : direct link'}, img= 'https://uptostream.com/images/logo.png', fanart= 'http://www.blazevideo.com/blog/wp-content/uploads/tv-shows-montage.jpg')
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
                addon.add_directory({'mode': 'GetLinks1a', 'url': url, 'listitem': listitem}, {'title':  'load stream' + ' : ' + url}, img= 'https://uptostream.com/images/logo.png', fanart= 'http://www.blazevideo.com/blog/wp-content/uploads/tv-shows-montage.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks1a(section, url):
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile("<source src='(.+?)' type='.+?' data-res='(.+?)'").findall(content)
        listitem = GetMediaInfo(content)
        for url, name in match:
                addon.add_directory({'mode': 'PlayVideo1', 'url': url, 'listitem': listitem}, {'title': name }, img= 'https://uptostream.com/images/logo.png', fanart= 'http://www.blazevideo.com/blog/wp-content/uploads/tv-shows-montage.jpg')
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
        li.setProperty('fanart_image', 'http://littletechboy.com/downloads/sins/modding/LoadingSplash.jpg')
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
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]OCW Latest Movies[/B] [/COLOR]>>'}, img=IconPath + 'movies.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/tv-shows/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]OCW Latest Tv episodes[/B] [/COLOR]>>'}, img=IconPath + 'tv.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL1 + '/category/tv-shows/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR green][B]Index[/B] Search Tv episodes[/COLOR]'}, img=IconPath + 'search.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery'},  {'title':  '[COLOR green][B]OCW[/B] Search (google)[/COLOR]'}, img=IconPath + 'search.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'ResolverSettings'}, {'title':  '[COLOR red]Resolver Settings[/COLOR]'}, img=IconPath + 'resolver.png', fanart=FanartPath + 'fanart.png')  
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


#------------------------------------------------------------------------ index search ----------------------------------------------------------------------------------------#


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
                addon.add_directory({'mode': 'PlayVideo1', 'url': url, 'listitem': listitem}, {'title': '[COLOR pink][B](' + name + ')[/B][/COLOR]' }, img= img, fanart=FanartPath + 'fanart.png')
        for name in match3:
                addon.add_directory({'mode': 'PlayVideo1', 'url': url, 'listitem': listitem}, {'title': '[COLOR blue][B]' + name + '[/B][/COLOR]' }, img= 'http://1.bp.blogspot.com/-oR18vqutgtA/VZbb1ZTZ3hI/AAAAAAAAOqc/_dt1ZdRQPD8/s1600/clapper2.png', fanart=FanartPath + 'fanart.png')
        for url in match2:
                addon.add_directory({'mode': 'GetLinks1', 'url':  url, 'listitem': listitem}, {'title':  'UpToStream : direct link'}, img= 'https://uptostream.com/images/logo.png', fanart=FanartPath + 'fanart.png')
        for url in match:
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host.replace('oneclickwatch.ws', 'Streamimg links below') }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]No Links [/B][/COLOR],[COLOR blue][B]Try OCW Google search [/B][/COLOR],7000,"")")


#################################################################################################################################################################################

    #try:
    #    url = 'http://moviesmaxim.com/' + query + '/'
    #    url = url.replace(' ', '-')
    #    print url
    #    html = net.http_GET(url).content
    #    listitem = GetMediaInfo(html)
    #    content = html
    #    match = re.compile('<a href="(.+?)" rel="nofollow"', re.DOTALL).findall(html)
    #    for url in match:
    #            host = GetDomain(url)
    #            if urlresolver.HostedMediaFile(url= url):
    #                    addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host + ' - ' + ' [COLOR green]...(MM)[/COLOR]' }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
    #except:
    #    xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry OneClickWatch search is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")


#################################################################################################################################################################################

if mode == 'main': 
	MainMenu()
elif mode == 'HelpMenu':
        HelpMenu()
elif mode == 'GetTitles': 
	GetTitles(section, url, startPage, numOfPages)
elif mode == 'GetTitles1': 
	GetTitles1(query, startPage, numOfPages)
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
elif mode == 'GetSearchQuery1':
	GetSearchQuery1()
elif mode == 'Search1':
	Search1(query)
elif mode == 'PlayVideo':
	PlayVideo(url, listitem)
elif mode == 'PlayVideo1':
	PlayVideo1(url, listitem)	
elif mode == 'ResolverSettings':
        urlresolver.display_settings()
xbmcplugin.endOfDirectory(int(sys.argv[1]))