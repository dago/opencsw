# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = torsocks
VERSION = 1.2
GARTYPE = v2

DESCRIPTION = Use SOCKS-friendly applications with Tor
define BLURB
  Torsocks allows you to use most SOCKS-friendly applications in a safe way with Tor. It ensures that DNS requests are handled safely and explicitly rejects UDP traffic from the application you're using.
endef

MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PATCHFILES = torsocks-HEAD-2034625.nww.solaris.patch

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

