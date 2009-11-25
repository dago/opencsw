GARNAME = libsmi
GARVERSION = 0.4.8
CATEGORIES = lib

DESCRIPTION = Allows management applications to access SMI MIB module definitions
define BLURB
  The core of the libsmi distribution is a library that allows management applications
  to access SMI MIB module definitions. On top of this library, there are tools to check,
  analyze dump, convert, and compare MIB definitions. Finally, the distribution contains
  a steadily maintained and revised archive of all IETF and IANA maintained standard MIB
  and PIB modules.
endef

MASTER_SITES = ftp://ftp.ibr.cs.tu-bs.de/pub/local/libsmi/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWlibsmi CSWlibsmimibs 

CATALOGNAME_CSWlibsmi = libsmi
CATALOGNAME_CSWlibsmimibs = libsmi_mibs

SPKG_DESC_CSWlibsmi = Library to access SMI MIB module definitions
SPKG_DESC_CSWlibsmimibs = SMI MIB definitions

SPKG_SOURCEURL = http://www.ibr.cs.tu-bs.de/projects/libsmi/

REQUIRED_PKGS_CSWlibsmi = CSWlibsmimibs

BUILD64 = 1
NO_ISAEXEC = 1
CONFIGURE_ARGS = $(DIRPATHS)

EXTRA_CPPFLAGS = -Dfabsf=fabs

MERGE_DIRS_isa-extra = $(libdir)

PKGFILES_CSWlibsmimibs = $(sharedstatedir)/mibs/.*
PKGFILES_CSWlibsmimibs += $(sharedstatedir)/pibs/.*

include gar/category.mk
