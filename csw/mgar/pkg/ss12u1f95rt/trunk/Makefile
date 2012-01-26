# $Id$
NAME = ss12f95rt
VERSION = 20100927
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Sun Studio 12u1 Fortran 95 Runtime Libraries
define BLURB
endef

MASTER_SITES = http://developers.sun.com/sunstudio/documentation/ss12u1/
DISTFILES  = DistributionREADME.txt

VENDOR_URL = http://developers.sun.com/sunstudio/documentation/ss12u1/DistributionREADME.txt

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

LICENSE = DistributionREADME.txt

RUNTIME_DEP_PKGS_CSWss12f95rt = CSWsunmath

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

# SPROl90s: Solaris SPARC Fortran libraries, comprising:
FLIBS-sparc  = libf77compat.so.1 libfai.so.3 libfai.so.2 libfai.so.1 libfai2.so.3 libfai2.so.2 libfai2.so.1
FLIBS-sparc += libfmaxlai.so.1 libfmaxvai.so.1 libfminlai.so.1 libfminvai.so.1 libfprodai.so.1 libfsumai.so.1
FLIBS-sparc += libfsu.so.1 libfui.so.2 libfui.so.1

# These are ISA-specific. Do them later if needed.
# FLIBS-sparc += libfai_isa.so.1 libfai2_isa.so.1
# FLIBS-sparc += libfmaxlai_isa.so.1 libfmaxvai_isa.so.1 libfminlai_isa.so.1 libfminvai_isa.so.1 libfprodai_isa.so.1 libfsumai_isa.so.1

# SPROl90s: Solaris x86 Fortran libraries, comprising:
FLIBS-i386 = libfsu.so.1 libfui.so.2 libfui.so.1

# This is a general lib needed, not Fortran-specific. May put this somewhere else??
FLIBS-sparc += libm9x.so.0
FLIBS-i386  += libm9x.so.0

include gar/category.mk

SRCDIR-sparcv9 = v9
SRCDIR-amd64   = amd64

install-custom:
	ginstall -d $(DESTDIR)$(libdir)
	$(foreach L,$(FLIBS-$(GARCH)),ginstall $(SOS12_CC_HOME)/lib/$L $(DESTDIR)$(libdir)/$L;)
	ginstall -d $(DESTDIR)$(libdir)/$(ISA_DEFAULT64)
	$(foreach L,$(FLIBS-$(GARCH)),if [ -f $(SOS12_CC_HOME)/lib/$(SRCDIR-$(ISA_DEFAULT64))/$L ]; then ginstall $(SOS12_CC_HOME)/lib/$(SRCDIR-$(ISA_DEFAULT64))/$L $(DESTDIR)$(libdir)/$(ISA_DEFAULT64)/$L; fi;)
	@$(MAKECOOKIE)
