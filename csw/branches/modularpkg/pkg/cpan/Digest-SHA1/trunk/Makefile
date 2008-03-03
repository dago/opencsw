GARNAME = Digest-SHA1
GARVERSION = 2.11
CATEGORIES = cpan
AUTHOR = GAAS

DESCRIPTION = interface to the SHA-1 Algorithm
define BLURB
  The Digest::SHA1 module allows you to use the NIST SHA-1 message digest
  algorithm from within Perl programs. The algorithm takes as input a message
  of arbitrary length and produces as output a 160-bit "fingerprint" or
  "message digest" of the input.
endef

DISTFILES = $(call admfiles,CSWpmdigestsha1,depend prototype)

# Missing alias for reset -> new
PATCHFILES = reset.diff

include gar/category.mk
