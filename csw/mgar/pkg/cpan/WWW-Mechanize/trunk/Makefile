NAME = WWW-Mechanize
VERSION = 1.72
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = JESSE

DESCRIPTION = Handy web browsing in a Perl object
define BLURB
endef

DISTFILES += COPYING

PACKAGES = CSWpm-www-mechanize
CATALOGNAME = pm_www_mechanize
SPKG_DESC_CSWpm-www-mechanize = $(DESCRIPTION)
OBSOLETED_BY_CSWpm-www-mechanize = CSWpmwwwmechanize
CATALOGNAME_CSWpmwwwmechanize = pm_wwwmechanize

ARCHALL = 1

RUNTIME_DEP_PKGS += CSWpm-html-form
RUNTIME_DEP_PKGS += CSWpm-html-parser
RUNTIME_DEP_PKGS += CSWpm-html-tree
RUNTIME_DEP_PKGS += CSWpm-http-daemon
RUNTIME_DEP_PKGS += CSWpm-http-message
RUNTIME_DEP_PKGS += CSWpm-http-server-simple
RUNTIME_DEP_PKGS += CSWpm-libwww-perl
RUNTIME_DEP_PKGS += CSWpm-test-warn
RUNTIME_DEP_PKGS += CSWpm-uri

CONFIGURE_ARGS = -nolive -nolocal

include gar/category.mk
