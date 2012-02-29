# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! cmake kills RPATH in linker flags somehow needs to be fixed.
#
NAME = FreeRDP
VERSION = 1.0.1
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = RDP client. Fork of the rdesktop project.
define BLURB
  Long description
endef

MASTER_SITES = http://github.com/downloads/FreeRDP/FreeRDP/
DISTFILES    = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz


PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386
GARCOMPILER = GCC4

PACKAGES += CSWfreerdp-dev
CATALOGNAME_CSWfreerdp-dev = FreeRDP_dev
SPKG_DESC_CSWfreerdp-dev += $(DESCRIPTION), development files
RUNTIME_DEP_PKGS_CSWfreerdp-dev += CSWfreerdp
PKGFILES_CSWfreerdp-dev += /opt/csw/lib/libfreerdp-cache.so
PKGFILES_CSWfreerdp-dev += /opt/csw/lib/libfreerdp-channels.so
PKGFILES_CSWfreerdp-dev += /opt/csw/lib/libfreerdp-codec.so
PKGFILES_CSWfreerdp-dev += /opt/csw/lib/libfreerdp-core.so
PKGFILES_CSWfreerdp-dev += /opt/csw/lib/libfreerdp-gdi.so
PKGFILES_CSWfreerdp-dev += /opt/csw/lib/libfreerdp-kbd.so
PKGFILES_CSWfreerdp-dev += /opt/csw/lib/libfreerdp-rail.so
PKGFILES_CSWfreerdp-dev += /opt/csw/lib/libfreerdp-utils.so
PKGFILES_CSWfeerdp-dev += $(PKGFILES_DEVEL)

PACKAGES += CSWfreerdp
SPKG_DESC_CSWfreerdp = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWfreerdp += CSWlibgcc-s1


CONFIGURE_ARGS = $(DIRPATHS)

# http://forge.mysql.com/wiki/Autotools_to_CMake_Transition_Guide
CMAKE_ARGS += -DCMAKE_INSTALL_PREFIX=$(prefix)
CMAKE_ARGS += -DCMAKE_C_FLAGS="$(CFLAGS)" -DCMAKE_CXX_FLAGS="$(CXXFLAGS)"
CMAKE_ARGS += -DCMAKE_INCLUDE_PATH="$(includedir)"
CMAKE_ARGS += -DCMAKE_LIBRARY_PATH="$(libdir)"
CMAKE_ARGS += -DWITH_SSE2=OFF 
CMAKE_ARGS += -DWITH_ALSA=OFF
CMAKE_ARGS += -DCMAKE_SKIP_RPATH=NO

CONFIGURE_SCRIPTS = custom

SKIPTEST = 1

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
