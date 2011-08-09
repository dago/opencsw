NAME = guilt
VERSION = 0.35
CATEGORIES = utils

DESCRIPTION = quilt on top of git
define BLURB
  Guilt (Git Quilt) adds functionality similar to quilt, Mercurial
  Queues or Stacked git to git. the main distinguishing feature from
  other quilt-like porcelains is the format of the patches directory.
  All information is stored as plain text - a series file and the
  patches (one per file). This easily lends itself to versioning the
  patches using git or whatever other SCM.
endef

MASTER_SITES = http://www.kernel.org/pub/linux/kernel/people/jsipek/guilt/
DISTFILES  = $(DISTNAME).tar.bz2
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom
PATCHFILES += 0001-use-bash-for-scripts.patch 0002-don-t-rebuild-man-pages.patch

LICENSE = COPYING
ARCHALL = 1

include gar/category.mk

install-custom:
	$(INSTALL_ENV) gmake -C $(WORKSRC) INSTALL=ginstall PREFIX=/opt/csw install install-doc
