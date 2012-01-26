NAME = convmv
VERSION = 1.14
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Converts filenames from one encoding to another
define BLURB
  convmv is meant to help convert a single filename, a directory tree
  and the contained files or a whole filesystem into a different encoding.
  It just converts the filenames, not the content of the files. A special
  feature of convmv is that it also takes care of symlinks, also converts
  the symlink target pointer in case the symlink target is being
  converted, too.
  
  All this comes in very handy when one wants to switch over from old
  8-bit locales to UTF-8 locales. It is also possible to convert
  directories to UTF-8 which are already partly UTF-8 encoded. convmv is
  able to detect if certain files are UTF-8 encoded and will skip them by
  default. To turn this smartness off use the --nosmart switch.
endef

MASTER_SITES = http://www.j3e.de/linux/convmv/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
LICENSE = GPL2
ARCHALL = 1

CONFIGURE_SCRIPTS = 
BUILD_SCRIPTS = 

INSTALL_ARGS = MANDIR=$(mandir) PREFIX=$(prefix)
TEST_ARGS = TAR=gtar

REINPLACEMENTS += perl
REINPLACE_MATCH_perl = /usr/bin/perl
REINPLACE_WITH_perl = /opt/csw/bin/perl
REINPLACE_FILES_perl += convmv

REINPLACEMENTS += ginstall
REINPLACE_MATCH_ginstall = \tinstall
REINPLACE_WITH_ginstall = \tginstall
REINPLACE_FILES_ginstall += Makefile

include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(NAME)
post-install-modulated:
	@ginstall -d $(DOCDEST)
	@(cd $(WORKSRC); cp CREDITS Changes TODO $(DOCDEST))
	@cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
