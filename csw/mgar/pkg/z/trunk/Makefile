NAME = z
VERSION = 2.6.1
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = A simple, safe and convenient front-end for various compression programs
define BLURB
  Z is a simple, safe and convenient front-end for the compress(1), uncompress(1),
  gzip(1), bzip2(1), lzip(1), tar(1), zip(1) and unzip(1) utilities for compressing
  and uncompressing files and directories. See the included man page for full details.
endef

MASTER_SITES = http://www.cs.indiana.edu/~kinzler/z/
DISTFILES  = $(NAME)-$(VERSION).tgz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tgz

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =

INSTALL_OVERRIDE_DIRS = BINDIR MANDIR
BINDIR = $(bindir)
MANDIR = $(mandir)
INSTALL_ARGS = install install.man

ARCHALL = 1

include gar/category.mk

pre-install-modulated:
	mkdir -p $(DESTDIR)$(bindir)
	mkdir -p $(DESTDIR)$(mandir)/man1
	@$(MAKECOOKIE)
