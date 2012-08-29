NAME = pca
VERSION = 20120829-01
CATEGORIES = utils
GARTYPE = v2

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

MASTER_SITES += http://www.par.univie.ac.at/solaris/pca/download/
MASTER_SITES += http://www.par.univie.ac.at/solaris/pca/contrib/
DISTFILES  = $(NAME)-$(VERSION)
DISTFILES += chkmin
DISTFILES += mkxref
DISTFILES += clean
DISTFILES += cleanup_sadm
DISTFILES += COPYING
DISTFILES += pca.conf

PATCHFILES  = 0001-prefer-opencsw-perl.diff
PATCHFILES += 0002-Add-etc-opt-csw-as-config-location.patch

WORKSRC = $(WORKDIR)
PATCHDIR = $(WORKDIR)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

VENDOR_URL = http://www.par.univie.ac.at/solaris/pca/
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
	ginstall -d $(DESTDIR)$(sharedstatedir)/pca/contrib
	ginstall $(WORKSRC)/chkmin $(DESTDIR)$(sharedstatedir)/pca/contrib/chkmin
	ginstall $(WORKSRC)/mkxref $(DESTDIR)$(sharedstatedir)/pca/contrib/mkxref
	ginstall $(WORKSRC)/clean $(DESTDIR)$(sharedstatedir)/pca/contrib/clean
	ginstall $(WORKSRC)/cleanup_sadm $(DESTDIR)$(sharedstatedir)/pca/contrib/cleanup_sadm
	ginstall -d $(DESTDIR)/etc/opt/csw
	ginstall $(WORKSRC)/pca.conf $(DESTDIR)/etc/opt/csw
	ginstall -d $(DESTDIR)$(mandir)/man8
	pod2man --section=8 $(WORKSRC)/pca > $(DESTDIR)$(mandir)/man8/pca.8
	@$(MAKECOOKIE)
