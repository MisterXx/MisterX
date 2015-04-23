import urllib,urllib2,re,xbmcplugin,xbmcgui
import urlresolver, xbmcaddon

#Porn Hub - Blazetamer.
addon = xbmcaddon.Addon ('plugin.video.pornhub')

url= 'http://www.pornhub.com/'

#PATHS

addonPath = addon.getAddonInfo('path')
artPath = addonPath + '/art/'
fanartPath = addonPath + '/art/'

#HOOKS
settings = xbmcaddon.Addon(id='plugin.video.pornhub')

def CATEGORIES():
    addDir('Search>>>','http://www.pornhub.com/video/search?search=',10,"'icon.png'")
    addDir('Top Rated','http://www.pornhub.com/video?o=tr',1,"'icon.png'")
    addDir('All Videos','http://www.pornhub.com/video',1,"'icon.png'")
    addDir('Amature Video','http://www.pornhub.com/video?c=3',1,"'icon.png'")
    addDir('Bi-Sexual','http://www.pornhub.com/video?c=76',1,"'icon.png'")
    addDir('Bondage','http://www.pornhub.com/video?c=10',1,"'icon.png'")
    addDir('Big Tits','http://www.pornhub.com/video?c=8',1,"'icon.png'")
    addDir('Threesome','http://www.pornhub.com/video?c=65',1,"'icon.png'")
    addDir('Celebrity','http://www.pornhub.com/video?c=12',1,"'icon.png'")
    addDir('Pornstar','http://www.pornhub.com/video?c=30',1,"'icon.png'")
    
    
def INDEX(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    match=re.compile('<a href="(.+?)" title="(.+?)" class="img" data-related-url=".+?">\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<img src=".+?" alt=".+?" data-smallthumb="(.+?)"').findall(link)
    for url, name, thumbnail in match:
            addDir(name,url,2,thumbnail)
                
def VIDEOLINKS(url,name):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<iframe src="(.+?)"  frameborder=0 height=380 width=505 scrolling=no name="ph_embed_video">').findall(link)
        for url in match:
                 EMBED(url,name)

def EMBED(url,name):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<div id="player">\r\n\t\t\t<video src="(.+?)" poster="(.+?)" x-webkit-airplay="allow"').findall(link)
        for url,iconimage in match:
                 addLink(name,url,iconimage)                 
#adding Resolver

def resolvelink(name,url,iconimage):
	play=xbmc.Player().play(url)
	try: _addon.resolve_url(url)
	except: pass
	
	PL=xbmc.PlayList(xbmc.PLAYLIST_VIDEO); PL.clear(); 
	try:
		import urlresolver
		stream_url=urlresolver.HostedMediaFile(url).resolve()
		PL.add(stream_url,listitem)
		play.play(PL)
	except: pass                 

#End Resolver
                 
#Set View Function
def set_view(content='none',view_mode=50,do_sort=False):
	h=int(sys.argv[1])
	if (content is not 'none'): xbmcplugin.setContent(h, content)
	if (tfalse(addst("auto-view"))==True): xbmc.executebuiltin("Container.SetViewMode(%s)" % str(view_mode))                

#Start Ketboard Function                
def _get_keyboard( default="", heading="", hidden=False ):
	""" shows a keyboard and returns a value """
	keyboard = xbmc.Keyboard( default, heading, hidden )
	keyboard.doModal()
	if ( keyboard.isConfirmed() ):
		return unicode( keyboard.getText(), "utf-8" )
	return default


#Start Search Function
def SEARCH(url):
	searchUrl = url 
	vq = _get_keyboard( heading="Searching  PornHub!!" )
	# if blank or the user cancelled the keyboard, return
	if ( not vq ): return False, 0
	# we need to set the title to our query
	title = urllib.quote_plus(vq)
	searchUrl += title 
	print "Searching URL: " + searchUrl 
	INDEX(searchUrl)        

                
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param





def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name,iconImage=iconimage,thumbnailImage=iconimage); liz.setInfo('video',{'Title':name,'Genre':'Live','Studio':name})
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        xbmc.sleep(1000)
        xbmc.Player ().play(url, liz, False)
        return ok
    #xbmc.PLAYER_CORE_PAPLAYER


def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        xbmc.executebuiltin("Container.SetViewMode(500)")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
        
              
params=get_params()
url=None
name=None
mode=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
       
elif mode==1:
        print ""+url
        INDEX(url)
        

elif mode==2:
        print ""+url
        VIDEOLINKS(url,name)

#For Search Function
elif mode==10:
        print ""+url
        SEARCH(url)        



xbmcplugin.endOfDirectory(int(sys.argv[1]))


