NAME = Geo-IP-PurePerl
VERSION = 1.25
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = BORISZ

DESCRIPTION = Look up country by IP Address
define BLURB
  This Perl module enables the user to find geographical and network
  information of an IP address. This is the Pure Perl version. There
  is also a faster implementation, Geo::IP which is a XS wrapper
  around the GeoIP C library, available from CPAN
endef

DISTFILES  = $(NAME)-$(VERSION).tar.gz

PACKAGES = CSWpm-geo-ip-pureperl
CATALOGNAME = pm_geo_ip_pureperl
SPKG_DESC_CSWpm-geo-ip-pureperl = $(DESCRIPTION)
ARCHALL = 1
OBSOLETED_BY_CSWpm-geo-ip-pureperl = CSWpmgeoippureperl
CATALOGNAME_CSWpmgeoippureperl = pm_geoippureperl

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS = CSWgeolitedb

CHECKPKG_OVERRIDES_CSWpmgeoippureperl += file-with-bad-content|/usr/local|root/opt/csw/share/perl/csw/Geo/IP/PurePerl.pm

include gar/category.mk

post-configure-modulated:
	@echo " ==> Post-configure for $(NAME) (custom)"
	@( cd $(WORKSRC)/lib/Geo/IP ; \
	   sed 's/\/usr\/local\/share\/GeoIP\/GeoIP.dat/\/opt\/csw\/share\/GeoIP\/GeoIP.dat/' PurePerl.pm > tmp.sed ; \
	   mv tmp.sed PurePerl.pm )
	@( cd $(WORKSRC) ; \
	   sed 's/\/usr\/local\/share\/GeoIP\/GeoIP.dat/\/opt\/csw\/share\/GeoIP\/GeoIP.dat/' geoip-lookup > tmp.sed ; \
	   mv tmp.sed geoip-lookup )
	@$(MAKECOOKIE)
