# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = cgipaf
VERSION = 1.3.3
GARTYPE = v2

DESCRIPTION = Batch-change passwords non-interactively

MASTER_SITES = http://www.wagemakers.be/downloads/cgipaf/
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES += 0003-Honour-LDFLAGS-during-linking.patch

VENDOR_URL = http://www.wagemakers.be/english/programs/cgipaf

PACKAGES += CSWchangepass
SPKG_DESC_CSWchangepass = Batch-change passwords non-interactively
# PKGFILES is catchall

CONFIGURE_ARGS += $(DIRPATHS)

# This seems not to be used on changepass
# CONFIGURE_ARGS += --with-libcrack

# There is no testsuite
TEST_SCRIPTS =

# Existing install script uses 'su' for installation
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	ginstall -D -m 0755 $(WORKSRC)/changepass $(DESTDIR)$(sbindir)/changepass
	ginstall -D -m 0644 $(WORKSRC)/changepass.man $(DESTDIR)$(mandir)/man1m/changepass.1m
	@$(MAKECOOKIE)
 
