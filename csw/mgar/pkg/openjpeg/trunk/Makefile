NAME = openjpeg
VERSION = 2.0.0
GARTYPE = v2

DESCRIPTION = Open-source JPEG 2000 codec written in C
define BLURB
The OpenJPEG library is an open-source JPEG 2000 codec written in C language. It has been developed in order to promote the use of JPEG 2000, the new still-image compression standard from the Joint Photographic Experts Group (JPEG). In addition to the basic codec, various other features are under development, among them the JP2 and MJ2 (Motion JPEG 2000) file formats, an indexing tool useful for the JPIP protocol, JPWL-tools for error-resilience, a Java-viewer for j2k-images, ..
endef

VENDOR_URL   = http://code.google.com/p/openjpeg/
MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES    = $(DISTNAME).tar.gz
LICENSE      = LICENSE

GARCOMPILER = GCC4

PACKAGES += CSWlibopenjp2-6
CATALOGNAME_CSWlibopenjp2-6 = libopenjp2_6
PKGFILES_CSWlibopenjp2-6 += $(call baseisadirs,$(libdir),libopenjp2\.so\.2\.0\.0)
PKGFILES_CSWlibopenjp2-6 += $(call baseisadirs,$(libdir),libopenjp2\.so\.6)
SPKG_DESC_CSWlibopenjp2-6 += $(DESCRIPTION), libopenjp2.so.6
RUNTIME_DEP_PKGS_CSWlibopenjp2-6 += CSWlibgcc-s1

PACKAGES += CSWopenjpeg-dev
CATALOGNAME_CSWopenjpeg-dev = openjpeg_dev
SPKG_DESC_CSWopenjpeg-dev += $(DESCRIPTION), development files
PKGFILES_CSWopenjpeg-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWopenjpeg-dev += CSWlibopenjp2-6

RUNTIME_DEP_PKGS_CSWopenjpeg += CSWlibopenjp2-6

# For some reason the so.6 links to the so.2.0.0
CHECKPKG_OVERRIDES_CSWlibopenjp2-6 += soname-not-part-of-filename|soname=libopenjp2.so.6|filename=libopenjp2.so.2.0.0

CMAKE_ARGS += -DCMAKE_C_FLAGS="$(CFLAGS)"
CMAKE_ARGS += -DCMAKE_LIBRARY_PATH="$(libdir)"
CMAKE_ARGS += -DCMAKE_PREFIX_PATH="$(prefix)"
CMAKE_ARGS += -DCMAKE_INCLUDE_PATH="$(includedir)"
CMAKE_ARGS += -DCMAKE_VERBOSE_MAKEFILE=ON
CMAKE_ARGS += -DCMAKE_INSTALL_PREFIX=$(prefix)
CMAKE_ARGS += -DBUILD_SHARED_LIBS:bool=on
CMAKE_ARGS += -DBUILD_CODEC:bool=on
CMAKE_ARGS += -DOPENJPEG_INSTALL_BIN_DIR=$(subst $(prefix)/,,$(bindir))
CMAKE_ARGS += -DOPENJPEG_INSTALL_LIB_DIR=$(subst $(prefix)/,,$(libdir))

BUILD64 = 1
ISAEXEC = 1

CONFIGURE_SCRIPTS = custom
TEST_TARGET = 

include gar/category.mk

configure-custom:
	(cd $(WORKSRC) && \
		/usr/bin/env -i \
			$(CONFIGURE_ENV) \
			cmake \
			. \
			$(CMAKE_ARGS))
	@$(MAKECOOKIE)

