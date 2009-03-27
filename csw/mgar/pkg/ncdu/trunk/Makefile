GARNAME = ncdu
GARVERSION = 1.4
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

EXTRA_INC = /opt/csw/include/ncurses

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
