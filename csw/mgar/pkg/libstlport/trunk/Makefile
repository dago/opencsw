NAME = libstlport
VERSION = 4.5.3
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = A multiplatform C++ standard library implementation

MASTER_SITES = manual://
PATC11
PATCH-i386  = 145731-11i386  = 145731-05
PATCH = $(PATCH-$(GARCH))
DISTNAME = $(PATCH)
DISTFILES += $(PATCH-sparc).zip
DISTFILES += $(PATCH-i386).zip
NOEXTRACT = $(filter-out $(addsuffix .zip,$(PATCH)),$(DISTFILES))

# Redistribution of libstlport.so.1 is allowed as noted in
#   http://developers.sun.com/sunstudio/documentation/ss12/mr/READMEs/runtime.libraries.html

# This patch requires some functions from libm only available on Solaris 10
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

VENDOR_URL = http://wesunsolve.net/patch/id/$(PATCH)

LICENSE = LEGAL_LICENSE.TXT

PACKAGES 
SPKG_DESC_CSWlibstlport1 = Runtime library for Sun Studio STLPort, libstlport.so.1 from patch $(PATCH)
# PKGFILES is catchall
OBSOLETED_BY_CSWlibstlport1 = CSWstlport

# Just keep the pathes as we copy the libs verbatim
CHECKPKG_OVERRIDES_CSWlibstlport1bstlport1-stlport += bad-rpath-entry

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

ISADIR_sparcv9 = v9
ISADIR_amd64 = amd64

install-custom:
	ginstall -d $(D(prefix)/stlport/lib
	ginstall $(WORKSRC)/SPRO-12u2-c++-libs/reloc/solstudio12.2/prod/lib/stlport4/libstlport.so.1 $(Dlib
	ginstall -d $(DESTDIR)$(prefix)$(prefix)/stlport/lib/$(ISA_DEFAULT64)
	ginstall $(WORKSRC)/SPRO-12u2-c++-libs/reloc/solstudio12.2/prod/lib/stlport4/$(ISADIR_$(ISA_DEFAULT64))/libstlport.so.1 $(Dlib/$(ISA_DEFAULT64)
	@$(MAKECOOKIE)
