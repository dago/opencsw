# $Id$

NAME = bison
VERSION = 3.0.2
GARTYPE = v2

DESCRIPTION = GNU Project parser generator (yacc replacement)
define BLURB
  Bison is a parser generator in the style of yacc(1). It should be upwardly
  compatible with input files designed for yacc.
endef

MASTER_SITES = $(GNU_MIRROR)

DISTFILES = $(DISTNAME).tar.gz

RUNTIME_DEP_PKGS_CSWbison += CSWlibintl8
RUNTIME_DEP_PKGS_CSWbison += CSWgm4

VENDOR_URL = http://www.gnu.org/software/bison/

PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

EXTRA_MERGE_EXCLUDE_FILES = $(libdir)/charset\.alias

# I guess we really need these
CHECKPKG_OVERRIDES_CSWbison += surplus-dependency|CSWgm4

# Tests 217-222 use zero-sized structs
EXTRA_CFLAGS += -features=extensions

# Our gcj just does not work cleanly
SKIPTEST ?= 1

include gar/category.mk

# Must use GNU grep during test
PATH := /opt/csw/gnu:$(PATH)

post-install-modulated:
	mv $(DESTDIR)$(bindir)/yacc $(DESTDIR)$(bindir)/gyacc
	ginstall -d $(DESTDIR)$(prefix)/gnu
	ln -s ../bin/gyacc $(DESTDIR)$(prefix)/gnu/yacc
	perl -pi \
		-e 's,/usr/local,$(prefix),g' \
		$(DESTDIR)$(infodir)/bison.info
	@$(MAKECOOKIE)
