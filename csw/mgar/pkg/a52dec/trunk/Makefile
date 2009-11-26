GARNAME = a52dec
GARVERSION = 0.7.4
CATEGORIES = lib

DESCRIPTION = A free ATSC A/52 stream decoder
define BLURB
  liba52 is a free library for decoding ATSC A/52 streams. It is released under the terms
  of the GPL license. The A/52 standard is used in a variety of applications, including
  digital television and DVD. It is also known as AC-3.
endef

MASTER_SITES = http://liba52.sourceforge.net/files/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += liba52.pc-32 liba52.pc-64

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = http://liba52.sourceforge.net/
UFILES_REGEX = (\d+(?:\.\d+)*)

PACKAGES = CSWliba52
CATALOGNAME = a52dec

REQUIRED_PKGS = CSWsunmath
EXTRA_LINKER_FLAGS = -lsunmath

BUILD64 = 1
NO_ISAEXEC = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared --disable-static

# This stupid configure script adds '-fast' overwriting -xarch and
# especially activating 64 bit.
BUILD_ARGS = CFLAGS="$(CFLAGS)"

MERGE_DIRS_isa-extra = $(libdir)

include gar/category.mk

post-install-modulated:
	ginstall -d $(DESTDIR)$(libdir)/pkgconfig
	ginstall $(WORKDIR)/liba52.pc-$(MEMORYMODEL) $(DESTDIR)$(libdir)/pkgconfig/liba52.pc
	@$(MAKECOOKIE)
