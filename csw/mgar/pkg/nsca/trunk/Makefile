GARNAME = nsca
GARVERSION = 2.7.2
CATEGORIES = apps

DESCRIPTION = passive checks for nagios
define BLURB
  NSCA allows you to integrate passive alerts and checks from remote machines and applications with Nagios. Useful for processing security alerts, as well as redundant and distributed Nagios setups.
endef

MASTER_SITES = http://mesh.dl.sourceforge.net/sourceforge/nagios/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWnsca, prototype checkinstall preinstall depend)
DISTFILES += $(call admfiles,CSWsendnsca, preinstall depend)
DISTFILES += nsca nsca.xml svc-nsca

PATCHFILES += submit_check_results.diff
PATCHFILES += makefile.diff

CONFIGURE_ARGS = $(DIRPATHS)
#CONFIGURE_ARGS += --with-nsca-user=nagios
#CONFIGURE_ARGS += --with-nsca-grp=nagios
CONFIGURE_ARGS += --with-nsca-port=5667

BUILD_TARGETS = nsca

SKIPTEST = 1

#INSTALL_ARGS = install-nsca
INSTALL_ARGS += install-sendnsca
INSTALL_ARGS += install-nsca

include gar/category.mk

pre-install-modulated:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)$(prefix)/nagios/bin
	ginstall -d $(DESTDIR)$(prefix)/nagios/etc
	$(MAKECOOKIE)
