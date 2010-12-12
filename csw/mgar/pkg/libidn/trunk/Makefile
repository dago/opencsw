NAME = libidn
VERSION = 1.19
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
DISTFILES  = $(NAME)-$(VERSION).tar.gz

SPKG_SOURCEURL = http://www.gnu.org/software/libidn/

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS = CSWggettextrt CSWiconv

BUILD64 = 1
NOISAEXEC = 1

# We don't need it and if defined the test breaks
LD_OPTIONS =
EXTRA_LINKER_FLAGS = $(RUNPATH_LINKER_FLAGS)

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

CHECKPKG_OVERRIDES_CSWlibidn += missing-dependency|CSWemacscommon

include gar/category.mk
