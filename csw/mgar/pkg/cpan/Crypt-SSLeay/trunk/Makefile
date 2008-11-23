GARNAME = Crypt-SSLeay
GARVERSION = 0.54
CATEGORIES = cpan
AUTHOR = DLAND

DESCRIPTION = OpenSSL glue that provides LWP https support
define BLURB
  This perl module provides support for the https protocol under LWP, so that
  a LWP::UserAgent can make https GET & HEAD & POST requests. Please see
  perldoc LWP for more information on POST requests.
endef

DISTFILES += $(call admfiles,CSWpmcryptssleay,depend prototype)

# Don't ask about networked tests -- the answer is no.
PATCHFILES += noask.diff

#DEPENDS += lib/openssl

CONFIGURE_ARGS = --lib=$(prefix)

include gar/category.mk
