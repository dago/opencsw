GARNAME = firefox
GARVERSION = 3.0.15
CATEGORIES = x11
DISTNAME = $(GARNAME)

DESCRIPTION = Firefox Community Edition web browser
define BLURB
 The award-winning, free Web browser is better than ever. Browse the Web with confidence - Firefox protects you from viruses, spyware and pop-ups. Enjoy improvements to performance, ease of use and privacy. It's easy to import your favorites and settings and get started. Download Firefox now and get the most out of the Web. 
endef

DISTFILES  = $(GARNAME)-$(GARVERSION)-source.tar.bz2
DISTFILES += CSWfirefox.postremove CSWfirefox.postinstall autoconf.mk.diff firefox.diff firefox.dist.bin.diff

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*)
MASTER_SITES = http://releases.mozilla.org/pub/mozilla.org/firefox/releases/$(GARVERSION)/source/
UPSTREAM_MASTER_SITES = http://releases.mozilla.org/pub/mozilla.org/firefox/releases/

PACKAGES 		= CSWfirefox
CATALOGNAME_CSWfirefox 	= $(GARNAME)
SPKG_DESC_CSWfirefox 	= $(DESCRIPTION)

PREREQUISITE_PKGS = CSWgtk2devel CSWlibdbusdev CSWdbusglibdev CSWsqlite3devel CSWkbproto CSWrenderproto

REQUIRED_PKGS_CSWfirefox  = CSWdbusglib
REQUIRED_PKGS_CSWfirefox += CSWfconfig
REQUIRED_PKGS_CSWfirefox += CSWftype2
REQUIRED_PKGS_CSWfirefox += CSWgconf2
REQUIRED_PKGS_CSWfirefox += CSWglib2
REQUIRED_PKGS_CSWfirefox += CSWgnomevfs2
REQUIRED_PKGS_CSWfirefox += CSWgtk2
REQUIRED_PKGS_CSWfirefox += CSWlibatk
REQUIRED_PKGS_CSWfirefox += CSWlibcairo
REQUIRED_PKGS_CSWfirefox += CSWlibdbus
REQUIRED_PKGS_CSWfirefox += CSWlibgnome
REQUIRED_PKGS_CSWfirefox += CSWlibx11
REQUIRED_PKGS_CSWfirefox += CSWlibxrender
REQUIRED_PKGS_CSWfirefox += CSWpango
REQUIRED_PKGS_CSWfirefox += CSWzlib
REQUIRED_PKGS_CSWfirefox += CSWsqlite3rt

# Defines the list of patches to be applied to the sources
PATCHFILES = autoconf.mk.in.diff
PATCHFILES += configure.diff
PATCHFILES += nsPluginsDirUnix.cpp.diff
PATCHFILES += packager.mk.diff
PATCHFILES += jemalloc.c.diff
PATCHFILES += nsMathUtils.h.diff
PATCHFILES += file_id.cc.diff
PATCHFILES += md5.h.diff
PATCHFILES += solaris_lwp.h.diff
PATCHFILES += nsNativeApSuportUnix.cpp.diff
PATCHFILES += nsExceptionHandler.cpp.diff 
PATCHFILES += SunOS5.mk.diff
PATCHFILES += nsWildCard.cpp.diff
PATCHFILES += softoken.manifest.mm.diff
PATCHFILES += softoken.config.mk.diff
PATCHFILES += legacydb.manifest.mm.diff
PATCHFILES += legacydb.config.mk.diff

# pkg-config options
EXTRA_PKG_CONFIG_PATH += /opt/csw/X11/lib/pkgconfig

PERL=/opt/csw/bin/perl
CXXFLAGS +=-xlibmil -xlibmopt -features=tmplife -norunpath
CFLAGS   +=-xlibmil -D__solaris__ 
CFLAGS   += -DG_HAVE_ISO_VARARGS
CXXFLAGS += -DG_HAVE_ISO_VARARGS
CPPFLAGS  = -I/opt/csw/include -I/opt/csw/X11/include
XCFLAGS   = -I/opt/csw/include -I/opt/csw/X11/include

EXTRA_CONFIGURE_EXPORTS = XCFLAGS

LDFLAGS+=-L/usr/lib/lwp -L/opt/csw/mozilla/firefox/lib -R/opt/csw/mozilla/firefox/lib -L/opt/csw/lib -R/opt/csw/lib -lsqlite3

export PERL CFLAGS CXXFLAGS LDFLAGS

CONFIGURE_ARGS = --prefix=/opt/csw/mozilla/firefox --disable-crashreporter

TEST_SCRIPTS = 

LICENSE = LICENSE

# Variable for direct access to working dir
WORK_BUILD   = $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/$(GARNAME)
WORK_INSTALL = $(WORKROOTDIR)/install-$(firstword $(MODULATIONS))

post-extract:
	mv $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/mozilla $(WORK_BUILD) 
	cp $(FILEDIR)/stdbool.h $(WORK_BUILD)/memory/jemalloc
	$(MAKECOOKIE)

pre-configure-modulated:
	@cp $(FILEDIR)/.mozconfig  $(WORK_BUILD)/.mozconfig

post-configure-modulated:
	@grep openwin $(WORKSRC)/config/autoconf.mk && gpatch -d$(WORKSRC) --forward -p1 -F2 < download/autoconf.mk.diff || true

pre-install-modulated:
	@grep "LD_LIBRARY_PATH=.LD_LIBRARY_PATH:/usr/lib/lwp" $(WORKSRC)/browser/app/firefox || gpatch -d$(WORKSRC) --forward  -p1 -F2 < $(FILEDIR)/firefox.diff
	@grep "LD_LIBRARY_PATH=.LD_LIBRARY_PATH:/usr/lib/lwp" $(WORKSRC)/dist/bin/firefox || gpatch -d$(WORKSRC) --forward  -p1 -F2 < $(FILEDIR)/firefox.dist.bin.diff
	( if [ ! -d $(WORK_INSTALL)/opt/csw/bin ] ; then mkdir -p $(WORK_INSTALL)/opt/csw/bin ; fi )
	( cd $(WORK_INSTALL)/opt/csw/bin ; rm -f firefox ; ln -sf ../mozilla/firefox/bin/firefox . )
	( mkdir -p $(WORK_INSTALL)/opt/csw/share/pixmaps )
	( cp $(WORK_BUILD)/other-licenses/branding/firefox/mozicon128.png $(WORK_INSTALL)/opt/csw/share/pixmaps/firefox.png )
	( mkdir -p $(WORK_INSTALL)/opt/csw/share/applications )
	( cp $(FILEDIR)/firefox.desktop $(WORK_INSTALL)/opt/csw/share/applications/firefox.desktop )
	( mkdir -p $(WORK_INSTALL)/opt/csw/share/gnome/mime-info )
	( cp $(FILEDIR)/firefox.keys $(WORK_INSTALL)/opt/csw/share/gnome/mime-info/firefox.keys )

post-install-modulated:
	( gfind $(WORK_INSTALL)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )
	( gfind $(WORK_INSTALL)/opt/csw -name chromelist.txt -exec bash -c " mv {} {}.temp && gsed -e  s\_`pwd`/$(WORK_BUILD)/\_\_g {}.temp > {} && rm {}.temp"  \; )
	( gfind $(WORK_INSTALL)/opt/csw/mozilla/firefox -name "*.js" -exec bash -c " mv {} {}.temp && gsed -e  s\_`pwd`/$(WORK_BUILD)/\_\_g {}.temp > {} && rm {}.temp"  \; )
	( gfind $(WORK_INSTALL)/opt/csw/mozilla/firefox -name "*.jar" -exec bash -c "`pwd`/removeBuildPathFromJar.sh {} `pwd` $(WORKDIR) $(DISTNAME)" \; )

include gar/category.mk
