GARNAME = convmv
GARVERSION = 1.14
CATEGORIES = utils

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
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
LICENSE = GPL2
ARCHALL = 1

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_SCRIPTS = 
BUILD_SCRIPTS = 

INSTALL_ARGS = MANDIR=$(mandir) PREFIX=$(prefix)
TEST_ARGS = TAR=gtar

include gar/category.mk

post-extract-modulated:
	@perl -pi -e 's|/usr/bin/perl|/opt/csw/bin/perl|' $(WORKSRC)/convmv
	@perl -pi -e 's|\tinstall|\tginstall|' $(WORKSRC)/Makefile
	@$(MAKECOOKIE)

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(GARNAME)
post-install-modulated:
	@ginstall -d $(DOCDEST)
	@(cd $(WORKSRC); cp CREDITS Changes TODO $(DOCDEST))
	@cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
