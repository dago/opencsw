NAME = tmpwatch
VERSION = 2.10.1
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Removes files which haven't been accessed for a period of time
define BLURB
  The tmpwatch utility recursively searches through specified directories
  and removes files which have not been accessed in a specified period of
  time. tmpwatch is normally used to clean up directories which are used
  for temporarily holding files (fr example, /tmp). 
endef

VENDOR_URL   = https://fedorahosted.org/tmpwatch/
MASTER_SITES = https://fedorahosted.org/releases/t/m/tmpwatch/
DISTFILES    = $(NAME)-$
PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)
TEST_SCRIPTS =

NORUNPATH = 1

include gar/category.mk

# Install changelog.CSW
post-merge: $(foreach P,$(_PKG_SPECS),install-changelog-$P)
install-changelog-%:
	ginstall -D $(FILEDIR)/changelog.CSW \
		$(PKGROOT)$(docdir)/$(call catalogname,$*)/changelog.CS