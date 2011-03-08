NAME = WWW-Curl
VERSION = 4.15
CATEGORIES = cpan
AUTHOR = SZBALINT

DESCRIPTION = Perl extension interface for libcurl
define BLURB
  The perl module WWW::Curl provides an interface to the cURL library libcurl.
endef

DISTFILES += COPYING

PACKAGES = CSWpm-www-curl
CATALOGNAME = pm_www_curl
SPKG_DESC_CSWpm-www-curl = $(DESCRIPTION)
OBSOLETES_CSWpm-www-curl = CSWpmwwwcurl
CATALOGNAME_CSWpmwwwcurl = pm_wwwcurl

RUNTIME_DEP_PKGS += CSWcurlrt
RUNTIME_DEP_PKGS += CSWlibidn
RUNTIME_DEP_PKGS += CSWoldaprt
RUNTIME_DEP_PKGS += CSWosslrt
RUNTIME_DEP_PKGS += CSWzlib
RUNTIME_DEP_PKGS += CSWlibcares

CONFIGURE_ARGS = 

# Note that 08ssl.t fails (probably due to connection issues)
#TEST_SCRIPTS = 

include gar/category.mk
