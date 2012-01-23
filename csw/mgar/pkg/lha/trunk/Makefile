# : Makefile 9089 2010-03-11 08:34:46Z wahwah $
NAME = lha
VERSION = 1.14i-ac20050924p1
SPKG_VERSION = $(shell echo $(VERSION) | tr '-' '_')
CATEGORIES = utils

DESCRIPTION = File archiving/compression program
define BLURB
endef

MASTER_SITES = http://sourceforge.jp/projects/lha/releases/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

DEP_PKGS = CSWiconv

VENDOR_URL = http://www2m.biglobe.ne.jp/~dolphin/lha/lha-unix.htm

EXTRA_LINKER_FLAGS = -liconv
CONFIGURE_ARGS = $(DIRPATHS)

# License is really unknown
CHECKPKG_OVERRIDES_CSWlha += license-missing|/opt/csw/share/doc/lha/license

include gar/category.mk
