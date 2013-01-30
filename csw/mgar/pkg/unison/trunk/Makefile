# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = unison
VERSION = 2.40.102
GARTYPE = v2

DESCRIPTION = File Synchronizer 
define BLURB
 Unison is a file-synchronization tool for Unix and Windows. It allows two replicas of a collection of files and directories to be stored on different hosts (or different disks on the same host), modified separately, and then brought up to date by propagating the changes in each replica to the other.
endef

MASTER_SITES = http://www.seas.upenn.edu/~bcpierce/unison//download/releases/stable/
DISTFILES  = $(DISTNAME).tar.gz

BUILD_DEP += CSWocaml

# only example
CHECKPKG_OVERRIDES_CSWunison += file-with-bad-content|/usr/local|root/opt/csw/bin/unison

# CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

BUILD_ARGS += UISTYLE=text
CFLAGS = 

include gar/category.mk

install-custom:
	ginstall -m 755 -d $(DESTDIR)$(bindir)
	ginstall -m 755  $(WORKSRC)/unison $(DESTDIR)$(bindir)
	@$(MAKECOOKIE)
