# $Id$

GARNAME = httpd
GARVERSION = 2.2.16
CATEGORIES = server

DESCRIPTION = A high performance HTTP server.
define BLURB
  Apache is the world\'s most popular HTTP server, being quite possibly the
  best around in terms of functionality, efficiency, security and speed.
endef

# Source location
MASTER_SITES  = http://www.ibiblio.com/pub/mirrors/apache/httpd/

# work around dumb checkpkg not recognizing the license file ...
LICENSE = LICENSE

# Build multiple mpm's and merge them all into one install
EXTRA_MODULATORS = MPM
MODULATIONS_MPM = prefork worker

MERGE_SCRIPTS_isa-default-mpm-prefork = copy-all
MERGE_SCRIPTS_isa-default-mpm-worker = copy-all

# Visitor information
SPKG_SOURCEURL = http://httpd.apache.org/

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += config.layout
# Standard package bits
DISTFILES += CSWapache2.killproc cswapache2

DISTFILES += CSWapache2.preinstall CSWapache2.postinstall
DISTFILES += CSWap2suexec.postinstall CSWap2suexec.preremove

# Configuration templates
DISTFILES += httpd.conf.CSW
DISTFILES += httpd-mpm.conf.CSW
DISTFILES += httpd-ssl.conf.CSW
DISTFILES += update20to22
DISTFILES += README.CSW.apache2 README.CSW.ap2_prefork README.CSW.ap2_worker
DISTFILES += README.CSW.apache2rt

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# The PACKAGES variable tell GAR which packages to build
PACKAGES  = CSWapache2 CSWapache2-devel CSWapache2-manual CSWap2suexec

NEED_DUMMY_AP2 = 1

ifeq ($(NEED_DUMMY_AP2), 1)
# These packages are dummy versions to make dependencies nicer
# as various things depend on CSWap2prefork currently
PACKAGES += CSWap2prefork CSWap2worker CSWapache2rt
endif

ARCHALL_CSWapache2-manual = 1
ifeq ($(NEED_DUMMY_AP2), 1)
ARCHALL_CSWap2prefork = 1
ARCHALL_CSWap2worker = 1
ARCHALL_CSWapache2rt = 1
endif

CATALOGNAME_CSWapache2 = apache2
CATALOGNAME_CSWapache2-devel = apache2_devel
CATALOGNAME_CSWapache2-manual = apache2_manual
CATALOGNAME_CSWap2suexec = ap2_suexec
ifeq ($(NEED_DUMMY_AP2), 1)
CATALOGNAME_CSWap2prefork = ap2_prefork
CATALOGNAME_CSWap2worker = ap2_worker
CATALOGNAME_CSWapache2rt = apache2rt
endif

SPKG_DESC_CSWapache2 = A high performance Unix-based HTTP server.
SPKG_DESC_CSWapache2-devel = The development files for Apache2.
SPKG_DESC_CSWapache2-manual = The Apache2 manual files.
SPKG_DESC_CSWap2suexec = The standard suEXEC binary for Apache2.
ifeq ($(NEED_DUMMY_AP2), 1)
SPKG_DESC_CSWap2prefork = A dummy stub for the old prefork mpm package
SPKG_DESC_CSWap2worker = A dummy stub for the old worker mpm package
SPKG_DESC_CSWapache2rt = A dummy stub for the old apache2rt package
endif

INCOMPATIBLE_PKGS_CSWapache2  = CSWapache2c
ifneq ($(NEED_DUMMY_AP2), 1)
INCOMPATIBLE_PKGS_CSWapache2 += CSWap2prefork CSWap2worker CSWapache2rt
endif

RUNTIME_DEP_PKGS_CSWapache2       += CSWexpat CSWiconv
RUNTIME_DEP_PKGS_CSWapache2       += CSWoldaprt CSWosslrt CSWzlib
RUNTIME_DEP_PKGS_CSWapache2       += CSWapr CSWapr-util CSWbdb48
RUNTIME_DEP_PKGS_CSWapache2-manual = CSWapache2
RUNTIME_DEP_PKGS_CSWapache2-devel  = CSWapache2
RUNTIME_DEP_PKGS_CSWap2suexec	   = CSWapache2
ifeq ($(NEED_DUMMY_AP2), 1)
RUNTIME_DEP_PKGS_CSWap2prefork     = CSWapache2
RUNTIME_DEP_PKGS_CSWap2worker      = CSWapache2
RUNTIME_DEP_PKGS_CSWapache2rt	   = CSWapache2
endif

CHECKPKG_OVERRIDES_CSWap2suexec  += surplus-dependency|CSWapache2
CHECKPKG_OVERRIDES_CSWapache2-devel += surplus-dependency|CSWapache2
CHECKPKG_OVERRIDES_CSWapache2-manual += surplus-dependency|CSWapache2
CHECKPKG_OVERRIDES_CSWapache2 += surplus-dependency|CSWalternatives
ifeq ($(NEED_DUMMY_AP2), 1)
CHECKPKG_OVERRIDES_CSWap2prefork += surplus-dependency|CSWapache2
CHECKPKG_OVERRIDES_CSWap2worker += surplus-dependency|CSWapache2
CHECKPKG_OVERRIDES_CSWapache2rt += surplus-dependency|CSWapache2
endif

# We need this to get bdb48/lib into the runpath
EXTRA_LIB = $(prefix)/bdb48/lib

# The SMF support: you don't need to specify cswinitsmf any more.  You need to
# make sure the the /etc/opt/csw/init.d/cswapache file gets installed during
# the post-install stage, and add "INITSMF = /etc/opt/csw/init.d/cswapache" to
# the Makefile.
INITSMF = /etc/opt/csw/init.d/cswapache2

POSTMSG = /opt/csw/share/doc/apache2/README.CSW

ALTERNATIVES_CSWapache2 = prefork worker
ALTERNATIVE_prefork = /opt/csw/apache2/sbin/httpd httpd /opt/csw/apache2/sbin/httpd.prefork 100
ALTERNATIVE_worker = /opt/csw/apache2/sbin/httpd httpd /opt/csw/apache2/sbin/httpd.worker 50

# Build Configuration
CONFIGURE_ARGS += --with-apr=$(prefix)/bin/apr-1-config
CONFIGURE_ARGS += --with-apr-util=$(prefix)/bin/apu-1-config
CONFIGURE_ARGS += --with-mpm=$(MPM)
CONFIGURE_ARGS += --disable-static
CONFIGURE_ARGS += --enable-layout=csw
CONFIGURE_ARGS += --enable-rule=SSL_EXPERIMENTAL
CONFIGURE_ARGS += --enable-ssl
CONFIGURE_ARGS += --with-z=$(prefix)
CONFIGURE_ARGS += --with-ssl=$(prefix)

ifneq ($(MPM),prefork)
CONFIGURE_ARGS += --enable-modules=none
else
CONFIGURE_ARGS += --enable-suexec
CONFIGURE_ARGS += --with-suexec-caller=nobody
CONFIGURE_ARGS += --with-suexec-docroot=$(prefix)/apache2/share/htdocs
CONFIGURE_ARGS += --with-suexec-userdir=public_html
CONFIGURE_ARGS += --with-suexec-uidmin=100
CONFIGURE_ARGS += --with-suexec-gidmin=100
CONFIGURE_ARGS += --with-suexec-logfile=$(prefix)/apache2/var/log/suexec_log
CONFIGURE_ARGS += --with-suexec-bin=$(prefix)/apache2/sbin/suexec
CONFIGURE_ARGS += --enable-authn-alias
CONFIGURE_ARGS += --enable-authnz-ldap
CONFIGURE_ARGS += --enable-file-cache
CONFIGURE_ARGS += --enable-cache
CONFIGURE_ARGS += --enable-disk-cache
CONFIGURE_ARGS += --enable-mem-cache
CONFIGURE_ARGS += --enable-bucketeer
CONFIGURE_ARGS += --enable-charset-lite
CONFIGURE_ARGS += --enable-ldap
CONFIGURE_ARGS += --enable-log-forensic
CONFIGURE_ARGS += --enable-usertrack
CONFIGURE_ARGS += --enable-unique-id
CONFIGURE_ARGS += --enable-version
CONFIGURE_ARGS += --enable-proxy
CONFIGURE_ARGS += --enable-proxy-connect
CONFIGURE_ARGS += --enable-proxy-ftp
CONFIGURE_ARGS += --enable-proxy-http
CONFIGURE_ARGS += --enable-proxy-ajp
CONFIGURE_ARGS += --enable-proxy-balancer
CONFIGURE_ARGS += --enable-cgid
CONFIGURE_ARGS += --enable-dav-lock
CONFIGURE_ARGS += --enable-mods-shared=all
endif

# Fixup target variables
APACHE_ROOT   = $(DESTDIR)$(prefix)/apache2
LIBTOOL_LADIR = $(APACHE_ROOT)/lib
STRIP_DIRS    = $(APACHE_ROOT)/sbin $(APACHE_ROOT)/libexec

PKGFILES_CSWap2suexec = .*sbin/suexec .*libexec/.*suexec.* .*/man/.*suexec.*
PKGFILES_CSWapache2-devel = $(PKGFILES_DEVEL)
PKGFILES_CSWapache2-manual = .*share/.*manual.* .*etc/extra/httpd-manual.conf
ifeq ($(NEED_DUMMY_AP2), 1)
PKGFILES_CSWap2prefork = .*share/doc/ap2_prefork.*
PKGFILES_CSWap2worker = .*share/doc/ap2_worker.*
PKGFILES_CSWapache2rt = .*share/doc/apache2rt.*
endif

include gar/category.mk

CFLAGS := -DSSL_EXPERIMENTAL -DSSL_ENGINE $(CFLAGS)

FIXCONFIG_DIRS     = $(DESTDIR)
FIXCONFIG_RMPATHS  = $(DESTDIR)

pre-configure-modulated:
	(cd $(WORKDIR)/$(GARNAME)-$(GARVERSION); ./buildconf)
	@gsed -e s,INSTALL_PREFIX,$(prefix)/apache2,g \
		$(WORKDIR)/config.layout > $(WORKDIR)/$(GARNAME)-$(GARVERSION)/config.layout
	@$(MAKECOOKIE)


post-install-modulated: rename-httpd copy-local-files create-templates copy-readmes

copy-readmes:
	@(cd $(WORKDIR); for f in README.CSW*; do \
		p=`echo $$f | sed 's/README.CSW.//'`; \
		ginstall -d -m0755 $(DESTDIR)/$(prefix)/share/doc/$$p; \
		ginstall -m 0644 $$f $(DESTDIR)/$(prefix)/share/doc/$$p/README.CSW; \
	done)

rename-httpd:
	@if test -f $(APACHE_ROOT)/sbin/httpd ; then \
	    ( cd $(APACHE_ROOT)/sbin ; mv httpd httpd.$(MPM) ) ; \
	fi

# Copy in specialized templates
copy-local-files:
	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	@ginstall $(WORKDIR)/cswapache2 $(DESTDIR)/etc/opt/csw/init.d
	@ginstall -m0644 $(WORKDIR)/httpd.conf.CSW $(APACHE_ROOT)/etc
	@ginstall -m0644 $(WORKDIR)/httpd-mpm.conf.CSW $(APACHE_ROOT)/etc/extra
	@ginstall -m0644 $(WORKDIR)/httpd-ssl.conf.CSW $(APACHE_ROOT)/etc/extra
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
