# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = ttcp
VERSION = 1.0
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = Test TCP (TTCP) Benchmarking Tool
define BLURB
endef

MASTER_SITES = http://www.pcausa.com/Utilities/pcattcp/
DISTNAME = LinuxTTCP
DISTFILES  = $(DISTNAME).zip
DISTFILES += COPYING
DISTFILES += ttcp.1

VENDOR_URL = http://www.pcausa.com/Utilities/pcattcp.htm

EXTRA_LINKER_FLAGS = -lsocket -lnsl

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

build-custom:
	cd $(WORKSRC) && $(CC) $(CPPFLAGS) $(CFLAGS) $(LDFLAGS) -o ttcp ttcp.c
	@$(MAKECOOKIE)

install-custom:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -m 755 $(WORKSRC)/ttcp $(DESTDIR)$(bindir)/ttcp
	ginstall -d $(DESTDIR)$(mandir)/man1
	ginstall -m 644 $(WORKDIR)/ttcp.1 $(DESTDIR)$(mandir)/man1
	@$(MAKECOOKIE)
