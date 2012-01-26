NAME = Shout
VERSION = 2.1
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = MYSELF

DESCRIPTION = Perl bindings for libshout 2
define BLURB
endef

MASTER_SITES = http://downloads.us.xiph.org/releases/libshout/
DISTFILES = $(DISTNAME).tar.gz

RUNTIME_DEP_PKGS = CSWlibogg CSWlibshout CSWspeex CSWtheora CSWvorbis CSWpkgconfig
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS)

PACKAGES = CSWpmshout
CATALOGNAME = pm_shout

EXTRA_MERGE_EXCLUDE_FILES = .*/example\.pl .*/example2\.pl

include gar/category.mk
