GARNAME = pkg_update_watch
GARVERSION = 1.0
CATEGORIES = utils

DESCRIPTION = Package updates watcher
define BLURB
   pkg-update-watch is a program aimed at be launched
   from cron and which send a mail to the administrator
   when it detects package updates are available.
endef

MASTER_SITES = 
SPKG_SOURCEURL = http://svn.blastwave.org/browser/csw/trunk/utils/pkg_update_watch/files
DISTFILES  = pkg-update-watch
DISTFILES += $(call admfiles,CSWpkgupdatewatch,prototype)
DISTFILES += pkg-update-watch.conf
DISTFILES += README.CSW

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS =

include gar/category.mk
