NAME = DBD-SQLite
VERSION = 1.31
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = ADAMK

DESCRIPTION = Self contained RDBMS in a DBI driver
define BLURB
    DBD::SQLite is a Perl DBI driver for SQLite, that includes the entire
    thing in the distribution. So in order to get a fast transaction capable
    RDBMS working for your perl project you simply have to install this
    module, and nothing else.
endef

PACKAGES = CSWpm-dbd-sqlite
CATALOGNAME = pm_dbd_sqlite
SPKG_DESC_CSWpm-dbd-sqlite = $(DESCRIPTION)
OBSOLETED_BY_CSWpm-dbd-sqlite = CSWpmdbdsqlite
CATALOGNAME_CSWpmdbdsqlite = pm_dbdsqlite

RUNTIME_DEP_PKGS = CSWpmdbi

LICENSE = LICENSE

include gar/category.mk

post-install-modulated:
	@echo "Post-Install (custom)"
	@ginstall -d -m 755 $(DESTDIR)$(docdir)/pm_dbdsqlite
	@ginstall -m 444 $(WORKSRC)/README $(DESTDIR)$(docdir)/pm_dbdsqlite
	@$(MAKECOOKIE)
