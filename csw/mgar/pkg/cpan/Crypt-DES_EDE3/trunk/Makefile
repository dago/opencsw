NAME = Crypt-DES_EDE3
VERSION = 0.01
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = BTROTT

DESCRIPTION = Triple-DES EDE encryption/decryption
define BLURB
  Crypt::DES_EDE3 implements DES-EDE3 encryption. This is triple-DES
  encryption where an encrypt operation is encrypt-decrypt-encrypt, and
  decrypt is decrypt-encrypt-decrypt. This implementation uses Crypt::DES to
  do its dirty DES work, and simply provides a wrapper around that module:
  setting up the individual DES ciphers, initializing the keys, and performing
  the encryption/decryption steps.
endef


CATALOGNAME     = pm_crypt_des_ede3
PACKAGES	= CSWpm-crypt-des-ede3

ARCHALL_CSWpm-crypt-des-ede3 = 1

LICENSE = README

RUNTIME_PKG_DEPS = CSWpmcryptdes

include gar/category.mk
