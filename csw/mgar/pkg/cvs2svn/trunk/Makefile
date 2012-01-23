NAME = cvs2svn
VERSION = 2.3.0
CATEGORIES = utils

DESCRIPTION = CVS to svn/git/hg/bzr Repository Converter
define BLURB
  cvs2svn is a tool for migrating a CVS repository to Subversion or git. The main design goals
  are robustness and 100% data preservation. cvs2svn can convert just about any CVS repository
  we've ever seen, including gcc, Mozilla, FreeBSD, KDE, GNOME...
endef

MASTER_SITES = http://cvs2svn.tigris.org/files/documents/1462/46528/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://cvs2svn.tigris.org/

ARCHALL = 1
PYCOMPILE = 1
RUNTIME_DEP_PKGS = CSWpython CSWrcs
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS)

CONFIGURE_SCRIPTS =

BUILD_ARGS = man

include gar/category.mk

