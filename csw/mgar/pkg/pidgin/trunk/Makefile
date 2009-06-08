GARNAME = pidgin
GARVERSION = 2.5.6
CATEGORIES = apps

DESCRIPTION = Multi-protocol IM client
define BLURB
 Pidgin is a chat program which lets you log in to accounts on multiple chat networks simultaneously. This means that you can be chatting with friends on MSN, talking to a friend on Google Talk, and sitting in a Yahoo chat room all at the same time.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += fixme.sh

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += '--with-dbus-services=/opt/csw/etc/dbus-1'
CONFIGURE_ARGS += '--with-tclconfig=/opt/csw/lib'
CONFIGURE_ARGS += '--with-tkconfig=/opt/csw/lib'
CONFIGURE_ARGS += '--enable-gnutls=yes'
CONFIGURE_ARGS += '--disable-nss'
CONFIGURE_ARGS += '--disable-avahi'
CONFIGURE_ARGS += '--disable-nm'

DOT=/opt/csw/graphviz2/bin/dot
XGETTEXT=/opt/csw/bin/gxgettext
MSGFMT=/opt/csw/bin/gmsgfmt
MSGMERGE=/opt/csw/bin/gmsgmerge
SED=/opt/csw/bin/gsed
X11_CFLAGS=-D_REENTRANT -D_POSIX_PTHREAD_SEMANTICS -DXTHREADS -DXUSE_MTSAFE_API
X11_LIBS=-lX11
EXTRA_CONFIGURE_EXPORTS = DOT XGETTEXT MSGFMT MSGMERGE SED X11_CFLAGS X11_LIBS
EXTRA_INC = /opt/csw/include/ncurses

TEST_TARGET = check

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

EXTRA_MERGE_EXCLUDE_FILES = .*/perllocal.pod

REQUIRED_PKGS_CSWpidgin  = CSWaspell CSWdbusglib CSWgcrypt CSWggettextrt CSWglib2
REQUIRED_PKGS_CSWpidgin += CSWgnutls CSWgstreamer CSWgtk2 CSWgtkspell CSWlibatk
REQUIRED_PKGS_CSWpidgin += CSWlibcairo CSWlibdbus CSWlibxml2 CSWmeanwhile CSWncurses
REQUIRED_PKGS_CSWpidgin += CSWpango CSWperl CSWpython CSWsilctoolkit CSWstartupnotif
REQUIRED_PKGS_CSWpidgin += CSWtcl CSWtk CSWiconv CSWsunmath CSWzlib CSWdbus

include gar/category.mk

post-configure-$(MODULATION):
	@(echo "~~~ Fixing Libtool ~~~")
	@$(DOWNLOADDIR)/fixme.sh $(WORKSRC)
	$(DONADA)
