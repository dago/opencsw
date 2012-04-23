# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = pymilter
VERSION = 0.9.5
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = Python Milter extension
define BLURB
  This is a python extension module to enable python scripts to attach to
  Sendmail's libmilter API, enabling filtering of messages as they arrive.
  Since it's a script, you can do anything you want to the message - screen
  out viruses, collect statistics, add or modify headers, etc.  You can, at
  any point, tell Sendmail to reject, discard, or accept the message.
endef

MASTER_SITES = http://downloads.sourceforge.net/project/pymilter/pymilter
DISTFILES  = $(DISTNAME).tar.gz

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

RUNTIME_DEP_PKGS_CSWpy-pymilter += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-pymilter += CSWlibmilter
CHECKPKG_OVERRIDES_CSWpy-pymilter += surplus-dependency|CSWlibmilter

LICENSE = COPYING

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

include gar/category.mk

