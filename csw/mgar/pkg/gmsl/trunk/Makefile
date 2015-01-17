# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = gmsl
VERSION = 1.1.7
GARTYPE = v2

DESCRIPTION = GNU Make Standard Library

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = custom
TEST_SCRIPTS =

VENDOR_URL = http://gmsl.sourceforge.net/

ARCHALL = 1

include gar/category.mk

# work
# `-- solaris10-sparc
#     |-- build-global
#     |   `-- gmsl-1.1.7.tar.gz
#     `-- build-isa-sparcv8plus
#         `-- gmsl-1.1.7
#             |-- README
#             |-- __gmsl
#             |-- gmsl
#             |-- gmsl-tests
#             `-- index.html
#
# 9 directories, 33 files

install-custom:
	ginstall -d $(DESTDIR)$(includedir)
	ginstall -m 644 $(WORKSRC)/__gmsl $(DESTDIR)$(includedir)
	ginstall -m 644 $(WORKSRC)/gmsl $(DESTDIR)$(includedir)
	ginstall -d $(DESTDIR)$(docdir)/gmsl
	ginstall -m 644 $(WORKSRC)/README $(DESTDIR)$(docdir)/gmsl
	ginstall -m 644 $(WORKSRC)/index.html $(DESTDIR)$(docdir)/gmsl
	ginstall -m 644 $(WORKSRC)/gmsl-tests $(DESTDIR)$(docdir)/gmsl
	@$(MAKECOOKIE)
