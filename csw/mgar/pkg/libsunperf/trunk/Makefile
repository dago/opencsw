# $Id: Makefile 16916 2012-01-26 13:25:13Z dmichelsen $
NAME = libsunperf
VERSION = 20121030
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Sun Studio U1 Performance Libraries
define BLURB
endef

MASTER_SITES = http://www.oracle.com/technetwork/server-storage/solarisstudio/documentation/ss12u1-distributionreadme-429216.txt
DISTFILES  = ss12u1-distributionreadme-429216.txt

VENDOR_URL = http://www.oracle.com/technetwork/server-storage/solarisstudio/documentation/ss12u1-distributionreadme-429216.txt

LICENSE = ss12u1-distributionreadme-429216.txt

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

# the .so versions are different on the different architectures
PACKAGES_sparc = CSWlibsunperf7
PACKAGES_i386 = CSWlibsunperf2

PACKAGES = $(PACKAGES_$(GARCH))
SPKG_DESC_CSWlibsunperf7 = $(DESCRIPTION) - sparc
SPKG_DESC_CSWlibsunperf2 = $(DESCRIPTION) - i386

FLIBS-sparc  = libsunperf.so.7
FLIBS-i386 = libsunperf.so.2

RUNTIME_DEP_PKGS += CSWsunmath
RUNTIME_DEP_PKGS += CSWss12f95rt

CHECKPKG_OVERRIDES += bad-rpath-entry
CHECKPKG_OVERRIDES += soname-not-found
CHECKPKG_OVERRIDES += surplus-dependency|CSWss12f95rt
CHECKPKG_OVERRIDES += surplus-dependency|CSWsunmath

CHECKPKG_OVERRIDES += sparc-SunOS5.10-missing|libsunperf2
CHECKPKG_OVERRIDES += i386-SunOS5.10-missing|libsunperf7

include gar/category.mk

SRCDIR-sparcv9 = v9
SRCDIR-amd64   = amd64

install-custom:
	ginstall -d $(DESTDIR)$(libdir)
	$(foreach L,$(FLIBS-$(GARCH)),if [ -f $(SOS12_CC_HOME)/lib/$L ]; then ginstall $(SOS12_CC_HOME)/lib/$L $(DESTDIR)$(libdir)/$L; fi)
	ginstall -d $(DESTDIR)$(libdir)/$(ISA_DEFAULT64)
	$(foreach L,$(FLIBS-$(GARCH)),if [ -f $(SOS12_CC_HOME)/lib/$(SRCDIR-$(ISA_DEFAULT64))/$L ]; then ginstall $(SOS12_CC_HOME)/lib/$(SRCDIR-$(ISA_DEFAULT64))/$L $(DESTDIR)$(libdir)/$(ISA_DEFAULT64)/$L; fi;)
	@$(MAKECOOKIE)
