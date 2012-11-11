NAME = chrpath
VERSION = 0.13
GARTYPE = v2

DESCRIPTION = A program to fix/change runpaths
define BLURB
endef

SPKG_SOURCEURL = http://directory.fsf.org/project/chrpath/
MASTER_SITES = http://ftp.tux.org/pub/X-Windows/ftp.hungry.com/chrpath/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PACKAGES = CSWchrpath
CATALOGNAME_CSWchrpath = chrpath
SPKG_DESC_CSWchrpath = $(DESCRIPTION)

PATCHFILES = chrpath_0.13-2.diff
PATCHDIR = $(WORKSRC)

# This is just docs
CHECKPKG_OVERRIDES_CSWchrpath += file-with-bad-content|/usr/local|root/opt/csw/share/doc/chrpath/INSTALL

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*).tar.gz

BUILD64_LIBS_ONLY = 1
NOISALIST = 1

CONFIGURE_ARGS  = $(DIRPATHS)

## There are no tests for this
## runtest.ksh is broken manual test required
TEST_SCRIPTS =

post-configure-modulated:
	@(perl -i -plne 's|docdir = .*|docdir = $(prefix)/share/doc/$(NAME)|'\
		$(WORKSRC)/Makefile)

include gar/category.mk
