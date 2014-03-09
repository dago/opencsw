# $Id$

NAME    = pidgin
VERSION = 2.10.9
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Multi-protocol IM client
define BLURB
 Pidgin is a chat program which lets you log in to accounts on multiple chat networks simultaneously. This means that you can be chatting with friends on MSN, talking to a friend on Google Talk, and sitting in a Yahoo chat room all at the same time.
endef

MASTER_SITES = $(SF_M+= $(NAME)-$(VERSION).tar.bz2
STRIP_LIBTOOL = 1

GARCOMPILER = SOS12U3

VENDOR_URL = http://pidgin.im

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-dbus-services=$(sysconfdir)/dbus-1
CONFIGURE_ARGS += --with-tclconfig=$(libdir)
CONFIGURE_ARGS += --with-tkconfig=$(libdir)
# GNUtls causes issues and failures to connect using SSL
# ... or not. Or sometimes it works better. Who knows.
CONFIGURE_ARGS += --enable-gnutls=yes
CONFIGURE_ARGS += --enable-nss=no
CONFIGURE_ARGS += --disable-avahi
CONFIGURE_ARGS += --disable-nm
CONFIGURE_ARGS += --with-x
CONFIGURE_ARGS += --disable-vv
CONFIGURE_ARGS += --enable-trayicon-compat 

CONFIGURE_ARGS += --enable-gtkui
CONFIGURE_ARGS += --enable-consoleui

# We deffinitely want SASL
CONFIGURE_ARGS += --enable-cyrus-sasl

# For msgfmt, msgmerge, xgettext and gettext to be used from GNU
CONFIGURE_ENV_PATH = $(prefix)/gnu:$(PATH)

EXTRA_CFLAGS  = -xc99 -D_XPG6 -D__EXTENSIONS__
EXTRA_LD_OPTIONS = -z nolazyload

NCURSES_HEADERS = /opt/csw/include/ncursesw
EXTRA_CONFIGURE_EXPORTS += CFLAGS NCURSES_HEADERS
TEST_SCRIPTS = = (\d+(MERGE_EXCLUDE_FILES = .*/perllocal.pod

RUNTIME_DEP_PKGS_CSWpidgin += CSWaspell
RUNTIME_DEP_PKGS_CSWpidgin += CSWlibdbus1-3
RUNTIME_DEP_PKGS_CSWpidgin += CSWlibdbus-glib1-2
RUNTIME_DEP_PKGS_CSWpidgin += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWpidgin += CSWlibgstreamer0-10-0
RUNTIME_DEP_PKGS_CSWpidgin += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWpidgin += CSWlibgtkspell0
RUNTIME_DEP_PKGS_CSWpidgin += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWpidgin += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWpidgin += CSWlibmeanwhile1
RUNTIME_DEP_PKGS_CSWpidgin += CSWlibpango1-0-0
RUNTIME_DEP_PKGS_CSWpidgin += CSWperl
RUNTIME_DEP_PKGS_CSWpidgin += CSWpython
RUNTIME_DEP_PKGS_CSWpidgin += CSWtcl
RUNTIME_DEP_PKGS_CSWpidgin += CSWtk
RUNTIME_DEP_PKGS_CSWpidgin += CSWdbus
RUNTIME_DEP_PKGS_CSWpidgin += CSWlibidn11
RUNTIME_DEP_PKGS_CSWpidgin += CSWlibnss3
RUNTIME_DEP_PKGS_CSWpidgin += CSWlibnspr4
RUNTIME_DEP_PKGS_CSWpidgin += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWpidgin += CSWlibsmime3
RUNTIME_DEP_PKGS_CSWpidgin += CSWlibssl3
RUNTIME_DEP_PKGS_CSWpidgin += CSWlibncursesw5
RUNTIME_DEP_PKGS_CSWpidgin += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWpidgin += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWpidgin += CSWlibintl8
RUNTIME_DEP_PKGS_CSWpidgin += CSWlibtcl8-5
RUNTIME_DEP_PKGS_CSWpidgin += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWpidgin += CSWlibtk8-5
RUNTIME_DEP_PKGS_CSWpidgin += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWpidgin += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWpidgin += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpidgin += CSWlibpanelw5
RUNTIME_DEP_PKGS_CSWpidgin += CSWlibsilc1-1-2
RUNTIME_DEP_PKGS_CSWpidgin += CSWlibsilcclient1-1-3
RUNTIME_DEP_PKGS_CSWpidgin += CSWlibsasl2-2

###
# due to the ld bug
RUNTIME_DEP_PKGS_CSWpidgin += CSWlibpangoft2-1-0-0
RUNTIME_DEP_PKGS_CSWpidgin += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWpidgin += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWpidgin += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWpidgin += CSWlibplc4
RUNTIME_DEP_PKGS_CSWpidgin += CSWlibnssutil3
RUNTIME_DEP_PKGS_CSWpidgin += CSWlibplds4
RUNTIME_DEP_PKGS_CSWpidgin += CSWlibpangocairo1-0-0
###

BUILD_DEP_PKGS += CSWpkgconfig
BUILD_DEP_PKGS += CSWlibxml2-dev
BUILD_DEP_PKGS += CSWlibharfbuzz-dev
BUILD_DEP_PKGS += CSWlibgtk2-dev
BUILD_DEP_PKGS += CSWlibgtkspell-dev
BUILD_DEP_PKGS += CSWlibglib2-dev
BUILD_DEP_PKGS += CSWggettext-dev
BUILD_DEP_PKGS += CSWlibpcre-dev
BUILD_DEP_PKGS += CSWfontconfig-dev
BUILD_DEP_PKGS += CSWlibfreetype-dev
BUILD_DEP_PKGS += CSWlibpng-dev
BUILD_DEP_PKGS += CSWsunx11devel
BUILD_DEP_PKGS += CSWdoxygen
BUILD_DEP_PKGS += CSWlibncurses-dev
BUILD_DEP_PKGS += CSWlibdbus-dev
BUILD_DEP_PKGS += CSWlibdbus-glib-dev
BUILD_DEP_PKGS += CSWlibidn-dev
BUILD_DEP_PKGS += CSWtcl-dev
BUILD_DEP_PKGS += CSWtk-dev
BUILD_DEP_PKGS += CSWlibnss-dev
BUILD_DEP_PKGS += CSWnspr-dev
BUILD_DEP_PKGS += CSWmeanwhile-devdBUILD_DEP_PKGS += CSWlibsilc-devdBUILD_DEP_PKGS += CSWgstreamer-dev
BUILD_DEP_PKGS += CSWsasl-devdBUILD_DEP_PKGS += CSWlibpango-devdev CSWgnutlsdevel

PATCHFILES += patch-pidgin-Makefile.in
PATCHFILES += patch-pidgin-plugin.c
PATCHFILES += patch-pidgin-plugins-perl-common-Makefile.PL.in
PATCHFILES += patch-libpurple-plugins-perl-commPATCHFILES += 0004-irc-with-sasl.patchmoCHECKPKG_OVERRIDES_CSWpidgin += file-with-bad-content|/usr/local|root/opt/csw/lib/pidgin/musicmessaging.so 
CHECKPKG_OVERRIDES_CSWpidgin += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/libgnt.so
CHECKPKG_OVERRIDES_CSWpidgin += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/libpurple-client.so
CHECKPKG_OVERRIDES_CSWpidgin += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/libpurple.so
CHECKPKG_OVERRIDES_CSWpidgin += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/purple-2/libjabber.so
CHECKPKG_OVERRIDES_CSWpidgin += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/purple-2/liboscar.so
CHECKPKG_OVERRIDES_CSWpidgin += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/purple-2/libymsg.so
CHECKPKG_OVERRIDES_CSWpidgin += shared-lib-pkgname-mismatch|file=opt/csw/lib/libgnt.so.0.8.10|soname=libgnt.so.0|pkgname=CSWpidgin|expected=CSWlibgnt0
CHECKPKG_OVERRIDES_CSWpidgin += shared-lib-pkgname-mismatch|file=opt/csw/lib/libpurple-client.so.0.10.9|soname=libpurple-client.so.0|pkgname=CSWpidgin|expected=CSWlibpurple-client0
CHECKPKG_OVERRIDES_CSWpidgin += shared-lib-pkgname-mismatch|file=opt/csw/lib/libpurple.so.0.10.9|soname=libpurple.so.0|pkgname=CSWpidgin|expected=CSWlibpurple0

CHECKPKG_OVERRIDES_CSWpidgin += surplus-dependency|CSWaspell
CHECKPKG_OVERRIDES_CSWpidgin += surplus-dependency|CSWtcl
CHECKPKG_OVERRIDES_CSWpidgin += surplus-dependency|CSWtk
CHECKPKG_OVERRIDES_CSWpidgin += surplus-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWpidgin += surplus-dependency|CSWdbus
mon-Makefile.PL.in

includ