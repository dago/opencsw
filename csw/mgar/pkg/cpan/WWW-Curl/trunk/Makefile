GARNAME = WWW-Curl
GARVERSION = 4.05
CATEGORIES = cpan
AUTHOR = SZBALINT

DESCRIPTION = Perl extension interface for libcurl
define BLURB
  The perl module WWW::Curl provides an interface to the cURL library "libcurl".
endef

DISTFILES += $(call admfiles,CSWpmwwwcurl,)

REQUIRED_PKGS = CSWcurlrt CSWlibidn CSWoldaprt CSWosslrt CSWzlib

EXTRA_MERGE_EXCLUDE_FILES = .*~ .*perllocal\.pod

#CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS = 

TEST_SCRIPTS = 

include gar/category.mk
