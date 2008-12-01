GARNAME = amavisd-new
GARVERSION = 2.6.1
CATEGORIES = server

DESCRIPTION = Interface between MTA and content checkers
define BLURB
	amavisd-new is a performance-enhanced daemonized version of amavis-perl
endef

MASTER_SITES = http://www.ijs.si/software/amavisd/#download
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWamavisdnew, depend postinstall preinstall prototype)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PATCHFILES += amavisd-agent.diff
PATCHFILES += amavisd-nanny.diff
PATCHFILES += amavisd-release.diff
PATCHFILES += amavisd.conf.diff
PATCHFILES += amavisd.diff
PATCHFILES += p0f-analyzer.pl.diff

SPKG_CLASSES = none cswinitsmf

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

AMAVISBIN=amavisd-agent amavisd-nanny amavisd-release p0f-analyzer.pl
AMAVISSBIN=amavisd-new
AMAVISDOC=LDAP.schema README_FILES RELEASE_NOTES AAAREADME.first \
          amavisd.conf-default amavisd.conf-sample

install-custom:
	echo " ==> Installing $(GARNAME)"
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
	$(MAKECOOKIE)

include gar/category.mk
