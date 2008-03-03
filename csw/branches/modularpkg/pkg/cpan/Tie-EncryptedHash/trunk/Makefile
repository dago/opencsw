GARNAME = Tie-EncryptedHash
GARVERSION = 1.21
CATEGORIES = cpan
AUTHOR = VIPUL

DESCRIPTION = hashes (and objects based on hashes) with encrypting fields.
define BLURB
  Tie::EncryptedHash augments Perl hash semantics to build secure, encrypting
  containers of data. Tie::EncryptedHash introduces special hash fields that
  are coupled with encrypt/decrypt routines to encrypt assignments at STORE()
  and decrypt retrievals at FETCH(). By design, encrypting fields are
  associated with keys that begin in single underscore. The remaining keyspace
  is used for accessing normal hash fields, which are retained without
  modification.
endef

DISTFILES += CSWpmtiecrypthash.gspec CSWpmtiecrypthash.depend

DEPENDS += cpan/Crypt-DES cpan/Crypt-Blowfish

include gar/category.mk
