NAME = hatari
VERSION = 1.8.0
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Atari ST emulator
define BLURB
Hatari is an Atari ST and STE emulator for GNU/Linux, BSD, BeOS, Mac OS X and other systems that are supported by the SDL library.
endef

MASTER_SITES tuxfamily.org/hatari/$(VERSION)/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
PACKAGES = CSWhatari

RUNTIME_DEP_PKGS_CSWhatari += CSWlibz1
RUNTIME_DEP_PKGS_CSWhatari += CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWhatari += CSWlibsdl1-2-0
RUNTIME_DEP_PKGS_CSWhatari += CSWlibreadline6

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

LICENSE = gpl.txt

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS = custom
INSTALL_SCRIPTS = custom

TEST_SCRIPTS =

# override no-direct-binding until we can figure out how to enable -Bdirect in cmake (see below)
CHECKPKG_OVERRIDES_CSWhatari += no-direct-binding|/opt/csw/bin/hatari|is|not|directly|bound|to|soname|libICE.so.6
CHECKPKG_OVERRIDES_CSWhatari += no-direct-binding|/opt/csw/bin/hatari|is|not|directly|bound|to|soname|libSDL-1.2.so.0
CHECKPKG_OVERRIDES_CSWhatari += no-direct-binding|/opt/csw/bin/hatari|is|not|directly|bound|to|soname|libSM.so.6
CHECKPKG_OVERRIDES_CSWhatari += no-direct-binding|/opt/csw/bin/hatari|is|not|directly|bound|to|soname|libX11.so.4
CHECKPKG_OVERRIDES_CSWhatari += no-direct-binding|/opt/csw/bin/hatari|is|not|directly|bound|to|soname|libXext.so.0
CHECKPKG_OVERRIDES_CSWhatari += no-direct-binding|/opt/csw/bin/hatari|is|not|directly|bound|to|soname|libpng15.so.15
CHECKPKG_OVERRIDES_CSWhatari += no-direct-binding|/opt/csw/bin/hatari|is|not|directly|bound|to|soname|libreadline.so.6
CHECKPKG_OVERRIDES_CSWhatari += no-direct-binding|/opt/csw/bin/hatari|is|not|directly|bound|to|soname|libz.so.1
CHECKPKG_OVERRIDES_CSWhatari += no-direct-binding|/opt/csw/bin/hmsa|is|not|directly|bound|to|soname|libz.so.1

include gar/category.mk

# use cmake to build

configure-custom:
	mkdir $(WORKSRC)/build
	cd $(WORKSRC)/build && \
	/opt/csw/bin/cmake \
	-DCMAKE_INSTALL_PREFIX=/opt/csw \
	-DCMAKE_INCLUDE_PATH=/opt/csw/include \
	-DCMAKE_LIBRARY_PATH=/opt/csw/lib \
	-DCMAKE_INSTALL_RPATH=/opt/csw/lib/\$$ISALIST /opt/csw/lib \
	-DCMAKE_EXE_LINKER_FLAGS=-Bdirect \
	-DCMAKE_C_COMPILER=gcc ..
	@$(MAKECOOKIE)

build-custom:
	cd $(WORKSRC)/build && /opt/csw/bin/gmake
	@$(MAKECOOKIE)

install-custom:
	cd $(WORKSRC)/build && /opt/csw/bin/gmake install DESTDIR=$(DESTDIR)
	@$(MAKECOOKIE)

post-install-modulated:
	gunzip $(DESTDIR)/opt/csw/share/man/man1/*.gz
	@$(MAKECOOKIE)
