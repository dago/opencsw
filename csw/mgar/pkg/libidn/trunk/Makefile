GARNAME = libidn
GARVERSION = 1.13
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

# The failing test is due to a bug in libiconv. This is fixed in libiconv 0.13
#TEST_TARGET = check
TEST_TARGET =

include gar/category.mk
