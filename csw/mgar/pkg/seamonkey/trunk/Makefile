GARNAME = seamonkey
GARVERSION = 1.1.17
CATEGORIES = x11
DISTNAME = $(GARNAME)

DESCRIPTION = Seamonkey all-in-one internet application suite
define BLURB
Web-browser, advanced e-mail and newsgroup client, IRC chat client, and HTML editing made simple -- all your Internet needs in one application. 
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).source.tar.bz2
# DISTFILES += CSWseamonkey.postremove CSWseamonkey.postinstall 

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*)
MASTER_SITES = http://releases.mozilla.org/pub/mozilla.org/seamonkey/releases/$(GARVERSION)/
UPSTREAM_MASTER_SITES = http://releases.mozilla.org/pub/mozilla.org/seamonkey/releases/

PACKAGES 			= CSWseamonkey
CATALOGNAME_CSWseamonkey 	= $(GARNAME)
SPKG_DESC_CSWseamonkey 		= $(DESCRIPTION)

# REQUIRED_PKGS_CSWseamonkey  = CSWdbusglib
# REQUIRED_PKGS_CSWseamonkey += CSWfconfig
# REQUIRED_PKGS_CSWseamonkey += CSWftype2
# REQUIRED_PKGS_CSWseamonkey += CSWgconf2
# REQUIRED_PKGS_CSWseamonkey += CSWglib2
# REQUIRED_PKGS_CSWseamonkey += CSWgnomevfs2
# REQUIRED_PKGS_CSWseamonkey += CSWgtk2
# REQUIRED_PKGS_CSWseamonkey += CSWlibatk
# REQUIRED_PKGS_CSWseamonkey += CSWlibcairo
# REQUIRED_PKGS_CSWseamonkey += CSWlibdbus
# REQUIRED_PKGS_CSWseamonkey += CSWlibgnome
# REQUIRED_PKGS_CSWseamonkey += CSWlibx11
# REQUIRED_PKGS_CSWseamonkey += CSWlibxrender
# REQUIRED_PKGS_CSWseamonkey += CSWpango
# REQUIRED_PKGS_CSWseamonkey += CSWsqlite3rt

# Defines the list of patches to be applied to the sources
# PATCHFILES = autoconf.mk.in.diff
# PATCHFILES += configure.diff
# PATCHFILES += nsPluginsDirUnix.cpp.diff
# PATCHFILES += packager.mk.diff
# PATCHFILES += jemalloc.c.diff
# PATCHFILES += nsMathUtils.h.diff
# PATCHFILES += file_id.cc.diff
# PATCHFILES += md5.h.diff
# PATCHFILES += solaris_lwp.h.diff
# PATCHFILES += nsNativeApSuportUnix.cpp.diff
# PATCHFILES += nsExceptionHandler.cpp.diff 

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

LDFLAGS+=-L/usr/lib/lwp -L/opt/csw/mozilla/seamonkey/lib -R/opt/csw/mozilla/seamonkey/lib -L/opt/csw/lib -R/opt/csw/lib -lsqlite3

export PERL CFLAGS CXXFLAGS LDFLAGS

CONFIGURE_ARGS = --prefix=/opt/csw/mozilla/seamonkey --disable-crashreporter

TEST_SCRIPTS = 

LICENSE = LICENSE

# Variable for direct access to working dir
WORK_BUILD   = $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/$(GARNAME)
WORK_INSTALL = $(WORKROOTDIR)/install-$(firstword $(MODULATIONS))

post-extract:
	@mv $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/mozilla $(WORK_BUILD)
#	@cp $(FILEDIR)/stdbool.h $(WORK_BUILD)/memory/jemalloc
	@$(MAKECOOKIE)

pre-configure:
	@cp $(FILEDIR)/.mozconfig  $(WORK_BUILD)/.mozconfig

pre-install:
	( if [ ! -d $(WORK_INSTALL)/opt/csw/bin ] ; then mkdir -p $(WORK_INSTALL)/opt/csw/bin ; fi )
	( cd $(WORK_INSTALL)/opt/csw/bin && ln -sf ../mozilla/seamonkey/bin/seamonkey . )
	( mkdir -p $(WORK_INSTALL)/opt/csw/share/pixmaps )
	( cp $(WORK_BUILD)/other-licenses/branding/seamonkey/mozicon128.png $(WORK_INSTALL)/opt/csw/share/pixmaps/seamonkey.png )
	( mkdir -p $(WORK_INSTALL)/opt/csw/share/applications )
	( cp $(FILEDIR)/seamonkey.desktop $(WORK_INSTALL)/opt/csw/share/applications/seamonkey.desktop )
	( mkdir -p $(WORK_INSTALL)/opt/csw/share/gnome/mime-info )
	( cp $(FILEDIR)/seamonkey.keys $(WORK_INSTALL)/opt/csw/share/gnome/mime-info/seamonkey.keys )

post-install:
	( gfind $(WORK_INSTALL)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )
	( gfind $(WORK_INSTALL)/opt/csw -name chromelist.txt -exec bash -c " mv {} {}.temp && gsed -e  s\_`pwd`/$(WORK_BUILD)/\_\_g {}.temp > {} && rm {}.temp"  \; )
	( gfind $(WORK_INSTALL)/opt/csw/mozilla/seamonkey -name "*.js" -exec bash -c " mv {} {}.temp && gsed -e  s\_`pwd`/$(WORK_BUILD)/\_\_g {}.temp > {} && rm {}.temp"  \; )
	( gfind $(WORK_INSTALL)/opt/csw/mozilla/seamonkey -name "*.jar" -exec bash -c "`pwd`/removeBuildPathFromJar.sh {} `pwd` $(WORKDIR) $(DISTNAME)" \; )

include gar/category.mk
