GARNAME = bison
# GARVERSION = 2.4.2.8-cb76
GARVERSION = 2.4.3
CATEGORIES = devel

DESCRIPTION = GNU Project parser generator (yacc replacement)
define BLURB
  Bison is a parser generator in the style of yacc(1). It should be upwardly
  compatible with input files designed for yacc.
endef

MASTER_SITES = $(GNU_MIRROR)
# MASTER_SITES += http://alpha.gnu.org/gnu/bison/

DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

BUILD_DEP_PKGS = CSWgnulinks
RUNTIME_DEP_PKGS = CSWggettextrt CSWiconv CSWgm4

SPKG_SOURCEURL = http://www.gnu.org/software/bison/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

EXTRA_MERGE_EXCLUDE_FILES = $(libdir)/charset\.alias

# I guess we really need these
CHECKPKG_OVERRIDES_CSWbison += surplus-dependency|CSWgm4
CHECKPKG_OVERRIDES_CSWbison += surplus-dependency|CSWiconv

include gar/category.mk

# Must use GNU grep during test
PATH := /opt/csw/gnu:$(PATH)

post-install-modulated:
	mv $(DESTDIR)$(bindir)/yacc $(DESTDIR)$(bindir)/gyacc
	ginstall -d $(DESTDIR)$(prefix)/gnu
	ln -s ../bin/gyacc $(DESTDIR)$(prefix)/gnu/yacc
	@$(MAKECOOKIE)
