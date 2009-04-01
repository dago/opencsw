GARNAME = chrpath
GARVERSION = 0.13
CATEGORIES = utils

DESCRIPTION = A program to fix/change runpaths
define BLURB
endef

MASTER_SITES = http://directory.fsf.org/project/chrpath/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PACKAGES = CSWchrpath
CATALOGNAME_CSWchrpath = chrpath
SPKG_DESC_CSWchrpath = $(DESCRIPTION)

PATCHFILES = chrpath_0.13-2.diff
PATCHDIR = $(WORKSRC)


# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1
NOISALIST = 1

CONFIGURE_ARGS  = $(DIRPATHS)

## There are no tests for this
## runtest.ksh is broken manual test required
TEST_SCRIPTS = skip

test-skip:
	$(DONADA)

post-configure-modulated:
	@(perl -i -plne 's|docdir = .*|docdir = $(prefix)/share/doc/$(GARNAME)|'\
		$(WORKSRC)/Makefile)

include gar/category.mk
