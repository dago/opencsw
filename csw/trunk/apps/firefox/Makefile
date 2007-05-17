GARNAME = firefox
GARVERSION = 2.0.0.3
CATEGORIES = apps
DISTNAME = $(GARNAME)

DESCRIPTION = Firefox Community Edition web browser
define BLURB
 The award-winning, free Web browser is better than ever. Browse the Web with confidence - Firefox protects you from viruses, spyware and pop-ups. Enjoy improvements to performance, ease of use and privacy. It's easy to import your favorites and settings and get started. Download Firefox now and get the most out of the Web. 
endef

MASTER_SITES = http://releases.mozilla.org/pub/mozilla.org/firefox/releases/$(GARVERSION)/source/
DISTFILES  = $(GARNAME)-$(GARVERSION)-source.tar.bz2
# DISTFILES += $(call admfiles,CSWfirefox, depend postinstall postremove )
DISTFILES += CSWfirefox.depend CSWfirefox.gspec CSWfirefox.prototype CSWfirefox.postinstall CSWfirefox.postremove
DISTFILES += CSWfirefoxrt.depend CSWfirefoxrt.gspec CSWfirefoxrt.prototype
DISTFILES += CSWfirefoxdevel.depend CSWfirefoxdevel.gspec CSWfirefoxdevel.prototype

PERL="/opt/csw/bin/perl"
CFLAGS=-xlibmil
CXXFLAGS="-xlibmil -xlibmopt -features=tmplife -norunpath"
LDFLAGS="-R'\$\$ORIGIN:\$\$ORIGIN/..' -L/opt/csw/lib -R/opt/csw/lib"

export PERL CFLAGS CXXFLAGS LDFLAGS

CONFIGURE_ARGS = --prefix=/opt/csw/mozilla/firefox

PATCHFILES = autoconf.mk.in.diff

TEST_SCRIPTS =

include ../category.mk

post-extract:
	( mv $(WORKDIR)/mozilla $(WORKDIR)/$(DISTNAME) )
	@$(MAKECOOKIE)

pre-configure:
	( mv $(HOME)/.mozconfig $(HOME)/.mozconfig.pre-CSWfirefox-build )
	( cp $(FILEDIR)/.mozconfig $(HOME)/.mozconfig )

pre-install:
	( if [ ! -d $(DESTDIR)/opt/csw/bin ] ; then mkdir -p $(DESTDIR)/opt/csw/bin ; fi )
	( cd $(DESTDIR)/opt/csw/bin && if [ -f firefox ] ; then rm firefox ; fi  && ln -s ../mozilla/firefox/bin/firefox . )
	( mkdir -p $(DESTDIR)/opt/csw/share/pixmaps )
	( cp $(WORKDIR)/$(DISTNAME)/other-licenses/branding/firefox/mozicon128.png $(DESTDIR)/opt/csw/share/pixmaps/firefox.png )
	( mkdir -p $(DESTDIR)/opt/csw/share/applications )
	( cp $(FILEDIR)/firefox.desktop $(DESTDIR)/opt/csw/share/applications/firefox.desktop )
	( mkdir -p $(DESTDIR)/opt/csw/share/gnome/mime-info )
	( cp $(FILEDIR)/firefox.keys $(DESTDIR)/opt/csw/share/gnome/mime-info/firefox.keys )

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | grep ELF | grep -e 'executable' -e 'dynamic lib' | grep 'not stripped' && strip {}"  \; )
	( mv $(DESTDIR)/opt/csw/mozilla/firefox/bin/firefox-config $(DESTDIR)/opt/csw/mozilla/firefox/bin/firefox-config.temp && gsed -e s\_-L$(DESTDIR)/opt/csw/lib\_\_g  $(DESTDIR)/opt/csw/mozilla/firefox/bin/firefox-config.temp > $(DESTDIR)/opt/csw/mozilla/firefox/bin/firefox-config && rm $(DESTDIR)/opt/csw/mozilla/firefox/bin/firefox-config.temp )
	( mv $(DESTDIR)/opt/csw/mozilla/firefox/lib/pkgconfig/firefox-nspr.pc $(DESTDIR)/opt/csw/mozilla/firefox/lib/pkgconfig/firefox-nspr.pc.temp && gsed -e s\_-L$(DESTDIR)/opt/csw/lib\_\_g  $(DESTDIR)/opt/csw/mozilla/firefox/lib/pkgconfig/firefox-nspr.pc.temp > $(DESTDIR)/opt/csw/mozilla/firefox/lib/pkgconfig/firefox-nspr.pc && rm $(DESTDIR)/opt/csw/mozilla/firefox/lib/pkgconfig/firefox-nspr.pc.temp )
	( gfind $(DESTDIR)/opt/csw -name chromelist.txt -exec bash -c " mv {} {}.temp && gsed -e  s\_`pwd`/$(WORKDIR)/$(DISTNAME)/\_\_g {}.temp > {} && rm {}.temp"  \; )
	( gfind $(DESTDIR)/opt/csw/mozilla/firefox -name "*.js" -exec bash -c " mv {} {}.temp && gsed -e  s\_`pwd`/$(WORKDIR)/$(DISTNAME)/\_\_g {}.temp > {} && rm {}.temp"  \; )
	( gfind $(DESTDIR)/opt/csw/mozilla/firefox -name "*.jar" -exec bash -c "`pwd`/removeBuildPathFromJar.sh {} `pwd` $(WORKDIR) $(DISTNAME)" \; )
