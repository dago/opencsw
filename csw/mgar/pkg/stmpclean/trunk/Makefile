NAME = stmpclean
VERSION = 0.3
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Removes old files from the specified directory
define BLURB
  The stmpclean utility never removes files or directories owned by root.
  It is a feature, not a bug. Great care is taken while descending into
  the directory, and the operation is secure. Unlike floating around Perl
  scripts that do the same task stmpclean never forks and consumes limited
  amount of memory (these Perl script easily turn into forking bombs when
  someone creates a lot a directories under /tmp). If your system is
  attacked and the attacker creates an extremely deep file hierarchy,
  stmpclean won't add to the problem by crashing your system trying to
  remove it.
endef

MASTER_SITES = http://shlang.com/stmpclean/
DISTFILES    = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_SCRIPTS =
BUILD_ARGS = $(NAME)
INSTALL_SCRIPTS = custom
TEST_SCRIPTS =

NORUNPATH = 1

include gar/category.mk

# Remove gcc'isms and non-POSIX LOG_PERROR option to openlog()
# http://www.gnu.org/s/libc/manual/html_node/openlog.html
pre-build-modulated:
	gsed -i -e '/^CFLAGS/d' $(WORKSRC)/Makefile
	gsed -i -e 's/| LOG_PERROR//' $(WORKSRC)/$(NAME).c
	@$(MAKECOOKIE)

install-custom: DOCDEST=$(DESTDIR)$(docdir)/$(NAME)
install-custom: DOCS=README FAQ
install-custom:
	ginstall -d $(DOCDEST)
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)$(mandir)/man8

	ginstall -m755 $(WORKSRC)/$(NAME) $(DESTDIR)$(bindir)/$(NAME)
	cp $(WORKSRC)/$(NAME).8 $(DESTDIR)$(mandir)/man8/
	cp $(addprefix $(WORKSRC)/,$(DOCS)) $(DOCDEST)
	cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
