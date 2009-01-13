GARNAME = pidgin
GARVERSION = 2.5.4
CATEGORIES = apps

DESCRIPTION = Multi-protocol IM client
define BLURB
 Pidgin is a chat program which lets you log in to accounts on multiple chat networks simultaneously. This means that you can be chatting with friends on MSN, talking to a friend on Google Talk, and sitting in a Yahoo chat room all at the same time.
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += x11.pc
DISTFILES += $(call admfiles,CSWpidgin,prototype depend)

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += '--with-dbus-services=/opt/csw/etc/dbus-1'
CONFIGURE_ARGS += '--with-tclconfig=/opt/csw/lib'
CONFIGURE_ARGS += '--with-tkconfig=/opt/csw/lib'
CONFIGURE_ARGS += '--enable-gnutls=yes'
CONFIGURE_ARGS += '--disable-nss'
CONFIGURE_ARGS += '--disable-avahi'
CONFIGURE_ARGS += '--disable-nm'

CONFIGURE_ENV += DOT="/opt/csw/graphviz2/bin/dot"

EXTRA_INC += /opt/csw/include/ncurses

#Need to include our own x11.pc file as solaris 8 doesn't have one
PKG_CONFIG_PATH += $(CURDIR)/$(WORKDIR)

#No tests
TEST_SCRIPTS =

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

include gar/category.mk
