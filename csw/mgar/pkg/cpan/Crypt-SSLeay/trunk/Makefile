NAME = Crypt-SSLeay
VERSION = 0.57
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DLAND

DESCRIPTION = OpenSSL glue that provides LWP https support
define BLURB
  This perl module provides support for the https protocol under LWP, so that
  a LWP::UserAgent can make https GET & HEAD & POST requests. Please see
  perldoc LWP for more information on POST requests.
endef

PACKAGES = CSWpmcryptssleay
CATALOGNAME = pm_cryptssleay

RUNTIME_DEP_PKGS     = CSWosslrt
BUILD_DEP_PKGS = CSWosslrt CSWpmmimebase64

CONFIGURE_ARGS = --lib=$(prefix)
# unset https_proxy, otherwise 1 test will fail as non root user
CONFIGURE_ENV += https_proxy=
# dont ask stupid questions
CONFIGURE_ENV += PERL_MM_USE_DEFAULT=1

include gar/category.mk
