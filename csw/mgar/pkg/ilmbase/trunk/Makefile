NAME = ilmbase
VERSION = 2.0.1
CATEGORIES = lib
GARTYPE = v2

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

PATCHFILES +=PATCHFILES += 0002_avoid_cpu_opt_on_sparcILES += ImathMath.patch

VENDOR_URL = http://www.openexr.com

LIGARCOMPILER = GCC4

PACKAGES += CSWlibhalf10
CATALOGNAME_CSWlibhalf10 = libhalf10
PKGFILES_CSWlibhalf10 += $(call baseisadirs,$(libdir),libHalf\.so\.10\.0\.1)
PKGFILES_CSWlibhalf10 += $(call baseisadirs,$(libdir),libHalf\.so\.10(\.\d+)*)
SPKG_DESC_CSWlibhalf10 += $(DESCRIPTION), libHalf.so.10
RUNTIME_DEP_PKGS_CSWlibhalf10 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibhalf10 += CSWlibstdc++6

PACKAGES += CSWlibiex2-0-10
CATALOGNAME_CSWlibiex2-0-10 = libiex2_0_10
PKGFILES_CSWlibiex2-0-10 += $(call baseisadirs,$(libdir),libIex-2_0\.so\.10\.0\.1)
PKGFILES_CSWlibiex2-0-10 += $(call baseisadirs,$(libdir),libIex-2_0\.so\.10(\.\d+)*)
SPKG_DESC_CSWlibiex2-0-10 += $(DESCRIPTION), libIex-2_0.so.10
RUNTIME_DEP_PKGS_CSWlibiex2-0-10 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibiex2-0-10 += CSWlibstdc++6

PACKAGES += CSWlibiexmath2-0-10
CATALOGNAME_CSWlibiexmath2-0-10 = libiexmath2_0_10
PKGFILES_CSWlibiexmath2-0-10 += $(call baseisadirs,$(libdir),libIexMath-2_0\.so\.10\.0\.1)
PKGFILES_CSWlibiexmath2-0-10 += $(call baseisadirs,$(libdir),libIexMath-2_0\.so\.10(\.\d+)*)
SPKG_DESC_CSWlibiexmath2-0-10 += $(DESCRIPTION), libIexMath-2_0.so.10
RUNTIME_DEP_PKGS_CSWlibiexmath2-0-10 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibiexmath2-0-10 += CSWlibstdc++6

PACKAGES += CSWlibilmthread2-0-10
CATALOGNAME_CSWlibilmthread2-0-10 = libilmthread2_0_10
PKGFILES_CSWlibilmthread2-0-10 += $(call baseisadirs,$(libdir),libIlmThread-2_0\.so\.10\.0\.1)
PKGFILES_CSWlibilmthread2-0-10 += $(call baseisadirs,$(libdir),libIlmThread-2_0\.so\.10(\.\d+)*)
SPKG_DESC_CSWlibilmthread2-0-10 += $(DESCRIPTION), libIlmThread-2_0.so.10
RUNTIME_DEP_PKGS_CSWlibilmthread2-0-10 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibilmthread2-0-10 += CSWlibstdc++6

PACKAGES += CSWlibimath2-0-10
CATALOGNAME_CSWlibimath2-0-10 = libimath2_0_10
PKGFILES_CSWlibimath2-0-10 += $(call baseisadirs,$(libdir),libImath-2_0\.so\.10\.0\.1)
PKGFILES_CSWlibimath2-0-10 += $(call baseisadirs,$(libdir),libImath-2_0\.so\.10(\.\d+)*)
SPKG_DESC_CSWlibimath2-0-10 += $(DESCRIPTION), libImath-2_0.so.10
RUNTIME_DEP_PKGS_CSWlibimath2-0-10 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibimath2-0-10 += CSWlibstdc++6
h6 += CSWilmbase

PACKAGES += CSWilmbase-dev
SPKG_DESC_CSWilmbase-dev += Development files for ILM base libraries
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWilmbhalf10
RUNTIME_DEP_PKGS_CSWilmbase-dev += CSWlibiex2-0-10
RUNTIME_DEP_PKGS_CSWilmbase-dev += CSWlibiexmath2-0-10
RUNTIME_DEP_PKGS_CSWilmbase-dev += CSWlibilmthread2-0-10
RUNTIME_DEP_PKGS_CSWilmbase-dev += CSWlibimath2-0-10v += CSWlibimath6
OBSOLETED_BY_CSWilmbase-dev += CSWilmbasedevel
CATALOGNAME_CSWilmbasedevel = ilmbase_devel_stub  = -lm
EXTRA_LD_OPTIONS = -z nolazyload

BUILD64_LIBS_ONLY = 1

# make check has some linking issues
SKIPTEST = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared
CONFIGURE_ARGS += --disable-staticD64_LIBS_ONLY = 1

include