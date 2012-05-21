NAME = nrpe
VERSION = 2.13
CATEGORIES = apps
GARTYPE = v2

SPKG_DESC_CSWnrpe 	= Nagios remote plugin executor
SPKG_DESC_CSWnrpeplugin =  Nagios plugin that connects to nrpe demon

define BLURB
  NRPE allows you to remotely execute Nagios plugins on other Linux/Unix machines. This allows you to monitor remote machine metrics (disk usage, CPU load, etc.). NRPE can also communicate with some of the Windows agent addons, so you can execute scripts and check metrics on remote Windows machines as well.
endef

SF_PROJ = nagios
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

#
# modulations
#

EXTRA_MODULATORS = SIZE
MODULATIONS_SIZE = 1k 8k

# Distfiles for CSWnrpe

DISTFILES += CSWnrpe.preinstall 
#DISTFILES += CSWnrpe.prototype 
DISTFILES += cswnrpe cswusergroup
DISTFILES += README_8k

# Distfiles for nrpe_plugin

#DISTFILES += CSWnrpeplugin.prototype

#PATCHFILES 	 = patch.diff 

PATCHFILES_isa-sparcv8-size-8k 	= 0002-changing-packetbuffer-length-to-8k.patch
PATCHFILES_isa-i386-size-8k 	= 0002-changing-packetbuffer-length-to-8k.patch

PACKAGING_PLATFORMS	= solaris10-sparc solaris10-i386

PACKAGES			= CSWnrpe CSWnrpeplugin
CATALOGNAME_CSWnrpe		= nrpe
CATALOGNAME_CSWnrpeplugin	= nrpe_plugin

PKGFILES_CSWnrpe 	 = /opt/csw/bin/nrpe_1k
PKGFILES_CSWnrpe	+= /opt/csw/bin/nrpe_8k
PKGFILES_CSWnrpe	+= /etc/opt/csw/nrpe.cfg.CSW
PKGFILES_CSWnrpe	+= /opt/csw/share/doc/nrpe
PKGFILES_CSWnrpe	+= /opt/csw/share/doc/nrpe/NRPE.pdf
PKGFILES_CSWnrpe	+= /opt/csw/share/doc/nrpe/LEGAL
PKGFILES_CSWnrpe	+= /opt/csw/share/doc/nrpe/license
PKGFILES_CSWnrpe	+= /opt/csw/share/doc/nrpe/README
PKGFILES_CSWnrpe	+= /opt/csw/share/doc/nrpe/README_8k
PKGFILES_CSWnrpe	+= /opt/csw/share/doc/nrpe/README.SSL
PKGFILES_CSWnrpe	+= /opt/csw/share/doc/nrpe/SECURITY
PKGFILES_CSWnrpe	+= /opt/csw/nagios
PKGFILES_CSWnrpe	+= /etc/opt/csw/init.d/cswnrpe
PKGFILES_CSWnrpe	+= /opt/csw/etc/templates/CSWnrpe$(CFGDIR)
PKGFILES_CSWnrpe	+= /opt/csw/etc/templates/CSWnrpe$(CFGDIR)/nrpe.cfg

PKGFILES_CSWnrpeplugin	  = /opt/csw/libexec/nagios-plugins
PKGFILES_CSWnrpeplugin	 += /opt/csw/libexec/nagios-plugins/check_nrpe
PKGFILES_CSWnrpeplugin	 += /opt/csw/libexec/nagios-plugins/check_nrpe_8k
PKGFILES_CSWnrpeplugin	 += /opt/csw/share/doc/nrpe
PKGFILES_CSWnrpeplugin	 += /opt/csw/share/doc/nrpe/README_8k
PKGFILES_CSWnrpeplugin	 += /opt/csw/share/doc/nrpe_plugin
PKGFILES_CSWnrpeplugin	 += /opt/csw/share/doc/nrpe_plugin/license


RUNTIME_DEP_PKGS_CSWnrpe       	= CSWosslrt CSWtcpwrap 
RUNTIME_DEP_PKGS_CSWnrpeplugin	= CSWosslrt 

#SPKG_CLASSES_CSWnrpe = none cswusergroup cswpreserveconf cswinitsmf

LICENSE = LEGAL

NOISALIST = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-ssl-lib=/opt/csw/lib
CONFIGURE_ARGS += --with-ssl-inc=/opt/csw/include
CONFIGURE_ARGS += --with-ssl-dir=/opt/csw/bin
CONFIGURE_ARGS += --with-kerberos-inc=/opt/csw/include
CONFIGURE_ARGS += --enable-command-args
CONFIGURE_ARGS += --prefix=/opt/csw
CONFIGURE_ARGS += --exec-prefix=/opt/csw

CFLAGS	+= "-I/opt/csw/include"

sysconfdir = /etc${prefix}
bindir = $(prefix)/bin
libexecdir = $(prefix)/libexec/nagios-plugins
datadir = $(prefix)/share

TEST_TARGET = all
INSTALL_SCRIPTS = custom

MERGE_SCRIPTS_isa-sparcv8-size-1k = copy-all
MERGE_SCRIPTS_isa-sparcv8-size-8k = copy-nrpe-only

MERGE_SCRIPTS_isa-i386-size-1k = copy-all
MERGE_SCRIPTS_isa-i386-size-8k = copy-nrpe-only

#
#
#

INITSMF          = /etc/opt/csw/init.d/cswnrpe
USERGROUP        = /etc/opt/csw/pkg/CSWnrpe/cswusergroup
#POSTMSG          = /opt/csw/share/doc/nrpe/README.CSW

include gar/category.mk

DOCDIR=$(datadir)/doc/nrpe
CFGDIR=$(sysconfdir)
LIBEXECDIR=$(libexecdir)
BINDIR=$(bindir)
CSWnrpe_TEMPLATEDIR     = /opt/csw/etc/templates/CSWnrpe$(CFGDIR)

install-custom:
	@ginstall -m 775 -d $(DESTDIR)$(DOCDIR)
	@ginstall -m 755 -d $(DESTDIR)$(LIBEXECDIR)
	@ginstall -m 755 -d $(DESTDIR)$(BINDIR)
	@ginstall -m 755 -d $(DESTDIR)/nagios
	@ginstall -m 755 $(WORKSRC)/src/check_nrpe $(DESTDIR)$(LIBEXECDIR)
	@ginstall -m 755 $(WORKSRC)/src/nrpe $(DESTDIR)$(BINDIR)/nrpe_1k
	@ginstall -m 644 $(WORKSRC)/docs/NRPE.pdf $(DESTDIR)$(DOCDIR)
	@ginstall -m 644 $(FILEDIR)/README_8k $(DESTDIR)$(DOCDIR)
	@ginstall -m 644 $(WORKSRC)/LEGAL $(DESTDIR)$(DOCDIR)
	@ginstall -m 644 $(WORKSRC)/README $(DESTDIR)$(DOCDIR)
	@ginstall -m 644 $(WORKSRC)/README.SSL $(DESTDIR)$(DOCDIR)
	@ginstall -m 644 $(WORKSRC)/SECURITY $(DESTDIR)$(DOCDIR)
	@#
	@# configuration file for CSWnrpe -> cswcptemplates
	@#
	@ginstall -m 775 -d $(DESTDIR)$(CSWnrpe_TEMPLATEDIR)
	@ginstall -m 644 $(WORKSRC)/sample-config/nrpe.cfg $(DESTDIR)$(CSWnrpe_TEMPLATEDIR)/nrpe.cfg
	@#
	@# create user and group -> cswusergroup
	@#
	@ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/pkg/CSWnrpe
	@ginstall -m 644 $(FILEDIR)/cswusergroup $(DESTDIR)/etc/opt/csw/pkg/CSWnrpe/cswusergroup
	@#
	@# Start / Stop script
	@#
	@ginstall -d $(DESTDIR)/etc/$(BUILD_PREFIX)/init.d
	@ginstall -m 755 $(FILEDIR)/cswnrpe $(DESTDIR)/etc/$(BUILD_PREFIX)/init.d/cswnrpe
	@$(MAKECOOKIE)

merge-copy-nrpe-only:
	cp $(INSTALLISADIR)$(bindir)/nrpe_1k $(PKGROOT)$(bindir)/nrpe_8k
	cp $(INSTALLISADIR)$(LIBEXECDIR)/check_nrpe $(PKGROOT)$(LIBEXECDIR)/check_nrpe_8k
	@$(MAKECOOKIE)

