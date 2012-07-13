NAME 		= icinga
VERSION 	= 1.7.1
CATEGORIES 	= apps
GARTYPE 	= v2

#
# package definition
#

PACKAGES		+= CSWicinga

SPKG_DESC_CSWicinga	= Icinga network monitoring base package (no plugins)

CATALOGNAME_CSWicinga	= icinga

PACKAGING_PLATFORMS	= solaris10-i386 solaris10-sparc

#
# blurb
#

define BLURB
   Icinga is an enterprise grade open source monitoring system which keeps watch over networks and any conceivable network resource, notifies the user of errors and recoveries and generates performance data for reporting. Icinga is a fork of Nagios and is backward compatible.
endef

#
# download, distfiles, patchfiles
#

MASTER_SITES	= $(SF_MIRRORS)
DISTNAME   	= $(NAME)-$(VERSION)
DISTFILES  	= $(NAME)-$(VERSION).tar.gz

PATCHFILES	+= 0001-use-of-CSW-perl.patch
PATCHFILES	+= 0002-changed-install-and-command-options-in-configure.patch

#
#
#

LICENSE = LICENSE

NOISALIST = 1

#
# reinplacements
#

REINPLACE_USRLOCAL	+= html/docs/de/*
REINPLACE_USRLOCAL	+= html/docs/en/*
REINPLACE_USRSHARE	+= html/docs/de/*
REINPLACE_USRSHARE	+= html/docs/en/*

REINPLACE_USRLOCAL	+= p1\.pl\.in
REINPLACE_USRLOCAL	+= base/icinga\.c
REINPLACE_USRLOCAL	+= sample-config/icinga\.cfg\.in
REINPLACE_USRLOCAL	+= sample-config/cgi\.cfg\.in
REINPLACE_USRLOCAL	+= module/idoutils/config/ido2db\.cfg-sample\.in
REINPLACE_USRLOCAL	+= module/idoutils/config/idomod\.cfg-sample\.in

#
# runtime dependencies
#

RUNTIME_DEP_PKGS_CSWicinga	+= CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWicinga	+= CSWlibz1
RUNTIME_DEP_PKGS_CSWicinga	+= CSWfreetype
RUNTIME_DEP_PKGS_CSWicinga	+= CSWlibgd2
RUNTIME_DEP_PKGS_CSWicinga	+= CSWperl
RUNTIME_DEP_PKGS_CSWicinga	+= CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWicinga	+= CSWapache2
RUNTIME_DEP_PKGS_CSWicinga	+= CSWap2-modphp5
RUNTIME_DEP_PKGS_CSWicinga	+= CSWnagios-plugins

#
# prototypes
#

ICINGA_UGFILES	+= /var/opt/csw/icinga*
ICINGA_UGFILES	+= /etc/opt/csw/icinga*
ICINGA_UGFILES	+= /opt/csw/etc/templates/CSWicinga/.*

PROTOTYPE_MODIFIERS	+= ugfiles
PROTOTYPE_FILES_ugfiles	+= $(ICINGA_UGFILES)
PROTOTYPE_USER_ugfiles 	+= icinga
PROTOTYPE_GROUP_ugfiles += icinga
PROTOTYPE_CLASS_ugfiles += cswcptemplates

ICINGA_CMD	+= /var/opt/csw/icinga/rw.*

PROTOTYPE_MODIFIERS	+= cmd
PROTOTYPE_FILES_cmd	+= $(ICINGA_CMD)
PROTOTYPE_USER_cmd 	+= icinga
PROTOTYPE_GROUP_cmd 	+= icingacm
PROTOTYPE_PERMS_cmd 	+= 2755
PROTOTYPE_CLASS_cmd 	+= cswcptemplates


#
# overrides
#

CHECKPKG_OVERRIDES_CSWicinga += file-with-bad-content|/usr/local|root/opt/csw/share/doc/icinga/Changelog

CHECKPKG_OVERRIDES_CSWicinga += surplus-dependency|CSWnagios-plugins
CHECKPKG_OVERRIDES_CSWicinga += surplus-dependency|CSWap2-modphp5

#
#
#

INITSMF          = /etc/opt/csw/init.d/cswicinga
USERGROUP        = /etc/opt/csw/pkg/CSWicinga/cswusergroup
#POSTMSG          = /opt/csw/share/doc/icinga/README.CSW	

#
# configure
#

prefix = $(BUILD_PREFIX)/icinga
libexecdir = $(BUILD_PREFIX)/libexec/nagios-plugins
sysconfdir = /etc$(prefix)

CONFIGURE_ARGS 	 = $(DIRPATHS)
CONFIGURE_ARGS 	+= --with-log-dir=/var/opt/csw/icinga/log
CONFIGURE_ARGS 	+= --prefix=$(prefix)
CONFIGURE_ARGS 	+= --exec-prefix=$(exec_prefix)
CONFIGURE_ARGS 	+= --with-httpd-conf=$(sysconfdir)
CONFIGURE_ARGS 	+= --with-gd-lib=$(BUILD_PREFIX)/lib
CONFIGURE_ARGS 	+= --with-gd-inc=$(BUILD_PREFIX)/inc
CONFIGURE_ARGS 	+= --with-dbi-lib=$(BUILD_PREFIX)/lib
CONFIGURE_ARGS 	+= --with-dbi-inc=$(BUILD_PREFIX)/include
CONFIGURE_ARGS 	+= --enable-embedded-perl
CONFIGURE_ARGS 	+= --with-lockfile=/var/opt/csw/icinga/icinga.lock
CONFIGURE_ARGS 	+= --localstatedir=/var$(prefix)
CONFIGURE_ARGS 	+= --enable-idoutils
CONFIGURE_ENV	+= install_user=$(USER) install_grp=csw # see patch 0002-changed-install-and-command-options-in-configure.patch
CONFIGURE_ENV   += PATH=/usr/bin:/usr/ccs/bin:/opt/csw/bin:/opt/csw/bin/
CONFIGURE_ENV  	+= CC=/opt/SUNWspro/bin/cc
CONFIGURE_ENV  	+= PERL=/opt/csw/bin/perl

#
# build
#

BUILD_ENV_PATH = $(bindir):$(PATH)

EXTRA_LIB = $(BUILD_PREFIX)/lib

LD_OPTIONS += -R/opt/csw/lib
LD_OPTIONS += -R/opt/csw/icinga/lib

BUILD_ARGS = all

TEST_SCRIPTS =

#
# install
#

# Icinga Makefile calls 'make install' by default

INSTALL_ARGS += install-commandmode

# Other install targets (which are done in this recipe in post-install-modulated):
#   install-init
#   install-config
#   install-webconf

include gar/category.mk

DOCS        = Changelog INSTALLING README UPGRADING
DOCDEST     = $(DESTDIR)$(BUILD_PREFIX)/share/doc/icinga
HTTPD_CONF  = $(DESTDIR)$(sysconfdir)
CFGDIR      = /etc/opt/csw/icinga
TEMPLATEDIR = /opt/csw/etc/templates/CSWicinga$(CFGDIR)

post-install-modulated:
	@#
	@# copying docs
	@#
	@ginstall -m 755 -d $(DOCDEST)
	@ginstall -m 755 -d $(HTTPD_CONF)
	@$(foreach DOC,$(DOCS),ginstall -m 644 $(WORKSRC)/$(DOC) $(DOCDEST);)
	@ginstall -m 644 $(WORKSRC)/LICENSE $(DOCDEST)
	@#ginstall -m 644 $(FILEDIR)/README.CSW $(DOCDEST)
	@#
	@# Start / Stopp script
	@#
	@ginstall -d $(DESTDIR)/etc/$(BUILD_PREFIX)/init.d
	@ginstall -m 755 $(FILEDIR)/cswicinga $(DESTDIR)/etc/$(BUILD_PREFIX)/init.d/cswicinga
	@#
	@# creating config dirs
	@#
	@ginstall -m 775 -d $(DESTDIR)$(CFGDIR)
	@ginstall -m 775 -d $(DESTDIR)$(CFGDIR)/objects
	@ginstall -m 775 -d $(DESTDIR)$(CFGDIR)/conf.d
	@ginstall -m 775 -d $(DESTDIR)$(CFGDIR)/modules
	@#
	@# preparing default config files -> cswcptemplate
	@#
	@ginstall -m 775 -d $(DESTDIR)$(TEMPLATEDIR)
	@ginstall -m 775 -d $(DESTDIR)$(TEMPLATEDIR)/objects
	@ginstall -b -m 664 $(WORKSRC)/sample-config/icinga.cfg $(DESTDIR)$(TEMPLATEDIR)/icinga.cfg
	@ginstall -b -m 664 $(WORKSRC)/module/idoutils/config/ido2db.cfg-sample $(DESTDIR)$(TEMPLATEDIR)/ido2db.cfg
	@ginstall -b -m 664 $(WORKSRC)/module/idoutils/config/idomod.cfg-sample $(DESTDIR)$(TEMPLATEDIR)/ido2db.cfg
	@ginstall -b -m 664 $(WORKSRC)/sample-config/cgi.cfg $(DESTDIR)$(TEMPLATEDIR)/cgi.cfg
	@ginstall -b -m 660 $(WORKSRC)/sample-config/resource.cfg $(DESTDIR)$(TEMPLATEDIR)/resource.cfg
	@ginstall -b -m 644 $(WORKSRC)/sample-config/httpd.conf $(DESTDIR)$(TEMPLATEDIR)/httpd-icinga.conf
	@ginstall -b -m 664 $(WORKSRC)/sample-config/template-object/templates.cfg $(DESTDIR)$(TEMPLATEDIR)/objects/templates.cfg
	@ginstall -b -m 664 $(WORKSRC)/sample-config/template-object/commands.cfg $(DESTDIR)$(TEMPLATEDIR)/objects/commands.cfg
	@ginstall -b -m 664 $(WORKSRC)/sample-config/template-object/contacts.cfg $(DESTDIR)$(TEMPLATEDIR)/objects/contacts.cfg
	@ginstall -b -m 664 $(WORKSRC)/sample-config/template-object/timeperiods.cfg $(DESTDIR)$(TEMPLATEDIR)/objects/timeperiods.cfg
	@ginstall -b -m 664 $(WORKSRC)/sample-config/template-object/localhost.cfg $(DESTDIR)$(TEMPLATEDIR)/objects/localhost.cfg
	@ginstall -b -m 664 $(WORKSRC)/sample-config/template-object/windows.cfg $(DESTDIR)$(TEMPLATEDIR)/objects/windows.cfg
	@ginstall -b -m 664 $(WORKSRC)/sample-config/template-object/printer.cfg $(DESTDIR)$(TEMPLATEDIR)/objects/printer.cfg
	@ginstall -b -m 664 $(WORKSRC)/sample-config/template-object/switch.cfg $(DESTDIR)$(TEMPLATEDIR)/objects/switch.cfg
	@#
	@# create user and group -> cswusergroup
	@#
	@ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/pkg/CSWicinga
	@ginstall -m 644 $(FILEDIR)/cswusergroup $(DESTDIR)/etc/opt/csw/pkg/CSWicinga/cswusergroup
	@#
	@# end of post-install
	@#
	@$(MAKECOOKIE)
