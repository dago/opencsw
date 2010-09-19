# $Id$

GARNAME = httpd
GARVERSION = 2.2.16
CATEGORIES = server

DESCRIPTION = A high performance HTTP server.
define BLURB
  Apache is the world\'s most popular HTTP server, being quite possibly the
  best around in terms of functionality, efficiency, security and speed.
endef

# work around dumb checkpkg not recognizing the license file ...
LICENSE = LICENSE

# Build multiple mpm's and merge them all into one install
EXTRA_MODULATORS = MPM
MODULATIONS_MPM = prefork worker event

MERGE_SCRIPTS_isa-default-mpm-prefork = copy-all
MERGE_SCRIPTS_isa-default-mpm-worker = copy-all
MERGE_SCRIPTS_isa-default-mpm-event = copy-all

include files/config.mk

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# The PACKAGES variable tell GAR which packages to build
PACKAGES  = CSWapache2 CSWapache2rt CSWapache2c
PACKAGES += CSWapache2-devel CSWapache2-manual
PACKAGES += CSWap2prefork CSWap2worker CSWap2event CSWap2suexec

CATALOGNAME_CSWapache2 = apache2
CATALOGNAME_CSWapache2rt = apache2rt
CATALOGNAME_CSWapache2c = apache2c
CATALOGNAME_CSWapache2-devel = apache2_devel
CATALOGNAME_CSWapache2-manual = apache2_manual
CATALOGNAME_CSWap2prefork = ap2_prefork
CATALOGNAME_CSWap2worker = ap2_worker
CATALOGNAME_CSWap2event = ap2_event
CATALOGNAME_CSWap2suexec = ap2_suexec

SPKG_DESC_CSWapache2 = A high performance Unix-based HTTP server.
SPKG_DESC_CSWapache2rt = Apache2 runtime support.
SPKG_DESC_CSWapache2c = Apache2 core files.
SPKG_DESC_CSWapache2-devel = The development files for Apache2.
SPKG_DESC_CSWapache2-manual = The Apache2 manual files.
SPKG_DESC_CSWap2prefork = The standard preforking mpm for Apache2.
SPKG_DESC_CSWap2worker = The standard threaded worker mpm for Apache2.
SPKG_DESC_CSWap2event = The standard event mpm for Apache2.
SPKG_DESC_CSWap2suexec = The standard suEXEC binary for Apache2.

# Standard package bits
DISTFILES += CSWapache2.killproc cswapache2

# Configuration templates
DISTFILES += httpd.conf.CSW
DISTFILES += httpd-mpm.conf.CSW
DISTFILES += httpd-ssl.conf.CSW
DISTFILES += update20to22

RUNTIME_DEP_PKGS_CSWapache2	   = CSWapache2c CSWap2prefork
RUNTIME_DEP_PKGS_CSWapache2c       = CSWexpat CSWiconv
RUNTIME_DEP_PKGS_CSWapache2c      += CSWoldaprt CSWosslrt CSWzlib
RUNTIME_DEP_PKGS_CSWapache2c      += CSWapr CSWapr-util CSWbdb48
RUNTIME_DEP_PKGS_CSWapache2c	   = CSWapache2rt
RUNTIME_DEP_PKGS_CSWapache2rt      = CSWexpat CSWiconv
RUNTIME_DEP_PKGS_CSWapache2rt     += CSWoldaprt CSWosslrt CSWzlib
RUNTIME_DEP_PKGS_CSWapache2rt     += CSWapr CSWapr-util CSWbdb48
RUNTIME_DEP_PKGS_CSWapache2-manual = CSWapache2
RUNTIME_DEP_PKGS_CSWapache2-devel  = CSWapache2
RUNTIME_DEP_PKGS_CSWap2prefork	   = CSWapache2
RUNTIME_DEP_PKGS_CSWap2suexec	   = CSWapache2
RUNTIME_DEP_PKGS_CSWap2worker	   = CSWapache2

# We need this to get bdb48/lib into the runpath
EXTRA_LIB = $(prefix)/bdb48/lib

# The SMF support: you don't need to specify cswinitsmf any more.  You need to
# make sure the the /etc/opt/csw/init.d/cswapache file gets installed during
# the post-install stage, and add "INITSMF = /etc/opt/csw/init.d/cswapache" to
# the Makefile.
INITSMF = /etc/opt/csw/init.d/cswapache2

pre-configure-modulated:
	(cd $(WORKDIR)/$(GARNAME)-$(GARVERSION); ./buildconf)

# Build Configuration
CONFIGURE_ARGS += --with-apr=$(prefix)/bin/apr-1-config
CONFIGURE_ARGS += --with-apr-util=$(prefix)/bin/apu-1-config
CONFIGURE_ARGS += --with-mpm=$(MPM)
CONFIGURE_ARGS += --disable-static
ifneq ($(MPM),prefork)
CONFIGURE_ARGS += --enable-modules=none
else
CONFIGURE_ARGS += --enable-mods-shared=all
endif

# Fixup target variables
APACHE_ROOT   = $(DESTDIR)$(prefix)/apache2
LIBTOOL_LADIR = $(APACHE_ROOT)/lib
STRIP_DIRS    = $(APACHE_ROOT)/sbin $(APACHE_ROOT)/libexec

include gar/category.mk
include files/rules.mk

CFLAGS := -DSSL_EXPERIMENTAL -DSSL_ENGINE $(CFLAGS)

FIXCONFIG_DIRS     = $(DESTDIR)
FIXCONFIG_RMPATHS  = $(DESTDIR)
#FIXCONFIG_RMPATHS += $(CURDIR)/$(WORKSRC)/$(GARNAME)-$(GARVERSION)/srclib/apr-util
#FIXCONFIG_RMPATHS += $(CURDIR)/$(WORKSRC)/$(GARNAME)-$(GARVERSION)/srclib/apr-util/include
#FIXCONFIG_RMPATHS += $(CURDIR)/$(WORKSRC)/$(GARNAME)-$(GARVERSION)/srclib/apr
#FIXCONFIG_RMPATHS += $(CURDIR)/$(WORKSRC)/$(GARNAME)-$(GARVERSION)/srclib/apr/include

post-install-modulated: rename-httpd copy-local-files create-templates

rename-httpd:
	@if test -f $(APACHE_ROOT)/sbin/httpd ; then \
	    ( cd $(APACHE_ROOT)/sbin ; mv httpd httpd.$(MPM) ) ; \
	fi

# Copy in specialized templates
copy-local-files:
	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	@ginstall $(WORKDIR)/cswapache2 $(DESTDIR)/etc/opt/csw/init.d
	@ginstall $(WORKDIR)/httpd.conf.CSW $(APACHE_ROOT)/etc
	@ginstall $(WORKDIR)/httpd-mpm.conf.CSW $(APACHE_ROOT)/etc/extra
	@ginstall $(WORKDIR)/httpd-ssl.conf.CSW $(APACHE_ROOT)/etc/extra
	@ginstall $(WORKDIR)/update20to22 $(APACHE_ROOT)/sbin

# Create stock templates
template_list  = share/htdocs/index.html
template_list += etc/extra/httpd-autoindex.conf
template_list += etc/extra/httpd-dav.conf
template_list += etc/extra/httpd-default.conf
template_list += etc/extra/httpd-info.conf
template_list += etc/extra/httpd-languages.conf
template_list += etc/extra/httpd-multilang-errordoc.conf
template_list += etc/extra/httpd-userdir.conf
template_list += etc/extra/httpd-vhosts.conf
template_list += etc/magic
template_list += etc/mime.types

create-templates:
	@echo "  => Creating template files"
	@( cd $(DESTDIR)$(prefix)/apache2 ; \
			for file in $(template_list) ; do \
				gmv -v $$file $$file.CSW ; \
			done )
	@$(MAKECOOKIE)
