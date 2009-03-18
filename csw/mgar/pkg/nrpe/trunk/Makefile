GARNAME = nrpe
GARVERSION = 2.12
CATEGORIES = apps

SPKG_DESC_CSWnrpe = nagios remote plugin executor (server files, client package is nrpeplugin)
SPKG_DESC_CSWnrpeplugin = nagios remote plugin executor (client files, server package is nrpe)

define BLURB
  NRPE allows you to remotely execute Nagios plugins on other Linux/Unix machines. This allows you to monitor remote machine metrics (disk usage, CPU load, etc.). NRPE can also communicate with some of the Windows agent addons, so you can execute scripts and check metrics on remote Windows machines as well.
endef

SF_PROJ = nagios
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWnrpe, prototype checkinstall preinstall preremove )
DISTFILES += cswnrpe
DISTFILES += $(call admfiles,CSWnrpeplugin, prototype )

REQUIRED_PKGS_CSWnrpe       = CSWosslrt CSWtcpwrap CSWcswclassutils
REQUIRED_PKGS_CSWnrpeplugin = CSWosslrt 

SPKG_CLASSES_CSWnrpe = none cswinitsmf

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-ssl-lib=/opt/csw/lib
CONFIGURE_ARGS += --with-ssl-inc=/opt/csw/include
CONFIGURE_ARGS += --with-ssl-dir=/opt/csw/bin
CONFIGURE_ARGS += --with-kerberos-inc=/opt/csw/include
CONFIGURE_ARGS += --prefix=/opt/csw
CONFIGURE_ARGS += --exec-prefix=/opt/csw

PATCHFILES = patch.diff	# Removal of LOG_AUTHPRIV and LOG_FTP
			# Solaris doesn't have these log facilities
PATCHFILES += configure.diff 

sysconfdir = $(prefix)/etc
bindir = $(prefix)/bin
libexecdir = $(prefix)/libexec/nagios-plugins
datadir = $(prefix)/share

TEST_TARGET = all
INSTALL_SCRIPTS = custom

include gar/category.mk

DOCDIR=$(datadir)/doc/nrpe
CFGDIR=$(sysconfdir)
LIBEXECDIR=$(libexecdir)
BINDIR=$(bindir)

install-custom:
	ginstall -m 775 -d $(DESTDIR)$(DOCDIR)
	ginstall -m 755 -d $(DESTDIR)$(LIBEXECDIR)
	ginstall -m 755 -d $(DESTDIR)$(BINDIR)
	ginstall -m 755 $(WORKSRC)/src/check_nrpe $(DESTDIR)$(LIBEXECDIR)
	ginstall -m 755 $(WORKSRC)/src/nrpe $(DESTDIR)$(BINDIR)
	ginstall -m 644 $(WORKSRC)/docs/NRPE.pdf $(DESTDIR)$(DOCDIR)
	ginstall -m 644 $(WORKSRC)/LEGAL $(DESTDIR)$(DOCDIR)
	ginstall -m 644 $(WORKSRC)/README $(DESTDIR)$(DOCDIR)
	ginstall -m 644 $(WORKSRC)/README.SSL $(DESTDIR)$(DOCDIR)
	ginstall -m 644 $(WORKSRC)/SECURITY $(DESTDIR)$(DOCDIR)
	ginstall -m 775 -d $(DESTDIR)$(CFGDIR)
	ginstall -m 644 $(WORKSRC)/sample-config/nrpe.cfg $(DESTDIR)$(CFGDIR)/nrpe.cfg-sample
	ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	ginstall -m 755 $(FILEDIR)/cswnrpe $(DESTDIR)/etc/opt/csw/init.d/cswnrpe
	@$(MAKECOOKIE)
