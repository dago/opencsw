# $Id: Makefile 18185 2012-06-01 02:30:46Z bdwalton $

NAME = httpd
VERSION = 2.4.3
CATEGORIES = server
GARTYPE = v2

PACKAGING_PLATFORMS = solaris10-i386 solaris10-sparc

DESCRIPTION = A high performance HTTP server.
define BLURB
  Apache is the world\'s most popular HTTP server, being quite possibly the
  best around in terms of functionality, efficiency, security and speed.
endef

# Source location
MASTER_SITES  = http://www.eu.apache.org/dist/httpd/

# work around dumb checkpkg not recognizing the license file ...
LICENSE = LICENSE

# Visitor information
SPKG_SOURCEURL = http://httpd.apache.org/

DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += cswapache24

PACKAGES = CSWapache24
SPKG_DESC_CSWapache24 = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWapache24 += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWapache24 += CSWlibaprutil1-0
RUNTIME_DEP_PKGS_CSWapache24 += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWapache24 += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWapache24 += CSWlibz1
RUNTIME_DEP_PKGS_CSWapache24 += CSWlibpcre1
RUNTIME_DEP_PKGS_CSWapache24 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWapache24 += CSWbdb48
RUNTIME_DEP_PKGS_CSWapache24 += CSWliblua5-2
RUNTIME_DEP_PKGS_CSWapache24 += CSWlibapr1-0
RUNTIME_DEP_PKGS_CSWapache24 += CSWlibldap2-4-2

PACKAGES += CSWapache24-manual
ARCHALL_CSWapache24-manual = 1
SPKG_DESC_CSWapache24-manual = The Apache 2.4 Manual
PKGFILES_CSWapache24-manual = /var/opt/csw/apache24/manual.*
RUNTIME_DEPS_CSWapache24-manual = CSWapache24
CHECKPKG_OVERRIDES_CSWapache24-manual += file-with-bad-content

PACKAGES += CSWapache24-dev
SPKG_DESC_CSWapache24-dev = The Apache 2.4 Development Files
PKGFILES_CSWapache24-dev = $(PKGFILES_DEVEL)

PATCHFILES += 0001-Add-an-OpenCSW-option-to-config.layout.patch
PATCHFILES += 0002-Switch-usr-local-for-opt-csw-in-default-cgi-path.patch

BUILD_DEP_PKGS += CSWlibaprutil-dev

INITSMF = /etc/opt/csw/init.d/cswapache24

PRESERVECONF += $(sysconfdir)/apache24/envvars
PRESERVECONF += $(sysconfdir)/apache24/mime.types
PRESERVECONF += $(sysconfdir)/apache24/extra/httpd-manual.conf
PRESERVECONF += $(sysconfdir)/apache24/extra/httpd-userdir.conf
PRESERVECONF += $(sysconfdir)/apache24/extra/httpd-languages.conf
PRESERVECONF += $(sysconfdir)/apache24/extra/httpd-vhosts.conf
PRESERVECONF += $(sysconfdir)/apache24/extra/httpd-info.conf
PRESERVECONF += $(sysconfdir)/apache24/extra/proxy-html.conf
PRESERVECONF += $(sysconfdir)/apache24/extra/httpd-dav.conf
PRESERVECONF += $(sysconfdir)/apache24/extra/httpd-multilang-errordoc.conf
PRESERVECONF += $(sysconfdir)/apache24/extra/httpd-autoindex.conf
PRESERVECONF += $(sysconfdir)/apache24/extra/httpd-mpm.conf
PRESERVECONF += $(sysconfdir)/apache24/extra/httpd-default.conf
PRESERVECONF += $(sysconfdir)/apache24/extra/httpd-ssl.conf
PRESERVECONF += $(sysconfdir)/apache24/envvars-std
PRESERVECONF += $(sysconfdir)/apache24/magic
PRESERVECONF += $(sysconfdir)/apache24/httpd.conf

SSLCERT = /etc/opt/csw/apache24/server

# We need this to get bdb48/lib into the runpath
EXTRA_LIB = $(prefix)/bdb48/lib

# Build Configuration
CONFIGURE_ARGS  = --with-apr=$(prefix)
CONFIGURE_ARGS += --with-pcre=$(prefix)
CONFIGURE_ARGS += --with-libxml2=$(includedir)/libxml2
CONFIGURE_ARGS += --with-lua=$(prefix)
CONFIGURE_ARGS += --enable-mpms-shared=all
CONFIGURE_ARGS += --enable-layout=OpenCSW
CONFIGURE_ARGS += --enable-mods-shared=all
CONFIGURE_ARGS += --enable-privileges
CONFIGURE_ARGS += --enable-vhost-alias
CONFIGURE_ARGS += --with-ssl=$(prefix)

# Fixup target variables
APACHE_ROOT   = $(DESTDIR)$(prefix)
LIBTOOL_LADIR = $(APACHE_ROOT)/lib
STRIP_DIRS    = $(APACHE_ROOT)/sbin $(APACHE_ROOT)/libexec

TEST_TARGET = test

include gar/category.mk

CFLAGS := -DSSL_EXPERIMENTAL -DSSL_ENGINE $(CFLAGS)

post-merge:
	@(cd $(PKGROOT)/$(sysconfdir)/apache24; \
		rm -rf original; \
		perl -pi -e 's|/usr/local/apache2|/etc/opt/csw/apache24|g' httpd.conf.CSW ; \
	  cd $(PKGROOT)/$(mandir); \
		perl -pi -e 's|usr/local/etc/apache|etc/opt/csw/apache24|g' man1/*; \
		perl -pi -e 's|/usr/local/apache2|/etc/opt/csw/apache2|g' man8/* )
	@( ginstall -d $(PKGROOT)/etc/opt/csw/init.d; \
	    ginstall $(WORKSRC_FIRSTMOD)/../cswapache24 $(PKGROOT)/etc/opt/csw/init.d )
	@(cd $(PKGROOT)/$(sbindir); \
	   for f in envvars*; do \
		mv $$f $(PKGROOT)/$(sysconfdir)/apache24/; \
		ln -s $(sysconfdir)/apache24/$$f $$f; \
	   done )

	@(cd $(PKGROOT)/$(sysconfdir)/apache24; \
		echo "# create server.(crt|csr)/server.key" > server )
	@$(MAKECOOKIE)
