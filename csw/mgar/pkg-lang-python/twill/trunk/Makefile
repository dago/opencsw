# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = twill
VERSION = 0.9
CATEGORIES = python

DESCRIPTION = An easy to use web automation kit
define BLURB
  Twill is a simple scripting language intended for programmatic or
  automated browsing of Web sites. It allows users to browse the Web from
  a command-line interface. So, you can navigate through Web sites that
  use forms, cookies, and most standard Web features. 
endef

VENDOR_URL   = http://twill.idyll.org/
MASTER_SITES = http://darcs.idyll.org/~t/projects/
DISTFILES    = $(DISTNAME).tar.gz
DISTFILES   += changelog.CSW

UPSTREAM_MASTER_SITES = $(VENDOR_URL)
LICENSE = doc/LICENSE.txt
ARCHALL = 1

# The the suite is a bit b0rked WRT to our behind-proxy-setup. It needs
# to have an unset http_proxy in order to access it's own test server
# on http://localhost:8080, but then tries to access http://google.com
# for other tests. 2 out of 36 tests fail.
TEST_SCRIPTS =

include gar/category.mk

# Use TEST_ENV directly. EXTRA_TEST_EXPORTS would see the non-overridable
# $(http_proxy) from /etc/opt/csw/garrc (at least on the buildfarm)
TEST_ENV += http_proxy=""
