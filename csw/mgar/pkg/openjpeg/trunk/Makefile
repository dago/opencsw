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

GARCOMPILER = GCC4

CMAKE_ARGS += -DCMAKE_C_FLAGS="$(CFLAGS)"
CMAKE_ARGS += -DCMAKE_CXX_FLAGS="$(CXXFLAGS)"
CMAKE_ARGS += -DCMAKE_LIBRARY_PATH="$(libdir)"
CMAKE_ARGS += -DCMAKE_PREFIX_PATH="$(prefix)"
CMAKE_ARGS += -DCMAKE_INCLUDE_PATH="$(includedir)"
CMAKE_ARGS += -DCMAKE_VERBOSE_MAKEFILE=ON
CMAKE_ARGS += -DCMAKE_INSTALL_PREFIX=$(prefix)
CMAKE_ARGS += -DBUILD_SHARED_LIBS:bool=on
CMAKE_ARGS += -DBUILD_CODEC:bool=on

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

