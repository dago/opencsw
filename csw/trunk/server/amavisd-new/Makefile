GARNAME = amavisd-new
GARVERSION = 2.6.0
CATEGORIES = server

DESCRIPTION = Interface between MTA and content checkers
define BLURB
	amavisd-new is a performance-enhanced daemonized version of amavis-perl
endef

MASTER_SITES = http://www.ijs.si/software/amavisd/#download
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWpackage,)

PATCHFILES += amavisd-agent.diff
PATCHFILES += amavisd-nanny.diff
PATCHFILES += amavisd-release.diff
PATCHFILES += amavisd.conf.diff
PATCHFILES += amavisd.diff
PATCHFILES += p0f-analyzer.pl.diff

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

AMAVIS_BINS=amavisd amavisd-agent amavisd-nanny amavisd-release p0f-analyzer.pl

install-custom:
	@echo " ==> Installing $(GARNAME)"
	@ginstall -d $(DESTDIR)$(prefix)/bin
	cp -r $(WORKSRC)/$(AMAVIS_BINS $(DESTDIR)
	@$(MAKECOOKIE)

include ../category.mk
