GARNAME = pca
GARVERSION = 20091216-02
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

MASTER_SITES = http://www.par.univie.ac.at/solaris/pca/download/
DISTFILES  = $(GARNAME)-$(GARVERSION)
DISTFILES += COPYING
DISTFILES += pca.conf

PATCHFILES = 0001-prefer-opencsw-perl.diff
#PATCHDIRLEVEL = 0

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d{8}-\d{2})

WORKSRC = $(WORKDIR)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

SPKG_SOURCEURL = http://www.par.univie.ac.at/solaris/pca/
SPKG_VERSION = $(shell echo $(GARVERSION) | sed -e 's/-/./g')

ARCHALL = 1

include gar/category.mk

post-extract-modulated:
	@mv $(WORKSRC)/$(DISTNAME) $(WORKSRC)/pca
	@$(MAKECOOKIE)

install-custom:
	@ginstall -d $(DESTDIR)$(bindir)
	@ginstall $(WORKSRC)/pca $(DESTDIR)$(bindir)/pca
	@ginstall -d $(DESTDIR)$(mandir)/man8
	@pod2man --section=8 $(WORKSRC)/pca > $(DESTDIR)$(mandir)/man8/pca.8
	@$(MAKECOOKIE)
