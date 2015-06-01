# $Id: Makefile 18185 2012-06-01 02:30:46Z bdwalton $

NAME = httpd
VERSION = 2.4.12
GARTYPE = v2

PACKAGING_PLATFORMS = solaris10-i386 solaris10-sparc

DESCRIPTION = A high performance HTTP server.
define BLURB
  Apache is the world\'s most popular HTTP server, being quite possibly the
  best around in terms of functionality, efficiency, security and speed.
endef

MASTER_SITES  = http://www.eu.apache.org/dist/httpd/
DISTFILES += $(DISTNAME).tar.gz
DISTFILES += cswapache24
EXPANDVARS += cswapache24

PATCHFILES += 0002-Switch-usr-local-for-opt-csw-in-default-cgi-path.patch
PATCHFILES += 0003-fix-43561-apxs.patch

#PATCHFILES += 0001-Add-an-OpenCSW-option-to-config.layout.patch
DISTFILES += 0001-Add-an-OpenCSW-option-to-config.layout.patch

EXPANDVARS += 0001-Add-an-OpenCSW-option-to-config.layout.patch

# SKIP_MODULATIONS += isa-sparcv8plus

VENDOR_URL = http://httpd.apache.org/
LICENSE = LICENSE

GARCOMPILER = SOS12U4

PACKAGES = CSWapache24
SPKG_DESC_CSWapache24 = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWapache24 += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWapache24 += CSWlibaprutil1-0
RUNTIME_DEP_PKGS_CSWapache24 += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWapache24 += CSWlibz1
RUNTIME_DEP_PKGS_CSWapache24 += CSWlibpcre1
RUNTIME_DEP_PKGS_CSWapache24 += CSWliblua5-2
RUNTIME_DEP_PKGS_CSWapache24 += CSWlibapr1-0
RUNTIME_DEP_PKGS_CSWapache24 += CSWlibldap2-4-2
RUNTIME_DEP_PKGS_CSWapache24 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWapache24 += CSWopenldap
RUNTIME_DEP_PKGS_CSWapache24 += CSWlighttpd
EXTRA_MERGE_DIRS_isa-extra += /etc/opt/csw/64/apache2/extra

# This is because /opt/csw/sbin/sparcv9 is missing, most certainly an checkpkg issue
# CHECKPKG_OVERRIDES_CSWapache24 += missing-dependency|CSWbonnie++|or|CSWcollectd|or|CSWleafnode|or|CSWlighttpd|or|CSWlogrotate|or|CSWopenldap|or|CSWproftpd|or|CSWsysstat|or|CSWzabbix-agent|or|CSWzabbix-server

PACKAGES += CSWapache24-manual
ARCHALL_CSWapache24-manual = 1
SPKG_DESC_CSWapache24-manual = The Apache 2.4 Manual
PKGFILES_CSWapache24-manual = /var/opt/csw/apache2/manual.*
RUNTIME_DEPS_CSWapache24-manual = CSWapache24
CHECKPKG_OVERRIDES_CSWapache24-manual += file-with-bad-content

PACKAGES += CSWapache24-dev
SPKG_DESC_CSWapache24-dev = The Apache 2.4 Development Files
PKGFILES_CSWapache24-dev = $(PKGFILES_DEVEL)

# This is a fallback
CHECKPKG_OVERRIDES_CSWapache24-dev += file-with-bad-content|/usr/local|root/opt/csw/include/apache2/httpd.h

BUILD_DEP_PKGS += CSWlibaprutil-dev

INITSMF = /etc/opt/csw/init.d/cswapache24

PRESERVECONF += $(sysconfdir)/apache2/envvars
PRESERVECONF += $(sysconfdir)/apache2/mime.types
PRESERVECONF += $(sysconfdir)/apache2/extra/httpd-manual.conf
PRESERVECONF += $(sysconfdir)/apache2/extra/httpd-userdir.conf
PRESERVECONF += $(sysconfdir)/apache2/extra/httpd-languages.conf
PRESERVECONF += $(sysconfdir)/apache2/extra/httpd-vhosts.conf
PRESERVECONF += $(sysconfdir)/apache2/extra/httpd-info.conf
PRESERVECONF += $(sysconfdir)/apache2/extra/proxy-html.conf
PRESERVECONF += $(sysconfdir)/apache2/extra/httpd-dav.conf
PRESERVECONF += $(sysconfdir)/apache2/extra/httpd-multilang-errordoc.conf
PRESERVECONF += $(sysconfdir)/apache2/extra/httpd-autoindex.conf
PRESERVECONF += $(sysconfdir)/apache2/extra/httpd-mpm.conf
PRESERVECONF += $(sysconfdir)/apache2/extra/httpd-default.conf
PRESERVECONF += $(sysconfdir)/apache2/extra/httpd-ssl.conf
PRESERVECONF += $(sysconfdir)/apache2/envvars-std
PRESERVECONF += $(sysconfdir)/apache2/magic
PRESERVECONF += $(sysconfdir)/apache2/httpd.conf

# These two are link destinations and put in place via PRESERVECONF
CHECKPKG_OVERRIDES_CSWapache24 += file-needed-but-no-package-satisfies-it|/etc/opt/csw/apache2/envvars|CSWapache24|contains|symlink|/opt/csw/sbin/envvars|which|needs|the|target|file:|/etc/opt/csw/apache2/envvars
CHECKPKG_OVERRIDES_CSWapache24 += file-needed-but-no-package-satisfies-it|/etc/opt/csw/apache2/envvars-std|CSWapache24|contains|symlink|/opt/csw/sbin/envvars-std|which|needs|the|target|file:|/etc/opt/csw/apache2/envvars-std
CHECKPKG_OVERRIDES_CSWapache24 += file-needed-but-no-package-satisfies-it|/etc/opt/csw/apache2/envvars|CSWapache24|contains|symlink|/opt/csw/sbin/sparcv9/envvars|which|needs|the|target|file:|/etc/opt/csw/apache2/envvars
CHECKPKG_OVERRIDES_CSWapache24 += file-needed-but-no-package-satisfies-it|/etc/opt/csw/apache2/envvars-std|CSWapache24|contains|symlink|/opt/csw/sbin/sparcv9/envvars-std|which|needs|the|target|file:|/etc/opt/csw/apache2/envvars-std
CHECKPKG_OVERRIDES_CSWapache24 += file-needed-but-no-package-satisfies-it|/etc/opt/csw/apache2/envvars|CSWapache24|contains|symlink|/opt/csw/sbin/amd64/envvars|which|needs|the|target|file:|/etc/opt/csw/apache2/envvars
CHECKPKG_OVERRIDES_CSWapache24 += file-needed-but-no-package-satisfies-it|/etc/opt/csw/apache2/envvars-std|CSWapache24|contains|symlink|/opt/csw/sbin/amd64/envvars-std|which|needs|the|target|file:|/etc/opt/csw/apache2/envvars-std

SSLCERT = /etc/opt/csw/apache2/server

# We need this to get bdb48/lib into the runpath
EXTRA_LIB = $(prefix)/bdb48/lib

BUILD64 = 1

# ifeq ($(MEMORYMODEL),64)
# 	MODULE_CONF=$(DESTDIR)$(sysconfdir)/64/apache2/extra/module.load
# else
# 	MODULE_CONF=$(DESTDIR)$(sysconfdir)/apache2/extra/module.load
# endif
MODULE_CONF=$(DESTDIR)$(sysconfdir)/$(MM_LIBDIR)/apache2/extra/modules.load

# Build Configuration
CONFIGURE_ARGS += --with-apr=$(prefix)
CONFIGURE_ARGS += --with-pcre=$(bindir)/pcre-config
CONFIGURE_ARGS += --with-libxml2=$(includedir)/libxml2
CONFIGURE_ARGS-32 += --with-lua=$(prefix)
#CONFIGURE_ARGS-64 += --without-lua
CONFIGURE_ARGS += --enable-mpms-shared=all
# CONFIGURE_ARGS += --with-mpm=prefork
CONFIGURE_ARGS += --enable-layout=OpenCSW
CONFIGURE_ARGS += --enable-mods-shared=all
CONFIGURE_ARGS += --enable-cgi
CONFIGURE_ARGS += --enable-privileges
CONFIGURE_ARGS += --enable-vhost-alias
#CONFIGURE_ARGS += --with-ssl=$(prefix)
CONFIGURE_ARGS += --with-ssl
# As requested in https://www.opencsw.org/mantis/view.php?id=5152
CONFIGURE_ARGS += --enable-proxy-html
CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(MEMORYMODEL))

EXTRA_CFLAGS += -DSSL_EXPERIMENTAL -DSSL_ENGINE

# Fixup target variables
APACHE_ROOT   = $(DESTDIR)$(prefix)
LIBTOOL_LADIR = $(APACHE_ROOT)/lib
STRIP_DIRS    = $(APACHE_ROOT)/sbin $(APACHE_ROOT)/libexec

TEST_TARGET = test

include gar/category.mk

# We need this special construct because the patch should have expandvars
post-patch:
	cd $(WORKSRC) && gpatch -p1 <$(abspath $(WORKDIR)/0001-Add-an-OpenCSW-option-to-config.layout.patch)
	@$(MAKECOOKIE)

post-install:
	(cd $(DESTDIR)$(sbindir); \
	   for f in envvars*; do \
		mv $$f $(DESTDIR)$(sysconfdir)/apache2/; \
		ln -s $(sysconfdir)/apache2/$$f $$f; \
	   done )
	rm -rf $(DESTDIR)$(sysconfdir)/apache2/original
	perl -pi -e 's|/usr/local/apache2|/etc/opt/csw/apache2|g' $(DESTDIR)$(sysconfdir)/apache2/httpd.conf
	perl -pi -e 's|usr/local/etc/apache|etc/opt/csw/apache2|g' $(DESTDIR)$(mandir)/man1/*
	perl -pi -e 's|/usr/local/apache2|/etc/opt/csw/apache2|g' $(DESTDIR)$(mandir)/man8/*
	ginstall -d $(dir $(MODULE_CONF))
	(cd $(DESTDIR)$(sysconfdir)/apache2 && \
		grep LoadModule httpd.conf > $(MODULE_CONF) && \
		gsed -e '/^#LoadModule/d' -i httpd.conf; \
		gsed -e '/^LoadModule/d' -i httpd.conf; \
		gsed -e '/# LoadModule/a <IfDefine 64bit>\n\Include $(sysconfdir)/64/apache2/extra/modules.load\n\</IfDefine>\n\<IfDefine !64bit>\n\Include $(sysconfdir)/apache2/extra/modules.load\n\</IfDefine>' -i httpd.conf; \
	)
	ginstall -D -m 0755 $(WORKDIR)/cswapache24 $(DESTDIR)/etc/opt/csw/init.d/cswapache24
	gsed -e '/APACHECTL=/s/sbin/sbin\$${MM}/' -i $(DESTDIR)/etc/opt/csw/init.d/cswapache24
	echo "# create server.(crt|csr)/server.key" > $(DESTDIR)$(sysconfdir)/apache2/server
	@$(MAKECOOKIE)
