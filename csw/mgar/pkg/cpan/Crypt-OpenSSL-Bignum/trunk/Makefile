GARNAME = Crypt-OpenSSL-Bignum
GARVERSION = 0.04
CATEGORIES = cpan
AUTHOR = IROBERTS

DESCRIPTION = OpenSSL's multiprecision integer arithmetic
define BLURB
  Crypt::OpenSSL::Bignum provides access to OpenSSL multiprecision
  integer arithmetic libraries. Presently, many though not all of the
  arithmetic operations that OpenSSL provides are exposed to perl. In
  addition, this module can be used to provide access to bignum values
  produced by other OpenSSL modules, such as key parameters from
  Crypt::OpenSSL::RSA.
endef

DISTFILES += $(call admfiles,CSWpmcryptosslbignum,)

REQUIRED_PKGS = CSWosslrt

include gar/category.mk
