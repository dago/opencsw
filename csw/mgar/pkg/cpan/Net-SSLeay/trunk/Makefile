NAME = Net-SSLeay
VERSION = 1.48
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = MIKEM

DESCRIPTION = Perl extension for using OpenSSL
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE_TEXT = This module is licensed under the unknown license

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

PACKAGES += CSWpm-net-ssleay
CATALOGNAME_CSWpm-net-ssleay = pm_net_ssleay
SPKG_DESC_CSWpm-net-ssleay = Perl extension for using OpenSSL
RUNTIME_DEP_PKGS_CSWpm-net-ssleay += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWpm-net-ssleay += CSWlibz1
OBSOLETED_BY_CSWpm-net-ssleay += CSWpmnetssleay
CATALOGNAME_CSWpmnetssleay = pm_netssleay_stub

# These are just docs
CHECKPKG_OVERRIDES_CSWpm-net-ssleay += file-with-bad-content|/usr/local|root/opt/csw/lib/perl/csw/Net/SSLeay.pod
CHECKPKG_OVERRIDES_CSWpm-net-ssleay += file-with-bad-content|/usr/local|root/opt/csw/share/man/man3/Net::SSLeay.3perl

CONFIGURE_ENV = OPENSSL_PREFIX=$(prefix) AUTOMATED_TESTING=1 PERL_MM_USE_DEFAULT=1

include gar/category.mk
