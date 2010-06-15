GARNAME = tin
GARVERSION = 1.9.5
CATEGORIES = net

DESCRIPTION = Terminal-based news reader
define BLURB
  tin is an easy-to-use USENET news reader for the console using NNTP.
  It supports threading, scoring, different charsets, and many other
  useful things. It has also support for different languages.
endef

MASTER_SITES = ftp://ftp.tin.org/pub/news/clients/tin/unstable/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += COPYING
PATCHFILES = configure.patch

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

DEP_PKGS = CSWpcrert CSWggettextrt CSWperl CSWlibidn CSWlibicu CSWiconv

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-coffee
CONFIGURE_ARGS += --enable-ipv6 --enable-curses
CONFIGURE_ARGS += --x-includes=/usr/openwin/include
CONFIGURE_ARGS += --x-libraries=/usr/openwin/lib 
CONFIGURE_ARGS += --with-x --with-Xaw3d

# tin requires to run 'make build'
BUILD_ARGS = build

# tin doesn't have a test target
TEST_TARGET =

include gar/category.mk

post-install-modulated:
	/usr/ccs/bin/strip $(DESTDIR)$(prefix)/bin/tin
	/usr/ccs/bin/mcs -d $(DESTDIR)$(prefix)/bin/tin

