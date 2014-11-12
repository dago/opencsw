# NOTE: cmake finds boost library but "mgar build" step can't find boost 
#	headers and setting EXTRA_INC or EXTRA_CPPFLAGS doesn't help.
NAME = wesnoth
VERSION = 1.10.7
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
UFILES_REGEX = $(NAME)RUNTIME_DEP_PKGS_CSWwesnoth += CSWlibpango1-0-0
RUNTIME_DEP_PKGS_CSWwesnoth += CSWemacs-common
RUNTIME_DEP_PKGS_CSWwesnoth += CSWlibintl8
RUNTIME_DEP_PKGS_CSWwesnoth += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWwesnoth += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWwesnoth += CSWsdlnet
RUNTIME_DEP_PKGS_CSWwesnoth += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWwesnoth += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWwesnoth += CSWlibsdl1-2-0
RUNTIME_DEP_PKGS_CSWwesnoth += CSWlibdbus1-3
RUNTIME_DEP_PKGS_CSWwesnoth += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWwesnoth += CSWsdlttf
RUNTIME_DEP_PKGS_CSWwesnoth += CSWsdlimage
RUNTIME_DEP_PKGS_CSWwesnoth += CSWlibpangocairo1-0-0
RUNTIME_DEP_PKGS_CSWwesnoth += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWwesnoth += CSWsdlmixer
RUNTIME_DEP_PKGS_CSWwesnoth += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWwesnoth += CSWlibboost-system1-49-0-gxx
RUNTIME_DEP_PKGS_CSWwesnoth += CSWlibboost-prog-opts1-49-0-gxx
RUNTIME_DEP_PKGS_CSWwesnoth += CSWlibboost-regex1-49-0-gxx
RUNTIME_DEP_PKGS_CSWwesnoth += CSWlibboost-iostreams1-49-0-gxx

# Temporarily overriding till we can figure out how to pass -Bdirect thru cmake
CHECKPKG_OVERRIDES_CSWwesnoth += no-direct-binding|/opt/csw/bin/wesnoth|is|not|directly|bound|to|soname|libSDL-1.2.so.0
CHECKPKG_OVERRIDES_CSWwesnoth += no-direct-binding|/opt/csw/bin/wesnoth|is|not|directly|bound|to|soname|libSDL_image-1.2.so.0
CHECKPKG_OVERRIDES_CSWwesnoth += no-direct-binding|/opt/csw/bin/wesnoth|is|not|directly|bound|to|soname|libSDL_mixer-1.2.so.0
CHECKPKG_OVERRIDES_CSWwesnoth += no-direct-binding|/opt/csw/bin/wesnoth|is|not|directly|bound|to|soname|libSDL_net-1.2.so.0
CHECKPKG_OVERRIDES_CSWwesnoth += no-direct-binding|/opt/csw/bin/wesnoth|is|not|directly|bound|to|soname|libSDL_ttf-2.0.so.0
CHECKPKG_OVERRIDES_CSWwesnoth += no-direct-binding|/opt/csw/bin/wesnoth|is|not|directly|bound|to|soname|libX11.so.4
CHECKPKG_OVERRIDES_CSWwesnoth += no-direct-binding|/opt/csw/bin/wesnoth|is|not|directly|bound|to|soname|libboost_iostreams.so.1.49.0
CHECKPKG_OVERRIDES_CSWwesnoth += no-direct-binding|/opt/csw/bin/wesnoth|is|not|directly|bound|to|soname|libboost_program_options.so.1.49.0
CHECKPKG_OVERRIDES_CSWwesnoth += no-direct-binding|/opt/csw/bin/wesnoth|is|not|directly|bound|to|soname|libboost_regex.so.1.49.0
CHECKPKG_OVERRIDES_CSWwesnoth += no-direct-binding|/opt/csw/bin/wesnoth|is|not|directly|bound|to|soname|libboost_system.so.1.49.0
CHECKPKG_OVERRIDES_CSWwesnoth += no-direct-binding|/opt/csw/bin/wesnoth|is|not|directly|bound|to|soname|libcairo.so.2
CHECKPKG_OVERRIDES_CSWwesnoth += no-direct-binding|/opt/csw/bin/wesnoth|is|not|directly|bound|to|soname|libdbus-1.so.3
CHECKPKG_OVERRIDES_CSWwesnoth += no-direct-binding|/opt/csw/bin/wesnoth|is|not|directly|bound|to|soname|libfontconfig.so.1
CHECKPKG_OVERRIDES_CSWwesnoth += no-direct-binding|/opt/csw/bin/wesnoth|is|not|directly|bound|to|soname|libgobject-2.0.so.0
CHECKPKG_OVERRIDES_CSWwesnoth += no-direct-binding|/opt/csw/bin/wesnoth|is|not|directly|bound|to|soname|libintl.so.8
CHECKPKG_OVERRIDES_CSWwesnoth += no-direct-binding|/opt/csw/bin/wesnoth|is|not|directly|bound|to|soname|libpango-1.0.so.0
CHECKPKG_OVERRIDES_CSWwesnoth += no-direct-binding|/opt/csw/bin/wesnoth|is|not|directly|bound|to|soname|libpangocairo-1.0.so.0
CHECKPKG_OVERRIDES_CSWwesnoth += no-direct-binding|/opt/csw/bin/wesnoth|is|not|directly|bound|to|soname|libstdc++.so.6
CHECKPKG_OVERRIDES_CSWwesnoth += no-direct-binding|/opt/csw/bin/wesnothd|is|not|directly|bound|to|soname|libSDL-1.2.so.0
CHECKPKG_OVERRIDES_CSWwesnoth += no-direct-binding|/opt/csw/bin/wesnothd|is|not|directly|bound|to|soname|libSDL_net-1.2.so.0
CHECKPKG_OVERRIDES_CSWwesnoth += no-direct-binding|/opt/csw/bin/wesnothd|is|not|directly|bound|to|soname|libboost_iostreams.so.1.49.0
CHECKPKG_OVERRIDES_CSWwesnoth += no-direct-binding|/opt/csw/bin/wesnothd|is|not|directly|bound|to|soname|libintl.so.8
CHECKPKG_OVERRIDES_CSWwesnoth += no-direct-binding|/opt/csw/bin/wesnothd|is|not|directly|bound|to|soname|libstdc++.so.6

NOGITPATCH = 1pt/csw/gxx/include

GARCOMPILER = GNU

TEST_SCRIPTS =

CONFIGUREBUILD_SCRIPTS = custom
INSTALL_SCRIPTS = custom

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

include gar/category.mk

# ./configure needs this to find ggettext
PATH := /opt/csw/gnu:$(PATH)

# Autotools build depreciated now using cmake
configure-custom:
	mkdir $(WORKSRC)/build
	cd $(WORKSRC)/build && \
	CC=gcc CXX=g++ CXXFLAGS=-Wno-delete-non-virtual-dtor \
	CPPFLAGS=-I/opt/csw/gxx/include LDFLAGS="-lintl -lsocket -Bdirect" \
	/opt/csw/bin/cmake VERBOSE=1 \
	-DCMAKE_INSTALL_PREFIX=/opt/csw \
	-DCMAKE_INCLUDE_PATH=/opt/csw/gxx/include /opt/csw/include \
	-DCMAKE_LIBRARY_PATH=/opt/csw/gxx/lib /opt/csw/lib \
	-DCMAKE_INSTALL_RPATH:STRING="/opt/csw/lib/\$$ISALIST:/opt/csw/lib:/opt/csw/gxx/lib" \
	-DBoost_DEBUG:BOOL=ON \
	-DBOOST_INCLUDEDIR=/opt/csw/gxx/include \
	..
	@$(MAKECOOKIE)

build-custom:
	# Link the boost headers to the build/src directory in order to work-
	# around boost headers not being found even though we try to include
	# them see above (CPPFLAGS) and (-DCMAKE_INCLUDE_PATH).
	ln -s /opt/csw/gxx/include/boost $(WORKSRC)/build/src/
	cd $(WORKSRC)/build && /opt/csw/bin/gmake VERBOSE=1
	@$(MAKECOOKIE)

install-custom:
	cd $(WORKSRC)/build && /opt/csw/bin/gmake install DESTDIR=$(DESTDIR)
	@$(MAKECOOKIE)

post-install-modulated:
	# remove .gitignore files from the package install
	find $(DESTDIR) -type f -name ".gitignore" -exec rm -f {} \;
	@$(MAKECOOKIE)
