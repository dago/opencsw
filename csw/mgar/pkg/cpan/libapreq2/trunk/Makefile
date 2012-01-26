NAME = libapreq2
VERSION = 2.12
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = JOESUF

DESCRIPTION = methods for dealing with Apache request data
define BLURB
  Apache::Request is a subclass of the Apache class, which adds methods for
  parsing GET requests and POST requests where Content-type is one of
  application/x-www-form-urlencoded or multipart/form-data. See the libapreq(3)
  manpage for more details.
endef

PACKAGES = CSWlibapreq2 CSWlibapreq2-devel CSWap2modapreq2 CSWpmapreq2
# individual packages below
CATALOGNAME_CSWlibapreq2 = libapreq2
SPKG_DESC_CSWlibapreq2 = Apache Request Library
PKGFILES_CSWlibapreq2  = /opt/csw/apache2/lib/libapreq2.so.*
RUNTIME_DEP_PKGS_CSWlibapreq2 += CSWiconv
RUNTIME_DEP_PKGS_CSWlibapreq2 += CSWapache2rt
RUNTIME_DEP_PKGS_CSWlibapreq2 += CSWbdb47

CATALOGNAME_CSWlibapreq2-devel = libapreq2_devel
SPKG_DESC_CSWlibapreq2-devel = Apache Request Library development support
PKGFILES_CSWlibapreq2-devel += /opt/csw/apache2/bin/apreq2-config
PKGFILES_CSWlibapreq2-devel += /opt/csw/apache2/include/apreq2/.*
PKGFILES_CSWlibapreq2-devel += /opt/csw/apache2/lib/libapreq2.a
RUNTIME_DEP_PKGS_CSWlibapreq2-devel += CSWlibapreq2

CATALOGNAME_CSWap2modapreq2 = ap2_modapreq2
SPKG_DESC_CSWap2modapreq2 = libapreq2 filter module for Apache 2
PKGFILES_CSWap2modapreq2 = /opt/csw/apache2/libexec/mod_apreq2.so
RUNTIME_DEP_PKGS_CSWap2modapreq2 += CSWiconv
RUNTIME_DEP_PKGS_CSWap2modapreq2 += CSWapache2rt
RUNTIME_DEP_PKGS_CSWap2modapreq2 += CSWlibapreq2

CATALOGNAME_CSWpmapreq2 = pm_apreq2
SPKG_DESC_CSWpmapreq2 = libapreq2 Perl language bindings
PKGFILES_CSWpmapreq2 += /opt/csw/lib/perl/.*
PKGFILES_CSWpmapreq2 += /opt/csw/share/man/.*
RUNTIME_DEP_PKGS_CSWpmapreq2 += CSWap2modperl
RUNTIME_DEP_PKGS_CSWpmapreq2 += CSWpmapachetst
RUNTIME_DEP_PKGS_CSWpmapreq2 += CSWpmextutxsbld

# Ensure args are requestrecs
PATCHFILES += requestrec.diff

# BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS) CSWbdb47-devel
AP2_ROOT = $(prefix)/apache2

CONFIGURE_ARGS  = --enable-perl-glue
CONFIGURE_ARGS += --with-perl=$(bindir)/perl
CONFIGURE_ARGS += --with-apache2-apxs=$(AP2_ROOT)/sbin/apxs
CONFIGURE_ARGS += --with-apr-config=$(AP2_ROOT)/bin/apr-config
CONFIGURE_ARGS += --with-apu-config=$(AP2_ROOT)/bin/apu-config
CONFIGURE_ARGS += --with-expat=$(prefix)
CONFIGURE_ARGS += --with-mm-opts="INSTALLDIRS=vendor"

PERL_CONFIGURE_ARGS =

FIXCONFIG_DIRS += $(DESTDIR)$(prefix)/apache2/lib
STRIP_DIRS   += $(DESTDIR)$(prefix)/apache2/libexec

EXTRA_INC = $(prefix)/bdb47/include
EXTRA_LIB = $(prefix)/bdb47/lib $(prefix)/apache2/lib

SKIPTEST = 1
# apache2 is not yet libtool free
STRIP_LIBTOOL = 1

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
