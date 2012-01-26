NAME = ncdu
VERSION = 1.8
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Ncurses version of the famous old 'du' unix
define BLURB
  As the name already suggests, ncdu is an ncurses version of the famous
  old 'du' unix command. It provides a fast and easy interface to your
  harddrive. Where is your disk space going? Why is your home directory
  that large? ncdu can answer those questions for you in just a matter of
  seconds!
endef

MASTER_SITES = http://dev.yorhel.nl/download/
DISTFILES = $(NAME)-$(VERSION).tar.gz

VENDOR_URL = http://dev.yorhel.nl/ncdu/

BUILD_DEP_PKGS += CSWlibncurses-dev
RUNTIME_DEP_PKGS_CSWncdu += CSWlibncursesw5

EXTRA_INC = /opt/csw/include/ncursesw

# ncdu doesn't come with a test suite
TEST_SCRIPTS = 

include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(NAME)
post-install-modulated:
	ginstall -d $(DOCDEST)
	cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
