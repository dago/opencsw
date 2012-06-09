NAME = WWW-Curl
VERSION = 4.15
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = SZBALINT

DESCRIPTION = Perl extension interface for libcurl
define BLURB
  The perl module WWW::Curl provides an interface to the cURL library libcurl.
endef

DISTFILES += COPYING

PACKAGES = CSWpm-www-curl
CATALOGNAME = pm_www_curl
SPKG_DESC_CSWpm-www-curl = $(DESCRIPTION)
OBSOLETED_BY_CSWpm-www-curl = CSWpmwwwcurl
CATALOGNAME_CSWpmwwwcurl = pm_wwwcurl_stub

RUNTIME_DEP_PKGS_CSWpm-www-curl += CSWlibidn11
RUNTIME_DEP_PKGS_CSWpm-www-curl += CSWlibz1
RUNTIME_DEP_PKGS_CSWpm-www-curl += CSWlibcurl4
RUNTIME_DEP_PKGS_CSWpm-www-curl += CSWlibssl1-0-0

CONFIGURE_ARGS = 

# Note that 08ssl.t fails (probably due to connection issues)
TEST_SCRIPTS = 

include gar/category.mk
