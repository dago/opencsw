NAME = nagios
VERSION = 3.4.1
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Nagios network monitoring base package (no plugins)
define BLURB
  Nagios is a powerful, enterprise-class host, service, application, and network monitoring program. Designed to be fast, flexible, and rock-solid stable. Nagios runs on *NIX hosts and can monitor Windows, Linux/Unix/BSD, Netware, and network devices.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTNAME   = nagios
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += CSWnagios.preinstall
DISTFILES += CSWnagios.postinstall
DISTFILES += cswnagios
DISTFILES += cswusergroup
DISTFILES += README.CSW

PATCHFILES	+= 0001-Removed-gcc-macro.patch
PATCHFILES	+= 0001-changed-install-and-command-options-in-configure.patch
PATCHFILES	+= 0003-changed-syntax-of-define-statement.patch
PATCHFILES	+= 0005-changed-object-files-to-executables.patch
PATCHFILES 	+= 0005-Adjusted-CFLAGS-to-solaris-compiler.patch
PATCHFILES 	+= 0006-path-to-csw-perl.patch
#PATCHFILES 	+= 0007-nagios-bug-244.patch
PATCHFILES 	+= 0008-changed-paths-to-match-csw-standards.patch

RUNTIME_DEP_PKGS_CSWnagios  = CSWapache2 CSWgd CSWglib2 CSWjpeg CSWlibtoolrt CSWggettextrt
RUNTIME_DEP_PKGS_CSWnagios += CSWperl CSWnagios-plugins CSWap2-modphp5 
RUNTIME_DEP_PKGS_CSWnagios += CSWlibgd2
RUNTIME_DEP_PKGS_CSWnagios += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWnagios += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWnagios += CSWlibz1
RUNTIME_DEP_PKGS_CSWnagios += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWnagios += CSWfreetype

LICENSE = LICENSE

NOISALIST = 1

#
# prototype
#

PROTOTYPE_FILTER = awk '$$$$3 ~ /\/etc\/opt\/csw\/nagios/ { $$$$2 = "cswcptemplates" ; $$$$5 = "nagios" ; $$$$6 = "nagios" } \
		        $$$$3 ~ /\/var\/opt\/csw\/nagios/ { $$$$2 = "cswcptemplates" ; $$$$5 = "nagios" ; $$$$6 = "nagios" } \
		        $$$$3 ~ /\/var\/opt\/csw\/nagios\/rw/ { $$$$2 = "cswcptemplates" ; $$$$4 = "2755" ; $$$$5 = "nagios" ; $$$$6 = "nagioscm" } \
		        { print }'


INITSMF          = /etc/opt/csw/init.d/cswnagios
USERGROUP        = /etc/opt/csw/pkg/CSWnagios/cswusergroup
POSTMSG          = /opt/csw/share/doc/nagios/README.CSW	

#
# configure
#

prefix = $(BUILD_PREFIX)/nagios
libexecdir = $(BUILD_PREFIX)/libexec/nagios-plugins
sysconfdir = /etc$(prefix)

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --prefix=$(prefix)
CONFIGURE_ARGS += --exec-prefix=$(exec_prefix)
CONFIGURE_ARGS += --with-command-user=nagios
CONFIGURE_ARGS += --with-command-group=nagioscm
CONFIGURE_ARGS += --with-httpd-conf=$(sysconfdir)
CONFIGURE_ARGS += --with-gd-lib=$(BUILD_PREFIX)/lib
CONFIGURE_ARGS += --with-gd-inc=$(BUILD_PREFIX)/inc
CONFIGURE_ARGS += --enable-embedded-perl
CONFIGURE_ARGS += --with-checkresult-dir=/var/opt/csw/nagios/spool/checkresults
CONFIGURE_ARGS += --with-lockfile=/var/opt/csw/nagios/nagios.lock
CONFIGURE_ARGS += --localstatedir=/var$(prefix)
CONFIGURE_ENV  += install_user=$(USER) install_grp=csw # see PATCHFILES
CONFIGURE_ENV   += PATH=/usr/bin:/usr/ccs/bin:/opt/csw/bin:/opt/csw/bin/
CONFIGURE_ENV  += CC=/opt/SUNWspro/bin/cc
CONFIGURE_ENV  += PERL=/opt/csw/bin/perl

#
# build
#

BUILD_ENV_PATH = $(bindir):$(PATH)

EXTRA_LIB = $(BUILD_PREFIX)/lib

LD_OPTIONS += -R/opt/csw/lib
LD_OPTIONS += -R/opt/csw/nagios/lib

BUILD_ARGS = all

# ENABLE_CHECK = 0

#TEST_TARGET = none
TEST_SCRIPTS =

#
# install
# Nagios Makefile calls install-basic by default
#

INSTALL_ARGS += install-commandmode

#
# override chkpkg
# (in all html and cfg files the string /usr/local appears, which is uncritical.)
#

CHECKPKG_OVERRIDES_CSWnagios += file-with-bad-content|/usr/local|root/opt/csw/etc/templates/CSWnagios/etc/opt/csw/nagios/nagios.cfg
CHECKPKG_OVERRIDES_CSWnagios += file-with-bad-content|/usr/local|root/opt/csw/etc/templates/CSWnagios/etc/opt/csw/nagios/cgi.cfg

#
# yes, we need this dependencies
#

CHECKPKG_OVERRIDES_CSWnagios += surplus-dependency|CSWgd
CHECKPKG_OVERRIDES_CSWnagios += surplus-dependency|CSWglib2
CHECKPKG_OVERRIDES_CSWnagios += surplus-dependency|CSWnagios-plugins
CHECKPKG_OVERRIDES_CSWnagios += surplus-dependency|CSWlibtoolrt
CHECKPKG_OVERRIDES_CSWnagios += surplus-dependency|CSWap2-modphp5
CHECKPKG_OVERRIDES_CSWnagios += surplus-dependency|CSWggettextrt

CHECKPKG_OVERRIDES_CSWnagios += surplus-dependency|CSWlibiconv2
CHECKPKG_OVERRIDES_CSWnagios += surplus-dependency|CSWjpeg

CHECKPKG_OVERRIDES_CSWnagios += unidentified-dependency|CSWnagios-plugins

include gar/category.mk

DOCS        = Changelog INSTALLING README UPGRADING
DOCDEST     = $(DESTDIR)$(BUILD_PREFIX)/share/doc/nagios
HTTPD_CONF  = $(DESTDIR)$(sysconfdir)
CFGDIR      = /etc/opt/csw/nagios
TEMPLATEDIR = /opt/csw/etc/templates/CSWnagios/etc/opt/csw/nagios

post-install-modulated:
	@#
	@# copying docs
	@#
	@ginstall -m 755 -d $(DOCDEST)
	@ginstall -m 755 -d $(HTTPD_CONF)
	@$(foreach DOC,$(DOCS),ginstall -m 644 $(WORKSRC)/$(DOC) $(DOCDEST);)
	@ginstall -m 644 $(WORKSRC)/LICENSE $(DOCDEST)
	@ginstall -m 644 $(FILEDIR)/README.CSW $(DOCDEST)
	@#
	@# Start / Stopp script
	@#
	@ginstall -d $(DESTDIR)/etc/$(BUILD_PREFIX)/init.d
	@ginstall -m 755 $(FILEDIR)/cswnagios $(DESTDIR)/etc/$(BUILD_PREFIX)/init.d/cswnagios
	@#
	@# creating config dirs
	@#
	@ginstall -m 775 -d $(DESTDIR)$(CFGDIR)
	@ginstall -m 775 -d $(DESTDIR)$(CFGDIR)/objects
	@#
	@# preparing default config files -> cswcptemplate
	@#
	@ginstall -m 775 -d $(DESTDIR)$(TEMPLATEDIR)
	@ginstall -m 775 -d $(DESTDIR)$(TEMPLATEDIR)/objects
	@ginstall -b -m 664 $(WORKSRC)/sample-config/nagios.cfg $(DESTDIR)$(TEMPLATEDIR)/nagios.cfg
	@ginstall -b -m 664 $(WORKSRC)/sample-config/cgi.cfg $(DESTDIR)$(TEMPLATEDIR)/cgi.cfg
	@ginstall -b -m 660 $(WORKSRC)/sample-config/resource.cfg $(DESTDIR)$(TEMPLATEDIR)/resource.cfg
	@ginstall -b -m 644 $(WORKSRC)/sample-config/httpd.conf $(DESTDIR)$(TEMPLATEDIR)/httpd-nagios.conf
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
	@ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/pkg/CSWnagios
	@ginstall -m 644 $(FILEDIR)/cswusergroup $(DESTDIR)/etc/opt/csw/pkg/CSWnagios/cswusergroup
	@#
	@# end of post-install
	@#
	@$(MAKECOOKIE)
