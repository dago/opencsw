NAME = colormake
VERSION = 0.2
GARTYPE = v2

DESCRIPTION = A colorizer for make
define BLURB
This is a simple wrapper around "make" to make its output more readable.
endef

MASTER_SITES = http://bre.klaki.net/programs/$(NAME)/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
PATCHFILES = 0001-Update-Paths-and-Binary-Tool-Names-for-CSW.patch

DISTNAME = $(NAME)

ARCHALL = 1

RUNTIME_DEP_PKGS = CSWgmake CSWcoreutils CSWperl CSWless

CHECKPKG_OVERRIDES_CSWcolormake += unidentified-dependency|CSWcoreutils
CHECKPKG_OVERRIDES_CSWcolormake += surplus-dependency|CSWgmake
CHECKPKG_OVERRIDES_CSWcolormake += surplus-dependency|CSWcoreutils
CHECKPKG_OVERRIDES_CSWcolormake += surplus-dependency|CSWless

# We define upstream file regex so we can be notifed of new upstream
# software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of
# MASTER_SITES, then uncomment the next line. Otherwise it is set by
# default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom: CMDD=$(docdir)/$(NAME)
install-custom:
	@(cd $(WORKSRC); \
		ginstall -d -m 0755 $(DESTDIR)$(bindir) $(DESTDIR)$(CMDD); \
		ginstall -m 0755 colormake.pl clmake $(DESTDIR)$(bindir); \
		ginstall -m 0755 cmake $(DESTDIR)$(bindir)/colormake; \
		ginstall -m 0644 AUTHORS README $(DESTDIR)$(CMDD) )
	@$(MAKECOOKIE)
