# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = exif-py
VERSION = 2.0.1
GIT_VERSION = $(VERSION)

CATEGORIES = python

DESCRIPTION = Extract Exif metadata from tiff and jpeg files 
define BLURB
  Long description
endef

MASTER_SITES =
GIT_REPOS = http://github.com/ianare/$(NAME).git
GIT_TREEISH_exif-git.git = $(GIT_VERSION)

LICENSE = LICENSE.txt

ARCHALL_CSWpy-exif-py = 1

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

