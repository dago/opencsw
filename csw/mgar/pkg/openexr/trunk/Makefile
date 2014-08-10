NAME = openexr
VERSION = 2.1.0
GARTYPE = v2

DESCRIPTION = High dynamic-rangenamic-range (HDR) image file format developed by Industrial Light & Magic
define BLURB
	IlmImf is our "EXR" file format for storing 16-bit FP images.  Libraries in
	this package depend on the IlmBase library.

	See the IlmImfExamples directory for some code that demonstrates how
	to use the IlmImf library to read and write OpenEXR files.  The doc
	directory contains some high-level documentation and history about the
	OpenEXR format.

	If you have questions about using the OpenEXR libraries, you may want
	to join our developer mailing list.  See http://www.openexr.com for
	details.
endef

MASTER_SITES = http://download.savannah.nongnu.org/releases/openexr/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

VENDOR_URL = http://www.openexr.com

LICGARCOMPILER = GCC4

PATCHFILES += 0003_no_posix_memalign.patch

BUILD_DEP_PKGS += CSWilmbase-dev

PACKAGES += CSWopenexr
CATALOGNAME_CSWopenexr = openexr
SPKG_DESC_CSWopenexr = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWopenexr += CSWlibilmimf-imf2-0-20
RUNTIME_DEP_PKGS_CSWopenexr += CSWlibhalf10
RUNTIME_DEP_PKGS_CSWopenexr += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWopenexr += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWopenexr += CSWlibiex2-0-10
OBSOLETED_BY_CSWopenexr += CSWopenexrrt
# Package is catchall

PACKAGES += CSWlibilmimf-imf2-0-20
CATALOGNAME_CSWlibilmimf-imf2-0-20 = libilmimf_imf2_0_20
PKGFILES_CSWlibilmimf-imf2-0-20 += $(call baseisadirs,$(libdir),libIlmImf-Imf_2_0\.so\.20\.0\.1)
PKGFILES_CSWlibilmimf-imf2-0-20 += $(call baseisadirs,$(libdir),libIlmImf-Imf_2_0\.so\.20(\.\d+)*)
SPKG_DESC_CSWlibilmimf-imf2-0-20 += $(DESCRIPTION), libIlmImf-Imf_2_0.so.20
RUNTIME_DEP_PKGS_CSWlibilmimf-imf2-0-20 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibilmimf-imf2-0-20 += CSWlibilmthread2-0-10
RUNTIME_DEP_PKGS_CSWlibilmimf-imf2-0-20 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibilmimf-imf2-0-20 += CSWlibiex2-0-10
RUNTIME_DEP_PKGS_CSWlibilmimf-imf2-0-20 += CSWlibhalf10
RUNTIME_DEP_PKGS_CSWlibilmimf-imf2-0-20 += CSWlibgcc-s1b
SPKG_DESC_CSW =

PACKAGES += CSWopenexr-dev
SPKG_DESC_CSWopenexr-dev = Development files for ...
PKGFILES_CSWopenexr-dev += $RUNTIME_DEP_PKGS_CSWopenexr-dev += CSWlibilmimf-imf2-0-20
OBSOLETED_BY_CSWopenexr-dev += CSWopenexrdevel

BUILD64 = 1
ISAEXEC = 1

SKIPTEST = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared
CONFIGURE_ARGS += --disable-static
CONFIGURE_ARGS += --disable-ilmbasetest

EXTRA_LD_OPTIONS = -z nolazyload

include gar/category.mk

post-install-modulated:
	perl -ip \
		-e 's/-pthread/-lpthread -D_REENTRANT -D_PTHREADS/g' \
		$(DESTDIR)$(libdir)/pkgconfig/*.pc
	@$(MAKECOOKIE)
