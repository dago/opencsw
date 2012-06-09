NAME = Crypt-SSLeay
VERSION = 0.58
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = NANIS

DESCRIPTION = OpenSSL glue that provides LWP https support
define BLURB
  This perl module provides support for the https protocol under LWP, so that
  a LWP::UserAgent can make https GET & HEAD & POST requests. Please see
  perldoc LWP for more information on POST requests.
endef

DISTFILES += COPYING

PACKAGES = CSWpm-crypt-ssleay
CATALOGNAME = pm_crypt_ssleay
SPKG_DESC_CSWpm-crypt-ssleay = $(DESCRIPTION)
OBSOLETED_BY_CSWpm-crypt-ssleay = CSWpmcryptssleay
CATALOGNAME_CSWpmcryptssleay = pm_cryptssleay_stub

RUNTIME_DEP_PKGS_CSWpm-crypt-ssleay += CSWlibssl1-0-0

# Documentation only
CHECKPKG_OVERRIDES_CSWpm-crypt-ssleay += file-with-bad-content|/usr/local|root/opt/csw/lib/perl/csw/Crypt/SSLeay.pm
CHECKPKG_OVERRIDES_CSWpm-crypt-ssleay += file-with-bad-content|/usr/local|root/opt/csw/share/man/man3/Crypt::SSLeay.3perl

CONFIGURE_ARGS = --lib=$(prefix)
# unset https_proxy, otherwise 1 test will fail as non root user
CONFIGURE_ENV += https_proxy=
# dont ask stupid questions
CONFIGURE_ENV += PERL_MM_USE_DEFAULT=1

include gar/category.mk
