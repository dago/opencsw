GARNAME = Crypt-DES
GARVERSION = 2.05
CATEGORIES = cpan
AUTHOR = DPARIS

DESCRIPTION = Perl DES encryption module
define BLURB
  The module implements the Crypt::CBC interface, which has the following
  methods
endef

DISTFILES += CSWpmcryptdes.gspec

# Fix name collision with des_*() functions
PATCHFILES = des_workaround.s9.diff

include ../category.mk
