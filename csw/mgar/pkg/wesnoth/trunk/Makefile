NAME = wesnoth
VERSION = 1.6.5
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = A free turn-based strategy game with a fanasy theme
define BLURB
  Build up a great army, gradually turning raw recruits into hardened veterans. In later games, recall your toughest warriors and form a deadly host against whom none can stand! Choose units from a large pool of specialists, and hand-pick a force with the right strengths to fight well on different terrains against all manner of opposition.  
endef

MASTER_SITES += $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=89495
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*)

PATCHFILES = language.cpp.diff
PATCHFILES += configure.diff
PATCHFILES += global.hpp.diff
PATCHFILES += generator_private.hpp.diff
PATCHFILES += image.cpp.diff
PATCHFILES += marked-up_text.cpp.diff
PATCHFILES += simple_wml.cpp.diff
PATCHFILES += time.hpp.diff

RUNTIME_DEP_PKGS_CSWwesnoth = CSWboostrt
RUNTIME_DEP_PKGS_CSWwesnoth += CSWfconfig
RUNTIME_DEP_PKGS_CSWwesnoth += CSWggettextrt
RUNTIME_DEP_PKGS_CSWwesnoth += CSWglib2
RUNTIME_DEP_PKGS_CSWwesnoth += CSWlibcairo
RUNTIME_DEP_PKGS_CSWwesnoth += CSWlibsdl
RUNTIME_DEP_PKGS_CSWwesnoth += CSWpango
RUNTIME_DEP_PKGS_CSWwesnoth += CSWpng
RUNTIME_DEP_PKGS_CSWwesnoth += CSWpython
RUNTIME_DEP_PKGS_CSWwesnoth += CSWsdlimage
RUNTIME_DEP_PKGS_CSWwesnoth += CSWsdlmixer
RUNTIME_DEP_PKGS_CSWwesnoth += CSWsdlnet
RUNTIME_DEP_PKGS_CSWwesnoth += CSWsdlttf
RUNTIME_DEP_PKGS_CSWwesnoth += CSWstlport
RUNTIME_DEP_PKGS_CSWwesnoth += CSWsunmath
RUNTIME_DEP_PKGS_CSWwesnoth += CSWzlib

CHECKPKG_OVERRIDES_CSWwesnoth += missing-dependency|CSWperl
CHECKPKG_OVERRIDES_CSWwesnoth += missing-dependency|CSWruby

EXTRA_LINKER_FLAGS = /usr/openwin/lib/libXext.so -L.

CONFIGURE_ARGS = --prefix=$(prefix)
CONFIGURE_ARGS += PKG_CONFIG_PATH=/opt/csw/X11/lib/pkgconfig
CONFIGURE_ARGS += CXXFLAGS='-features=extensions -library=stlport4'
CONFIGURE_ARGS += LIBS='-lstlport -lintl -lsocket -lnsl -lresolv -lboost_iostreams -lsunmath -lSDL_ttf -lcairo -lpango-1.0 -lpangocairo-1.0'
CONFIGURE_ARGS += PANGO_CFLAGS='-I/opt/csw/include/pango-1.0 -I/opt/csw/include/glib-2.0 -I/opt/csw/lib/glib-2.0/include -I/opt/csw/include/cairo'
CONFIGURE_ARGS += PANGO_LIBS='-L/opt/csw/lib -lpango-1.0 -lgobject-2.0 -lgmodule-2.0 -lglib-2.0 -lintl'
CONFIGURE_ARGS += LUA_CFLAGS=-I/opt/csw/include
CONFIGURE_ARGS += LUA_LIBS=-L/opt/csw/lib
CONFIGURE_ARGS += --with-fifodir=/var/opt/csw/run
CONFIGURE_ARGS += --enable-server
CONFIGURE_ARGS += --enable-tools
CONFIGURE_ARGS += --enable-editor
CONFIGURE_ARGS += --with-boost=/opt/csw
CONFIGURE_ARGS += --disable-strict-compilation
CONFIGURE_ARGS += --with-zlib-prefix=/opt/csw

TEST_SCRIPTS =

include gar/category.mk
