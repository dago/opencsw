# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = sslscan
VERSION = 1.8.2
GARTYPE = v2

DESCRIPTION = Fast SSL Scanner

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tgz

VENDOR_URL = http://sourceforge.net/projects/sslscan/
LICENSE = LICENSE

RUNTIME_DEP_PKGS_CSWsslscan += CSWlibssl1-0-0

# This is supersimple
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
TEST_SCRIPTS = 
INSTALL_SCRIPTS = custom

include gar/category.mk

build-custom:
	cd $(WORKSRC) && $(BUILD_ENV) $(CC) $(CPPFLAGS) $(CFLAGS) $(LDFLAGS) -lcrypto -lssl -lsocket -lnsl -o sslscan sslscan.c
	@$(MAKECOOKIE)

install-custom:
	ginstall -D $(WORKSRC)/sslscan $(DESTDIR)$(bindir)/sslscan
	ginstall -D $(WORKSRC)/sslscan.1 $(DESTDIR)$(mandir)/man1/sslscan.1
	@$(MAKECOOKIE)
