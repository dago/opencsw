GARNAME = wgetpaste
GARVERSION = 2.13
CATEGORIES = utils

DESCRIPTION = A command-line utility for text pasting websites.
define BLURB
  Pipe text into it and it'll send it to dpaste.com,
  giving you a link back to your paste.
endef

MASTER_SITES = http://wgetpaste.zlin.dk/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

REQUIRED_PKGS = CSWshutils

PATCHFILES = wgetpaste-$(GARVERSION).patch

ARCHALL = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = wgetpaste
TEST_SCRIPTS =

install-wgetpaste:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -m 755 $(WORKSRC)/wgetpaste $(DESTDIR)$(bindir)
	@$(MAKECOOKIE)

include gar/category.mk
