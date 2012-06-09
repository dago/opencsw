NAME = Crypt-OpenSSL-Bignum
VERSION = 0.04
CATEGORIES = cpan
GARTYPE = v2
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

LICENSE = LICENSE

PACKAGES = CSWpm-crypt-openssl-bignum
CATALOGNAME = pm_crypt_openssl_bignum
SPKG_DESC_CSWpm-crypt-openssl-bignum = $(DESCRIPTION)
OBSOLETED_BY_CSWpm-crypt-openssl-bignum = CSWpmcryptosslbignum
CATALOGNAME_CSWpmcryptosslbignum = pm_crypt_openssl_bignum_stub

RUNTIME_DEP_PKGS_CSWpm-crypt-openssl-bignum += CSWlibssl1-0-0

include gar/category.mk
