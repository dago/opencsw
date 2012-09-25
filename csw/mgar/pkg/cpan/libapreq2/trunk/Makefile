NAME = libapreq2
VERSION = 2.13
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = JOESUF

DESCRIPTION = Methods for dealing with Apache request data
define BLURB
  Apache::Request is a subclass of the Apache class, which adds methods for
  parsing GET requests and POST requests where Content-type is one of
  application/x-www-form-urlencoded or multipart/form-data. See the libapreq(3)
  manpage for more details.
endef

LICENSE = LICENSE

PACKAGES += CSWlibapreq2-3
SPKG_DESC_CSWlibapreq2-3 = Apache Request Library
PKGFILES_CSWlibapreq2-3 += $(call pkgfiles_lib,libapreq2.so.3)
RUNTIME_DEP_PKGS_CSWlibapreq2-3 += CSWbdb48
RUNTIME_DEP_PKGS_CSWlibapreq2-3 += CSWlibapr1-0
RUNTIME_DEP_PKGS_CSWlibapreq2-3 += CSWlibaprutil1-0
OBSOLETED_BY_CSWlibapreq2-3 += CSWlibapreq2

PACKAGES += CSWlibapreq2-dev
SPKG_DESC_CSWlibapreq2-dev = Apache Request Library development support for libapreq2.so.3
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibapreq2-dev += CSWlibapreq2-3
RUNTIME_DEP_PKGS_CSWlibapreq2-dev += CSWapache2
OBSOLETED_BY_CSWlibapreq2-dev += CSWlibapreq2-devel

# This is just for the path
CHECKPKG_OVERRIDES_CSWlibapreq2-dev += file-with-bad-content|/usr/local|root/opt/csw/bin/apreq2-config

PACKAGES += CSWap2modapreq2
CATALOGNAME_CSWap2modapreq2 = ap2_modapreq2
# Keep the package name for now until all apache naming has been sanitized
CHECKPKG_OVERRIDES_CSWap2modapreq2 += catalogname-does-not-match-pkgname|pkgname=CSWap2modapreq2|catalogname=ap2_modapreq2|expected-catalogname=ap2modapreq2
SPKG_DESC_CSWap2modapreq2 = Apache 2 filter module libapreq2
PKGFILES_CSWap2modapreq2 += /opt/csw/apache2/libexec/mod_apreq2.so
RUNTIME_DEP_PKGS_CSWap2modapreq2 += CSWlibapreq2-3
RUNTIME_DEP_PKGS_CSWap2modapreq2 += CSWlibaprutil1-0
RUNTIME_DEP_PKGS_CSWap2modapreq2 += CSWlibapr1-0
RUNTIME_DEP_PKGS_CSWap2modapreq2 += CSWapache2

PACKAGES += CSWpm-apr-request2
SPKG_DESC_CSWpm-apr-request2 = libapreq2 Perl language bindings
PKGFILES_CSWpm-apr-request2 += /opt/csw/lib/perl/.*
PKGFILES_CSWpm-apr-request2 += /opt/csw/share/man/.*
RUNTIME_DEP_PKGS_CSWpm-apr-request2 += CSWap2modperl
# This is part of CSWap2modperl
# RUNTIME_DEP_PKGS_CSWpm-apr-request2 += CSWpmapachetst
RUNTIME_DEP_PKGS_CSWpm-apr-request2 += CSWpm-extutils-xsbuilder
OBSOLETED_BY_CSWpm-apr-request2 += CSWpmapreq2
CATALOGNAME_CSWpmapreq2 = pm_apreq2_stub

# Ensure args are requestrecs
PATCHFILES += requestrec.diff

# BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS) CSWbdb48-devel
AP2_ROOT = $(prefix)/apache2

CONFIGURE_ARGS  = --enable-perl-glue
CONFIGURE_ARGS += --with-perl=$(bindir)/perl
CONFIGURE_ARGS += --with-apache2-apxs=$(AP2_ROOT)/sbin/apxs
CONFIGURE_ARGS += --with-apr-config=$(bindir)/apr-1-config
CONFIGURE_ARGS += --with-apu-config=$(bindir)/apu-1-config
CONFIGURE_ARGS += --with-expat=$(prefix)
CONFIGURE_ARGS += --with-mm-opts="INSTALLDIRS=vendor"

PERL_CONFIGURE_ARGS =

FIXCONFIG_DIRS += $(DESTDIR)$(prefix)/apache2/lib
STRIP_DIRS   += $(DESTDIR)$(prefix)/apache2/libexec

EXTRA_INC = $(prefix)/bdb48/include
EXTRA_LIB = $(prefix)/bdb48/lib $(prefix)/apache2/lib

SKIPTEST ?= 1
# apache2 is not yet libtool free
# STRIP_LIBTOOL = 1

include gar/category.mk

pre-package: test fix-cfgscript

fix-cfgscript:
	perl -i -plne 's/(APREQ_(?:SOURCE|BUILD)_DIR=).*$$/\1""/' \
		$(DESTDIR)$(prefix)/apache2/bin/apreq2-config

# since apache2 is not yet free of libtool, we need to remove
# the BUILT_SOURCES targets, which in fact are libapr-1.la and
# libaprutil-1.la. Once apache is libtool free we can remove this.
post-configure-modulated:
	gsed -i'' 's/^BUILT_SOURCES.*//' $(WORKSRC)/library/Makefile
