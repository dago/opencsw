# $Id$

NAME = flex
VERSION = 2.5.39
GARTYPE = v2

DESCRIPTION = A tool for generating text-scanning programs-scanning programs.
define BLURB
  Flex is a tool for generating programs that recognize lexical patterns in
  text.  There are many applications for Flex, including writing compilers in
  conjunction with GNU Bison. Flex is a free implementation of the well known
  Lex program. It features a Lex compatibility mode, and also provides several
  new features such as exclusive start MASTER_SITES += $(SF_MIRRORS)
DISTFILES += $(DISTNAME).tar.xz

# This is probably the same cause as the bug reported here:
#   https://sourceforge.net/p/flex/bugs/170/
PATCHFILES += 0001-Allow-undefined-symbols-in-shared-libs.patch

VENDOR_URL = http://flex.sourceforge.net/

PACKAGES += CSWflex
SPKG_DESC_CSWflex = A tool for generating text-scanning programs
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWflex += CSWlibfl-pic2
RUNTIME_DEP_PKGS_CSWflex += CSWlibfl2
RUNTIME_DEP_PKGS_CSWflex += CSWlibintl8

# Previously the default flex was 2.5.4a and 2.5.35 was in /opt/csw/libexec/flex-2.5.35/bin
OBSOLETED_BY_CSWflex += CSWflex-new
CATALOGNAME_CSWflex-new += flex_new_stub
PKGFILES_CSWflex-new += $(bindir)/newflexudPACKAGES += CSWlibfl2
SPKG_DESC_CSWlibfl2 = Library for Flex, libfl.so.2
PKGFILES_CSWlibfl2 += $(call pkgfiles_lib,libfl.so.2)

PACKAGES += CSWlibfl-pic2
SPKG_DESC_CSWlibfl-pic2 = Library for Flex, libfl_pic.so.2
PKGFILES_CSWlibfl-pic2 += $(call pkgfiles_lib,libfl_pic.so.2)udBUILD64 = 1ude gar/category.mk

# Must use GNU diff for option '-q' or two tests fail due to bailing ou_PATH = $(prefix)/gnu:$(PATH)

# There are two tests failing, this is a known issue:
#    Executing test test-bison-yylloc
#   Test test-bison-yylloc FAILED. See test-bison-yylloc/OUTPUT for details.
#   Executing test test-bison-yylval
#   Test test-bison-yylval FAILED. See test-bison-yylval/OUTPUT for details.
# See for details
#   https://sourceforge.net/p/flex/bugs/144/

SKIPTEST ?= 1

include gar/category.mk

post-install:
	gln -s flex $(DESTDIR)$(bindir)/newflex
	@$(MAKECOOKIE)
