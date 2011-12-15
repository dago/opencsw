# $Id$

NAME = smartmontools
VERSION = 5.42
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = S.M.A.R.T. disk monitoring tools
define BLURB
  The smartmontools package contains two utility programs (smartctl and smartd)
  to control and monitor storage systems using the Self-Monitoring, Analysis
  and Reporting Technology System (S.M.A.R.T.) built into most modern ATA and
  SCSI hard disks.  It is derived from the smartsuite package, and includes
  support for ATA/ATAPI-5 disks.
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-docdir=$(sharedstatedir)/doc/$(NAME)
CONFIGURE_ARGS += --with-initscriptdir=/etc/opt/csw/init.d

INITSMF = $(sysconfdir)/init.d/cswsmartd

CHECKPKG_OVERRIDES_CSWsmartmontools += file-with-bad-content
EXTRA_CFLAGS = -xnorunpath
EXTRA_CXXFLAGS = -norunpath

include gar/category.mk

# Moving the configuration file.
post-install-modulated:
	(cd $(DESTDIR)$(sysconfdir); \
	for i in smartd.conf; do \
		if [ -r "$$i" ]; then \
			gmv -v "$$i" "$$i.CSW";     \
		fi \
	done)
	(cd $(DESTDIR)$(sysconfdir)/init.d; \
	for i in smartd; do \
		if [ -r "$$i" ]; then \
			gmv -v "$$i" "csw$$i";     \
		fi \
	done)

# The 5.42 version needs GNU sed going by 'sed'.
PATH := /opt/csw/gnu:$(PATH)
