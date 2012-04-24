NAME = libstlport
VERSION = 4.5.3
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = A multiplatform C++ standard library implementation

MASTER_SITES = manual://
PATCH-sparc = 145730-05
PATCH-i386  = 145731-05
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

PACKAGES += CSWlibstlport1-stlport
SPKG_DESC_CSWlibstlport1-stlport = Runtime library for Sun Studio STLPort, libstlport.so.1 from patch $(PATCH)
PKGFILES_CSWlibstlport1-stlport += $(call baseisadirs,$(prefix)/stlport/lib,libstlport.so.1)
OBSOLETED_BY_CSWlibstlport1-stlport = CSWstlport
# These are legacy symlinks. Add them to the stub packages for packages that have not been rebuild and require
# the libstlport.so.1 in /opt/csw/lib
PKGFILES_CSWstlport += $(libdir)/.*
# Disable archall as the directories contain sparcv9|amd64
ARCHALL_CSWstlport =

# Just keep the pathes as we copy the libs verbatim
CHECKPKG_OVERRIDES_CSWlibstlport1-stlport += bad-rpath-entry

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

ISADIR_sparcv9 = v9
ISADIR_amd64 = amd64

install-custom:
	ginstall -d $(DESTDIR)$(prefix)/stlport/lib
	ginstall $(WORKSRC)/SPRO-12u2-c++-libs/reloc/solstudio12.2/prod/lib/stlport4/libstlport.so.1 $(DESTDIR)$(prefix)/stlport/lib
	ginstall -d $(DESTDIR)$(prefix)/stlport/lib/$(ISA_DEFAULT64)
	ginstall $(WORKSRC)/SPRO-12u2-c++-libs/reloc/solstudio12.2/prod/lib/stlport4/$(ISADIR_$(ISA_DEFAULT64))/libstlport.so.1 $(DESTDIR)$(prefix)/stlport/lib/$(ISA_DEFAULT64)
	ginstall -d $(DESTDIR)$(prefix)/lib
	ln -s ../stlport/lib/libstlport.so.1 $(DESTDIR)$(prefix)/lib
	ginstall -d $(DESTDIR)$(prefix)/lib/$(ISA_DEFAULT64)
	ln -s ../../stlport/lib/$(ISA_DEFAULT64)/libstlport.so.1 $(DESTDIR)$(prefix)/lib/$(ISA_DEFAULT64)
	@$(MAKECOOKIE)
