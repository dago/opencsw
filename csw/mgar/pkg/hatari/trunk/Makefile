NAME = hatari
VERSION = 1.3.1
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Atari ST emulator
define BLURB
Hatari is an Atari ST and STE emulator for GNU/Linux, BSD, BeOS, Mac OS X and other systems that are supported by the SDL library.
endef

MASTER_SITES = http://download.berlios.de/hatari/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
PACKAGES = CSWhatari
RUNTIME_DEP_PKGS = CSWlibsdl CSWpng CSWpython CSWreadline CSWzlib

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

LICENSE = gpl.txt
PATCHFILES = solaris8-compile.patch

GARCOMPILER = GNU
TEST_SCRIPTS =
CONFIGURE_ARGS = $(DIRPATHS) LIBS='-lm -lsocket -L/opt/csw/lib'

include gar/category.mk
