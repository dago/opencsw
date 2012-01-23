NAME = argtable
VERSION = 2.13
CATEGORIES = utils

DESCRIPTION = Parsing GNU style command line options with a minimum of fuss
define BLURB
  Argtable is an ANSI C library for parsing GNU style command line options with a minimum of fuss.
  It enables a program's command line syntax to be defined in the source code as an array of argtable
  structs. The command line is then parsed according to that specification and the resulting values
  are returned in those same structs where they are accessible to the main program. Both tagged
  (-v, --verbose, --foo=bar) and untagged arguments are supported, as are multiple instances of
  each argument. Syntax error handling is automatic and the library also provides the means for
  generating a textual description of the command line syntax.
endef

MASTER_SITES = $(SF_MIRROR)
DISTNAME = $(NAME)$(subst .,-,$(VERSION))
DISTFILES  = $(DISTNAME).tar.gz

VENDOR_URL = http://argtable.sourceforge.net/

PACKAGES += CSWlibargtable2-0
SPKG_DESC_CSWlibargtable2-0 = Parsing GNU style command line options with a minimum of fuss, libargtable2.so.0
PKGFILES_CSWlibargtable2-0 += $(call pkgfiles_lib,libargtable2.so.0)

PACKAGES += CSWlibargtable2-dev
SPKG_DESC_CSWlibargtable2-dev = Development files for libargtable2.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibargtable2-dev += CSWlibargtable2-0

# These are just examples in the docs
CHECKPKG_OVERRIDES_CSWlibargtable2-dev += file-with-bad-content|/usr/local|root/opt/csw/share/doc/argtable2/argtable2.ps
CHECKPKG_OVERRIDES_CSWlibargtable2-dev += file-with-bad-content|/usr/local|root/opt/csw/share/doc/argtable2/argtable2-intro.html
CHECKPKG_OVERRIDES_CSWlibargtable2-dev += file-with-bad-content|/usr/share|root/opt/csw/share/doc/argtable2/argtable2-intro.ps
CHECKPKG_OVERRIDES_CSWlibargtable2-dev += file-with-bad-content|/usr/share|root/opt/csw/share/doc/argtable2/argtable2-advanced.ps

EXTRA_LDFLAGS = -lintl

BUILD64_LIBS_ONLY = 1

include gar/category.mk
