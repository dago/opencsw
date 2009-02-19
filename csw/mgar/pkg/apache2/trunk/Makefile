GARNAME = httpd
GARVERSION = 2.2.11
CATEGORIES = server

DESCRIPTION = A high performance Unix-based HTTP server.
define BLURB
  Apache is the world\'s most popular HTTP server, being quite possibly the
  best around in terms of functionality, efficiency, security and speed.
endef

include files/config.mk

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# Dummy toplevel package
DISTFILES += $(call admfiles,CSWapache2,depend prototype)
# Runtime
DISTFILES += $(call admfiles,CSWapache2rt,depend prototype checkinstall)
# Server (core)
CSWapache2c_admfiles = depend prototype postinstall space
DISTFILES += $(call admfiles,CSWapache2c,$(CSWapache2c_admfiles))
# Prefork MPM (default)
CSWap2prefork_admfiles  = depend prototype postinstall postremove space
DISTFILES += $(call admfiles,CSWap2prefork,$(CSWap2prefork_admfiles))
# mod_suexec
CSWap2suexec_admfiles = depend prototype postinstall preremove
DISTFILES += $(call admfiles,CSWap2suexec,$(CSWap2suexec_admfiles))
# Manual
DISTFILES += $(call admfiles,CSWapache2-manual,depend prototype)
# Development support
DISTFILES += $(call admfiles,CSWapache2-devel,depend prototype)

# Standard package bits
DISTFILES += CSWapache2.killproc cswapache2 svc-cswapache2 cswapache2.xml

# Configuration templates
DISTFILES += httpd.conf.CSW
DISTFILES += httpd-mpm.conf.CSW
DISTFILES += httpd-ssl.conf.CSW
DISTFILES += update20to22

pre-configure-modulated:
	(cd $(WORKDIR)/$(GARNAME)-$(GARVERSION); \
	./buildconf)

# Build Configuration
CONFIGURE_ARGS += --with-mpm=prefork

# Fixup target variables
APACHE_ROOT   = $(DESTDIR)$(prefix)/apache2
LIBTOOL_LADIR = $(APACHE_ROOT)/lib
STRIP_DIRS    = $(APACHE_ROOT)/sbin $(APACHE_ROOT)/libexec

include gar/category.mk
include files/rules.mk

CFLAGS := -DSSL_EXPERIMENTAL -DSSL_ENGINE $(CFLAGS)

FIXCONFIG_DIRS     = $(DESTDIR)
FIXCONFIG_RMPATHS  = $(DESTDIR)
FIXCONFIG_RMPATHS += $(CURDIR)/$(WORKSRC)/$(GARNAME)-$(GARVERSION)/srclib/apr-util
FIXCONFIG_RMPATHS += $(CURDIR)/$(WORKSRC)/$(GARNAME)-$(GARVERSION)/srclib/apr-util/include
FIXCONFIG_RMPATHS += $(CURDIR)/$(WORKSRC)/$(GARNAME)-$(GARVERSION)/srclib/apr
FIXCONFIG_RMPATHS += $(CURDIR)/$(WORKSRC)/$(GARNAME)-$(GARVERSION)/srclib/apr/include

post-install-modulated: rename-httpd copy-local-files create-templates

rename-httpd:
	@if test -f $(APACHE_ROOT)/sbin/httpd ; then \
	    ( cd $(APACHE_ROOT)/sbin ; mv httpd httpd.prefork ) ; \
	fi

# Copy in specialized templates
copy-local-files:
	@ginstall -d $(DESTDIR)/etc/init.d
	@ginstall $(WORKDIR)/cswapache2 $(DESTDIR)/etc/init.d
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

