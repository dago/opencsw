# TODO (release-critical prefixed with !, non release-critical with *)
# ! Build fails
#   libtool: link: cannot find the library `/opt/csw/lib/libgconf-2.la' or unhandled argument `/opt/csw/lib/libgconf-2.la'
#
NAME = ghex
VERSION = 2.24.0
CATEGORIES = utils

DESCRIPTION = The GNOME binary hex editor
define BLURB
  Long description
endef

MASTER_SITES = http://ftp.acc.umu.se/pub/GNOME/sources/ghex/2.24/
DISTFILES    = $(DISTNAME).tar.gz
UFILES_REGEX = (\d+(?:\.\d+)*)
UPSTREAM_MASTER_SITES = http://ftp.acc.umu.se/pub/GNOME/sources/ghex/

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

# GNU gettext required
PATH:=$(prefix)/gnu:$(PATH)
