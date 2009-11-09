GARNAME = sox
GARVERSION = 14.3.0
CATEGORIES = apps

DESCRIPTION = Sound Processing Tool
define BLURB
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES = $(DISTNAME).tar.gz

# There is a hack in there to rewind pipes when detecting file formats.
# As the FILE struct is opaque in 64 bit we must disable this for 64 bit.
# But as we only need the library in 64 bit anyway this shouldn't hurt.
PATCHFILES = 0001-Disable-stdio-hack-to-rewind-pipes.patch

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://sox.sourceforge.net/

# XXX: Add gsm, lpc10 and wavpack
REQUIRED_PKGS = CSWvorbis CSWlibogg CSWlibmad CSWlame CSWlibid3tag
REQUIRED_PKGS += CSWflac CSWlibao CSWlibsndfile CSWpng CSWwavpack CSWzlib

PREREQUISITE_PKGS = $(REQUIRED_PKGS)

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS +=  --without-libltdl

BUILD64 = 1
NO_ISAEXEC = 1
TEST_TARGET = check

MERGE_DIRS_isa-extra = $(libdir)

include gar/category.mk
