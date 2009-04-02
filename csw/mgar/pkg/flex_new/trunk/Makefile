GARNAME = flex
GARVERSION = 2.5.35
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
DISTNAME = flex-$(GARVERSION)
DISTFILES  = $(DISTNAME).tar.bz2

PACKAGES = CSWflex-new
CATALOGNAME = flex_new

REQUIRED_PKGS = CSWggettextrt CSWiconv

NOISALIST = 1
CONFIGURE_ARGS = --prefix=$(libexecdir)/$(GARNAME)-$(GARVERSION)

TEST_TARGET = check

include gar/category.mk

# Must use GNU diff for option '-q' or two tests fail due to bailing out Sun diff
TEST_ENV += PATH=$(prefix)/gnu:$(PATH)

post-install-modulated:
	@mkdir -p $(DESTDIR)$(bindir)
	@gln -sf ../libexec/$(GARNAME)-$(GARVERSION)/bin/flex $(DESTDIR)$(bindir)/newflex
	@gln -sf ../libexec/$(GARNAME)-$(GARVERSION)/bin/flex $(DESTDIR)$(bindir)/flex-$(GARVERSION)
	@rm -f $(DESTDIR)$(libexecdir)/$(GARNAME)-$(GARVERSION)/info/dir
	@$(MAKECOOKIE)
