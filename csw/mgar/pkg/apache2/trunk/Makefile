# $Id$

GARNAME = httpd
GARVERSION = 2.2.14
CATEGORIES = server

DESCRIPTION = A high performance HTTP server.
define BLURB
  Apache is the world\'s most popular HTTP server, being quite possibly the
  best around in terms of functionality, efficiency, security and speed.
endef

include files/config.mk

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# The PACKAGES variable tell GAR which packages to build
PACKAGES  = CSWapache2
# packages with dashes need this so gar does not thing -devel is a version number
# CATALOGNAME_CSWapache2-devel = apache2_devel

# Descriptions for every package
# SPKG_DESC_CSWapache2 = $(DESCRIPTION)

# Contents for every package.
# You don't define PKGFILES_CSWapache2, it's going to be the default,
# catch-all package.
# PKGFILES_CSWapache2 =

# Standard package bits
DISTFILES += CSWapache2.killproc cswapache2

# Configuration templates
DISTFILES += httpd.conf.CSW
DISTFILES += httpd-mpm.conf.CSW
DISTFILES += httpd-ssl.conf.CSW
DISTFILES += update20to22

REQUIRED_PKGS_CSWapache2        = CSWbdb CSWexpat CSWgdbm CSWiconv
REQUIRED_PKGS_CSWapache2       += CSWlibnet CSWoldaprt CSWosslrt CSWsasl CSWzlib
REQUIRED_PKGS_CSWapache2       += CSWsqlite3rt CSWsqlite3 CSWcswclassutils
REQUIRED_PKGS_CSWapache2       += CSWggettextrt CSWgsed
REQUIRED_PKGS_CSWapache2       += CSWperl

# The SMF support: you don't need to specify cswinitsmf any more.  You need to
# make sure the the /etc/opt/csw/init.d/cswapache file gets installed during
# the post-install stage, and add "INITSMF = /etc/opt/csw/init.d/cswapache" to
# the Makefile.

pre-configure-modulated:
	(cd $(WORKDIR)/$(GARNAME)-$(GARVERSION); ./buildconf)

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
