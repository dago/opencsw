NAME = libwww-perl
VERSION = 6.04
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = GAAS

DESCRIPTION = The World-Wide Web library for Perl
define BLURB
  The libwww-perl collection is a set of Perl modules which provides a simple
  and consistent application programming interface (API) to the World-Wide Web.
  The main focus of the library is to provide classes and functions that allow
  you to write WWW clients. The library also contain modules that are of more
  general use and even classes that help you implement simple HTTP servers.
endef

LICENSE_TEXT = This module is licensed under the perl license

PACKAGES = CSWpm-libwww-perl
CATALOGNAME = pm_libwww_perl
SPKG_DESC_CSWpm-libwww-perl = $(DESCRIPTION)

ARCHALL = 1

# Name change
OBSOLETED_BY_CSWpm-libwww-perl = CSWpmlibwww
CATALOGNAME_CSWpmlibwww = pm_libwww_stub

# avoid an error with configure-style default options
CONFIGURE_ARGS =

RUNTIME_DEP_PKGS += CSWpm-encode-locale
RUNTIME_DEP_PKGS += CSWpm-file-listing
RUNTIME_DEP_PKGS += CSWpm-html-parser
RUNTIME_DEP_PKGS += CSWpm-http-cookies
RUNTIME_DEP_PKGS += CSWpm-http-daemon
RUNTIME_DEP_PKGS += CSWpm-http-date
#RUNTIME_DEP_PKGS += CSWpm-http-message
RUNTIME_DEP_PKGS += CSWpm-http-negotiate
# http-request?
# http-response?
# http-status?
RUNTIME_DEP_PKGS += CSWpm-lwp-mediatypes
RUNTIME_DEP_PKGS += CSWpm-mime-base64
RUNTIME_DEP_PKGS += CSWpm-net-http
RUNTIME_DEP_PKGS += CSWpm-uri
RUNTIME_DEP_PKGS += CSWpm-www-robotrules

include gar/category.mk
