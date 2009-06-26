GARNAME = icinga
GARVERSION = 0.8.1
CATEGORIES = apps

DESCRIPTION = icinga network monitoring base package (no plugins)
define BLURB
endef

SF_PROJ = icinga
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWicinga, prototype)
DISTFILES += cswicinga
DISTFILES += cswusergroup

PATCHFILES = cmd.c.diff		# cgi/cmd.c - GNU macro __attribute__ unknown to compiler

PATCHFILES += patch.diff	# http://article.gmane.org/gmane.network.nagios.devel/4726
				# (Error 2)
#PATCHFILES += configure.diff	# configure.in
				# http://unix.derkeiler.com/Mailing-Lists/SunManagers/2004-11/0424.html
				# -lsunmath is needed in configure for checking of libgd
PATCHFILES += install-opts.diff	# sets in every Makefile.in "INSTALL_OPT="" (empty)
				# necessary, so ginstall doesn't get -o and -g options

REQUIRED_PKGS  = CSWgd CSWggettextrt CSWglib2 CSWiconv CSWjpeg CSWperl CSWpng CSWzlib
REQUIRED_PKGS += CSWnagiosp CSWcswclassutils

SPKG_CLASSES = none cswusergroup ugfiles cswpreserveconf cswinitsmf

NOISALIST = 1

ENABLE_CHECK = 0

prefix = $(BUILD_PREFIX)/icinga
libexecdir = $(BUILD_PREFIX)/libexec/nagios-plugins
localstatedir = /var/opt/csw/icinga

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --prefix=$(prefix)
CONFIGURE_ARGS += --exec-prefix=$(exec_prefix)
CONFIGURE_ARGS += --with-command-user=icinga
CONFIGURE_ARGS += --with-command-group=icinga
CONFIGURE_ARGS += --with-httpd-conf=/opt/csw/apache2/etc
CONFIGURE_ARGS += --enable-embedded-perl
#CONFIGURE_ARGS += --enable-idoutils # requires libdbi.so
CONFIGURE_ARGS += --with-checkresult-dir=/var/opt/csw/icinga/spool/checkresults
CONFIGURE_ARGS += --with-lockfile=/var/opt/csw/icinga/icinga.lock

EXTRA_LIB = $(BUILD_PREFIX)/lib

BUILD_ARGS = all

#ENABLE_CHECK = 0

TEST_TARGET = none

INSTALL_ARGS += install-init
#INSTALL_ARGS += install-config
INSTALL_ARGS += install-commandmode

LD_OPTIONS += -R/opt/csw/lib
LD_OPTIONS -= -R/opt/csw/nagios/lib

include gar/category.mk

DOCS = Changelog INSTALLING README UPGRADING
DOCDEST = $(DESTDIR)$(BUILD_PREFIX)/share/doc/icinga
HTTPD_CONF = $(DESTDIR)/opt/csw/apache2/etc
CFGDIR = $(prefix)/etc

post-install-modulated:
	@ginstall -m 755 -d $(DOCDEST)
	@ginstall -m 755 -d $(HTTPD_CONF)
	@$(foreach DOC,$(DOCS),ginstall -m 644 $(WORKSRC)/$(DOC) $(DOCDEST);)
	@ginstall -m 644 $(WORKSRC)/LICENSE $(DOCDEST)
#	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
#	@ginstall -m 755 $(FILEDIR)/cswnagios $(DESTDIR)/etc/opt/csw/init.d/cswnagios
	@ginstall -m 775 -d $(DESTDIR)$(CFGDIR)
	@ginstall -m 775 -d $(DESTDIR)$(CFGDIR)/objects
	@ginstall -b -m 664 $(WORKSRC)/sample-config/README $(DESTDIR)$(CFGDIR)/README
	@ginstall -b -m 664 $(WORKSRC)/sample-config/cgi.cfg $(DESTDIR)$(CFGDIR)/cgi.cfg.CSW
	@ginstall -m 644 $(WORKSRC)/sample-config/httpd.conf $(DESTDIR)$(CFGDIR)/httpd-nagios.conf
	@ginstall -b -m 664 $(WORKSRC)/sample-config/icinga.cfg $(DESTDIR)$(CFGDIR)/icinga.cfg.CSW
	@ginstall -b -m 660 $(WORKSRC)/sample-config/mrtg.cfg $(DESTDIR)$(CFGDIR)/mrtg.cfg.CSW
	@ginstall -b -m 660 $(WORKSRC)/sample-config/resource.cfg $(DESTDIR)$(CFGDIR)/resource.cfg.CSW
	@ginstall -b -m 664 $(WORKSRC)/sample-config/template-object/templates.cfg $(DESTDIR)$(CFGDIR)/objects/templates.cfg.CSW
	@ginstall -b -m 664 $(WORKSRC)/sample-config/template-object/commands.cfg $(DESTDIR)$(CFGDIR)/objects/commands.cfg.CSW
	@ginstall -b -m 664 $(WORKSRC)/sample-config/template-object/contacts.cfg $(DESTDIR)$(CFGDIR)/objects/contacts.cfg.CSW
	@ginstall -b -m 664 $(WORKSRC)/sample-config/template-object/timeperiods.cfg $(DESTDIR)$(CFGDIR)/objects/timeperiods.cfg.CSW
	@ginstall -b -m 664 $(WORKSRC)/sample-config/template-object/localhost.cfg $(DESTDIR)$(CFGDIR)/objects/localhost.cfg.CSW
	@ginstall -b -m 664 $(WORKSRC)/sample-config/template-object/windows.cfg $(DESTDIR)$(CFGDIR)/objects/windows.cfg.CSW
	@ginstall -b -m 664 $(WORKSRC)/sample-config/template-object/printer.cfg $(DESTDIR)$(CFGDIR)/objects/printer.cfg.CSW
	@ginstall -b -m 664 $(WORKSRC)/sample-config/template-object/switch.cfg $(DESTDIR)$(CFGDIR)/objects/switch.cfg.CSW
	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	@ginstall -m 755 $(FILEDIR)/cswicinga $(DESTDIR)/etc/opt/csw/init.d/cswicinga
	@ginstall -d $(DESTDIR)/opt/csw/etc/pkg/CSWicinga
	@ginstall -m 644 $(FILEDIR)/cswusergroup $(DESTDIR)/opt/csw/etc/pkg/CSWicinga/cswusergroup
	@$(MAKECOOKIE)
