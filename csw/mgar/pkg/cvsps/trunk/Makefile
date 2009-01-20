GARNAME = cvsps
GARVERSION = 2.1
CATEGORIES = apps

DESCRIPTION = Brief description
define BLURB
  Long description
endef

MASTER_SITES = http://www.cobite.com/cvsps/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWcvsps,)

PATCHFILES = patch-extralibs.diff

REQUIRED_PKGS = CSWzlib

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# We don't have configure
CONFIGURE_SCRIPTS =

BUILD_ARGS = CC="$(CC)" CFLAGS="-I. -DVERSION=\"$(GARVERSION)\" $(CFLAGS)" prefix="$(prefix)"
BUILD_ARGS += _EXTRA_LIBS="-lnsl -lsocket"

TEST_SCRIPTS =

INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)$(mandir)/man1
	ginstall -m 755 $(WORKSRC)/cvsps $(DESTDIR)$(bindir)/
	ginstall -m 644 $(WORKSRC)/cvsps.1 $(DESTDIR)$(mandir)/man1/
