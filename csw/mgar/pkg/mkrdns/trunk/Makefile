NAME = mkrdns
VERSION = 3.3
REAL_VERSION = $(subst .,_,$(VERSION))
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = An automatic reverse DNS zone generator
define BLURB
  Have you ever gotten tired of having to change both the forward and
  reverse zone maps when adding, removing, or changing hosts in DNS? If
  so, then mkrdns is for you! mkrdns automates the tedious procedure of
  editing both forward and reverse zones when making changes to your zones
  with likely no changes to your current configuration file.
endef

MASTER_SITES = http://sites.google.com/a/kluge.net/mkrdns/
DISTNAME     = $(NAME)-$(REAL_VERSION)
DISTFILES    = $(DISTNAME).gz
UFILES_REGEX = $(NAME)-(\d+(?:\_\d+)*).gz

# Regular download ends up with a file name including heaps of 
# redirect-related query variables, we need sth. more plain
WGET_OPTS    = -O $(PARTIALDIR)/$(DISTNAME).gz

CONFIGURE_SCRIPTS =
TEST_SCRIPTS = 
BUILD_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom: DOCDEST=$(DESTDIR)$(docdir)/$(NAME)
install-custom:
	mkdir -p $(DESTDIR)$(mandir)/man8
	cp $(WORKDIR)/$(DISTNAME) $(WORKDIR)/mkrdns
	pod2man --section=8 $(WORKDIR)/mkrdns > $(DESTDIR)$(mandir)/man8/mkrdns.8
	ginstall -m755 -D $(WORKDIR)/mkrdns $(DESTDIR)$(bindir)/mkrdns
	ginstall -m644 -D $(FILEDIR)/changelog.CSW $(DOCDEST)/changelog.CSW
	@$(MAKECOOKIE)
