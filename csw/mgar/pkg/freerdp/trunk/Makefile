# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! cmake kills RPATH in linker flags somehow needs to be fixed.
# ! Error: recv: Resource temporarily unavailable
#     as reported in https://github.com/FreeRDP/FreeRDP/issues/571
#
NAME = FreeRDP
VERSION = 1.0.1
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = RDP client, a fork of the rdesktop project

MASTER_SITES = http://github.com/downloads/FreeRDP/FreeRDP/
DISTFILES += $(NAME)-$(VERSION).tar.gz

BUILD_DEP_PKGS += CSWffmpeg-dev
BUILD_DEP_PKGS += CSWxmlto

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386
PACKAGING_PLATFORMS += solaris11-sparc solaris11-i386
GARCOMPILER = GCC4

PACKAGES += CSWfreerdp-dev
SPKG_DESC_CSWfreerdp-dev += Development files for FreeRDP
PKGFILES_CSWfreerdp-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWfreerdp-dev += CSWfreerdp

PACKAGES += CSWfreerdp
SPKG_DESC_CSWfreerdp = RDP client, a fork of the rdesktop project
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWfreerdp += CSWlibgcc-s1

# Add flag as recommended in https://github.com/FreeRDP/FreeRDP/issues/571
#EXTRA_CFLAGS += -mt
EXTRA_CFLAGS += -threads

#EXTRA_CPPFLAGS = -features=extensions -D__FUNCTION__=__func__

CONFIGURE_ARGS = $(DIRPATHS)

# http://forge.mysql.com/wiki/Autotools_to_CMake_Transition_Guide
CMAKE_ARGS += -DCMAKE_INSTALL_PREFIX=$(prefix)
CMAKE_ARGS += -DCMAKE_C_FLAGS="$(CPPFLAGS) $(CFLAGS)"
# CMAKE_ARGS += -DCMAKE_CXX_FLAGS="$(CXXFLAGS)"
CMAKE_ARGS += -DCMAKE_INCLUDE_PATH="$(includedir)"
CMAKE_ARGS += -DCMAKE_LIBRARY_PATH="$(libdir)"
CMAKE_ARGS += -DWITH_SSE2=OFF 
CMAKE_ARGS += -DWITH_ALSA=OFF
CMAKE_ARGS += -DCMAKE_SKIP_RPATH=NO

CONFIGURE_SCRIPTS = custom

# There is no testsuite
TEST_SCRIPTS =

include gar/category.mk

post-extract-isa-$(ISA_DEFAULT_$(GARCH)):
	@( cd $(WORKDIR) ; mv Free* $(NAME)-$(VERSION$) )
	@$(MAKECOOKIE)

configure-custom:
	(cd $(WORKSRC) && \
		/usr/bin/env -i \
		  $(CONFIGURE_ENV) \
			cmake \
			. \
			$(CMAKE_ARGS))
	@$(MAKECOOKIE)
