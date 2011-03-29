NAME = pca
VERSION = 20110329-01
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
DISTFILES  = $(NAME)-$(VERSION)
DISTFILES += COPYING
DISTFILES += pca.conf

PATCHFILES  = 0001-prefer-opencsw-perl.diff
PATCHFILES += 0002-Add-etc-opt-csw-as-config-location.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d{8}-\d{2})

WORKSRC = $(WORKDIR)
PATCHDIR = $(WORKDIR)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

SPKG_SOURCEURL = http://www.par.univie.ac.at/solaris/pca/
SPKG_VERSION = $(shell echo $(VERSION) | sed -e 's/-/./g')

SAMPLECONF = /etc/opt/csw/pca.conf

ARCHALL = 1

# Search path for wget, get all we can
CHECKPKG_OVERRIDES_CSWpca += file-with-bad-content|/usr/local|root/opt/csw/bin/pca
CHECKPKG_OVERRIDES_CSWpca += file-with-bad-content|/usr/local|root/opt/csw/share/man/man8/pca.8

include gar/category.mk

post-extract-modulated:
	mv $(WORKSRC)/$(DISTNAME) $(WORKSRC)/pca
	@$(MAKECOOKIE)

install-custom:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall $(WORKSRC)/pca $(DESTDIR)$(bindir)/pca
	ginstall -d $(DESTDIR)/etc/opt/csw
	ginstall $(WORKSRC)/pca.conf $(DESTDIR)/etc/opt/csw
	ginstall -d $(DESTDIR)$(mandir)/man8
	pod2man --section=8 $(WORKSRC)/pca > $(DESTDIR)$(mandir)/man8/pca.8
	@$(MAKECOOKIE)
