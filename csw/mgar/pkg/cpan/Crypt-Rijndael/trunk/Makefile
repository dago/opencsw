NAME = Crypt-Rijndael
VERSION = 1.09
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = BDFOY

DESCRIPTION = Crypt::CBC compliant Rijndael encryption module
define BLURB
  This module implements the Rijndael cipher, which has just been selected as
  the Advanced Encryption Standard.
endef

PACKAGES     = CSWpmcryptrijndael
CATALOGNAME  = pm_cryptrijndael

# MODE_CTR (not common AFAIK) tests fail on Solaris/x86 32-bit, but
# not on Solaris/SPARC 64-bit.  This does not appear to be a show
# stopper, as the tests are able to recover the plaintext, but are
# not seeing the expected encrypted text.
# TEST_SCRIPTS =

include gar/category.mk
