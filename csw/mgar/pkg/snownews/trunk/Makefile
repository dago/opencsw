# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! build state unknown, work in progress, please verify
#
NAME = snownews
VERSION = 1.5.12
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Text mode RSS/RDF news reader
define BLURB
  Long description
endef

VENDOR_URL   = http://kiza.kcore.de/software/snownews/
MASTER_SITES = http://kiza.kcore.de/media/software/snownews/
DISTFILES    = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = --prefix=$(prefix)

EXTRA_INC=/opt/csw/include/ncursesw/

include gar/category.mk

# snownews doesn't use autoconf, but a very simple perl ./configure script
pre-configure-modulated:
	perl -pi -e 's|-Wall -Wno-format-y2k||' $(WORKSRC)/configure
	@$(MAKECOOKIE)
