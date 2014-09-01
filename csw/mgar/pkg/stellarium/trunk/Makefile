# : Makefile 9089 2010-03-11 08:34:46Z wahwah $
# NOTE: Qt QTSCRIPT library not found on unstable10s (sparc) but builds on x86
NAME = stellarium
VERSION = 0.11.4
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Planetarium with a realistic 3D sky just like seeing with naked eye
define BLURB
  Stellarium is a free open source planetarium for your computer. It shows a realistic
  sky in 3D, just like what you see with the naked eye, binoculars or a telescope. 
  It is being used in planetarium projectors. Just set your coordinates and go.
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?RUNTIME_DEP_PKGS_CSWstellarium += CSWlibqtcore4
RUNTIME_DEP_PKGS_CSWstellarium += CSWlibqtopengl4
RUNTIME_DEP_PKGS_CSWstellarium += CSWlibz1
RUNTIME_DEP_PKGS_CSWstellarium += CSWlibintl8
RUNTIME_DEP_PKGS_CSWstellarium += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWstellarium += CSWlibqtnetwork4
RUNTIME_DEP_PKGS_CSWstellarium += CSWmesa
RUNTIME_DEP_PKGS_CSWstellarium += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWstellarium += CSWlibqtgui4
RUNTIME_DEP_PKGS_CSWstellarium += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWstellarium += CSWlibqtscript4

PATCHFILES += 0001-avoid-compiler-confusion-change-int-to-float.patch
PATCHFILES += 0002-add-detect-solaris-and-undef-FS.patch

# need to override until we can figure out how to pass -Bdirect to cmake build
CHECKPKG_OVERRIDES_CSWstellarium += no-direct-binding|/opt/csw/bin/stellarium|is|not|directly|bound|to|soname|libGL.so.1
CHECKPKG_OVERRIDES_CSWstellarium += no-direct-binding|/opt/csw/bin/stellarium|is|not|directly|bound|to|soname|libQtCore.so.4
CHECKPKG_OVERRIDES_CSWstellarium += no-direct-binding|/opt/csw/bin/stellarium|is|not|directly|bound|to|soname|libQtGui.so.4
CHECKPKG_OVERRIDES_CSWstellarium += no-direct-binding|/opt/csw/bin/stellarium|is|not|directly|bound|to|soname|libQtNetwork.so.4
CHECKPKG_OVERRIDES_CSWstellarium += no-direct-binding|/opt/csw/bin/stellarium|is|not|directly|bound|to|soname|libQtOpenGL.so.4
CHECKPKG_OVERRIDES_CSWstellarium += no-direct-binding|/opt/csw/bin/stellarium|is|not|directly|bound|to|soname|libQtScript.so.4
CHECKPKG_OVERRIDES_CSWstellarium += no-direct-binding|/opt/csw/bin/stellarium|is|not|directly|bound|to|soname|libintl.so.8
CHECKPKG_OVERRIDES_CSWstellarium += no-direct-binding|/opt/csw/bin/stellarium|is|not|directly|bound|to|soname|libstdc++.so.6

CONFIGURE_ARGS = $(DIRPATHS)

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS = custom
INSTALL_SCRIPTS = custom
TEST_SCRIPTS =

include gar/category.mk

# ./configure needs this to find ggettext
PATH := /opt/csw/gnu:$(PATH)

# customize configure to perform a cmake build
configure-custom:
	mkdir $(WORKSRC)/build
	cd $(WORKSRC)/build && \
	/opt/csw/bin/cmake \
	-DCMAKE_INSTALL_PREFIX=/opt/csw \
	-DCMAKE_INCLUDE_PATH=/opt/csw/include \
	-DCMAKE_LIBRARY_PATH=/opt/csw/lib \
	-DCMAKE_SHARED_LINKER_FLAGS=-Bdirect \
	-DCMAKE_C_COMPILER=gcc \
	-DCMAKE_CXX_COMPILER=g++ ..
	@$(MAKECOOKIE)

build-custom:
	cd $(WORKSRC)/build && /opt/csw/bin/gmake
	@$(MAKECOOKIE)

install-custom:
	cd $(WORKSRC)/build && /opt/csw/bin/gmake install DESTDIR=$(DESTDIR)
	@$(MAKECOOKIE)
