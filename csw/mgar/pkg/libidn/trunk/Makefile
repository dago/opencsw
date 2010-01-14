GARNAME = libidn
GARVERSION = 1.16
CATEGORIES = lib

DESCRIPTION = GNU IDN Library
define BLURB
  GNU Libidn is a fully documented implementation of the Stringprep,
  Punycode and IDNA specifications. Libidn's purpose is to encode and
  decode internationalized domain names. The native C, C# and Java
  libraries are available under the GNU Lesser General Public License
  version 2.1 or later.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

SPKG_SOURCEURL = http://www.gnu.org/software/libidn/

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1
NO_ISAEXEC = 1

REQUIRED_PKGS = CSWggettextrt CSWiconv

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
