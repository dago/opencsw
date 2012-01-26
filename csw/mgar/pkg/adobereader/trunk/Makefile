# $Id$
NAME = adobereader
VERSION_sparc = 8.1.7
FILEVERSION_sparc = 8.1.7
VERSION_i386 = 9.4.1
FILEVERSION_i386 = 9.4.1
VERSION = $(VERSION_$(GARCH))
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Adobe Acrobat Reader
define BLURB
endef

MAJORVERSION_sparc = $(shell echo $(VERSION_sparc) | cut -d. -f1)
MAJORVERSION_i386  = $(shell echo $(VERSION_i386) | cut -d. -f1)

MASTER_SITES_sparc = ftp://ftp.adobe.com/pub/adobe/reader/unix/$(MAJORVERSION_sparc).x/$(VERSION_sparc)/enu/
MASTER_SITES_i386 = ftp://ftp.adobe.com/pub/adobe/reader/unix/$(MAJORVERSION_i386).x/$(VERSION_i386)/enu/
MASTER_SITES = $(MASTER_SITES_sparc) $(MASTER_SITES_i386)
DISTFILES_sparc = AdobeReader_enu-$(FILEVERSION_sparc)-1.sparc.tar.bz2
DISTFILES_i386 = AdbeRdr$(FILEVERSION_i386)-1_i486solaris_enu.tar.bz2
DISTFILES = $(DISTFILES_sparc) $(DISTFILES_i386)
NOEXTRACT = $(filter-out $(DISTFILES_$(GARCH)),$(DISTFILES))
DISTNAME = AdobeReader

# File name regex to get notifications about upstream software releases
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

LICENSE = AdobeReader/ReadMe.htm

VENDOR_URL = $(MASTER_SITES_$(GARCH))

PACKAGING_PLATFORMS = solaris9-sparc solaris10-i386

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

# They have strange pathes all over the place and fix it with LD_LIBRARY_PATH during execution
CHECKPKG_OVERRIDES  = binary-architecture-does-not-match-placement
CHECKPKG_OVERRIDES += bad-rpath-entry
CHECKPKG_OVERRIDES += soname-not-found

# Can't check the library depepdency as this is done via LD_LIBRARY_PATH in the run scri√pt
CHECKPKG_OVERRIDES_sparc += surplus-dependency|CSWpango
CHECKPKG_OVERRIDES += $(CHECKPKG_OVERRIDES_$(GARCH))

RUNTIME_DEP_PKGS_sparc = CSWpango
RUNTIME_DEP_PKGS  = $(RUNTIME_DEP_PKGS_$(GARCH))

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)$(sharedstatedir)
	cd $(WORKSRC) && ./INSTALL --install_path=$(DESTDIR)$(sharedstatedir)
	ginstall -d $(DESTDIR)$(bindir)
	ln -s ../share/Adobe/Reader$(MAJORVERSION_$(GARCH))/bin/acroread $(DESTDIR)$(bindir)/acroread
	@$(MAKECOOKIE)

# Entries with spaces in the filepath are not allowed in the pkgmap.
# Adjust the directory path to the help pages in 8.1.7
post-install-modulated:
	cd $(DESTDIR); find . -type d -name "* *" | \
	while read F; do \
		N=`echo $$F | tr ' ' '_'`; \
		mv "$$F" $$N; \
	done;
	cd $(DESTDIR); find . -type f -name "* *" | \
	while read F; do \
		N=`echo $$F | tr ' ' '_'`; \
		mv "$$F" $$N; \
	done;
	@$(MAKECOOKIE)

# The older Sparc version needs libpangoxft-1.0.so.0 from CSWpango (or another location)
# Make sure it can be found by explicitly setting LD_LIBRARY_PATH in environment setting
post-install-isa-sparcv8:
	perl -i -npe 'if( /^ACRO_LD_LIBRARY_PATH=/ ) { print "LD_LIBRARY_PATH=$(libdir)\n" }' $(DESTDIR)$(sharedstatedir)/Adobe/Reader$(MAJORVERSION_$(GARCH))/bin/acroread
	@$(MAKECOOKIE)
