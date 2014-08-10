# $Id$

NAME = hexdump
VERSION = 1.8
GARTYPE = v2

DESCRIPTION = A hex dumper that can handle EBCDIC
define BLURB
endef

MASTER_SITES = http://www.catb.org/~esr/hexdump/
DISTFILES    = $(NAME)-$(VERSION).tar.gz

CONFIGURE_SCRIPTS =
BUILD_TARGETS = hexdump hexdump.1
TEST_SCRIPTS =
INSTALLGARCOMPILER = GNU

# hexdump Makefile only uses $(CC), not $(CFLAGS)
BUILD_ARGS = CC='$(CC) $(CFLAGS) -std=c99'
NORUNPATH = 1

PACKAGING_PLATFORMS = solaris9-i386 solaris9-sparcAGS)'
NORUNPATH = 1

include gar/category.mk

install-custom:
	ginstall -D $(WORKSRC)/hexdump $(DESTDIR)$(bindir)/hexdump
	ginstall -D $(WORKSRC)/hexdump.1 $(DESTDIR)$(mandir)/man1/hexdump.1
	@$(MAKECOOKIE)

post-install-modulated: DOCS=README
post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(NAME)
post-install-modulated:
	ginstall -d $(DOCDEST)
	cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	cp $(addprefix $(WORKSRC)/, $(DOCS)) $(DOCDES