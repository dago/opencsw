GARNAME = Crypt-IDEA
GARVERSION = 1.04
CATEGORIES = cpan
AUTHOR = DPARIS

DESCRIPTION = Perl interface to IDEA block cipher
define BLURB
  This perl extension is an implementation of the IDEA block cipher algorithm.
endef

DISTFILES = $(call admfiles,CSWpmcryptidea,depend prototype)

# Define u_int16_t in terms of a type Solaris knows about
PATCHFILES += typedef.diff

# 1.04 was supposed to fix byte order, but the fix only worked
# for 32-bit systems.
PATCHFILES += byteorder.diff

include ../category.mk
