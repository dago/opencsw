GARNAME = Geo-IP-PurePerl
GARVERSION = 1.23
CATEGORIES = cpan
AUTHOR = BORISZ

DESCRIPTION = Look up country by IP Address
define BLURB
  This Perl module enables the user to find geographical and network information of
  an IP address. This is the Pure Perl version. There is also a faster implementation,
  Geo::IP which is a XS wrapper around the GeoIP C library, available from CPAN
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWpmgeoippureperl,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS = CSWgeolitedb

EXTRA_MERGE_EXCLUDE_FILES = .*~ .*perllocal\.pod

include gar/category.mk

post-configure-modulated:
	@echo " ==> Post-configure for $(GARNAME) (custom)"
	@echo "$(WORKSRC)"
	@( cd $(WORKSRC)/lib/Geo/IP ; \
	   sed 's/\/usr\/local\/share\/GeoIP\/GeoIP.dat/\/opt\/csw\/share\/GeoIP\/GeoIP.dat/' PurePerl.pm > tmp.sed ; \
	   mv tmp.sed PurePerl.pm )
	@$(MAKECOOKIE)
