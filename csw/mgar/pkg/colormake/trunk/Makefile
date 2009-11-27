GARNAME = colormake
GARVERSION = 0.2
CATEGORIES = utils

DESCRIPTION = A colorizer for make
define BLURB
This is a simple wrapper around "make" to make its output more readable.
endef

MASTER_SITES = http://bre.klaki.net/programs/$(GARNAME)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
PATCHFILES = 0001-Update-Paths-and-Binary-Tool-Names-for-CSW.patch

ARCHALL = 1

REQUIRED_PKGS = CSWgmake CSWshutils

# We define upstream file regex so we can be notifed of new upstream
# software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of
# MASTER_SITES, then uncomment the next line. Otherwise it is set by
# default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

post-extract-modulated:
	@cd $(WORKDIR_FIRSTMOD); mv $(GARNAME) $(GARNAME)-$(GARVERSION);
	@$(MAKECOOKIE)

install-custom: CMDD=$(docdir)/$(GARNAME)
install-custom:
	@(cd $(WORKSRC); \
		ginstall -d -m 0755 $(DESTDIR)$(bindir) $(DESTDIR)$(CMDD); \
		ginstall -m 0755 colormake.pl cmake clmake $(DESTDIR)$(bindir); \
		ginstall -m 0644 AUTHORS README $(DESTDIR)$(CMDD) )
	@$(MAKECOOKIE)
