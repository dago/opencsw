GARNAME = Crypt-SSLeay
GARVERSION = 0.57
CATEGORIES = cpan
AUTHOR = DLAND

DESCRIPTION = OpenSSL glue that provides LWP https support
define BLURB
  This perl module provides support for the https protocol under LWP, so that
  a LWP::UserAgent can make https GET & HEAD & POST requests. Please see
  perldoc LWP for more information on POST requests.
endef

# Don't ask about networked tests -- the answer is no.
PATCHFILES += noask.diff

PACKAGES = CSWpmcryptssleay
CATALOGNAME = pm_cryptssleay

REQUIRED_PKGS     = CSWosslrt
PREREQUISITE_PKGS = CSWosslrt

CONFIGURE_ARGS = --lib=$(prefix)

include gar/category.mk
