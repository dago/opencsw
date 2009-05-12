GARNAME = bison
GARVERSION = 2.4.1
CATEGORIES = devel

DESCRIPTION = GNU Project parser generator (yacc replacement)
define BLURB
  Bison is a parser generator in the style of yacc(1). It should be upwardly
  compatible with input files designed for yacc.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.bz2

REQUIRED_PKGS = CSWggettextrt CSWiconv CSWgm4

SPKG_SOURCEURL = http://www.gnu.org/software/bison/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

TAR_ARGS =
OPT_FLAGS_SOS = -xO1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

# Must use GNU grep during test
PATH := /opt/csw/gnu:$(PATH)

post-install-modulated:
	(cd $(DESTDIR)$(prefix)/bin; \
	/usr/ccs/bin/strip bison; \
	/usr/ccs/bin/mcs -d bison; \
	mv yacc gyacc)
