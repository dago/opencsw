NAME = Crypt-ECB
VERSION = 1.45
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = APPEL

DESCRIPTION = Perl ECB Encryption Module
define BLURB
  This module is a Perl-only implementation of the ECB mode. In combination with
  a block cipher such as DES, IDEA or Blowfish, you can encrypt and decrypt
  messages of arbitrarily long length. Though for security reasons other modes
  than ECB such as CBC should be preferred. See textbooks on cryptography if you
  want to know why.

  The functionality of the module can be accessed via OO methods or via standard
  function calls. Remember that some crypting module like for example Blowfish
  has to be installed. The syntax follows that of Crypt::CBC.
endef

PACKAGES = CSWpm-crypt-ecb
CATALOGNAME_CSWpm-crypt-ecb = pm_crypt_ecb

PACKAGING_PLATFORMS +=  solaris10-sparc solaris10-i386

ARCHALL = 1

include gar/category.mk
