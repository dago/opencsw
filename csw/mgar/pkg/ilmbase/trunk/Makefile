NAME = ilmbase
VERSION = 1.0.2
CATEGORIES = lib

DESCRIPTION = Base libraries used by OpenEXR
define BLURB
	Half is a class that encapsulates our 16-bit floating-point format.

	IlmThread is a thread abstraction library for use with OpenEXR
	and other software packages.  It currently supports pthreads and
	Windows threads.

	Imath implements 2D and 3D vectors, 3x3 and 4x4 matrices, quaternions
	and other useful 2D and 3D math functions.

	Iex is an exception-handling library.

	If you have questions about using the IlmBase libraries, you may want
	to join our developer mailing list.  See http://www.openexr.com for
	details.
endef

MASTER_SITES = http://download.savannah.nongnu.org/releases/openexr/ 
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PATCHFILES += ImathMath.patch

VENDOR_URL = http://www.openexr.com

LICENSE = LICENSE

PACKAGES += CSWlibhalf6
SPKG_DESC_CSWlibhalf6 += $(DESCRIPTION), libHalf.so.6
PKGFILES_CSWlibhalf6 += $(call pkgfiles_lib,libHalf.so.6)
OBSOLETED_BY_CSWlibhalf6 += CSWilmbase
RUNTIME_DEP_PKGS_CSWlibilmthread6 += CSWlibiex6

PACKAGES += CSWlibiex6
SPKG_DESC_CSWlibiex6 += $(DESCRIPTION), libIex.so.6
PKGFILES_CSWlibiex6 += $(call pkgfiles_lib,libIex.so.6)
OBSOLETED_BY_CSWlibiex6 += CSWilmbase

PACKAGES += CSWlibilmthread6
SPKG_DESC_CSWlibilmthread6 += $(DESCRIPTION), libIlmThread.so.6
PKGFILES_CSWlibilmthread6 += $(call pkgfiles_lib,libIlmThread.so.6)
OBSOLETED_BY_CSWlibilmthread6 += CSWilmbase

PACKAGES += CSWlibimath6
SPKG_DESC_CSWlibimath6 += $(DESCRIPTION), libImath.so.6
PKGFILES_CSWlibimath6 += $(call pkgfiles_lib,libImath.so.6)
RUNTIME_DEP_PKGS_CSWlibimath6 += CSWlibiex6
OBSOLETED_BY_CSWlibimath6 += CSWilmbase

PACKAGES += CSWilmbase-dev
SPKG_DESC_CSWilmbase-dev += Development files for ILM base libraries
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWilmbase-dev += CSWlibilmthread6
RUNTIME_DEP_PKGS_CSWilmbase-dev += CSWlibhalf6
RUNTIME_DEP_PKGS_CSWilmbase-dev += CSWlibiex6
RUNTIME_DEP_PKGS_CSWilmbase-dev += CSWlibimath6
OBSOLETED_BY_CSWilmbase-dev += CSWilmbasedevel
CATALOGNAME_CSWilmbasedevel = ilmbase_devel_stub

EXTRA_LD_FLAGS = -lm

EXTRA_CXXFLAGS += -norunpath
REINPLACE_MATCH = (\|-xarch=)
REINPLACE_WITH = |-norunpath$$1
REINPLACE_FILES += ltmain.sh

BUILD64_LIBS_ONLY = 1

include gar/category.mk
