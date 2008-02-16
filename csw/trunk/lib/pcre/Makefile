GARNAME = pcre
GARVERSION = 7.6
CATEGORIES = lib

DESCRIPTION = Perl-compatible regular expression library
define BLURB
  The PCRE library is a set of functions that implement regular
  expression pattern matching using the same syntax and semantics
  as Perl 5. PCRE has its own native API, as well as a set of
  wrapper functions that correspond to the POSIX regular expression API.
endef

MASTER_SITES = ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWpcre)

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include ../category.mk
