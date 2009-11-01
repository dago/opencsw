GARNAME = sox
GARVERSION = 14.3.0
CATEGORIES = apps

DESCRIPTION = Sound Processing Tool
define BLURB
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES = $(DISTNAME).tar.gz

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://sox.sourceforge.net/

# XXX: Add gsm, lpc10 and wavpack
REQUIRED_PKGS = CSWvorbis CSWlibogg CSWlibmad CSWlame CSWlibid3tag
PREREQUISITE_PKGS = $(REQUIRED_PKGS)

CONFIGURE_ARGS  = $(DIRPATHS)

BUILD64 = 1

TEST_TARGET = check

include gar/category.mk
