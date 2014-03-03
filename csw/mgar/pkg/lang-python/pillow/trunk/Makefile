# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = Pillow
VERSION = 2.3.0b
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = Python Imaging Library (fork)
define BLURB
  Pillow is the "friendly" PIL fork by Alex Clark and Contributors. PIL is the Python Imaging Library by Fredrik Lundh and Contributors.
endef

GIT_REPOS = git://github.com/python-imaging/Pillow.git
# DISTFILES  = $(DISTNAME).zip

LICENSE = docs/COPYING

PACKAGES += CSWpy-pillow
RUNTIME_DEP_PKGS_CSWpy-pillow += CSWlibtiff5
RUNTIME_DEP_PKGS_CSWpy-pillow += CSWlibwebp4
RUNTIME_DEP_PKGS_CSWpy-pillow += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWpy-pillow += CSWlibz1
RUNTIME_DEP_PKGS_CSWpy-pillow += CSWlibtcl8-5
RUNTIME_DEP_PKGS_CSWpy-pillow += CSWlibpython2-7-1-0
RUNTIME_DEP_PKGS_CSWpy-pillow += CSWlibtk8-5
RUNTIME_DEP_PKGS_CSWpy-pillow += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWpy-pillow += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-pillow += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWpy-pillow += CSWliblcms2-2

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

