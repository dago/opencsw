GARNAME = pca
GARVERSION = $(shell test -f $(DOWNLOADDIR)/pca && perl $(DOWNLOADDIR)/pca -v | cut -f2 -d' ' | sed -e 's/-/./g')
CATEGORIES = utils

DESCRIPTION = Patch Check Advanced
define BLURB
  Patch Check Advanced (pca) generates lists of installed and
  missing patches for Sun Solaris systems and optionally downloads patches.
  It resolves dependencies between patches and installs them in correct order.
  It can be the only tool you ever need for patch management on a single
  machine or a complete network. Just one perl script, it doesn't need
  compilation nor installation, and it doesn't need root permissions to run.
  It works on all versions of Solaris, both SPARC and x86.
endef

MASTER_SITES = http://www.par.univie.ac.at/solaris/pca/
DISTFILES  = $(GARNAME)
DISTFILES += $(call admfiles,CSWpca)

WORKSRC = $(WORKDIR)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	@ginstall $(WORKSRC)/pca $(DESTDIR)$(bindir)/pca
	@ginstall -d $(DESTDIR)$(mandir)/man8
	@pod2man $(WORKSRC)/pca > $(DESTDIR)$(mandir)/man8/pca.8
	@$(MAKECOOKIE)
