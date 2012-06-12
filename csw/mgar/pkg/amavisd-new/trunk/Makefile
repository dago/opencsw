NAME = amavisd-new
VERSION = 2.7.1
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
RUNTIME_DEP_PKGS += CSWpmnetsnmp
RUNTIME_DEP_PKGS += CSWunrar
RUNTIME_DEP_PKGS += CSWtnef
RUNTIME_DEP_PKGS += CSWcabex
RUNTIME_DEP_PKGS += CSWunarj
RUNTIME_DEP_PKGS += CSWp7zip
RUNTIME_DEP_PKGS += CSWzip
RUNTIME_DEP_PKGS += CSWlzop
RUNTIME_DEP_PKGS += CSWxz
RUNTIME_DEP_PKGS += CSWgzip
RUNTIME_DEP_PKGS += CSWbzip2

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
CHECKPKG_OVERRIDES_CSWamavisdnew += surplus-dependency|CSWp7zip
CHECKPKG_OVERRIDES_CSWamavisdnew += surplus-dependency|CSWunarj
CHECKPKG_OVERRIDES_CSWamavisdnew += surplus-dependency|CSWgzip
CHECKPKG_OVERRIDES_CSWamavisdnew += surplus-dependency|CSWxz
CHECKPKG_OVERRIDES_CSWamavisdnew += surplus-dependency|CSWcabex
CHECKPKG_OVERRIDES_CSWamavisdnew += surplus-dependency|CSWlzop
CHECKPKG_OVERRIDES_CSWamavisdnew += surplus-dependency|CSWtnef
CHECKPKG_OVERRIDES_CSWamavisdnew += surplus-dependency|CSWbzip2
CHECKPKG_OVERRIDES_CSWamavisdnew += surplus-dependency|CSWzip
CHECKPKG_OVERRIDES_CSWamavisdnew += surplus-dependency|CSWunrar
CHECKPKG_OVERRIDES_CSWamavisdnew += surplus-dependency|CSWpmnetsnmp

PATCHFILES += 0001-amavisd-agent.patch
PATCHFILES += 0001-amavisd-nanny.patch
PATCHFILES += 0001-amavisd-release.patch
PATCHFILES += 0001-amavisd.conf.patch
PATCHFILES += 0001-amavisd.patch
PATCHFILES += p0f-analyzer.pl.diff
PATCHFILES += 0001-amavisd-signer.patch
PATCHFILES += 0001-amavisd-snmp-subagent.patch
PATCHFILES += 0001-amavisd-submit.patch

CHECKPKG_OVERRIDES_CSWamavisdnew += file-with-bad-content|/usr/local|root/opt/csw/sbin/amavisd-new
CHECKPKG_OVERRIDES_CSWamavisdnew += file-with-bad-content|/usr/local|root/opt/csw/share/doc/amavisd-new/RELEASE_NOTES
CHECKPKG_OVERRIDES_CSWamavisdnew += file-with-bad-content|/usr/local|root/opt/csw/share/doc/amavisd-new/README_FILES/README.milter
CHECKPKG_OVERRIDES_CSWamavisdnew += file-with-bad-content|/usr/local|root/opt/csw/share/doc/amavisd-new/README_FILES/README.sendmail
CHECKPKG_OVERRIDES_CSWamavisdnew += file-with-bad-content|/usr/local|root/opt/csw/share/doc/amavisd-new/README_FILES/README.old.scanners
CHECKPKG_OVERRIDES_CSWamavisdnew += file-with-bad-content|/usr/local|root/opt/csw/share/doc/amavisd-new/README_FILES/README.chroot
CHECKPKG_OVERRIDES_CSWamavisdnew += file-with-bad-content|/usr/share|root/opt/csw/share/doc/amavisd-new/README_FILES/README.sendmail-dual
CHECKPKG_OVERRIDES_CSWamavisdnew += file-with-bad-content|/usr/share|root/opt/csw/share/doc/amavisd-new/README_FILES/README.sendmail
CHECKPKG_OVERRIDES_CSWamavisdnew += file-with-bad-content|/usr/share|root/opt/csw/share/doc/amavisd-new/README_FILES/README.chroot
CHECKPKG_OVERRIDES_CSWamavisdnew += file-with-bad-content|/usr/share|root/opt/csw/share/doc/amavisd-new/README_FILES/README.sendmail-dual.old
CHECKPKG_OVERRIDES_CSWamavisdnew += file-with-bad-content|/usr/local|root/opt/csw/bin/amavisd-snmp-subagent

CHECKPKG_OVERRIDES_CSWamavisdnew += catalogname-does-not-match-pkgname|pkgname=CSWamavisdnew|catalogname=amavisd_new|expected-catalogname=amavisdnew

INITSMF    = /etc/opt/csw/init.d/cswamavisdnew
USERGROUP  = /etc/opt/csw/pkg/CSWamavisdnew/cswusergroup
SAMPLECONF = /etc/opt/csw/amavisn/amavisd-new.conf

PROTOTYPE_MODIFIERS              = amavis_ugfiles
AMAVIS_UGFILES                    = /var/opt/csw/amavisn /var/opt/csw/amavisn/tmp /var/opt/csw/amavisn/var /var/opt/csw/amavisn/db /var/var/opt/csw/amavisn/virusmails
PROTOTYPE_FILES_amavis_ugfiles   = $(AMAVIS_UGFILES)
PROTOTYPE_USER_amavis_ugfiles    = amavisn
PROTOTYPE_GROUP_amavis_ugfiles   = amavisn
PROTOTYPE_CLASS_amavis_ugfiles   = ugfiles

PROTOTYPE_MODIFIERS   += amavis_chmod
PROTOTYPE_FILES_chmod  = $(AMAVIS_UGFILES)
PROTOTYPE_PERMS_chmod  = 0750

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

PCONFDIR = $(DESTDIR)/etc/opt/csw
PVARDIR = $(DESTDIR)/var/opt/csw/$(NAME)

AMAVISBIN = amavisd-agent amavisd-nanny amavisd-release p0f-analyzer.pl
AMAVISBIN += amavisd-nanny amavisd-signer amavisd-snmp-subagent
AMAVISBIN += amavisd-release amavisd-submit
AMAVISBIN += p0f-analyzer.pl

AMAVISSBIN = amavisd-new

AMAVISDOC = LDAP.schema
AMAVISDOC += README_FILES
AMAVISDOC += RELEASE_NOTES
AMAVISDOC += AAAREADME.first
AMAVISDOC += amavisd.conf-default
AMAVISDOC += test-messages

install-custom:
	echo " ==> Installing $(NAME)"
	ginstall -d $(DESTDIR)/etc/opt/csw/amavisn
	ginstall -d $(DESTDIR)$(prefix)/bin
	ginstall -d $(DESTDIR)$(prefix)/sbin
	ginstall -d $(DESTDIR)$(prefix)/share/doc/amavisd-new
	cd $(WORKSRC); \
	mv amavisd amavisd-new; \
	cp amavisd-new.conf $(DESTDIR)/etc/opt/csw/amavisn; \
	cp $(AMAVISBIN) $(DESTDIR)$(prefix)/bin; \
	cp $(AMAVISSBIN) $(DESTDIR)$(prefix)/sbin; \
	cp -r $(AMAVISDOC) $(DESTDIR)$(prefix)/share/doc/amavisd-new
	ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	ginstall -m 755 files/cswamavisdnew $(DESTDIR)/etc/opt/csw/init.d/cswamavisdnew
	ginstall -d $(DESTDIR)/etc/opt/csw/pkg/CSWamavisdnew
	ginstall -m 644 files/CSWamavisdnew.cswusergroup $(DESTDIR)/etc/opt/csw/pkg/CSWamavisdnew/cswusergroup
	$(MAKECOOKIE)

include gar/category.mk
