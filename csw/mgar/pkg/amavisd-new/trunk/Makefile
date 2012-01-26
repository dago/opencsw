NAME = amavisd-new
VERSION = 2.6.4
CATEGORIES = server
GARTYPE = v2

DESCRIPTION = Interface between MTA and content checkers
define BLURB
	amavisd-new is a performance-enhanced daemonized version of amavis-perl
endef

PACKAGES = CSWamavisdnew
CATALOGNAME = amavisd_new
ARCHALL = 1
LICENSE = LICENSE

MASTER_SITES = http://www.ijs.si/software/amavisd/#download
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += CSWamavisdnew.cswusergroup
DISTFILES += CSWamavisdnew.postinstall
DISTFILES += CSWamavisdnew.preinstall

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS += CSWbdb47
RUNTIME_DEP_PKGS += CSWperl
RUNTIME_DEP_PKGS += CSWpmiostringy
RUNTIME_DEP_PKGS += CSWpmnetserver
RUNTIME_DEP_PKGS += CSWpmmailtools
RUNTIME_DEP_PKGS += CSWpmmimetools
RUNTIME_DEP_PKGS += CSWpmiocompress
RUNTIME_DEP_PKGS += CSWpmarchivezip
RUNTIME_DEP_PKGS += CSWspamassassin
RUNTIME_DEP_PKGS += CSWpmberkeleydb
RUNTIME_DEP_PKGS += CSWpmconverttnef
RUNTIME_DEP_PKGS += CSWpmconvertuulib
RUNTIME_DEP_PKGS += CSWpmmaildkim
RUNTIME_DEP_PKGS += CSWpmunixsyslog

CHECKPKG_OVERRIDES_CSWamavisdnew += surplus-dependency|CSWpmmaildkim
CHECKPKG_OVERRIDES_CSWamavisdnew += surplus-dependency|CSWpmnetserver
CHECKPKG_OVERRIDES_CSWamavisdnew += surplus-dependency|CSWbdb47
CHECKPKG_OVERRIDES_CSWamavisdnew += surplus-dependency|CSWpmiostringy
CHECKPKG_OVERRIDES_CSWamavisdnew += surplus-dependency|CSWpmconverttnef
CHECKPKG_OVERRIDES_CSWamavisdnew += surplus-dependency|CSWpmberkeleydb
CHECKPKG_OVERRIDES_CSWamavisdnew += surplus-dependency|CSWpmiocompress
CHECKPKG_OVERRIDES_CSWamavisdnew += surplus-dependency|CSWpmarchivezip
CHECKPKG_OVERRIDES_CSWamavisdnew += surplus-dependency|CSWpmconvertuulib
CHECKPKG_OVERRIDES_CSWamavisdnew += surplus-dependency|CSWpmmailtools
CHECKPKG_OVERRIDES_CSWamavisdnew += surplus-dependency|CSWspamassassin
CHECKPKG_OVERRIDES_CSWamavisdnew += surplus-dependency|CSWpmmimetools
CHECKPKG_OVERRIDES_CSWamavisdnew += surplus-dependency|CSWpmunixsyslog

PATCHFILES += amavisd-agent.diff
PATCHFILES += amavisd-nanny.diff
PATCHFILES += amavisd-release.diff
PATCHFILES += amavisd.conf.diff
PATCHFILES += amavisd.diff
PATCHFILES += p0f-analyzer.pl.diff

SPKG_CLASSES = none cswinitsmf
PROTOTYPE_FILTER  = awk ' \
    $$$$3 ~ /\/init.d\/cswamavisdnew$$$$/ { $$$$2 = "cswinitsmf" } \
    $$$$3 ~ /\/csw\/amavisd-new.conf$$$$/ { $$$$2 = "cswcpsampleconf" } \
    { print }'

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

PCONFDIR = $(DESTDIR)/etc/opt/csw
PVARDIR = $(DESTDIR)/var/opt/csw/$(NAME)

AMAVISBIN = amavisd-agent amavisd-nanny amavisd-release p0f-analyzer.pl
AMAVISBIN += amavisd-nanny
AMAVISBIN += amavisd-release
AMAVISBIN += p0f-analyzer.pl

AMAVISSBIN = amavisd-new

AMAVISDOC = LDAP.schema
AMAVISDOC += README_FILES
AMAVISDOC += RELEASE_NOTES
AMAVISDOC += AAAREADME.first
AMAVISDOC += amavisd.conf-default
AMAVISDOC += amavisd.conf-sample

install-custom:
	echo " ==> Installing $(NAME)"
	ginstall -d $(DESTDIR)$(prefix)/etc
	ginstall -d $(DESTDIR)$(prefix)/bin
	ginstall -d $(DESTDIR)$(prefix)/sbin
	ginstall -d $(DESTDIR)$(prefix)/share/doc/amavisd-new
	cd $(WORKSRC); \
	mv amavisd amavisd-new; \
	mv amavisd.conf amavisd-new.conf.CSW; \
	cp amavisd-new.conf.CSW $(DESTDIR)$(prefix)/etc; \
	cp $(AMAVISBIN) $(DESTDIR)$(prefix)/bin; \
	cp $(AMAVISSBIN) $(DESTDIR)$(prefix)/sbin; \
	cp -r $(AMAVISDOC) $(DESTDIR)$(prefix)/share/doc/amavisd-new
	ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	ginstall -m 755 files/cswamavisdnew $(DESTDIR)/etc/opt/csw/init.d/cswamavisdnew
	ginstall -d $(DESTDIR)/etc/opt/csw/pkg/CSWamavisdnew
	ginstall -m 644 files/CSWamavisdnew.cswusergroup $(DESTDIR)/etc/opt/csw/pkg/CSWamavisdnew/cswusergroup
	$(MAKECOOKIE)

include gar/category.mk
