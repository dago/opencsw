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

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

# CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_SCRIPTS =
BUILD_ARGS += UISTYLE=text

include gar/category.mk

