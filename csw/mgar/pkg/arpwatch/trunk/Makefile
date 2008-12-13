GARNAME = arpwatch
GARVERSION = 2.1a15
CATEGORIES = server

DESCRIPTION = A network monitoring tool for tracking IP/MAC addresses on a network.
define BLURB
 The arpwatch package contains arpwatch and arpsnmp. Both utilities monitor Ethernet or FDDI network traffic and build databases of Ethernet/IP address pairs, and can report certain changes. 
endef

MASTER_SITES = ftp://ftp.ee.lbl.gov/
DISTFILES = $(GARNAME).tar.gz
DISTFILES += $(call admfiles,CSWarpwatch,depend prototype)
# Smf/init stuffs
DISTFILES += cswarpwatch.xml svc-cswarpwatch cswarpwatch arpwatch.conf

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# This patch add an system header include 
# in arpwatch.h so u_int32 is defined
# TODO: this should be done in configure
# and reported upstream
PATCHFILES += u_int32_type.patch 

# This patch allow to build the package
# without being root
PATCHFILES += no_root_build.patch

# this patch put arp.dat and ethercodes.dat
# in more standard compliant paths
PATCHFILES += file_location.patch

CONFIGURE_ARGS = $(DIRPATHS)

# we must add libdir in the library search path
# so libpcap is found
SUN_CC_OPT += -L$(libdir)

# No test target in arpwatch Makefile
SKIPTEST = 1

include gar/category.mk

pre-configure:
	# we fix a bug in configure which make some test fail
	# TODO: report upstream
	@echo "Fixing configure..."
	@perl -pi -e 's/^#define *$$//' $(WORKSRC)/configure


pre-install:
	@mkdir -p $(DESTDIR)/$(mandir)/man8
	@mkdir -p $(DESTDIR)/$(sbindir)
	@$(MAKECOOKIE)
	
post-install: 
	@echo " ==> Running make install-man in $(WORKSRC)"
	$(INSTALL_ENV) $(MAKE) DESTDIR=$(DESTDIR) $(foreach TTT,$(INSTALL_OVERRIDE_DIRS),$(TTT)="$(DESTDIR)$($(TTT))") -C $(WORKSRC) $(INSTALL_ARGS) install-man
	@ginstall -D $(WORKSRC)/ethercodes.dat $(DESTDIR)$(sharedstatedir)/$(GARNAME)/ethercodes.dat
	@$(MAKECOOKIE)

