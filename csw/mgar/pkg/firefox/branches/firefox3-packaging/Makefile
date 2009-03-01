GARNAME = firefox
GARVERSION = 3.0.4
CATEGORIES = apps
DISTNAME = $(GARNAME)

DESCRIPTION = Firefox Community Edition web browser
define BLURB
 The award-winning, free Web browser is better than ever. Browse the Web with confidence - Firefox protects you from viruses, spyware and pop-ups. Enjoy improvements to performance, ease of use and privacy. It's easy to import your favorites and settings and get started. Download Firefox now and get the most out of the Web. 
endef

include gar/category.mk

UPSTREAM_MASTER_SITES = http://releases.mozilla.org/pub/mozilla.org/firefox/releases/
MASTER_SITES = http://releases.mozilla.org/pub/mozilla.org/firefox/releases/$(GARVERSION)/source/
DISTFILES  = $(GARNAME)-$(GARVERSION)-source.tar.bz2
DISTFILES += $(call admfiles,CSWfirefox, depend postinstall postremove )

# Defines the list of patches to be applied to the sources
PATCHFILES = autoconf.mk.in.diff
PATCHFILES += packager.mk.diff
PATCHFILES += jemalloc.c.diff
PATCHFILES += nsMathUtils.h.diff
PATCHFILES += file_id.cc.diff
PATCHFILES += md5.h.diff
PATCHFILES += solaris_lwp.h.diff
PATCHFILES += nsNativeApSuportUnix.cpp.diff
PATCHFILES += nsExceptionHandler.cpp.diff 

PERL=/opt/csw/bin/perl
CXXFLAGS+=-xlibmil -xlibmopt -features=tmplife -norunpath
CFLAGS+=-xlibmil -D__solaris__ 

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*)

CFLAGS+= -DG_HAVE_ISO_VARARGS
CXXFLAGS+= -DG_HAVE_ISO_VARARGS
LDFLAGS+=-L/usr/lib/lwp -L/opt/csw/mozilla/firefox/lib -R/opt/csw/mozilla/firefox/lib -L/opt/csw/lib -R/opt/csw/lib -lsqlite3

export PERL CFLAGS CXXFLAGS LDFLAGS

CONFIGURE_ARGS = --prefix=/opt/csw/mozilla/firefox

TEST_SCRIPTS = none

test-none:
	@$(MAKECOOKIE)

post-extract:
	( mv $(WORKDIR)/mozilla $(WORKDIR)/$(DISTNAME) )
	( cp $(FILEDIR)/stdbool.h $(WORKDIR)/$(DISTNAME)/memory/jemalloc/ )
	@$(MAKECOOKIE)

pre-configure:
	( cp $(FILEDIR)/.mozconfig  $(WORKDIR)/$(DISTNAME)/.mozconfig )

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
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )
	( gfind $(DESTDIR)/opt/csw -name chromelist.txt -exec bash -c " mv {} {}.temp && gsed -e  s\_`pwd`/$(WORKDIR)/$(DISTNAME)/\_\_g {}.temp > {} && rm {}.temp"  \; )
	( gfind $(DESTDIR)/opt/csw/mozilla/firefox -name "*.js" -exec bash -c " mv {} {}.temp && gsed -e  s\_`pwd`/$(WORKDIR)/$(DISTNAME)/\_\_g {}.temp > {} && rm {}.temp"  \; )
	( gfind $(DESTDIR)/opt/csw/mozilla/firefox -name "*.jar" -exec bash -c "`pwd`/removeBuildPathFromJar.sh {} `pwd` $(WORKDIR) $(DISTNAME)" \; )

