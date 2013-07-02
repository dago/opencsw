# $Id$

NAME = flex
VERSION = 2.5.37
GARTYPE = v2

DESCRIPTION = A tool for generating text-scanning programs-scanning programs.
define BLURB
  Flex is a tool for generating programs that recognize lexical patterns in
  text.  There are many applications for Flex, including writing compilers in
  conjunction with GNU Bison. Flex is a free implementation of the well known
  Lex program. It features a Lex compatibility mode, and also provides several
  new features such as exclusive start MASTER_SITES += $(SF_MIRRORS)
DISTFILES += $(DISTNAME).tar.bz2

VENDOR_URL = http://flex.sourceforge.net/

PACKAGES += CSWflex
SPKG_DESC_CSWflex = A tool for generating text-scanning programs
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWflex += CSWlibintl8

# Previously the default flex was 2.5.4a and 2.5.35 was in /opt/csw/libexec/flex-2.5.35/bin
OBSOLETED_BY_CSWflex += CSWflex-new
CATALOGNAME_CSWflex-new += flex_new_stub
PKGFILES_CSWflex-new += $(bindir)/newflexude gar/category.mk

# Must use GNU diff for option '-q' or two tests fail due to bailing ou_PATH = $(prefix)/gnu:$(PATH)

include gar/category.mk

post-install:
	gln -s flex $(DESTDIR)$(bindir)/newflex
	@$(MAKECOOKIE)
