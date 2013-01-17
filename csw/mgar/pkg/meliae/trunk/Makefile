# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = meliae
VERSION = 0.4.0

CATEGORIES = python

DESCRIPTION = Python memory profiler
define BLURB
endef

MASTER_SITES = https://launchpad.net/meliae/trunk/0.4/+download/
DISTFILES  = $(DISTNAME).tar.gz

LICENSE = COPYING.txt

ARCHALL_CSWpy-meliae = 1
CHECKPKG_OVERRIDES_CSWpy-meliae += surplus-dependency|CSWpython

include gar/category.mk

