NAME = seamonkey
VERSION = 1.1.19
CATEGORIES = apps
GARTYPE = v2
DISTNAME = mozilla

DESCRIPTION = Seamonkey all-in-one internet application suite
define BLURB
Web-browser, advanced e-mail and newsgroup client, IRC chat client, and HTML editing made simple -- all your Internet needs in one application. 
endef

DISTFILES  = $(NAME)-$(VERSION).source.tar.bz2
DISTFILES += CSWseamonkey.postremove CSWseamonkey.postinstall 
DISTFILES += .mozconfig

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*)
MASTER_SITES = http://releases.mozilla.org/pub/mozilla.org/seamonkey/releases/$(VERSION)/
UPSTREAM_MASTER_SITES = http://releases.mozilla.org/pub/mozilla.org/seamonkey/releases/

# Build firefox only on solaris 10 platforms
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

PACKAGES       			= CSWseamonkey
CATALOGNAME_CSWseamonkey 	= $(NAME)
SPKG_DESC_CSWseamonkey 		= $(DESCRIPTION)

RUNTIME_DEP_PKGS_CSWseamonkey += CSWbonobo2
RUNTIME_DEP_PKGS_CSWseamonkey += CSWfconfig
RUNTIME_DEP_PKGS_CSWseamonkey += CSWftype2
RUNTIME_DEP_PKGS_CSWseamonkey += CSWgconf2
RUNTIME_DEP_PKGS_CSWseamonkey += CSWggettextrt
RUNTIME_DEP_PKGS_CSWseamonkey += CSWglib2
RUNTIME_DEP_PKGS_CSWseamonkey += CSWgnomekeyring
RUNTIME_DEP_PKGS_CSWseamonkey += CSWgnomevfs2
RUNTIME_DEP_PKGS_CSWseamonkey += CSWgtk2
RUNTIME_DEP_PKGS_CSWseamonkey += CSWlibart
RUNTIME_DEP_PKGS_CSWseamonkey += CSWlibatk
RUNTIME_DEP_PKGS_CSWseamonkey += CSWlibbonoboui
RUNTIME_DEP_PKGS_CSWseamonkey += CSWlibcairo
RUNTIME_DEP_PKGS_CSWseamonkey += CSWlibgnome
RUNTIME_DEP_PKGS_CSWseamonkey += CSWlibgnomecanvas
RUNTIME_DEP_PKGS_CSWseamonkey += CSWlibgnomeui
RUNTIME_DEP_PKGS_CSWseamonkey += CSWlibidl
RUNTIME_DEP_PKGS_CSWseamonkey += CSWlibpopt
RUNTIME_DEP_PKGS_CSWseamonkey += CSWlibxft2
RUNTIME_DEP_PKGS_CSWseamonkey += CSWlibxrender
RUNTIME_DEP_PKGS_CSWseamonkey += CSWorbit2
RUNTIME_DEP_PKGS_CSWseamonkey += CSWpango
RUNTIME_DEP_PKGS_CSWseamonkey += CSWsqlite3rt
RUNTIME_DEP_PKGS_CSWseamonkey += CSWzlib

# Defines the list of patches to be applied to the sources
PATCHFILES += autoconf.mk.in.diff
PATCHFILES += SunOS5.mk.diff
PATCHFILES += legacydb.manifest.mm.diff
PATCHFILES += legacydb.config.mk.diff
PATCHFILES += softoken.manifest.mm.diff
PATCHFILES += softoken.config.mk.diff
PATCHFILES += packager.mk.diff
PATCHFILES += lber-int.h.diff
PATCHFILES += ldap-int.h.diff
PATCHFILES += ldappr-int.h.diff

# PATCHFILES += configure.diff

# pkg-config options
# EXTRA_PKG_CONFIG_PATH += /opt/csw/X11/lib/pkgconfig

PERL=/opt/csw/bin/perl
EXTRA_CFLAGS   += -xlibmil -D__solaris__ 
EXTRA_CXXFLAGS += -xlibmil -xlibmopt -features=tmplife -norunpath
EXTRA_CFLAGS   += -DG_HAVE_ISO_VARARGS
EXTRA_CXXFLAGS += -DG_HAVE_ISO_VARARGS
EXTRA_CPPFLAGS  = -I/opt/csw/include/cairo
EXTRA_XCFLAGS   = -I/opt/csw/include/cairo

EXTRA_CONFIGURE_EXPORTS = XCFLAGS

EXTRA_LINKER_FLAGS = -L/usr/lib/lwp -L/opt/csw/mozilla/seamonkey/lib -R/opt/csw/mozilla/seamonkey/lib -lsqlite3

export PERL CFLAGS CXXFLAGS

CONFIGURE_ARGS = --prefix=/opt/csw/mozilla/seamonkey
CONFIGURE_ARGS += --disable-crashreporter

TEST_SCRIPTS = 

LICENSE = LICENSE

# Variable for direct access to working dir
WORK_BUILD   = $(WORKSRC)
WORK_INSTALL = $(WORKROOTDIR)/install-$(firstword $(MODULATIONS))

pre-configure-modulated::
	@cp $(WORKDIR)/.mozconfig  $(WORKSRC)/.mozconfig

pre-install-modulated::
	( if [ ! -d $(WORK_INSTALL)/opt/csw/bin ] ; then mkdir -p $(WORK_INSTALL)/opt/csw/bin ; fi )
	( cd $(WORK_INSTALL)/opt/csw/bin ; rm -f seamonkey ; ln -sf ../mozilla/seamonkey/bin/seamonkey . )

post-install-modulated::
	( gfind $(WORK_INSTALL)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )
	( gfind $(WORK_INSTALL)/opt/csw -name chromelist.txt -exec bash -c " mv {} {}.temp && gsed -e  s\_`pwd`/$(WORKSRC)/\_\_g {}.temp > {} && rm {}.temp"  \; )
	( gfind $(WORK_INSTALL)/opt/csw/mozilla/seamonkey -name "*.js" -exec bash -c " mv {} {}.temp && gsed -e  s\_`pwd`/$(WORKSRC)/\_\_g {}.temp > {} && rm {}.temp"  \; )
	( gfind $(WORK_INSTALL)/opt/csw/mozilla/seamonkey -name "*.jar" -exec bash -c "`pwd`/removeBuildPathFromJar.sh {} `pwd` $(WORKDIR) $(DISTNAME)" \; )

include gar/category.mk
