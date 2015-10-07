import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import re, string, sys, os
import urlresolver
from TheYid.common.addon import Addon
from TheYid.common.net import Net
import HTMLParser
addon_id = 'plugin.video.theyidrh'
plugin = xbmcaddon.Addon(id=addon_id)
net = Net()
addon = Addon('plugin.video.theyidrh', sys.argv)
DB = os.path.join(xbmc.translatePath("special://database"), 'theyidrh.db')

########### url's ##########
BASE_URL2 = 'http://www.discovery360.net/'
BASE_URL3 = 'http://crazyhdsource.com/'
BASE_URL5 = 'http://www.theextopia.com/'
BASE_URL6 = 'http://com2dl.com/'
BASE_URL7 = 'http://2ddl.link/'
BASE_URL8 = 'http://sceper.ws/'
BASE_URL9 = 'http://scenedown.in/'
BASE_URL10 = 'http://www.ddlvalley.rocks/'
BASE_URL11 = 'http://www.rlsbb.com/'
BASE_URL12 = 'http://300mbmovies4u.com/'
BASE_URL15 = 'http://www.fullmatches.net/'
BASE_URL16 = 'http://tv-release.net/'
BASE_URL20 = 'http://0dayreleases.net/'
BASE_URL21 = 'http://www.moviefone.com/'
BASE_URL22 = 'http://rlsblog.se/'
BASE_URL24 = 'http://dx-tv.com/'
BASE_URL25 = 'http://www.tvhq.info/'
BASE_URL25b = 'http://www.allcinemamovies.com/'
BASE_URL26 = 'http://www.tvhq.info/'
BASE_URL27 = 'https://raw.githubusercontent.com/TheYid/yidpics/master'
BASE_URL28 = 'http://www.movie.huborama.com/'
BASE_URL29 = 'http://www.israbox.net/'
BASE_URL30 = 'http://scnlog.eu/'
BASE_URL31 = 'http://www.tvguide.com/'
BASE_URL41 = 'http://www.episodes-tv.com/'
BASE_URL42 = 'http://www.rls-dl.com/'
BASE_URL43 = 'http://www.pogdesign.co.uk/'
BASE_URL44 = 'http://watchseries-onlines.ch/'

BASE_URL1 = addon.get_setting('custurl')
if not BASE_URL1.endswith("/"):
    BASE_URL1 = BASE_URL1 + "/"

###### PATHS #########
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

#---------------------------------------------------------------------- 0dayreleases ----------------------------------------------------------------------------------------------#

def GetTitles1(section, url, startPage= '1', numOfPages= '1'):  
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
                match = re.compile('<h2 class="post-title"><a href="(.+?)" title=".+?" rel="bookmark">(.+?)</a></h2>.+?src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search10&query=%s)' %(name.strip().replace('.', ' '))
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip().replace('.', ' ')}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles1', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')        
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))


#---------------------------------------------------------------------- scnlog ----------------------------------------------------------------------------------------------#

def GetTitles2a(section, url, startPage= '1', numOfPages= '1'):  
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
                match = re.compile('title="" /><a href="(.+?)" rel="bookmark" title="(.+?)">.+?</a></h1>', re.DOTALL).findall(html)
                for movieUrl, name in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search10&query=%s)' %(name.strip().replace('.', ' '))
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip().replace('.', ' ')}, contextmenu_items= cm, img= 'https://pbs.twimg.com/profile_images/378800000657168025/6408df8fd1766c7621c717fa521a206d.png', fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles2a', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')        
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------- discovery360 ----------------------------------------------------------------------------------------------#

def GetTitles2(section, url, startPage= '1', numOfPages= '1'):  #music
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
                match = re.compile('<h3 class="btl"><img style=".+?" alt=".+?" src=".+?" title="(.+?)"><a href="(.+?)">.+?</a></h3>', re.DOTALL).findall(html)
                for name, movieUrl in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search10&query=%s)' %(name.strip().replace('.', ' '))
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks8', 'section': section, 'url': movieUrl}, {'title':  name.strip().replace('.', ' ')}, contextmenu_items= cm, img= 'http://website.informer.com/thumbnails/280x202/d/discovery360.net.png', fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles2', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')        
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
#----------------------------------------------------------------------------------rls-tv----------------------------------------------------------------------------------------------#

def GetTitles8(section, url, startPage= '1', numOfPages= '1'): 
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/index.php?page=' + startPage + ''
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/index.php?page=' + str(page) + ''
                        html = net.http_GET(pageUrl).content
                match = re.compile("width='.+?' style='text-align:left; font-size:12px;font-weight:bold;'><a href='(.+?)'>(.+?)-(.+?)</a></td><td", re.DOTALL).findall(html)
                for movieUrl, name, title, in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search10&query=%s)' %(name.strip().replace('X264', '').replace('x264', ''))
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks1', 'section': section, 'url': movieUrl}, {'title':  name.strip() + '-' + title}, contextmenu_items= cm, img=IconPath + 'rlstv.png', fanart=FanartPath + 'fanart.png') 
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-----------------------------------------------------------------------------------crazyhdsource---------------------------------------------------------------------------------------------#

def GetTitles3(section, url, startPage= '1', numOfPages= '1'): 
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
                match = re.compile('<h4><span>.+?href="(.+?)".+?>(.+?)<.+?src=.+? .+?="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search10&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles3', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue]Next...[/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------com2dl------------------------------------------------------------------------------------------------#

def GetTitles4(section, url, startPage= '1', numOfPages= '1'):
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
                match = re.compile('shstory4-img.+?href="(.+?)"><img src="(.+?)" alt="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, img, name in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search10&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles4', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')       
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------------300mbmovies4u--------------------------------------------------------------------------------------------#

def GetTitles5(section, url, startPage= '1', numOfPages= '1'): 
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
                match = re.compile('<li>\s*?<h2><a href="(.+?)" title=".+?">(.+?)</a></h2>\s*?<div class=".+?"><a href=".+?" title=".+?"><img src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search10&query=%s)' %(name.strip().replace('300MB', '').replace('400MB', '').replace('1.1GB', '').replace('900MB', '').replace('1.2GB', '').replace('1.8GB', '').replace('800MB', '').replace('350MB', '').replace('700MB', '').replace('1.7GB', '').replace('x264', ''))
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles5', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view') 
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#----------------------------------------------------------------------------Scene down----------------------------------------------------------------------------------------------------#

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
                match = re.compile('postTitle.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search10&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles6', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')        
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-----------------------------------------------------------------------------------Sceper---------------------------------------------------------------------------------------------#

def GetTitles7(section, url, startPage= '1', numOfPages= '1'): 
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
                match = re.compile('<h2.+?href="(.+?)">(.+?)<.+?src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search10&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles7', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')       
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))


#----------------------------------------------------------------------------scnsrc----------------------------------------------------------------------------------------------------#

def GetTitles1(section, url, startPage= '1', numOfPages= '1'): 
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
                match = re.compile('<h2>.+?href="(.+?)".+?>(.+?)<.+?.+?src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search10&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles1', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')        
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------#

def GetTitles10(section, url, startPage= '1', numOfPages= '1'): #scnsrc tv
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
                match = re.compile('<h2> <a href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h2>', re.DOTALL).findall(html)
                for movieUrl, name in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search10&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= 'https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png', fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles10', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')       
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------------ddlv-----------------------------------------------------------------------------------------------#

def GetTitles11(section, url, startPage= '1', numOfPages= '1'): 
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
                match = re.compile('<h2>.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search10&query=%s)' %(name.strip().replace('.', ' '))
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks3', 'section': section, 'url': movieUrl}, {'title':  name.strip().replace('.', ' ')}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles11', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')        
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------rlsbb------------------------------------------------------------------------------------------------#

def GetTitles12(section, url, startPage= '1', numOfPages= '1'): 
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
                match = re.compile('postHeader.+?href="(.+?)".+?>(.+?)<.+?src=.+? src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search10&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles12', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------#

def GetTitles13(section, url, startPage= '1', numOfPages= '1'):  #rbbsport
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + ''
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + ''
                        html = net.http_GET(pageUrl).content                      
                match = re.compile('postTitle.+?href="(.+?)".+?>(.+?)<.+?src=.+?src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')                        
                addon.add_directory({'mode': 'GetTitles13', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue]Come back soon[/COLOR]'}, img=IconPath + '', fanart=FanartPath + 'fanart.png')        
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------------Extopia-----------------------------------------------------------------------------------------------#

def GetTitles14(section, url, startPage= '1', numOfPages= '1'): 
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
                match = re.compile('<h2><a.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search10&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles14', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')       
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------fullmatch------------------------------------------------------------------------------------------------#

def GetTitles16(section, url, startPage= '1', numOfPages= '1'): 
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
                match = re.compile('<h2><a.+?href="(.+?)".+?>(.+?)<.+?src=.+?.+?', re.DOTALL).findall(html)
                for movieUrl, name in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search12&query=%s)' %(name.strip().replace('Download', '').replace('Full', '').replace('Match', ''))
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip().replace('Download', '')}, contextmenu_items= cm, img=IconPath + 'fullsport.png', fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles16', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------------- dx-tv --------------------------------------------------------------------------------------#

def GetTitles24(section, url, startPage= '1', numOfPages= '1'): 
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '?paged=' + startPage + ''
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '?paged=' + startPage + ''
                        html = net.http_GET(pageUrl).content                         
                match = re.compile('entry-title.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search11&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks5', 'section': section, 'url': movieUrl}, {'title':  name.strip().replace('.', ' ')}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')    
                addon.add_directory({'mode': 'GetTitles24', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------------- github -----------------------------------------------------------------------------------#

def GetTitles27(url):
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<>title="(.+?)" href="(.+?)" />< src="(.+?)"').findall(content)
        for name, url, img in match:
                addon.add_directory({'mode': 'PlayVideo3', 'url': url, 'listitem': listitem}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def PlayVideo3(url, listitem):
    try:
        print 'in PlayVideo %s' % url
        stream_url = urlresolver.HostedMediaFile(url).resolve()
        xbmc.Player().play(stream_url)
        addon.add_directory({'mode': 'help'}, {'title':  '[COLOR slategray][B]^^^ Press back ^^^[/B] [/COLOR]'},'','')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry Link may have been removed ![/B][/COLOR],[COLOR lime][B]Please try a different link/host !![/B][/COLOR],7000,"")")

#----------------------------------------------------------------------2ddl----------------------------------------------------------------------------------------------#

def GetTitles33(section, url, startPage= '1', numOfPages= '1'):  
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
                match = re.compile('<h2>.+?href="(.+?)".+?>(.+?)<.+?.+?src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search10&query=%s)' %(name.strip().replace('.', ' '))
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip().replace('.', ' ')}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles33', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')        
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------- israbox ----------------------------------------------------------------------------------------------#

def GetTitles29(section, url, startPage= '1', numOfPages= '1'):  
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
                match = re.compile('<h2><a href="(.+?)">(.+?)</a></h2>\s*?<div class="content">\s*?<a href=".+?"><img src="(.+?)" alt=".+?" class=".+?" /></a>', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search10&query=%s)' %(name.strip().replace('.', ' '))
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks8', 'section': section, 'url': movieUrl}, {'title':  name.strip().replace('.', ' ')}, contextmenu_items= cm, img= img.replace('/uploads/posts/', 'http://www.israbox.net/uploads/posts/'), fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles29', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')        
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------- rlsblog ----------------------------------------------------------------------------------------------------#

def GetTitles22(section, url, startPage= '1', numOfPages= '1'): 
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
                match = re.compile('<h2 class="title">.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search10&query=%s)' %(name.strip().replace('.', ' '))
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip().replace('.', ' ')}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles22', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')        
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------- rls-dl ----------------------------------------------------------------------------------------------------#

def GetTitles42(section, url, startPage= '1', numOfPages= '1'): 
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
                match = re.compile('<div class="thumbn"><img src="(.+?)" alt="(.+?)" /></div>\s*?<div class="filmkutu-bilgi-hover">\s*?<ul class="filmkutu-bilgi-hover-liste">\s*?<li class="izlenme">\s*?<a href="(.+?)">', re.DOTALL).findall(html)
                for img, name, movieUrl in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.theyidrh/?mode=Search10&query=%s)' %(name.strip().replace('.', ' '))
        		cm.append(('[COLOR blue]R[/COLOR]elease Search', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip().replace('.', ' ')}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles42', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')        
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))


###################################### index ################################## index ################################################# index ##########################################

#---------------------------------------------------------------------------- TV Calendar index ----------------------------------------------------------------------------------------------------#

def GetTitles43(section, url):
    try:
        pageUrl = url
        html = net.http_GET(pageUrl).content
        match = re.compile('<strong><a href="./day/(.+?)" title="(.+?)">', re.DOTALL).findall(html)
        match1 = re.compile('<div class="month_name"><div class="prev-month"><a href="/cat/(.+?)"><span>.+?</span> <strong>(.+?)</strong></a></div> <h1><a href=".+?">.+?</a></h1> <div class=".+?"><a href=".+?"><span>.+?</span> <strong>.+?</strong></a></div></div><div id="loginbox"', re.DOTALL).findall(html)
        match2 = re.compile('<div class="next-month"><a href="/cat/(.+?)"><span>.+?</span> <strong>(.+?)</strong></a></div></div>\s*?<div class="box728 atop">', re.DOTALL).findall(html)
        for movieUrl, name in match1:
                addon.add_directory({'mode': 'GetTitles43', 'section': section, 'url': 'http://www.pogdesign.co.uk/cat/' + movieUrl }, {'title': '<< ' + name}, img= 'https://www.globalbrigades.org/media_gallery/thumb/320/0/VRS_Calendar2_512x512x32_2.png',  fanart=FanartPath + 'fanart.png') 
        for movieUrl, name in match:
                addon.add_directory({'mode': 'GetTitles43a', 'section': section, 'url': 'http://www.pogdesign.co.uk/cat/day/' + movieUrl }, {'title': '[B]' + name.replace('Thursday 1st October 2015', 'Choose a day') + '[/B]'}, img= 'https://www.globalbrigades.org/media_gallery/thumb/320/0/VRS_Calendar2_512x512x32_2.png',  fanart=FanartPath + 'fanart.png') 
        for movieUrl, name in match2:
                addon.add_directory({'mode': 'GetTitles43', 'section': section, 'url': 'http://www.pogdesign.co.uk/cat/' + movieUrl }, {'title': name + ' >>'}, img= 'https://www.globalbrigades.org/media_gallery/thumb/320/0/VRS_Calendar2_512x512x32_2.png',  fanart=FanartPath + 'fanart.png') 
    except:
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetTitles43a(query, section): 
    try:
        pageUrl = url
        html = net.http_GET(pageUrl).content                     
        match = re.compile('<div class="contbox ovbox" style=" background-image: url(.+?);">\s*?<h4><a href=".+?">(.+?)<span>.+?</span></a></h4>\s*?<h5><a href=".+?">(.+?)<span>(.+?)/span></a></h5>\s*?<div class=".+?">(.+?)<a href=".+?">.+?</a></div> \s*?<ul class=".+?">\s*?<li><strong>.+?</strong>(.+?)</li>',re.DOTALL).findall(html)
        for img, name1, query1, name, sum, time in match:
                img = 'http://www.pogdesign.co.uk/' + img.replace('(', '').replace(')', '')
                query = name1.replace('[', '').replace(']', '') + name.replace("'", "").replace(' 1,', '01').replace(' 2,', '02').replace(' 3,', '03').replace(' 4,', '04').replace(' 5,', '05').replace(' 6,', '06').replace(' 7,', '07').replace(' 8,', '08').replace(' 9,', '09').replace(' 1<', '01').replace(' 2<', '02').replace(' 3<', '03').replace(' 4<', '04').replace(' 5<', '05').replace(' 6<', '06').replace(' 7<', '07').replace(' 8<', '08').replace(' 9<', '09').replace('Season', 's').replace('Episode', 'e').replace(',', '').replace('<', '').replace('-', '').replace(' ', '').replace('(', '').replace(')', '')
                title = '[COLOR blue][B]' + name1 +'[/B][/COLOR]' + ' - ' + '[COLOR lime]' + query1 + '[/COLOR]' + ' - ' + '[COLOR pink][I]' + name.replace('<', ' ') + '[/I][/COLOR]' + ' - ' + '[COLOR khaki]' + sum + '[/COLOR]' + ' - ' + time
                query = query.replace('This Is England ', 'this is england 90 ')
                query = query.replace('Doctor Who ', 'Doctor Who 2005 ')
                query = query.replace('The Late Late Show Corden ', 'James Corden 2015')
                addon.add_directory({'mode': 'Search12', 'section': section, 'query': query}, {'title': title}, img= img,  fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'calendar-view')
    except:
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------- watchseries-onlines a/z index ----------------------------------------------------------------------------------------------------#

def GetTitles44(section, query):
    try:
        pageUrl = url
        html = net.http_GET(pageUrl).content
        match = re.compile('<option class="level-0" value=".+?">(.+?)</option>', re.DOTALL).findall(html)
        for movieUrl in match:
                addon.add_directory({'mode': 'Search12', 'section': section, 'query': movieUrl}, {'title': movieUrl}, img= 'https://briantudor.files.wordpress.com/2010/12/tv-icon1.png', fanart= 'http://www.blazevideo.com/blog/wp-content/uploads/tv-shows-montage.png') 
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site mite be down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------- TvHQ TV index ---------------------------------------------------------------------------------#

def GetTitles25a(query):
    try:
        pageUrl = url
        html = net.http_GET(pageUrl).content                     
        match = re.compile('<img class="img-responsive hoverZoomLink" src="(.+?)" alt="(.+?)">',re.DOTALL).findall(html)
        for img, query in match:
                addon.add_directory({'mode': 'Search12', 'query': query.replace('-', ' ').replace('[', ' ').replace(']', ' ') + ' s'}, {'title':  query.replace('-', ' ').replace('[', ' ').replace(']', ' ')}, img= img, fanart=FanartPath + 'fanart4.png')
        setView('tvshows', 'tvshows-view')
    except:
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
#\s*?#

#---------------------------------------------------------------------------------- allcinemamovies index TV -----------------------------------------------------------------------------------#

def GetTitles25b(query):
    try:
        pageUrl = url
        html = net.http_GET(pageUrl).content                     
        match = re.compile('<img class="img-preview spec-border show-thumbnail"  src=".+?src=(.+?)&amp;w=130&amp;h=190&amp;zc=1" alt="Watch (.+?)Online" />',re.DOTALL).findall(html)
        for img, query in match:
                addon.add_directory({'mode': 'Search12', 'query': query.replace('-', ' ').replace('[', ' ').replace(']', ' ') + ' s'}, {'title':  query.replace('-', ' ').replace('[', ' ').replace(']', ' ')}, img= img, fanart=FanartPath + 'fanart4.png')
        setView('tvshows', 'tvshows-view')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------- moviefone index ---------------------------------------------------------------------------------#

def GetTitles32(query):
    try:
        pageUrl = url
        html = net.http_GET(pageUrl).content                     
        match = re.compile('<img name="replace-image" rel=".+?" id=".+?" class=".+?" src=".+?" data-src="(.+?)" alt="(.+?)"/>',re.DOTALL).findall(html)
        for img, query in match:
                addon.add_directory({'mode': 'Search10', 'query': query}, {'title':  query}, img= img, fanart=FanartPath + 'fanart3.png')
        setView('tvshows', 'tvshows-view')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------------- movie index  -----------------------------------------------------------------------------------#

def GetTitles28(query):
    try:
        pageUrl = url
        html = net.http_GET(pageUrl).content                     
        match = re.compile('<div class="thumb ph " title="(.+?)">\s*?<a class=".+?" href=".+?" title=".+?" target="_blank" style="" rel="nofollow"><img src=".+?" class="ph"/></a>\s*?<a href=".+?" title=".+?" target="_blank" rel="nofollow">\s*?<div class="thumb_img_wrapper"><img src="(.+?)" alt=".+?" style=".+?" class="ph"/></div>',re.DOTALL).findall(html)
        for query, img in match:
                addon.add_directory({'mode': 'Search10', 'query': query.replace('(', '').replace(')', '').replace('.', ' ').replace('[', '').replace(']', '').replace('-', ' ').replace('RARBG', '').replace('MAJESTiC', '').replace('ACAB', '').replace('MP3', '')}, {'title':  query.replace('.', ' ').replace('[', '').replace(']', '')}, img= img, fanart=FanartPath + 'fanart3.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------- tvguide index ---------------------------------------------------------------------------------#

def GetTitles34(query):
    try:
        pageUrl = url
        html = net.http_GET(pageUrl).content                     
        match = re.compile('<span class="show-card show-card-small">\s*?<img src="(.+?)_100x133.png" class=".+?" alt=".+?" title="(.+?)" srcset=".+?" width=".+?" height=".+?" />',re.DOTALL).findall(html)
        for img, query in match:
                addon.add_directory({'mode': 'Search12', 'query': query}, {'title':  query}, img= img + '_1000x339.png', fanart=FanartPath + 'fanart4.png')
        setView('tvshows', 'tvshows-view')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#----------------------------------------------------------------------------- episodes-tv index ---------------------------------------------------------------------------------#

def GetTitles41(query, startPage= '1', numOfPages= '1'): 
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
                match = re.compile('<div class="movieposter" title="Watch Video (.+?)" >\s*?<a href=".+?"><img class="bannersIMG" src="(.+?)" alt=".+?" title=".+?" /></a>', re.DOTALL).findall(html)
                for query, img in match:
                        addon.add_directory({'mode': 'Search12', 'section': section, 'query': query}, {'title':  query}, img= img, fanart=FanartPath + 'fanart4.png')
                addon.add_directory({'mode': 'GetTitles41', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart4.png') 
        setView('tvshows', 'tvshows-view')       
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site mite be down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------- rls-dl search ----------------------------------------------------------------------------------------------------#

def GetTitles42a(section, url, startPage= '1', numOfPages= '1'): 
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
                match = re.compile('<div class="thumbn"><img src="(.+?)" alt="(.+?)" /></div>\s*?<div class="filmkutu-bilgi-hover">\s*?<ul class="filmkutu-bilgi-hover-liste">\s*?<li class="izlenme">\s*?<a href="(.+?)">', re.DOTALL).findall(html)
                for img, name, movieUrl in match:
                        addon.add_directory({'mode': 'GetTitles42b', 'section': section, 'url': movieUrl}, {'title': name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles42a', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')  
        setView('tvshows', 'tvshows-view')       
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetTitles42b(query):
    try:
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<img class=".+?" src="(.+?)" alt="(.+?)" width=".+?" height=".+?" />').findall(content)
        for img, query in match:
                addon.add_directory({'mode': 'Search10', 'query': query}, {'title': '[COLOR blue][B]SEARCH : [/B][/COLOR]' + query}, img= img, fanart=FanartPath + 'fanart4.png')     
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site mite be down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))




##.replace('/', ' ')## \s*? ## 
#################################################################################getlinks###############################################################################################

def GetLinks(section, url): # Get Links
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        r = re.search('<strong>Links.*</strong>', html)
        if r:
                content = html[r.end():]

        r = re.search('commentblock', content)
        if r:
                content = content[:r.start()]
                
        match = re.compile('href="(.+?)"').findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                host = GetDomain(url)

                if 'Unknown' in host:
                                continue
                        
                # ignore .rar files
                r = re.search('\.rar[(?:\.html|\.htm)]*', url, re.IGNORECASE)
                if r:
                        continue

                if urlresolver.HostedMediaFile(url= url):
                        print 'in GetLinks if loop'
                        title = url.rpartition('/')
                        title = title[2].replace('.html', '')
                        title = title.replace('.htm', '')
                        title = title.replace('.rar', '[COLOR red][B][I]RAR no streaming[/B][/I][/COLOR]')
                        title = title.replace('rar', '[COLOR red][B][I]RAR no streaming[/B][/I][/COLOR]')
                        title = title.replace('sample', '[COLOR lime]Movie Trailer[/COLOR]')
                        title = title.replace('www.', '')
                        title = title.replace ('-',' ')
                        title = title.replace('_',' ')
                        title = title.replace('.',' ')
                        title = title.replace('gaz','')
                        title = title.replace('NTb','')
                        title = title.replace('1st','[COLOR coral][B]1st HALF[/B][/COLOR]')
                        title = title.replace('2nd','[COLOR coral][B]2nd HALF[/B][/COLOR]')
                        title = title.replace('fullmatches net','')
                        title = title.replace('.',' ')
                        title = title.replace('480p','[COLOR coral][B][I]480p[/B][/I][/COLOR]')
                        title = title.replace('720p','[COLOR gold][B][I]720p[/B][/I][/COLOR]')
                        title = title.replace('1080p','[COLOR orange][B][I]1080p[/B][/I][/COLOR]')
                        title = title.replace('mkv','[COLOR gold][B][I]MKV[/B][/I][/COLOR] ')
                        title = title.replace('avi','[COLOR pink][B][I]AVI[/B][/I][/COLOR] ')
                        title = title.replace('mp4','[COLOR purple][B][I]MP4[/B][/I][/COLOR] ')
                        title = title.replace('%20',' ')
                        host = host.replace('youtube.com','[COLOR lime]Movie Trailer[/COLOR]')
                        host = host.replace('k2s.cc','[COLOR red]Unsupported Link[/COLOR]')
                        host = host.replace('ryushare.com','[COLOR red]Unsupported Link[/COLOR]')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host + ' [COLOR gold]:[/COLOR] ' + title }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')

        find = re.search('commentblock', html)
        if find:
                print 'in comments if'
                html = html[find.end():]
                match = re.compile('<a href="(.+?)" rel="nofollow"', re.DOTALL).findall(html)
                print len(match)
                for url in match:
                        host = GetDomain(url)
                        if 'Unknown' in host:
                                continue
                        
                        # ignore .rar files
                        r = re.search('\.rar[(?:\.html|\.htm)]*', url, re.IGNORECASE)
                        if r:
                                continue
                        try:
                                if urlresolver.HostedMediaFile(url= url):
                                        print 'in GetLinks if loop'
                                        title = url.rpartition('/')
                                        title = title[2].replace('.html', '')
                                        title = title.replace('.htm', '')
                                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host + ' : ' + title}, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')

                        except:

                                continue


        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------------RLStv-----------------------------------------------------------------------------------------------#

def GetLinks1(section, url): 
    try:
        html = net.http_GET(str(url)).content
        sources = []
        listitem = GetMediaInfo(html)
        print 'LISTITEM: '+str(listitem)
        content = html
        print'CONTENT: '+str(listitem)
        r = re.search('<strong>Links.*</strong>', html)
        if r:
                content = html[r.end():]
        match = re.compile("href='(.+?)'").findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                host = GetDomain(url)

                if 'Unknown' in host:
                        continue
                print '*****************************' + host + ' : ' + url
                title = url.rpartition('/')
                name = host
                hosted_media = urlresolver.HostedMediaFile(url=url, title=name)
                sources.append(hosted_media)
        find = re.search('commentblock', html)
        if find:
                print 'in comments if'
                html = html[find.end():]
                print 'MATCH IS: '+str(match)
                print len(match)
                for url in match:
                        host = GetDomain(url)
                        if 'Unknown' in host:
                                continue
        source = urlresolver.choose_source(sources)
        if source: stream_url = source.resolve()
        else: stream_url = ''
        xbmc.Player().play(stream_url)
        addon.add_directory({'mode': 'help'}, {'title':  '[COLOR slategray][B]^^^ Press back ^^^[/B] [/COLOR]'},'','')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry Link may have been removed ![/B][/COLOR],[COLOR lime][B]Please try a different link/host !![/B][/COLOR],7000,"")")

#-------------------------------------------------------------------------------ddlvalley-------------------------------------------------------------------------------------------------#

def GetLinks3(section, url): 
    try:
        html = net.http_GET(str(url)).content
        sources = []
        listitem = GetMediaInfo(html)
        print 'LISTITEM: '+str(listitem)
        content = html
        print'CONTENT: '+str(listitem)
        match = re.compile('href="(.+?)"').findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                host = GetDomain(url)
                if 'Unknown' in host:
                                continue
                r = re.search('\part1\part2\part3\part4\part5\.rar.html\.rar\.file[(?:\.html|\.htm)]*', url, re.IGNORECASE)
                if r:
                        continue
                print '*****************************' + host + ' : ' + url
                title = url.rpartition('/')
                title = title[2].replace('.html', '')
                title = title.replace('.htm', '')
                title = title.replace('.rar', '[COLOR red][B][I]RAR no streaming[/B][/I][/COLOR]')
                title = title.replace('DDLValley.net_', ' ')
                title = title.replace('www.', '')
                title = title.replace ('-','')
                title = title.replace('_',' ')
                title = title.replace('gaz','')
                title = title.replace('NTb','')
                title = title.replace('part1','')
                title = title.replace('part2','')
                title = title.replace('part3','')
                title = title.replace('part4','')
                title = title.replace('part5','')
                title = title.replace('.',' ')
                title = title.replace('720p','[COLOR gold][B][I]720p[/B][/I][/COLOR]')
                title = title.replace('1080p','[COLOR orange][B][I]1080p[/B][/I][/COLOR]')
                title = title.replace('mkv','[COLOR gold][B][I]MKV[/B][/I][/COLOR] ')
                title = title.replace('avi','[COLOR pink][B][I]AVI[/B][/I][/COLOR] ')
                title = title.replace('mp4','[COLOR purple][B][I]MP4[/B][/I][/COLOR] ')
                name = host+'-'+title
                hosted_media = urlresolver.HostedMediaFile(url=url, title=name)
                sources.append(hosted_media)
        source = urlresolver.choose_source(sources)
        if source: stream_url = source.resolve()
        else: stream_url = ''
        xbmc.Player().play(stream_url)
        addon.add_directory({'mode': 'help'}, {'title':  '[COLOR slategray][B]^^^ Press back ^^^[/B] [/COLOR]'},'','')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry Link may have been removed ![/B][/COLOR],[COLOR lime][B]Please try a different link/host !![/B][/COLOR],7000,"")")

#-------------------------------------------------------------------------------dxtv--------------------------------------------------------------------------------------#

def GetLinks5(section, url): 
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<span style="color: #008000;"><strong>(.+?)<').findall(content)
        match1 = re.compile('(http://u.+?)<').findall(content)
        match2 = re.compile('(http://rapidgator.net/file/.+?)<').findall(content)
        match3 = re.compile('(https://www.secureupload.eu/.+?)<').findall(content)
        match4 = re.compile('<p><iframe src="(.+?)"').findall(content)
        listitem = GetMediaInfo(content)
        for url in match + match1 + match2 + match3 + match4:
                host = GetDomain(url)

                if 'Unknown' in host:
                                continue
                        
                # ignore .rar files
                r = re.search('\.rar[(?:\.html|\.htm)]*', url, re.IGNORECASE)
                if r:
                        continue

                if urlresolver.HostedMediaFile(url= url):
                        print 'in GetLinks if loop'
                        title = url.rpartition('/')
                        title = title[2].replace('.html', '')
                        title = title.replace('.htm', '')
                        title = title.replace('480p','[COLOR coral][B][I]480p[/B][/I][/COLOR]')
                        title = title.replace('720p','[COLOR gold][B][I]720p[/B][/I][/COLOR]')
                        title = title.replace('1080p','[COLOR orange][B][I]1080p[/B][/I][/COLOR]')
                        title = title.replace('mkv','[COLOR gold][B][I]MKV[/B][/I][/COLOR] ')
                        title = title.replace('avi','[COLOR pink][B][I]AVI[/B][/I][/COLOR] ')
                        title = title.replace('mp4','[COLOR purple][B][I]MP4[/B][/I][/COLOR] ')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host + ' [COLOR gold]:[/COLOR] ' + title }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------------------------------ufd--------------------------------------------------------------------------------------#

def GetLinks6(section, url): 
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<p>(.+?)</p>').findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                host = GetDomain(url)

                if 'Unknown' in host:
                                continue
                if urlresolver.HostedMediaFile(url= url):
                        print 'in GetLinks if loop'
                        title = url.rpartition('/')
                        title = title[2].replace('.html', '')
                        title = title.replace('.htm', '')
                        title = title.replace('480p','[COLOR coral][B][I]480p[/B][/I][/COLOR]')
                        title = title.replace('720p','[COLOR gold][B][I]720p[/B][/I][/COLOR]')
                        title = title.replace('1080p','[COLOR orange][B][I]1080p[/B][/I][/COLOR]')
                        title = title.replace('mkv','[COLOR gold][B][I]MKV[/B][/I][/COLOR] ')
                        title = title.replace('avi','[COLOR pink][B][I]AVI[/B][/I][/COLOR] ')
                        title = title.replace('mp4','[COLOR purple][B][I]MP4[/B][/I][/COLOR] ')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host + ' [COLOR gold]:[/COLOR] ' + title }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))


#-------------------------------------------------------------------------------rlssource--------------------------------------------------------------------------------------#

def GetLinks8(section, url): 
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('href=(.+?) target=_blank>.+?<').findall(content)
        match1 = re.compile('<a target="_blank" href="http://300mblinks.com/goto/(.+?)"').findall(content)
        match2 = re.compile('target="_blank">(.+?)</a>').findall(content)
        match3 = re.compile('href="(.+?)" target="_blank">').findall(content)
        listitem = GetMediaInfo(content)
        for url in match + match1 + match2 + match3:
                host = GetDomain(url)

                if 'Unknown' in host:
                                continue
                if urlresolver.HostedMediaFile(url= url):
                        print 'in GetLinks if loop'
                        title = url.rpartition('/')
                        title = title[2].replace('.html', '')
                        title = title.replace('.htm', '')
                        title = title.replace('480p','[COLOR coral][B][I]480p[/B][/I][/COLOR]')
                        title = title.replace('720p','[COLOR gold][B][I]720p[/B][/I][/COLOR]')
                        title = title.replace('1080p','[COLOR orange][B][I]1080p[/B][/I][/COLOR]')
                        title = title.replace('mkv','[COLOR gold][B][I]MKV[/B][/I][/COLOR] ')
                        title = title.replace('avi','[COLOR pink][B][I]AVI[/B][/I][/COLOR] ')
                        title = title.replace('mp4','[COLOR purple][B][I]MP4[/B][/I][/COLOR] ')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host + ' [COLOR gold]:[/COLOR] ' + title }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

############################################################################# PlayVideo #################################################################################

def PlayVideo(url, listitem):
    try:
        stream_url = urlresolver.HostedMediaFile(url).resolve()
        xbmc.Player().play(stream_url)
        addon.add_directory({'mode': 'help'}, {'title':  '[COLOR slategray][B]^^^ Press back ^^^[/B] [/COLOR]'},'','')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry Link may have been removed ![/B][/COLOR],[COLOR lime][B]Please try a different link/host !![/B][/COLOR],7000,"")")

#---------------------------------------------------------------------------------------------------------------#

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
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

############################################################################# homescreen ################################################################################################

def MainMenu():        
        addon.add_directory({'mode': 'menu2'}, {'title': '[COLOR blue][B]Movies >>[/B] [/COLOR]>>'}, img=IconPath + 'films.png', fanart=FanartPath + 'fanart.png') 
        addon.add_directory({'mode': 'menu4'}, {'title': '[COLOR darkorange][B]Tv Shows >>[/B] [/COLOR]>>'}, img=IconPath + 'tv2.png', fanart=FanartPath + 'fanart.png') 
        addon.add_directory({'mode': 'menu6'}, {'title': '[COLOR lemonchiffon][B]Sport >>[/B] [/COLOR]>>'}, img=IconPath + 'sport1.png', fanart=FanartPath + 'fanart.png') 
        addon.add_directory({'mode': 'menu7'}, {'title': '[COLOR violet][B]Anime >>[/B] [/COLOR]>>'}, img=IconPath + 'anex.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'MusicMenu'}, {'title':  '[COLOR cadetblue][B]Music >[/B][/COLOR] >'}, img=IconPath + 'music.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'menu5'}, {'title': '[COLOR green][B]Searches >>[/B] [/COLOR]>>'}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png') 
        addon.add_directory({'mode': 'ResolverSettings'}, {'title':  '[COLOR red]Resolver Settings[/COLOR]'}, img=IconPath + 'resolver.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[COLOR aquamarine][B]News & Help  >[/B][/COLOR] >'}, img=IconPath + 'newshelp.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------- Music ----------------------------------------------------------------------------------------#

def MusicMenu():
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL2 + '/music/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cadetblue][B]Latest Music[/B] [/COLOR] [COLOR pink](discovery360)[/COLOR] >>'}, img=IconPath + 'd360m.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL11 + '/category/music/',
                             'startPage': '1', 'numOfPages': '2'}, {'title':  '[COLOR cadetblue][B]Latest Music[/B] [/COLOR] [COLOR gold](ReleaseBB)[/COLOR] >>'}, img=IconPath + 'bbm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles29', 'section': 'ALL', 'url': BASE_URL29 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cadetblue][B]Latest Music[/B] [/COLOR] [COLOR rosybrown](israbox)[/COLOR] >>'}, img=IconPath + 'ib.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1])) 

#------------------------------------------------------------------------------- help ----------------------------------------------------------------------------------------#

def HelpMenu():  
        addon.add_directory({'mode': 'Help'}, {'title':  'Release [COLOR dodgerblue][B]HUB[/B][/COLOR] : [COLOR lime]News >[/COLOR] >'}, img=IconPath + 'twit.png', fanart=FanartPath + 'fanart.png') 
        addon.add_directory({'mode': 'GetTitles27', 'url': BASE_URL27 + '/help.txt'}, {'title':  '[COLOR deeppink][B]Help & how to vids >[/COLOR][/B] >'}, img=IconPath + 'h2.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[B][COLOR gold]If you like this addon[/COLOR][/B]'}, img=IconPath + 'twit.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[B][COLOR gold]Please install Entertainment HUB from TheYids REPO[/COLOR][/B]'}, img= 'https://raw.githubusercontent.com/TheYid/My-Repo/master/plugin.video.allinone/icon.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[B][COLOR gold]& if you like rave music install Rave player from TheYids REPO[/COLOR][/B]'}, img= 'https://raw.githubusercontent.com/TheYid/My-Repo/master/plugin.audio.raveplayer/icon.png', fanart= 'https://raw.githubusercontent.com/TheYid/My-Repo/master/plugin.audio.raveplayer/fanart.jpg')
        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[B][COLOR blue]System/Add-ons/Get Add-ons/TheYids REPO[/COLOR][/B]'}, img= 'https://raw.githubusercontent.com/TheYid/My-Repo/master/repository.TheYid/icon.png', fanart= 'https://raw.githubusercontent.com/TheYid/My-Repo/master/plugin.video.allinone/fanart.jpg')
        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[B][COLOR aqua]@TheYid009[/COLOR][/B] - [B][COLOR gold]Add me on twitter for all the latest news & updates..[/COLOR][/B]'}, img=IconPath + 'twit.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[B][COLOR red]This addon works best with a real-debrid.com premium account[/COLOR][/B]'}, img=IconPath + 'twit.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------- movies -------------------------------------------------------------------------------------------------#

def Menu2(): 
        addon.add_directory({'mode': 'GetTitles32', 'url': BASE_URL21 + '/new-movie-releases'}, {'title':  '[COLOR cornflowerblue][B]Box office[/B] [/COLOR]: [COLOR greenyellow]Index Search[/COLOR] (moviefone)'}, img=IconPath + 'isbo.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32', 'url': BASE_URL21 + '/dvd'}, {'title':  '[COLOR cornflowerblue][B]Featured[/B] [/COLOR]: [COLOR greenyellow]Index Search[/COLOR] (moviefone)'}, img=IconPath + 'inf.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32', 'url': BASE_URL21 + '/dvd/coming-soon'}, {'title':  '[COLOR cornflowerblue][B]Featured now[/B] [/COLOR]: [COLOR greenyellow]Index Search[/COLOR] (moviefone)'}, img=IconPath + 'inf.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28', 'url': BASE_URL28 + '/'}, {'title':  '[COLOR blue][B]Released Today[/B] [/COLOR]: [COLOR greenyellow]Index Search[/COLOR]'}, img=IconPath + 'reto.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL11 + '/category/movies/',
                             'startPage': '1', 'numOfPages': '2'}, {'title':  '[COLOR blue][B]Latest Movies[/B] [/COLOR] [COLOR gold](ReleaseBB)[/COLOR] >>'}, img=IconPath + 'moviebb.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles11', 'section': 'ALL', 'url': BASE_URL10 + '/category/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]Latest Movies[/B] [/COLOR] [COLOR powderblue](DDLvalley)[/COLOR] >>'}, img=IconPath + 'ddlmo.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL1 + '/films/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]Latest Movies[/B] [/COLOR] [COLOR orangered](Scene Source)[/COLOR] >>'}, img=IconPath + 'ssmovies.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles7', 'section': 'ALL', 'url': BASE_URL8 + '/category/movies',
                             'startPage': '1', 'numOfPages': '2'}, {'title':  '[COLOR blue][B]Latest Movies[/B] [/COLOR] [COLOR mediumspringgreen](Sceper)[/COLOR] >>'}, img=IconPath + 'scmovie.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL20 + '/category/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]Latest Movies[/B] [/COLOR] [COLOR olive](0DayReleases)[/COLOR] >>'}, img=IconPath + 'odm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles6', 'section': 'ALL', 'url': BASE_URL9 + '/category/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]Latest Movies[/B] [/COLOR] [COLOR plum](Scene down)[/COLOR] >>'}, img=IconPath + 'sdmovies.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles33', 'section': 'ALL', 'url': BASE_URL7 + '/category/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]Latest Movies[/B] [/COLOR] [COLOR yellow](2DDL)[/COLOR] >>'}, img=IconPath + '2d2.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles14', 'section': 'ALL', 'url': BASE_URL5 + '/category/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]Latest Movies[/B] [/COLOR] [COLOR whitesmoke](The Extopia)[/COLOR] >>'}, img=IconPath + 'exmo.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles22', 'section': 'ALL', 'url': BASE_URL22 + '/category/movies/',
                             'startPage': '1', 'numOfPages': '2'}, {'title':  '[COLOR blue][B]Latest Movies[/B] [/COLOR] [COLOR orangered](rlsblog)[/COLOR] >>'}, img=IconPath + 'rbm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'menu9'}, {'title': '[COLOR blue][B]Latest Movies[/B] [/COLOR] [COLOR crimson](300mb movies4u)[/COLOR] >>'}, img=IconPath + 'm4u1.png', fanart=FanartPath + 'fanart.png') 
        addon.add_directory({'mode': 'menu3'}, {'title': '[COLOR blue][B]Latest Movies[/B] [/COLOR] [COLOR powderblue](1080p Zone)[/COLOR] >>'}, img=IconPath + '10z.png', fanart=FanartPath + 'fanart.png') 
        addon.add_directory({'mode': 'GetSearchQuery10'},  {'title':  '[COLOR khaki][B]M[/COLOR][COLOR blue]E[/COLOR][COLOR salmon]G[/COLOR][COLOR darkseagreen]A[/COLOR][/B] [COLOR blue][B]R[/B][/COLOR]elease [COLOR blue][B]HUB[/B][/COLOR] (Movies) : [COLOR green]Search[/COLOR]'}, img=IconPath + 'rhs.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------------- 300mbmovies4u ----------------------------------------------------------------------------------------------#

def Menu9():   #300mbmovies4u
        addon.add_directory({'mode': 'GetTitles5', 'section': 'ALL', 'url': BASE_URL12 + '/category/hollywood-movie/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]Latest Movies[/B][/COLOR] [COLOR crimson](Hollywood) [/COLOR] >>'}, img=IconPath + 'm4u1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles5', 'section': 'ALL', 'url': BASE_URL12 + '/category/hollywood-movie/english-1080p-movie/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]HD 1080p Movies[/B][/COLOR] [COLOR crimson](Hollywood) [/COLOR] >>'}, img=IconPath + 'm4u1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles5', 'section': 'ALL', 'url': BASE_URL12 + '/category/bollywood-movie/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]Latest Movies[/B][/COLOR] [COLOR crimson](Bollywood) [/COLOR] >>'}, img=IconPath + 'm4u1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles5', 'section': 'ALL', 'url': BASE_URL12 + '/category/tamil-movie/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]Latest Movies[/B][/COLOR] [COLOR crimson](Tamil) [/COLOR] >>'}, img=IconPath + 'm4u1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles5', 'section': 'ALL', 'url': BASE_URL12 + '/category/hd-video/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]HD Music video[/B][/COLOR] [COLOR crimson](International) [/COLOR] >>'}, img=IconPath + 'm4u1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------- HD Zone movies ----------------------------------------------------------------------------------------------------------#

def Menu3():
        addon.add_directory({'mode': 'GetTitles5', 'section': 'ALL', 'url': BASE_URL12 + '/category/hollywood-movie/english-3d-movie/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR steelblue][B]Latest 3D[/B][/COLOR] [COLOR crimson](300mb movies4u) [/COLOR] >>'}, img=IconPath + 'm4u1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles11', 'section': 'ALL', 'url': BASE_URL10 + '/category/movies/yify-rips/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR steelblue][B]Latest YIFY[/B] [/COLOR] [COLOR powderblue](DDLvalley)[/COLOR] >>'}, img=IconPath + 'ddlmo.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL6 + '/movie/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]Latest Movies[/B] [/COLOR] [COLOR darkorchid](Com2dl.com)[/COLOR] >>'}, img=IconPath + 'commovies.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2a', 'section': 'ALL', 'url': BASE_URL30 + '/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]Latest Movies[/B] [/COLOR] [COLOR pink](scnlog)[/COLOR] >>'}, img=IconPath + 'slm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL20 + '/category/hd-720p-1080p/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]Latest Movies 1080p[/B] [/COLOR] [COLOR olive](0DayReleases)[/COLOR] >>'}, img=IconPath + 'odm.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------- tv -------------------------------------------------------------------------------------------------#

def Menu4():
        addon.add_directory({'mode': 'GetTitles43', 'section': 'ALL', 'url': BASE_URL43 + '/cat/'}, {'title':  '[COLOR orchid][B]*TV Calendar Search*[/B][/COLOR]'}, img=IconPath + 'tcs.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles44', 'section': 'ALL', 'url': BASE_URL44 + '/'}, {'title':  '[COLOR greenyellow][B]*TV Index Search[/B] (A-Z)*[/COLOR]'}, img=IconPath + 'tas.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles41', 'section': 'ALL', 'url': BASE_URL41 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest Episodes[/B] [/COLOR]: [COLOR green]Index Search[/COLOR] >>'}, img=IconPath + 'intvs.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles34', 'url': BASE_URL31 + '/tvshows/'}, {'title':  '[COLOR darkorange][B]Top Shows[/B] [/COLOR]: [COLOR green]Index Search[/COLOR]'}, img=IconPath + 'rt.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL11 + '/category/tv-shows/',
                             'startPage': '1', 'numOfPages': '2'}, {'title':  '[COLOR darkorange][B]Latest Tv Shows[/B] [/COLOR] [COLOR gold](ReleaseBB)[/COLOR] >>'}, img=IconPath + 'tvbb.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles22', 'section': 'ALL', 'url': BASE_URL22 + '/category/tv-shows/',
                             'startPage': '1', 'numOfPages': '2'}, {'title':  '[COLOR darkorange][B]Latest Tv Shows[/B] [/COLOR] [COLOR orangered](rlsblog)[/COLOR] >>'}, img=IconPath + 'rbt.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles33', 'section': 'ALL', 'url': BASE_URL7 + '/category/tv-shows/',
                             'startPage': '1', 'numOfPages': '2'}, {'title':  '[COLOR darkorange][B]Latest Tv Shows[/B] [/COLOR] [COLOR yellow](2DDL)[/COLOR] >>'}, img=IconPath + '2d.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles11', 'section': 'ALL', 'url': BASE_URL10 + '/category/tv-shows/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest Tv Shows[/B] [/COLOR] [COLOR powderblue](DDLvalley)[/COLOR] >>'}, img=IconPath + 'ddltv.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles7', 'section': 'ALL', 'url': BASE_URL8 + '/category/tv-shows',
                             'startPage': '1', 'numOfPages': '2'}, {'title':  '[COLOR darkorange][B]Latest Tv Shows[/B] [/COLOR] [COLOR mediumspringgreen](Sceper)[/COLOR] >>'}, img=IconPath + 'setv.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL1 + '/category/tv/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest Tv Shows[/B] [/COLOR] [COLOR orangered](Scene Source)[/COLOR] >>'}, img=IconPath + 'sstv.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles6', 'section': 'ALL', 'url': BASE_URL9 + '/category/tv-shows/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest Tv Shows[/B] [/COLOR] [COLOR plum](Scene down)[/COLOR] >>'}, img=IconPath + 'sdtv.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2a', 'section': 'ALL', 'url': BASE_URL30 + '/tv-shows/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest Tv Shows[/B] [/COLOR] [COLOR blue](scnlog)[/COLOR] >>'}, img=IconPath + 'slt1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles42', 'section': 'ALL', 'url': BASE_URL42 + '/category/tv-shows/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest Tv shows[/B] [/COLOR] [COLOR azure](rls-dl) [/COLOR]>>'}, img=IconPath + 'rls10.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles14', 'section': 'ALL', 'url': BASE_URL5 + '/category/tvshow/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest Releases[/B] [/COLOR] [COLOR whitesmoke](The Extopia)[/COLOR] >>'}, img=IconPath + 'extv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles5', 'section': 'ALL', 'url': BASE_URL12 + '/category/tv-shows/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest Tv Shows[/B][/COLOR] [COLOR crimson](300mb movies4u)[/COLOR] >>'}, img=IconPath + '3mb4.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'menu11'}, {'title': '[COLOR darkorange][B]Latest Added[/B] [/COLOR] [COLOR blue](1080p zone)[/COLOR] >>'}, img=IconPath + '1080.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery12'},  {'title':  '[COLOR khaki][B]M[/COLOR][COLOR blue]E[/COLOR][COLOR salmon]G[/COLOR][COLOR darkseagreen]A[/COLOR][/B] [COLOR blue][B]R[/B][/COLOR]elease [COLOR blue][B]HUB[/B][/COLOR] (Tv Episodes) : [COLOR green]Search[/COLOR]'}, img=IconPath + 'rhs.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles25b', 'url': BASE_URL25b + '/tv-shows'}, {'title':  '[COLOR darkorange][B]TV Shows[/B] [/COLOR]: [COLOR green]Index Search[/COLOR] (TVHQ)'}, img=IconPath + 'intvs.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles25a', 'url': BASE_URL25 + '/tv-shows'}, {'title':  '[COLOR darkorange][B]TV Shows[/B] [/COLOR]: [COLOR green]Index Search[/COLOR] (allcinemamovies)'}, img=IconPath + 'intvs.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------------ hd zone tv --------------------------------------------------------------------------------------------#

def Menu11():
        addon.add_directory({'mode': 'GetTitles33', 'section': 'ALL', 'url': BASE_URL7 + '/category/tv-shows/tv-1080p/',
                             'startPage': '1', 'numOfPages': '2'}, {'title':  '[COLOR darkorange][B]Latest 1080p / 720p[/B] [/COLOR] [COLOR yellow](2DDL)[/COLOR] >>'}, img=IconPath + '2d.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL20 + '/category/tv-shows/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest 1080p[/B] [/COLOR] [COLOR olive](0DayReleases)[/COLOR] >>'}, img=IconPath + 'od.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'menu12'}, {'title': '[COLOR darkorange][B]Latest 1080p / 720p[/B] [/COLOR] [COLOR red](Rls-TV)[/COLOR] >>'}, img=IconPath + 'rlstv.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/tv-show',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest 1080p Releases[/B] [/COLOR] [COLOR lightcyan](Crazy hd Source)[/COLOR] >>'}, img=IconPath + 'chd.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles14', 'section': 'ALL', 'url': BASE_URL5 + '/category/tvshow/web-dl/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest 1080p / 720p packs[/B] [/COLOR] [COLOR whitesmoke](The Extopia)[/COLOR] >>'}, img=IconPath + 'extv1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#----------------------------------------------------------------------------------- rlstv ---------------------------------------------------------------------------------------------#

def Menu12():
        addon.add_directory({'mode': 'GetTitles8', 'section': 'ALL', 'url': BASE_URL16 + '/?cat=TV-720p',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Page 1[/B] [/COLOR]>>'}, img=IconPath + 'rlstv.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles8', 'section': 'ALL', 'url': BASE_URL16 + '/index.php?page=2&cat=TV-720p',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Page 2[/B] [/COLOR]>>'}, img=IconPath + 'rlstv.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles8', 'section': 'ALL', 'url': BASE_URL16 + '/index.php?page=3&cat=TV-720p',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Page 3[/B] [/COLOR]>>'}, img=IconPath + 'rlstv.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles8', 'section': 'ALL', 'url': BASE_URL16 + '/index.php?page=4&cat=TV-720p',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Page 4[/B] [/COLOR]>>'}, img=IconPath + 'rlstv.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles8', 'section': 'ALL', 'url': BASE_URL16 + '/index.php?page=5&cat=TV-720p',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Page 5[/B] [/COLOR]>>'}, img=IconPath + 'rlstv.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles8', 'section': 'ALL', 'url': BASE_URL16 + '/index.php?page=6&cat=TV-720p',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Page 6[/B] [/COLOR]>>'}, img=IconPath + 'rlstv.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles8', 'section': 'ALL', 'url': BASE_URL16 + '/index.php?page=7&cat=TV-720p',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Page 7[/B] [/COLOR]>>'}, img=IconPath + 'rlstv.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles8', 'section': 'ALL', 'url': BASE_URL16 + '/index.php?page=8&cat=TV-720p',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Page 8[/B] [/COLOR]>>'}, img=IconPath + 'rlstv.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles8', 'section': 'ALL', 'url': BASE_URL16 + '/index.php?page=9&cat=TV-720p',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Page 9[/B] [/COLOR]>>'}, img=IconPath + 'rlstv.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles8', 'section': 'ALL', 'url': BASE_URL16 + '/index.php?page=10&cat=TV-720p',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Page 10[/B] [/COLOR]>>'}, img=IconPath + 'rlstv.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------------- sport -------------------------------------------------------------------------------------------#

def Menu6():
        addon.add_directory({'mode': 'GetSearchQuery11'},  {'title':  '[COLOR khaki][B]M[/COLOR][COLOR blue]E[/COLOR][COLOR salmon]G[/COLOR][COLOR darkseagreen]A[/COLOR][/B] [COLOR blue][B]R[/B][/COLOR]elease [COLOR blue][B]HUB[/B][/COLOR] (Sport) : [COLOR green]Search[/COLOR]'}, img=IconPath + 'rhs.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles33', 'section': 'ALL', 'url': BASE_URL7 + '/category/tv-shows/sport/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Latest Sport[/B] [/COLOR] [COLOR yellow](2DDL)[/COLOR] >>'}, img=IconPath + '2d3.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles11', 'section': 'ALL', 'url': BASE_URL10 + '/category/tv-shows/sports/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Latest Sport[/B] [/COLOR] [COLOR powderblue](DDLvalley)[/COLOR] >>'}, img=IconPath + 'ddlsport.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles11', 'section': 'ALL', 'url': BASE_URL10 + '/category/tv-shows/sports/english-premier-league/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Latest EPL (HD)[/B] [/COLOR] [COLOR powderblue](DDLvalley)[/COLOR] >>'}, img=IconPath + 'ddlsport.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles11', 'section': 'ALL', 'url': BASE_URL10 + '/category/tv-shows/sports/nba/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Latest NBA[/B] [/COLOR] [COLOR powderblue](DDLvalley)[/COLOR] >>'}, img=IconPath + 'ddlsport.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles13', 'section': 'ALL', 'url': BASE_URL11 + '/page/1/?s=ufc&submit=Find',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Latest (7) UFC[/B] [COLOR gold](ReleaseBB)[/COLOR] >>'}, img=IconPath + 'bbsport.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles13', 'section': 'ALL', 'url': BASE_URL11 + '/?s=wwe&submit=Find',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Latest (7) WWE[/B] [COLOR gold](ReleaseBB)[/COLOR] >>'}, img=IconPath + 'bbsport.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles13', 'section': 'ALL', 'url': BASE_URL11 + '/?s=tna&submit=Find',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Latest (7) TNA[/B] [COLOR gold](ReleaseBB)[/COLOR] >>'}, img=IconPath + 'bbsport.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles13', 'section': 'ALL', 'url': BASE_URL11 + '/?s=boxing&submit=Find',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Latest (7) Boxing[/B] [COLOR gold](ReleaseBB)[/COLOR] >>'}, img=IconPath + 'bbsport.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles13', 'section': 'ALL', 'url': BASE_URL11 + '/?s=match+of+the+day&submit=Find',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Latest (7) Match Of The Day[/B] [COLOR gold](ReleaseBB)[/COLOR] >>'}, img=IconPath + 'bbsport.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'menu8'}, {'title': '[COLOR lightyellow][B]Football Full Matches[/B] [/COLOR]>>'}, img=IconPath + 'fullsport.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles24', 'section': 'ALL', 'url': BASE_URL24 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Latest Wrestling/MMA/Boxing[/B] [COLOR chartreuse](DX-TV)[/COLOR] >>'}, img=IconPath + 'dx.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#----------------------------------------------------------------------------------- fullmatch ---------------------------------------------------------------------------------------------#

def Menu8():
        addon.add_directory({'mode': 'GetTitles16', 'section': 'ALL', 'url': BASE_URL15 + '/category/full-matches/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lightyellow]Full Matches [/COLOR]>>'}, img=IconPath + 'fullsport.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles16', 'section': 'ALL', 'url': BASE_URL15 + '/category/full-matches/england-premier-league/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lightyellow]England Premier League [/COLOR]>>'}, img=IconPath + 'fullsport.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles16', 'section': 'ALL', 'url': BASE_URL15 + '/category/full-matches/la-liga/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lightyellow]La Liga [/COLOR]>>'}, img=IconPath + 'fullsport.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles16', 'section': 'ALL', 'url': BASE_URL15 + '/category/full-matches/serie-a/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lightyellow]Serie A [/COLOR]>>'}, img=IconPath + 'fullsport.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles16', 'section': 'ALL', 'url': BASE_URL15 + '/category/full-matches/bundesliga/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lightyellow]Bundesliga [/COLOR]>>'}, img=IconPath + 'fullsport.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles16', 'section': 'ALL', 'url': BASE_URL15 + '/category/full-matches/ligue-1/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lightyellow]Ligue 1 [/COLOR]>>'}, img=IconPath + 'fullsport.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles16', 'section': 'ALL', 'url': BASE_URL15 + '/category/full-matches/matches-other/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lightyellow]Matches Other [/COLOR]>>'}, img=IconPath + 'fullsport.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles16', 'section': 'ALL', 'url': BASE_URL15 + '/category/full-matches/uefa-champions-league/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lightyellow]Uefa Champions League [/COLOR]>>'}, img=IconPath + 'fullsport.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles16', 'section': 'ALL', 'url': BASE_URL15 + '/category/full-matches/uefa-europa-league/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lightyellow]Uefa Europa League [/COLOR]>>'}, img=IconPath + 'fullsport.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------------- anime ----------------------------------------------------------------------------------------------#

def Menu7():
        addon.add_directory({'mode': 'GetTitles14', 'section': 'ALL', 'url': BASE_URL5 + '/category/anime/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR violet][B]Latest[/B] [/COLOR] [COLOR whitesmoke](The Extopia)[/COLOR] >>'}, img=IconPath + 'exan.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles14', 'section': 'ALL', 'url': BASE_URL5 + '/category/anime/movie/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR violet][B]Anime Movies[/B] [/COLOR] [COLOR whitesmoke](The Extopia)[/COLOR] >>'}, img=IconPath + 'exan.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles14', 'section': 'ALL', 'url': BASE_URL5 + '/category/anime/ovaspecial/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR violet][B]Anime Ova & Special[/B] [/COLOR] [COLOR whitesmoke](The Extopia)[/COLOR] >>'}, img=IconPath + 'exan.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles14', 'section': 'ALL', 'url': BASE_URL5 + '/category/anime/packs/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR violet][B]Anime Packs[/B] [/COLOR] [COLOR whitesmoke](The Extopia)[/COLOR] >>'}, img=IconPath + 'exan.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------------------------------- search ------------------------------------------------------------------------------------------------#

def Menu5():
        addon.add_directory({'mode': 'GetSearchQuery10'},  {'title':  '[COLOR khaki][B]M[/COLOR][COLOR blue]E[/COLOR][COLOR salmon]G[/COLOR][COLOR darkseagreen]A[/COLOR][/B] [COLOR blue][B]R[/B][/COLOR]elease [COLOR blue][B]HUB[/B][/COLOR] (Movies) : [COLOR green]Search[/COLOR]'}, img=IconPath + 'rhs.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery12'},  {'title':  '[COLOR khaki][B]M[/COLOR][COLOR blue]E[/COLOR][COLOR salmon]G[/COLOR][COLOR darkseagreen]A[/COLOR][/B] [COLOR blue][B]R[/B][/COLOR]elease [COLOR blue][B]HUB[/B][/COLOR] (Tv Episodes) : [COLOR green]Search[/COLOR]'}, img=IconPath + 'rhs.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery11'},  {'title':  '[COLOR khaki][B]M[/COLOR][COLOR blue]E[/COLOR][COLOR salmon]G[/COLOR][COLOR darkseagreen]A[/COLOR][/B] [COLOR blue][B]R[/B][/COLOR]elease [COLOR blue][B]HUB[/B][/COLOR] (Sport) : [COLOR green]Search[/COLOR]'}, img=IconPath + 'rhs.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles41', 'section': 'ALL', 'url': BASE_URL41 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest Episodes[/B] [/COLOR]: [COLOR green]Index Search[/COLOR] >>'}, img=IconPath + 'nintvs.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles25b', 'url': BASE_URL25b + '/tv-shows'}, {'title':  '[COLOR darkorange][B]TV Shows[/B] [/COLOR]: [COLOR green]Index Search[/COLOR] (Latest A)'}, img=IconPath + 'intvs.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles25a', 'url': BASE_URL25 + '/tv-shows'}, {'title':  '[COLOR darkorange][B]TV Shows[/B] [/COLOR]: [COLOR green]Index Search[/COLOR] (Latest B)'}, img=IconPath + 'intvs.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles34', 'url': BASE_URL31 + '/tv-shows/'}, {'title':  '[COLOR darkorange][B]Top Shows[/B] [/COLOR]: [COLOR green]Index Search[/COLOR]'}, img=IconPath + 'rt.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28', 'url': BASE_URL28 + '/'}, {'title':  '[COLOR blue][B]Released Today[/B] [/COLOR]: [COLOR greenyellow]Index Search[/COLOR]'}, img=IconPath + 'reto.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32', 'url': BASE_URL21 + '/new-movie-releases'}, {'title':  '[COLOR cornflowerblue][B]Box office[/B] [/COLOR]: [COLOR greenyellow]Index Search[/COLOR] (moviefone)'}, img=IconPath + 'isbo.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32', 'url': BASE_URL21 + '/dvd'}, {'title':  '[COLOR cornflowerblue][B]Featured[/B] [/COLOR]: [COLOR greenyellow]Index Search[/COLOR] (moviefone)'}, img=IconPath + 'inf.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32', 'url': BASE_URL21 + '/dvd/coming-soon'}, {'title':  '[COLOR cornflowerblue][B]Featured now[/B] [/COLOR]: [COLOR greenyellow]Index Search[/COLOR] (moviefone)'}, img=IconPath + 'inf.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery1'},  {'title':  '[COLOR gold][B]ReleaseBB[/COLOR][/B] : [COLOR green]Search[/COLOR]'}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

############################################################################## searches movies #############################################################################################

def GetSearchQuery10():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]MEGA ADDON SEARCH[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search10(query)
	else:
                return
def Search10(query):
    try:
        url = 'http://www.rlsbb.com/search/' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('postHeader.+?href="(.+?)".+?>(.+?)<.+?src=.+? src="(.+?)"', re.DOTALL).findall(html)
        for movieUrl, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': movieUrl}, {'title':  title + ' [COLOR gold](ReleaseBB)[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry rlsbb search is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
    try:
        url = 'http://www.ddlvalley.rocks/search/' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h2>.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
        for movieUrl, title, img in match:
                title = title.replace('.', ' ')
                addon.add_directory({'mode': 'GetLinks3', 'url': movieUrl}, {'title':  title + ' [COLOR powderblue](DDLvalley)[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry ddlvalley search is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
    try:
        url = 'http://releasefree.eu/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h2 class="entry-title"><a href="(.+?)" rel="bookmark">(.+?)</a></h2>', re.DOTALL).findall(html)
        for url, title in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title + ' [COLOR darkorchid]...(releasefree)[/COLOR]'}, img= 'https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry releasefree is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
    try:
        url = 'http://300mbmovies4u.com/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('class="cover"><a\s*?href="(.+?)" title="(.+?)"><img\s*?src="(.+?)" alt=".+?" class=".+?" width=".+?" height=".+?" /></a></div><div', re.DOTALL).findall(html)
        for movieUrl, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': movieUrl}, {'title':  title + ' [COLOR crimson](300mb movies4u)[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry 300mbmovies4u search is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
    try:
        url = 'http://rlssource.net/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h2 class="entry-title"><a href="(.+?)" title=".+?" rel="bookmark">(.+?)</a></h2>', re.DOTALL).findall(html)
        for movieUrl, title in match:
                addon.add_directory({'mode': 'GetLinks8', 'url': movieUrl}, {'title':  title + ' [COLOR firebrick](rlssource)[/COLOR]'}, img= 'https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry rlssource search is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
    try:
        url = BASE_URL1 + '/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h2> <a href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h2>', re.DOTALL).findall(html)
        for movieUrl, title in match:
                title = title.replace('.', ' ')
                addon.add_directory({'mode': 'GetLinks', 'url': movieUrl}, {'title':  title + ' [COLOR orange](Scene Source)[/COLOR]'}, img= 'https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry Scene Source search is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
    try:
        url = 'http://tv-release.net/?s='+query+'&cat='
        url = url.replace(' ', '%20')
        print url
        html = net.http_GET(url).content
        match = re.compile("width='60%' style='text-align:left; font-size:12px;font-weight:bold;'><a href='(.+?)'>(.+?)</a></td><td", re.DOTALL).findall(html)
        for movieUrl, title in match:
                title = title.replace('.', ' ')
                addon.add_directory({'mode': 'GetLinks1', 'url': movieUrl}, {'title':  title + ' [COLOR red](Rls-TV)[/COLOR]'}, img= 'https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry RLSTV search is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
    try:
        url = 'http://2ddl.link/?s=' + query 
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h2><a href="(.+?)" title=".+?">(.+?)</a></h2></div><div class="postmeta"><div class="metaleft">.+?<a href=".+?" title=".+?" rel=".+?">.+?</a>.+?<a href=".+?" title=".+?">.+?</a> <span><a href=".+?" title=".+?">.+?</a></span></div><div class="metaright"> <span class=".+?"><a href=".+?" title=".+?">.+?</a></span></div><div class="clear"></div></div><div class="postarea"><div align="center"><img\s*?src="(.+?)" alt=".+?"').findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title + ' [COLOR yellow]...(2ddl)[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry 2ddl is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
    try:
        url = 'http://rlsblog.se/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h2 class="title">.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)"').findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title + ' [COLOR orangered]...(rlsblog)[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry rlsblog is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
    try:
        url = 'http://scnlog.eu/movies/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('title=""/><a href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h1>').findall(html)
        for url, title in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title + ' [COLOR navy]...(scnlog.eu)[/COLOR]'}, img= 'https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry scnlog.eu is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
    try:
        url = 'http://extbb.com/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h2 class="postTitle"><span></span><a href="(.+?)" title=".+?">(.+?)</a></h2>.+?src="(.+?)"').findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title + ' [COLOR green]...(extbb)[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry extbb is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))


############################################################################## searches tv #############################################################################################


def GetSearchQuery12():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]MEGA ADDON SEARCH[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search12(query)
	else:
                return
def Search12(query):
    try:
        url = 'http://www.rlsbb.com/search/' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('postHeader.+?href="(.+?)".+?>(.+?)<.+?src=.+? src="(.+?)"', re.DOTALL).findall(html)
        for movieUrl, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': movieUrl}, {'title':  title + ' [COLOR gold](ReleaseBB)[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry rlsbb search is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
    try:
        url = 'http://www.ddlvalley.rocks/search/' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h2>.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
        for movieUrl, title, img in match:
                title = title.replace('.', ' ')
                addon.add_directory({'mode': 'GetLinks3', 'url': movieUrl}, {'title':  title + ' [COLOR powderblue](DDLvalley)[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry ddlvalley search is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
    try:
        url = 'http://2ddl.link/?s=' + query 
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('class="posttitle"><h2><a\s*?href="(.+?)" title=".+?">(.+?)</a></h2></div><div\s*?class=".+?"><div\s*?class=".+?">.+?<a\s*?href=".+?" title=".+?" rel=".+?">.+?</a>.+?<a\s*?href=".+?" title=".+?">.+?</a> <span><a\s*?href=".+?" title=".+?">.+?</a></span></div><div\s*?class=".+?"> <span\s*?class=".+?"><a\s*?href=".+?" title=".+?">.+?</a></span></div><div\s*?class=".+?"></div></div><div\s*?class=".+?"><div\s*?align=".+?"><img\s*?src="(.+?)"').findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title + ' [COLOR yellow]...(2ddl)[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry 2ddl is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
    try:
        url = 'http://releasefree.eu/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h2 class="entry-title"><a href="(.+?)" rel="bookmark">(.+?)</a></h2>', re.DOTALL).findall(html)
        for url, title in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title + ' [COLOR darkorchid]...(releasefree)[/COLOR]'}, img= 'https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry releasefree is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
    try:
        url = 'http://tv-release.net/?s='+query+'&cat='
        url = url.replace(' ', '%20')
        print url
        html = net.http_GET(url).content
        match = re.compile("<td width='.+?' style='.+?'><a href='(.+?)'>(.+?)</a></td><td", re.DOTALL).findall(html)
        for movieUrl, title in match:
                title = title.replace('.', ' ')
                addon.add_directory({'mode': 'GetLinks1', 'url': movieUrl}, {'title':  title + ' [COLOR red](Rls-TV)[/COLOR]'}, img= 'https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry RLSTV search is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
    try:
        url = 'http://sceper.ws/search/' + query
        url = url.replace(' ', '_')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h2 class="title"><a href="(.+?)">(.+?)</a></h2>\s*?<div class=".+?">\s*?<p style=".+?"><img class=".+?" src="(.+?)" alt=".+?"').findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title + ' [COLOR lightcyan]...(sceper)[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry sceper is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
    try:
        url = 'http://rlsblog.se/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h2 class="title"><a href="(.+?)" title=".+?">(.+?)</a></h2>.+?src="(.+?)"').findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title + ' [COLOR orangered]...(rlsblog)[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry rlsblog is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
    try:
        url = 'http://scnlog.eu/tv-shows/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<a href="(.+?)" rel="bookmark" title="(.+?)">.+?</a></h1>').findall(html)
        for url, title in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title + ' [COLOR navy]...(scnlog.eu)[/COLOR]'}, img= 'https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry scnlog.eu is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))


#------------------------------------------------------------------------------ sport search ----------------------------------------------------------------------------------#

def GetSearchQuery11():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]MEGA ADDON SEARCH[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search11(query)
	else:
                return

def Search11(query):
    try:
        url = 'http://dx-tv.com/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('entry-title.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
        for movieUrl, title, img in match:
                title = title.replace('.', ' ')
                addon.add_directory({'mode': 'GetLinks', 'url': movieUrl}, {'title':  title + ' [COLOR chartreuse](DX-TV)[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry DXTV search is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
    try:
        url = 'http://tv-release.net/?s=' +query+'&cat='
        url = url.replace(' ', '%20')
        print url
        html = net.http_GET(url).content
        match = re.compile("width='60%' style='text-align:left; font-size:12px;font-weight:bold;'><a href='(.+?)'>(.+?)</a></td><td", re.DOTALL).findall(html)
        for movieUrl, title in match:
                title = title.replace('.', ' ')
                addon.add_directory({'mode': 'GetLinks1', 'url': movieUrl}, {'title':  title + ' [COLOR red](Rls-TV)[/COLOR]'}, img= 'https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry RLSTV search is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
    try:
        url = 'http://releasefree.eu/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h2 class="entry-title"><a href="(.+?)" rel="bookmark">(.+?)</a></h2>', re.DOTALL).findall(html)
        for url, title in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title + ' [COLOR darkorchid]...(releasefree)[/COLOR]'}, img= 'https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry releasefree is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
    try:
        url = 'http://www.ddlvalley.rocks/search/' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h2>.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
        for movieUrl, title, img in match:
                title = title.replace('.', ' ')
                addon.add_directory({'mode': 'GetLinks3', 'url': movieUrl}, {'title':  title + ' [COLOR powderblue](DDLvalley)[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry ddlvalley search is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
    try:
        url = 'http://2ddl.link/?s=' + query 
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h2><a href="(.+?)" title=".+?">(.+?)</a></h2></div><div class="postmeta"><div class="metaleft">.+?<a href=".+?" title=".+?" rel=".+?">.+?</a>.+?<a href=".+?" title=".+?">.+?</a> <span><a href=".+?" title=".+?">.+?</a></span></div><div class="metaright"> <span class=".+?"><a href=".+?" title=".+?">.+?</a></span></div><div class="clear"></div></div><div class="postarea"><div align="center"><img\s*?src="(.+?)" alt=".+?"').findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title + ' [COLOR yellow]...(2ddl)[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry 2ddl is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

##.replace('/', ' ')## \s*? ## 
#-------------------------------------------------------------------------- rlsbb ----------------------------------------------------------------------------------------------#

def GetSearchQuery1():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]RLSBB SEARCH[/COLOR]')
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
        url = 'http://www.rlsbb.com/search/' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('postHeader.+?href="(.+?)".+?>(.+?)<.+?src=.+? src="(.+?)"', re.DOTALL).findall(html)
        for movieUrl, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': movieUrl}, {'title':  title }, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry rlsbb search is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))


#https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png#\s*?#
####################################################################### setViews #######################################################################################

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

#######################################################################################################################################################################

if mode == 'main': 
	MainMenu()
elif mode == 'HelpMenu':
        HelpMenu()
elif mode == 'MusicMenu':
        MusicMenu()
elif mode == 'GetTitles': 
	GetTitles(section, url, startPage, numOfPages)
elif mode == 'GetTitles1': 
	GetTitles1(section, url, startPage, numOfPages)
elif mode == 'GetTitles2': 
	GetTitles2(section, url, startPage, numOfPages)
elif mode == 'GetTitles2a': 
	GetTitles2a(section, url, startPage, numOfPages)
elif mode == 'GetTitles3': 
	GetTitles3(section, url, startPage, numOfPages)
elif mode == 'GetTitles4': 
	GetTitles4(section, url, startPage, numOfPages)
elif mode == 'GetTitles5': 
	GetTitles5(section, url, startPage, numOfPages)
elif mode == 'GetTitles6': 
	GetTitles6(section, url, startPage, numOfPages)
elif mode == 'GetTitles7': 
	GetTitles7(section, url, startPage, numOfPages)
elif mode == 'GetTitles8': 
	GetTitles8(section, url, startPage, numOfPages)
elif mode == 'GetTitles9': 
	GetTitles9(section, url, startPage, numOfPages)
elif mode == 'GetTitles1': 
	GetTitles1(section, url, startPage, numOfPages)
elif mode == 'GetTitles10': 
	GetTitles10(section, url, startPage, numOfPages)
elif mode == 'GetTitles11': 
	GetTitles11(section, url, startPage, numOfPages)
elif mode == 'GetTitles12': 
	GetTitles12(section, url, startPage, numOfPages)
elif mode == 'GetTitles13': 
	GetTitles13(section, url, startPage, numOfPages)
elif mode == 'GetTitles14': 
	GetTitles14(section, url, startPage, numOfPages)
elif mode == 'GetTitles16': 
	GetTitles16(section, url, startPage, numOfPages)
elif mode == 'GetTitles17': 
	GetTitles17(section, url, startPage, numOfPages)
elif mode == 'GetTitles18': 
	GetTitles18(section, url, startPage, numOfPages)
elif mode == 'GetTitles19': 
	GetTitles19(section, url, startPage, numOfPages)
elif mode == 'GetTitles20': 
	GetTitles20(section, url, startPage, numOfPages)
elif mode == 'GetTitles21': 
	GetTitles21(section, url, startPage, numOfPages)
elif mode == 'GetTitles22': 
	GetTitles22(section, url, startPage, numOfPages)
elif mode == 'GetTitles24': 
	GetTitles24(section, url, startPage, numOfPages)
elif mode == 'GetTitles25': 
	GetTitles25(query)
elif mode == 'GetTitles25a': 
	GetTitles25a(query)
elif mode == 'GetTitles25b': 
	GetTitles25b(query)
elif mode == 'GetTitles26': 
	GetTitles26(query)
elif mode == 'GetTitles27': 
	GetTitles27(url)
elif mode == 'GetTitles28': 
	GetTitles28(query)
elif mode == 'GetTitles29': 
	GetTitles29(section, url, startPage, numOfPages)
elif mode == 'GetTitles30': 
	GetTitles30(section, url, startPage, numOfPages)
elif mode == 'GetTitles32': 
	GetTitles32(query)
elif mode == 'GetTitles33': 
	GetTitles33(section, url, startPage, numOfPages)
elif mode == 'GetTitles34': 
	GetTitles34(query)
elif mode == 'GetTitles41': 
	GetTitles41(query, startPage, numOfPages)
elif mode == 'GetTitles42': 
	GetTitles42(section, url, startPage, numOfPages)
elif mode == 'GetTitles42a': 
	GetTitles42a(section, url, startPage, numOfPages)
elif mode == 'GetTitles42b': 
	GetTitles42b(query)
elif mode == 'GetLinks':
	GetLinks(section, url)
elif mode == 'GetLinks1':
	GetLinks1(section, url)
elif mode == 'GetLinks3':
	GetLinks3(section, url)
elif mode == 'GetLinks5':
	GetLinks5(section, url)
elif mode == 'GetLinks6':
	GetLinks6(section, url)
elif mode == 'GetLinks7':
	GetLinks7(section, url)
elif mode == 'GetLinks8':
	GetLinks8(section, url)
elif mode == 'Categories':
        Categories(url)
elif mode == 'GetSearchQuery1':
	GetSearchQuery1()
elif mode == 'Search1':
	Search1(query)
elif mode == 'GetSearchQuery10':
	GetSearchQuery10()
elif mode == 'Search10':
	Search10(query)
elif mode == 'GetSearchQuery11':
	GetSearchQuery11()
elif mode == 'Search11':
	Search11(query)
elif mode == 'GetSearchQuery12':
	GetSearchQuery12()
elif mode == 'Search12':
	Search12(query)
elif mode == 'PlayVideo':
	PlayVideo(url, listitem)
elif mode == 'PlayVideo3':
	PlayVideo3(url, listitem)	
elif mode == 'ResolverSettings':
        urlresolver.display_settings()
elif mode == 'Categories':
        Categories()
elif mode == 'GetTitles43': 
	GetTitles43(section, url)
elif mode == 'GetTitles43a': 
	GetTitles43a(query, section)
elif mode == 'GetTitles44': 
	GetTitles44(section, query)
if mode == 'menu2':
       Menu2()
if mode == 'menu3':
       Menu3()
if mode == 'menu4':
       Menu4()
if mode == 'menu5':
       Menu5()
if mode == 'menu6':
       Menu6()
if mode == 'menu7':
       Menu7()
if mode == 'menu8':
       Menu8()
if mode == 'menu9':
       Menu9()
if mode == 'menu11':
       Menu11()
if mode == 'menu12':
       Menu12()
if mode == 'menu13':
       Menu13()
if mode == 'menu14':
       Menu14()
if mode == 'menu15':
       Menu15()
elif mode == 'Help':
    import helpbox
    helpbox.HelpBox()

xbmcplugin.endOfDirectory(int(sys.argv[1]))