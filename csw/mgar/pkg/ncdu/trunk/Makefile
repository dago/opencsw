GARNAME = ncdu
GARVERSION = 1.5
CATEGORIES = utils

DESCRIPTION = Ncurses version of the famous old 'du' unix
define BLURB
As the name already suggests, ncdu is an ncurses version of the famous old 'du'
unix command. It provides a fast and easy interface to your harddrive. Where is
your disk space going? Why is your home directory that large? ncdu can answer
those questions for you in just a matter of seconds!
endef

SPKG_SOURCEURL = http://dev.yorhel.nl/ncdu/
MASTER_SITES = http://dev.yorhel.nl/download/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS = CSWncurses

TEST_SCRIPTS = 

EXTRA_INC = /opt/csw/include/ncursesw

CONFIGURE_ARGS = $(DIRPATHS)

# - Autoconf check and replacement for non-POSIX dirfd()
# See http://sf.net/tracker/?func=detail&aid=2789779&group_id=200175&atid=972449
# - Fix for non-void return in src/delete.c:void delete_process()
# See http://sf.net/tracker/?func=detail&aid=2789781&group_id=200175&atid=972449
PATCHFILES=gar-base.diff

include gar/category.mk

pre-configure-modulated:
	@cd $(WORKSRC) && autoconf
	@$(MAKECOOKIE)

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(GARNAME)
post-install-modulated:
	@ginstall -d $(DOCDEST)
	@cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
