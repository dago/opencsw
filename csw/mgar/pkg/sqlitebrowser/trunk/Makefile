# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = sqlitebrowser
VERSION = 3.4.0
GIT_VERSION = v$(VERSION)
GARTYPE = v2
CATEGORIES = gnome

DESCRIPTION = DB Browser for SQLite
define BLURB
  DB Browser for SQLite is a high quality, visual, open source tool to create, design, and edit database files compatible with SQLite.
endef

MASTER_SITES =
GIT_REPOS = http://github.com/$(NAME)/$(NAME).git
GIT_TREEISH_sqlitebrowser.git = $(GIT_VERSION)

# g++4 handles nested namespaces different
PATCHFILES += 0001-fix-namespace.patch

BUILD_DEP_PKGS += CSWqt4-dev
BUILD_DEP_PKGS += CSWcmake

GARCOMPILER = GCC4
SKIPTEST = 1

RUNTIME_DEP_PKGS_CSWsqlitebrowser += CSWlibqtcore4
RUNTIME_DEP_PKGS_CSWsqlitebrowser += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWsqlitebrowser += CSWlibqtnetwork4
RUNTIME_DEP_PKGS_CSWsqlitebrowser += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWsqlitebrowser += CSWlibqtgui4
RUNTIME_DEP_PKGS_CSWsqlitebrowser += CSWlibgcc-s1
# QT apps need fonconfig
RUNTIME_DEP_PKGS_CSWsqlitebrowser += CSWfontconfig
CHECKPKG_OVERRIDES_CSWsqlitebrowser += surplus-dependency|CSWfontconfig

CONFIGURE_ARGS = $(DIRPATHS)

# http://dev.mysql.com/doc/internals/en/autotools-to-cmake.html
CMAKE_ARGS += -DCMAKE_INSTALL_PREFIX=$(prefix)
CMAKE_ARGS += -DCMAKE_C_FLAGS="$(CPPFLAGS) $(CFLAGS)"
# CMAKE_ARGS += -DCMAKE_CXX_FLAGS="$(CXXFLAGS)"
CMAKE_ARGS += -DCMAKE_INCLUDE_PATH="$(includedir)"
CMAKE_ARGS += -DCMAKE_LIBRARY_PATH="$(libdir)"
CMAKE_ARGS += -DCMAKE_SKIP_RPATH=NO
CMAKE_ARGS += -DCMAKE_EXE_LINKER_FLAGS="-Wl,-Bdirect -Wl,-zignore"
CMAKE_ARGS += -DCMAKE_VERBOSE_MAKEFILE=1

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS = custom
INSTALL_SCRIPTS = custom

configure-custom: 
	cd $(WORKSRC) && ([ ! -d build ] && mkdir build || true) && cd build && \
	$(CONFIGURE_ENV) cmake .. $(CMAKE_ARGS)
	@$(MAKECOOKIE)

build-custom: 
	cd $(WORKSRC)/build && gmake V=1
	@$(MAKECOOKIE)

install-custom: 
	cd $(WORKSRC)/build && gmake install DESTDIR=$(DESTDIR)
	@$(MAKECOOKIE)

#	cd $(WORKSRC) && $(bindir)/qmake $(call tolower,$(NAME)).pro
include gar/category.mk

