NAME 		= nsca
VERSION 	= 2.9.1
CATEGORIES 	= apps
GARTYPE 	= v2

#
# package definition
#

PACKAGES 		= CSWnsca CSWsendnsca

SPKG_DESC_CSWnsca 	= Nagios service check acceptor
SPKG_DESC_CSWsendnsca 	= Sends check results to nsca daemon

CATALOGNAME_CSWnsca 	= nsca
CATALOGNAME_CSWsendnsca = sendnsca

#
# Blurb
#

define BLURB
  NSCA allows you to integrate passive alerts and checks from remote machines and applications with Nagios. Useful for processing security alerts, as well as redundant and distributed Nagios setups.
endef

#
# download, distfiles, patchfiles
#

MASTER_SITES	 = http://sourceforge.net/projects/nagios/files/nsca-2.x/$(NAME)-$(VERSION)/

DISTFILES  	 = $(NAME)-$(VERSION).tar.gz
DISTFILES	+= asprintf.c
DISTFILES 	+= CSWsendnsca.cswusergroup
DISTFILES 	+= submit_check_results.sh
DISTFILES	+= cswnsca
DISTFILES	+= CSWnsca.cswusergroup
DISTFILES	+= CSWnsca.preinstall

PATCHFILES	+= 0001-asprintf-for-solaris-10.patch # taken from https://dev.icinga.org/issues/2409
PATCHFILES 	+= 0002-generated-by-autoconf-for-asprintf-patch.patch # configure file for patch above

#
# reinplacements
#

REINPLACE_USRLOCAL	+= README
REINPLACE_USRLOCAL	+= sample-config/nsca.cfg.in

#
#
#

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

RUNTIME_DEP_PKGS_CSWnsca += CSWlibmcrypt4
RUNTIME_DEP_PKGS_CSWnsca += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWnsca += CSWlibwrap1

RUNTIME_DEP_PKGS_CSWsendnsca += CSWlibmcrypt4
RUNTIME_DEP_PKGS_CSWsendnsca += CSWlibltdl7

#
# files for CSWnsca
#

NSCA_SMF           	+= /etc/opt/csw/init.d/cswnsca
NSCA_USERGROUP     	+= /opt/csw/etc/pkg/CSWnsca/cswusergroup
NSCA_PREINSTALL		+= .*CSWnsca.preinstall
NSCA_DOCS		+= $(NSCADOCDIR).*
NSCA_CONF_DIR		+= /etc/opt/csw/nagios/*
NSCA_CONF_FILE		+= /opt/csw/etc/templates/CSWnsca/etc/opt/csw/nagios/nsca.cfg
NSCA_EXEC		+= /opt/csw/nagios/bin/nsca

PKGFILES_CSWnsca	+= $(NSCA_SMF)
PKGFILES_CSWnsca	+= $(NSCA_USERGROUP)
PKGFILES_CSWnsca	+= $(NSCA_PREINSTALL)
PKGFILES_CSWnsca	+= $(NSCA_DOCS)
PKGFILES_CSWnsca	+= $(NSCA_CONF_DIR)
PKGFILES_CSWnsca	+= $(NSCA_CONF_FILE)
PKGFILES_CSWnsca	+= $(NSCA_EXEC)

#
# files for CSWsendnsca
#

SEND_NSCA_USERGROUP	+= CSWsendnsca.cswusergroup
SEND_NSCA_DOCS		+= $(SENDNSCADOCDIR).*
SEND_NSCA_CONF_DIR	+= /etc/opt/csw/nagios/*
SEND_NSCA_CONF_FILE	+= /opt/csw/etc/templates/CSWsendnsca/etc/opt/csw/nagios/send_nsca.cfg
SEND_NSCA_EXEC		+= /opt/csw/nagios/bin/send_nsca

PKGFILES_CSWsendnsca	+= $(SEND_NSCA_USERGROUP)
PKGFILES_CSWsendnsca	+= $(SEND_NSCA_DOCS)
PKGFILES_CSWsendnsca	+= $(SEND_NSCA_CONF_DIR)
PKGFILES_CSWsendnsca	+= $(SEND_NSCA_CONF_FILE)
PKGFILES_CSWsendnsca	+= $(SEND_NSCA_EXEC)

#
# prototypes
#

PROTOTYPE_MODIFIERS	+= ugfiles

PROTOTYPE_FILES_ugfiles	+= $(NSCA_CONF_FILE) $(SEND_NSCA_CONF_FILE)
PROTOTYPE_USER_ugfiles	+= nagios
PROTOTYPE_GROUP_ugfiles	+= nagios
PROTOTYPE_CLASS_ugfiles	+= cswcptemplates
PROTOTYPE_PERMS_ugfiles	+= 0644

PROTOTYPE_MODIFIERS	+= ugdirs

PROTOTYPE_FILES_ugdirs	+= $(NSCA_CONF_DIR) $(SEND_NSCA_CONF_DIR)
PROTOTYPE_USER_ugdirs	+= nagios
PROTOTYPE_GROUP_ugdirs	+= nagios
PROTOTYPE_PERMS_ugdirs	+= 0755

#
#
#

INITSMF		= $(NSCA_SMF)
USERGROUP_CSWnsca	= $(NSCA_USERGROUP)
USERGROUP_CSWsendnsca	= $(SEND_NSCA_USERGROUP)

#
#
#

NOISALIST = 1

#
# configure
#

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-nsca-port=5667
CONFIGURE_ARGS += --localstatedir=/var/opt/csw/nagios

LICENSE = LEGAL

BUILD_TARGETS = nsca

SKIPTEST = 1

include gar/category.mk

BINDIR			= $(prefix)/bin
NAGIOSBINDIR		= $(prefix)/nagios/bin
NAGIOSCFGDIR		= /etc$(prefix)/nagios
NSCADOCDIR		= $(prefix)/share/doc/nsca
SENDNSCADOCDIR		= $(prefix)/share/doc/send_nsca
CSWnsca_TEMPLATEDIR	= /opt/csw/etc/templates/CSWnsca/$(NAGIOSCFGDIR)
CSWsendnsca_TEMPLATEDIR	= /opt/csw/etc/templates/CSWsendnsca/$(NAGIOSCFGDIR)

pre-build-modulated:
	@ginstall -m  644 $(FILEDIR)/asprintf.c $(WORKSRC)/src/asprintf.c

post-install-modulated:
	@ginstall -d $(DESTDIR)$(prefix)/bin
	@ginstall -d $(DESTDIR)$(prefix)/etc
	@ginstall -d $(DESTDIR)$(NAGIOSBINDIR)
	@ginstall -d $(DESTDIR)$(NAGIOSCFGDIR)
	@ginstall -d $(DESTDIR)$(CSWnsca_TEMPLATEDIR)
	@ginstall -d $(DESTDIR)$(CSWsendnsca_TEMPLATEDIR)
	@ginstall -m 755 -d $(DESTDIR)$(NSCADOCDIR)
	@ginstall -m 755 $(WORKSRC)/src/nsca $(DESTDIR)$(NAGIOSBINDIR)
	@ginstall -m 644 $(WORKSRC)/Changelog $(DESTDIR)$(NSCADOCDIR)
	@ginstall -m 644 $(WORKSRC)/LEGAL $(DESTDIR)$(NSCADOCDIR)
	@ginstall -m 644 $(WORKSRC)/README $(DESTDIR)$(NSCADOCDIR)
	@ginstall -m 644 $(WORKSRC)/SECURITY $(DESTDIR)$(NSCADOCDIR)
	@ginstall -m 755 $(WORKSRC)/src/send_nsca $(DESTDIR)$(NAGIOSBINDIR)
	@ginstall -m 755 -d $(DESTDIR)$(SENDNSCADOCDIR)
	@ginstall -m 755 files/submit_check_results.sh $(DESTDIR)$(SENDNSCADOCDIR)
	@ginstall -m 644 $(WORKSRC)/Changelog $(DESTDIR)$(SENDNSCADOCDIR)
	@ginstall -m 644 $(WORKSRC)/LEGAL $(DESTDIR)$(SENDNSCADOCDIR)
	@ginstall -m 644 $(WORKSRC)/README $(DESTDIR)$(SENDNSCADOCDIR)
	@ginstall -m 644 $(WORKSRC)/SECURITY $(DESTDIR)$(SENDNSCADOCDIR)
	@#
	@## configuration file for CSWnsca -> cswcptemplates
	@#
	@ginstall -m 600 $(WORKSRC)/sample-config/nsca.cfg $(DESTDIR)$(CSWnsca_TEMPLATEDIR)/nsca.cfg
	@#
	@## configuration file for CSWsendnsca -> cswcptemplates
	@#
	@ginstall -m 600 $(WORKSRC)/sample-config/send_nsca.cfg $(DESTDIR)$(CSWsendnsca_TEMPLATEDIR)/send_nsca.cfg
	@#
	@## Start / Stop script for CSWnsca
	@#
	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d/
	@ginstall -m 755 $(FILEDIR)/cswnsca $(DESTDIR)/etc/opt/csw/init.d/
	@#
	@## create user and group  for CSWsendnsca -> cswusergroup
	@#
	@ginstall -m 755 -d $(DESTDIR)/opt/csw/etc/pkg/CSWsendnsca
	@ginstall -m 644 $(FILEDIR)/CSWsendnsca.cswusergroup $(DESTDIR)/opt/csw/etc/pkg/CSWsendnsca/cswusergroup
	@#
	@## create user and group for CSWnsca -> cswusergroup
	@#
	@ginstall -m 755 -d $(DESTDIR)/opt/csw/etc/pkg/CSWnsca
	@ginstall -m 644 $(FILEDIR)/CSWnsca.cswusergroup $(DESTDIR)/opt/csw/etc/pkg/CSWnsca/cswusergroup
	@$(MAKECOOKIE)
