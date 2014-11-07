NAME = Cairo
VERSION = 1.104
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = XAOC

DESCRIPTION = Perl interface to the cairo 2d vector graphics library
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

PACKAGES += CSWpm-cairo
CATALOGNAME_CSWpm-cairo = pm_cairo
SPKG_DESC_CSWpm-cairo = Perl interface to the cairo 2d vector graphics library
RUNTIME_DEP_PKGS_CSWpm-cairo += CSWlibcairo2
OBSOLETED_BY_CSWpm-cairo += CSWpmcairo
CATALOGNAME_CSWpmcairo = pm_cairo_stub

# This is for the font path /usr/share/fonts/truetype/ttf-bitstream-vera/Vera.ttf
CHECKPKG_OVERRIDES_CSWpm-cairo += file-with-bad-content|/usr/share|root/opt/csw/lib/perl/csw/Cairo.pm

include gar/category.mk
