NAME = xtitle
VERSION = 1.0.2
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Set the window's title and/or icon name to the script's arguments
define BLURB
  Xtitle is a relatively simple shell script program that, when run in an xterm or
  xterm-like window, will set the window's title and/or icon name to the script's
  arguments.
endef

MASTER_SITES = http://www.cs.indiana.edu/~kinzler/xtitle/
DISTFILES  = $(NAME)-$(VERSION).tgz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tgz

VENDOR_URL = http://www.cs.indiana.edu/~kinzler/xtitle/

CONFIGURE_SCRIPTS = $(WORKSRC)/Imakefile

TEST_SCRIPTS =

INSTALL_OVERRIDE_VARS = BINDIR MANDIR
INSTALL_OVERRIDE_VAR_BINDIR = $(bindir)
INSTALL_OVERRIDE_VAR_MANDIR = $(mandir)
INSTALL_ARGS = install install.man

ARCHALL = 1

include gar/category.mk
