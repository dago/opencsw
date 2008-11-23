GARNAME = micq
GARVERSION = 0.6.1
CATEGORIES = net

DESCRIPTION = terminal-based ICQ client
define BLURB
  mICQ is a very portable text-mode ICQ clone - it is known to compile under
  Linux, Solaris, BSD, AIX, HPUX, Windows, AmigaOS and with restrictions
  BeOS.
endef

MASTER_SITES = http://www.micq.org/
#DISTFILES  = $(GARNAME)-$(GARVERSION).tgz
DISTFILES = $(call admfiles,CSWmicq,prototype depend)
GARCH=all

# dummy package; nothing to configure, build or install
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS =

# micq doesn't have a test target
TEST_TARGET =

include gar/category.mk
