GARNAME = smartmontools
GARVERSION = 5.38
CATEGORIES = utils

DESCRIPTION = S.M.A.R.T. disk monitoring tools
define BLURB
  The smartmontools package contains two utility programs (smartctl and smartd)
  to control and monitor storage systems using the Self-Monitoring, Analysis
  and Reporting Technology System (S.M.A.R.T.) built into most modern ATA and
  SCSI hard disks.  It is derived from the smartsuite package, and includes
  support for ATA/ATAPI-5 disks.
endef

MASTER_SITES = http://smartmontools.sourceforge.net/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWsmartmontools, postinstall depend prototype)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
UPSTREAM_MASTER_SITES = http://surfnet.dl.sourceforge.net/sourceforge/smartmontools/

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-docdir=$(sharedstatedir)/doc/$(GARNAME)
CONFIGURE_ARGS += --with-initscriptdir=/etc/opt/csw/init.d

TEST_TARGET = check

# moving configuration file
post-install:
	(cd $(DESTDIR)$(prefix)/etc; \
	for i in smartd.conf; do \
		if [ -r "$$i" ]; then \
			echo "$$i -> $$i.CSW"; \
			mv "$$i" "$$i.CSW";     \
		fi \
	done)
	(cd $(DESTDIR)/etc/opt/csw/init.d; \
	for i in smartd; do \
		if [ -r "$$i" ]; then \
			echo "$$i -> csw$$i"; \
			mv "$$i" "csw$$i";     \
		fi \
	done)

include gar/category.mk
