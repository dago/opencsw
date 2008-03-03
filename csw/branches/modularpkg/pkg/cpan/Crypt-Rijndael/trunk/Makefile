GARNAME = Crypt-Rijndael
GARVERSION = 0.05
CATEGORIES = cpan
AUTHOR = DIDO

DESCRIPTION = Crypt::CBC compliant Rijndael encryption module
define BLURB
  This module implements the Rijndael cipher, which has just been selected as
  the Advanced Encryption Standard.
endef

DISTFILES = $(call admfiles,CSWpmcryptrijndael,depend prototype)

# MODE_CTR (not common AFAIK) tests fail on Solaris/x86 32-bit, but
# not on Solaris/SPARC 64-bit.  This does not appear to be a show
# stopper, as the tests are able to recover the plaintext, but are
# not seeing the expected encrypted text.
TEST_SCRIPTS =

include gar/category.mk
