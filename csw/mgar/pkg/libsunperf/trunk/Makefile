# $Id: Makefile 16916 2012-01-26 13:25:13Z dmichelsen $
NAME = libsunperf
VERSION = 20140926
GARTYPE = v2

DESCRIPTION = Sun Studio 12U3 Performance Libraries

MASTER_SITES6.txt

VENDOR_URL = http://www.oracle.com/technetwork/server-storage/solarisstud

VENDOR_URL = http://docs.oracle.com/cd/E24457_01/html/E26748/ossdr.html

LICENSE_TEXT = The shared libraries are freely distributablereadme-429216.txt

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

# the .so versions are different on the different architectures
PACKAGES_spar8
PACKAGES_i386 = CSWlibsunperf4

PACKAGES = $(PACKAGES_$(GARCH))
SPKG_DESC_CSWlibsunperf8 = $(DESCRIPTION) - sparc
SPKG_DESC_CSWlibsunperf4 = $(DESCRIPTION) v4 - i386
# PKGFILES is catchall

# Yes, indeed, SOS12u3 contains .so.4 for 32 bit and .so.3 for 64 bit. WTF?!?
CHECKPKG_OVERRIDES_CSWlibsunperf4 += shared-lib-pkgname-mismatch|file=opt/csw/lib/amd64/libsunperf.so.3|soname=libsunperf.so.3|pkgname=CSWlibsunperf4|expected=CSWlibsunperf3

FLIBS-sparc-32 += libsunperf.so.8
FLIBS-sparc-64 += libsunperf.so.8
FLIBS-i386-32 += libsunperf.so.4
FLIBS-i386-64 +== libsunperf.so.2 libsunperf.so.3

RUNTIME_DEP_PKGS += CSWsunmath
RUNTIME_DEP_PKGS += CSWss12f95rt

C_CSWlibsunperf4 += bad-rpath-entry
CHECKPKG_OVERRIDES_CSWlibsunperf8 += bad-rpath-entry

# They are binary blobs which we have no control of
CHECKPKG_OVERRIDES_CSWlibsunperf4 += no-direct-binding
CHECKPKG_OVERRIDES_CSWlibsunperf8 += no-direct-binding

include gar/category.mk
eSRCDIR-sparcv9 = v9
SRCDIR-amd64   = amd64

install-custom-i386:
	ginstall -d $(DESTDIR)$(libdir)
	$(foreach L,$(FLIBS-$(GARCH)-32),if [ -f $(SOS12U3_CC_HOME)/lib/$L ]; then ginstall $(SOS12U3_CC_HOME)/lib/$L $(DESTDIR)$(libdir)$(ISA_SS32-$(GARCH))/$L; fi;)
	@$(MAKECOOKIE)

install-custom-sparc:
	ginstall -d $(DESTDIR)$(libdir)
	#ginstall -d $(DESTDIR)$(libdir)/v8
	#ln -s v8/$(FLIBS-$(GARCH)-32) $(DESTDIR)$(libdir)/$(FLIBS-$(GARCH)-32)
	#$(foreach L,$(FLIBS-$(GARCH)-32),if [ -f $(SOS12U3_CC_HOME)/lib/$L ]; then ginstall $(SOS12U3_CC_HOME)/lib/$L $(DESTDIR)$(libdir)$(ISA_SS32-$(GARCH))/v8/$L; fi;)
	$(foreach L,$(FLIBS-$(GARCH)-32),if [ -f $(SOS12U3_CC_HOME)/lib/$L ]; then ginstall $(SOS12U3_CC_HOME)/lib/$L $(DESTDIR)$(libdir)$(ISA_SS32-$(GARCH))/$L; fi;)
	@$(MAKECOOKIE)

install-custom: install-custom-$(GARCH$(libdir)/$L; fi;)
	ginstall -d $(DESTDIR)$(libdir)/$(ISA_DEFAULT64)
	$(foreach L-64),if [ -f $(SOS12U3_CC_HOME)/lib/$(SRCDIR-$(ISA_DEFAULT64))/$L ]; then ginstall $(SOS12U3 ginstall $(SOS12_CC_HOME)/lib/$(SRCDIR-$(ISA_DEFAULT64))/$L $(DESTDIR)$(libdir)/$(ISA_DEFAULT64)/$L; fi;)