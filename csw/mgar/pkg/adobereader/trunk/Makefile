# $Id$
GARNAME = adobereader
GARVERSION_sparc = 8.1.7
FILEVERSION_sparc = 8.1.7
GARVERSION_i386 = 9.4.0
FILEVERSION_i386 = 9.4
GARVERSION = $(GARVERSION_$(GARCH))
CATEGORIES = apps

DESCRIPTION = Adobe Acrobat Reader
define BLURB
endef

MASTER_SITES  = ftp://ftp.adobe.com/pub/adobe/reader/unix/$(shell echo $(GARVERSION_sparc) | cut -d. -f1).x/$(GARVERSION_sparc)/enu/
MASTER_SITES += ftp://ftp.adobe.com/pub/adobe/reader/unix/$(shell echo $(GARVERSION_i386) | cut -d. -f1).x/$(GARVERSION_i386)/enu/
DISTFILES_sparc  = AdobeReader_enu-$(FILEVERSION_sparc)-1.sparc.tar.bz2
DISTFILES_i386  = AdbeRdr$(FILEVERSION_i386)-1_i486solaris_enu.tar.bz2
DISTFILES = $(DISTFILES_sparc) $(DISTFILES_i386)
NOEXTRACT = $(filter-out $(DISTFILES_$(GARCH)),$(DISTFILES))
DISTNAME = AdobeReader

# File name regex to get notifications about upstream software releases
# UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

LICENSE = AdobeReader/ReadMe.htm

PACKAGING_PLATFORMS = solaris9-sparc solaris10-i386

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

# They have strange pathes all over the place and fix it with LD_LIBRARY_PATH during execution
CHECKPKG_OVERRIDES  = binary-architecture-does-not-match-placement
CHECKPKG_OVERRIDES += bad-rpath-entry
CHECKPKG_OVERRIDES += soname-not-found

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)$(sharedstatedir)
	cd $(WORKSRC) && ./INSTALL --install_path=$(DESTDIR)$(sharedstatedir)
	ginstall -d $(DESTDIR)$(bindir)
	ln -s ../share/Adobe/Reader9/bin/acroread $(DESTDIR)$(bindir)/acroread
	@$(MAKECOOKIE)

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
