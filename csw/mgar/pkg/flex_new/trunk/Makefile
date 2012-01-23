# $Id$

NAME = flex
VERSION = 2.5.35
CATEGORIES = devel

DESCRIPTION = A tool for generating text-scanning programs.
define BLURB
  Flex is a tool for generating programs that recognize lexical patterns in
  text.  There are many applications for Flex, including writing compilers in
  conjunction with GNU Bison. Flex is a free implementation of the well known
  Lex program. It features a Lex compatibility mode, and also provides several
  new features such as exclusive start conditions.
endef

SPKG_SOURCEURL = http://flex.sourceforge.net/

SF_PROJ = flex
MASTER_SITES = $(SF_MIRRORS)
DISTNAME = flex-$(VERSION)
DISTFILES  = $(DISTNAME).tar.bz2

PACKAGES = CSWflex-new
CATALOGNAME = flex_new

RUNTIME_DEP_PKGS = CSWggettextrt

NOISALIST = 1
CONFIGURE_ARGS = --prefix=$(libexecdir)/$(NAME)-$(VERSION)

EXTRA_MERGE_EXCLUDE_FILES = $(prefix)/.*\.a

include gar/category.mk

# Must use GNU diff for option '-q' or two tests fail due to bailing out Sun diff
TEST_ENV += PATH=$(prefix)/gnu:$(PATH)

post-install-modulated:
	@mkdir -p $(DESTDIR)$(bindir)
	@gln -sf ../libexec/$(NAME)-$(VERSION)/bin/flex $(DESTDIR)$(bindir)/newflex
	@gln -sf ../libexec/$(NAME)-$(VERSION)/bin/flex $(DESTDIR)$(bindir)/flex-$(VERSION)
	@rm -f $(DESTDIR)$(libexecdir)/$(NAME)-$(VERSION)/info/dir
	@$(MAKECOOKIE)
