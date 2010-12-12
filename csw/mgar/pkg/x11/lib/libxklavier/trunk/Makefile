NAME = libxklavier
VERSION = 4.0
CATEGORIES = x11

DESCRIPTION = X11 high-level API for X Keyboard Extension
define BLURB
  libxklavier is a library providing high-level API for X Keyboard 
  Extension known as XKB. This library is indended to support XFree86 
  and other commercial X servers. It is useful for creating XKB-related 
  software (layout indicators etc).
endef

MASTER_SITES = http://downloads.sourceforge.net/project/gswitchit/libxklavier/$(VERSION)/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

PACKAGES = CSWlibxklavier CSWlibxklavierdevel

CATALOGNAME_CSWlibxklavier = libxklavier
CATALOGNAME_CSWlibxklavierdevel = libxklavier_devel

SPKG_DESC_CSWlibxklavier = $(DESCRIPTION)
SPKG_DESC_CSWlibxklavierdevel = $(DESCRIPTION) development files

BUILD_DEP_PKGS = CSWiso-codes CSWlibxkbfiledevel CSWlibxml2devel CSWgtk-doc
RUNTIME_DEP_PKGS_CSWlibxklavier += CSWggettextrt CSWglib2 CSWlibx11 CSWlibxml2 
RUNTIME_DEP_PKGS_CSWlibxklavier += CSWlibxkbfile
RUNTIME_DEP_PKGS_CSWlibxklavierdevel += $(RUNTIME_DEP_PKGS_CSWlibxklavier)
RUNTIME_DEP_PKGS_CSWlibxklavierdevel += CSWlibxklavier

PKGFILES_CSWlibxklavierdevel  = $(PKGFILES_DEVEL)

BUILD64 = 1
NOISALIST = 1
STRIP_LIBTOOL = 1

LICENSE = COPYING.LIB

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --x-includes=$(includedir)
CONFIGURE_ARGS += --x-libraries=$(libdir)

include gar/category.mk
pre-configure-modulated:
	# remove GCCish
	gsed -i 's/-Wall//' $(WORKSRC)/libxklavier/Makefile.in
	gsed -i 's/-Wall//' $(WORKSRC)/tests/Makefile.in
	gsed -i 's/-Werror//' $(WORKSRC)/tests/Makefile.in
	gsed -i 's,<getopt.h>,<unistd.h>,' $(WORKSRC)/tests/test_config.c
	gsed -i 's,<getopt.h>,<unistd.h>,' $(WORKSRC)/tests/test_monitor.c
	@$(MAKECOOKIE)
