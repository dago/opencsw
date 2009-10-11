GARNAME = nrpe
GARVERSION = 2.12
CATEGORIES = apps

SPKG_DESC_CSWnrpe = nagios remote plugin executor
SPKG_DESC_CSWnrpeplugin =  nagios plugin that connects to nrpe demon

define BLURB
  NRPE allows you to remotely execute Nagios plugins on other Linux/Unix machines. This allows you to monitor remote machine metrics (disk usage, CPU load, etc.). NRPE can also communicate with some of the Windows agent addons, so you can execute scripts and check metrics on remote Windows machines as well.
endef

SF_PROJ = nagios
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# Distfiles for CSWnrpe

DISTFILES += CSWnrpe.preinstall CSWnrpe.prototype
DISTFILES += cswnrpe cswusergroup
DISTFILES += README_8k

# Distfiles for check_nrpe

DISTFILES += CSWnrpeplugin.prototype

PATCHFILES = patch.diff configure.diff

PATCHFILES_isa-sparcv8-size-8k = common.h.diff
PATCHFILES_isa-i386-size-8k = common.h.diff

PACKAGES = CSWnrpe CSWnrpeplugin
CATALOGNAME_CSWmuninmaster = nrpe
CATALOGNAME_CSWmuninnode = nrpe_plugin

REQUIRED_PKGS_CSWnrpe       = CSWosslrt CSWtcpwrap CSWcswclassutils
REQUIRED_PKGS_CSWnrpeplugin = CSWosslrt 

SPKG_CLASSES_CSWnrpe = none cswusergroup cswpreserveconf cswinitsmf

EXTRA_MODULATORS = SIZE
MODULATIONS_SIZE = 1k 8k

NOISALIST = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-ssl-lib=/opt/csw/lib
CONFIGURE_ARGS += --with-ssl-inc=/opt/csw/include
CONFIGURE_ARGS += --with-ssl-dir=/opt/csw/bin
CONFIGURE_ARGS += --with-kerberos-inc=/opt/csw/include
CONFIGURE_ARGS += --enable-command-args
CONFIGURE_ARGS += --prefix=/opt/csw
CONFIGURE_ARGS += --exec-prefix=/opt/csw

sysconfdir = /etc/${prefix}
bindir = $(prefix)/bin
libexecdir = $(prefix)/libexec/nagios-plugins
datadir = $(prefix)/share

TEST_TARGET = all
INSTALL_SCRIPTS = custom

MERGE_SCRIPTS_isa-sparcv8-size-1k = copy-all
MERGE_SCRIPTS_isa-sparcv8-size-8k = copy-nrpe-only

MERGE_SCRIPTS_isa-i386-size-1k = copy-all
MERGE_SCRIPTS_isa-i386-size-8k = copy-nrpe-only

include gar/category.mk

DOCDIR=$(datadir)/doc/nrpe
CFGDIR=$(sysconfdir)
LIBEXECDIR=$(libexecdir)
BINDIR=$(bindir)

install-custom:
	ginstall -m 775 -d $(DESTDIR)$(DOCDIR)
	ginstall -m 755 -d $(DESTDIR)$(LIBEXECDIR)
	ginstall -m 755 -d $(DESTDIR)$(BINDIR)
	ginstall -m 755 -d $(DESTDIR)/nagios
	ginstall -m 755 $(WORKSRC)/src/check_nrpe $(DESTDIR)$(LIBEXECDIR)
	ginstall -m 755 $(WORKSRC)/src/nrpe $(DESTDIR)$(BINDIR)/nrpe_1k
	ginstall -m 644 $(WORKSRC)/docs/NRPE.pdf $(DESTDIR)$(DOCDIR)
	ginstall -m 644 $(FILEDIR)/README_8k $(DESTDIR)$(DOCDIR)
	ginstall -m 644 $(WORKSRC)/LEGAL $(DESTDIR)$(DOCDIR)
	ginstall -m 644 $(WORKSRC)/README $(DESTDIR)$(DOCDIR)
	ginstall -m 644 $(WORKSRC)/README.SSL $(DESTDIR)$(DOCDIR)
	ginstall -m 644 $(WORKSRC)/SECURITY $(DESTDIR)$(DOCDIR)
	ginstall -m 775 -d $(DESTDIR)$(CFGDIR)
	ginstall -m 644 $(WORKSRC)/sample-config/nrpe.cfg $(DESTDIR)$(CFGDIR)/nrpe.cfg.CSW
	ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	ginstall -m 755 $(FILEDIR)/cswnrpe $(DESTDIR)/etc/opt/csw/init.d/cswnrpe
	@ginstall -m 755 -d $(DESTDIR)/opt/csw/etc/pkg/CSWnrpe
	@ginstall -m 644 $(FILEDIR)/cswusergroup $(DESTDIR)/opt/csw/etc/pkg/CSWnrpe/cswusergroup
	@$(MAKECOOKIE)

merge-copy-nrpe-only:
	cp $(INSTALLISADIR)$(bindir)/nrpe_1k $(PKGROOT)$(bindir)/nrpe_8k
	cp $(INSTALLISADIR)$(LIBEXECDIR)/check_nrpe $(PKGROOT)$(LIBEXECDIR)/check_nrpe_8k
	@$(MAKECOOKIE)

