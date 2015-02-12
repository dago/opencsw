# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = stud
VERSION = 0.3p53
GARTYPE = v2

DESCRIPTION = Brief description
define BLURB
  Long description
endef

MASTER_SITES = http://rohara.fedorapeople.org/stud/
DISTFILES  = bumptech-stud-0.3-51-g0b88039.tar.gz
PATCHFILES += 0001-solaris-fix.patch
PATCHFILES += 0002-fix-makefile.patch

GARCOMPILER = GCC4

BUILD64 = 1
ISAEXEC = 1

CONFIGURE_SCRIPTS =
CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

include gar/category.mk

post-extract:
	mv $(WORKDIR)/bumptech-stud-0b88039 $(WORKDIR)/stud-0.3p53
	@$(MAKECOOKIE)
