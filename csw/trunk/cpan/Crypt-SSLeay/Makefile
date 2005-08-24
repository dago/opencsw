GARNAME = Crypt-SSLeay
GARVERSION = 0.51
CATEGORIES = cpan
AUTHOR = CHAMAS

DESCRIPTION = OpenSSL glue that provides LWP https support
define BLURB
  This perl module provides support for the https protocol under LWP, so that
  a LWP::UserAgent can make https GET & HEAD & POST requests. Please see
  perldoc LWP for more information on POST requests.
endef

DISTFILES += CSWpmcryptssleay.gspec CSWpmcryptssleay.depend

DEPENDS += lib/openssl

CONFIGURE_ARGS = --default $(tool_prefix)

include ../category.mk
