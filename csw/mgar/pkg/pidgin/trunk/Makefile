# $Id$

NAME = pidgin
VERSION = 2.6.6
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Multi-protocol IM client
define BLURB
 Pidgin is a chat program which lets you log in to accounts on multiple chat networks simultaneously. This means that you can be chatting with friends on MSN, talking to a friend on Google Talk, and sitting in a Yahoo chat room all at the same time.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz
STRIP_LIBTOOL = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += '--with-dbus-services=/opt/csw/etc/dbus-1'
CONFIGURE_ARGS += '--with-tclconfig=/opt/csw/lib'
CONFIGURE_ARGS += '--with-tkconfig=/opt/csw/lib'
CONFIGURE_ARGS += '--enable-gnutls=yes'
CONFIGURE_ARGS += '--disable-nss'
CONFIGURE_ARGS += '--disable-avahi'
CONFIGURE_ARGS += '--disable-screensaver'
CONFIGURE_ARGS += '--disable-nm'
CONFIGURE_ARGS += --x-includes=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(prefix)/X11/lib
CONFIGURE_ARGS += --disable-vv


PATH = $(SOS11_CC_HOME)/bin:$(PATH)
EXTRA_EXPORTS = PATH

DOT=/opt/csw/graphviz2/bin/dot
XGETTEXT=/opt/csw/bin/gxgettext
MSGFMT=/opt/csw/bin/gmsgfmt
MSGMERGE=/opt/csw/bin/gmsgmerge
SED=/opt/csw/bin/gsed
X11_CFLAGS=-D_REENTRANT -D_POSIX_PTHREAD_SEMANTICS -DXTHREADS -DXUSE_MTSAFE_API
X11_LIBS=-lX11
LIBS=-lm
EXTRA_CONFIGURE_EXPORTS  = DOT XGETTEXT MSGFMT MSGMERGE SED PKG_CONFIG_PATH
EXTRA_CONFIGURE_EXPORTS += X11_CFLAGS X11_LIBS LIBS
EXTRA_INC = /opt/csw/include/ncurses
TEST_SCRIPTS =
# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib
EXTRA_LDFLAGS = -R $(prefix)/X11/lib
EXTRA_SOS_LD_FLAGS = -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))
EXTRA_SOS_LD_OPTIONS = -R$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))
EXTRA_LINKER_FLAGS = /usr/openwin/lib/libXext.so

EXTRA_MERGE_EXCLUDE_FILES = .*/perllocal.pod

RUNTIME_DEP_PKGS  = CSWaspell CSWdbusglib CSWgcrypt CSWggettextrt CSWglib2
RUNTIME_DEP_PKGS += CSWgnutls CSWgstreamer CSWgtk2 CSWgtkspell CSWlibatk
RUNTIME_DEP_PKGS += CSWlibcairo CSWlibdbus CSWlibxml2 CSWmeanwhile CSWncurses
RUNTIME_DEP_PKGS += CSWpango CSWperl CSWpython CSWsilctoolkit CSWstartupnotif
RUNTIME_DEP_PKGS += CSWtcl CSWtk CSWiconv CSWsunmath CSWzlib CSWdbus
RUNTIME_DEP_PKGS += CSWfconfig CSWftype2 CSWlibx11 CSWbdb47 CSWlibidn
RUNTIME_DEP_PKGS += CSWlibice CSWlibxext CSWlibsm CSWgstplugins

BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS) CSWlibdbusdev CSWdbusglibdev CSWgnutlsdevel

PATCHFILES += patch-pidgin-Makefile.in
PATCHFILES += patch-pidgin-plugin.c
PATCHFILES += patch-pidgin-plugins-perl-common-Makefile.PL.in
PATCHFILES += patch-libpurple-plugins-perl-common-Makefile.PL.in

include gar/category.mk
