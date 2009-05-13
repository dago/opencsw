GARNAME = libmcal
GARVERSION = 0.7
CATEGORIES = lib
DRIVERNAME = mcaldrivers
DRIVERVERSION = 0.9

DESCRIPTION = Modular Calendar Access Library
define BLURB
	mcal stands for Modular Calendar Access Library. 
	libmcal is a C library for accessing calendars. 
	It's written to be very modular, with pluggable drivers. 
	One of the main drivers it handles is ICAP.
endef

MASTER_SITES = $(SF_MIRRORS)

BUILD64 = 1
NO_ISAEXEC = 1

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(DRIVERNAME)-$(DRIVERVERSION).tar.gz
DISTNAME = $(GARNAME)
PACKAGES = CSWlibmcal
CATALOGNAME_CSWlibmcal = libmcal
SPKG_DESC_CSWlibmcal = $(DESCRIPTION)

#REQUIRED_PKGS_CSWlibmcal  = 

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz


CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-mstore 
CONFIGURE_ARGS += --with-icap

## There are no tests for this
TEST_SCRIPTS = skip

test-skip:
	$(DONADA)

post-extract-modulated:
	perl -i -pe 's|CC=gcc|CC=$(CC)|' $(WORKSRC)/Makefile.in
	perl -i -pe 's|CFLAGS=.*|CFLAGS=$$\\$$(INCLUDE) $(CFLAGS) -xcode=pic32 |' $(WORKSRC)/Makefile.in
	perl -i -pne 's|gcc|$$\\$$(CC)|' $(WORKSRC)/Makefile.in
	perl -i -pne 's|-shared|-G -xcode=pic32 |' $(WORKSRC)/Makefile.in
	perl -i -pne 's|install -m 755 -o 0 -g 0|ginstall -m 0755|' $(WORKSRC)/Makefile.in
	perl -i -pne 's|install -m 644 -o 0 -g 0|ginstall -m 0644|' $(WORKSRC)/Makefile.in
	perl -i -pne 's|\@prefix\@/lib|\@libdir\@|' $(WORKSRC)/Makefile.in
	perl -i -pne 's|\@prefix\@/include|\@includedir\@|' $(WORKSRC)/Makefile.in
	#
	cd $(WORKDIR); gzip -dc $(abspath $(DOWNLOADDIR)/$(DRIVERNAME)-$(DRIVERVERSION).tar.gz) |tar xf -
	cd $(WORKDIR)/mcal-drivers; cp -R * $(abspath $(WORKSRC))
	perl -i -pe 's|CC=gcc|CC=$(CC)|' $(WORKSRC)/mstore/Makefile
	perl -i -pe 's|CFLAGS=.*|CFLAGS=$$\\$$(INCLUDE) $(CFLAGS) -xcode=pic32 |' $(WORKSRC)/mstore/Makefile
	gmake -C $(WORKSRC)/mstore
	perl -i -pe 's|CC=gcc|CC=$(CC)|' $(WORKSRC)/icap/Makefile
	perl -i -pe 's|CFLAGS=.*|CFLAGS=$$\\$$(INCLUDE) $(CFLAGS) -xcode=pic32 |' $(WORKSRC)/icap/Makefile
	gmake -C $(WORKSRC)/icap
	@$(MAKECOOKIE)

include gar/category.mk
