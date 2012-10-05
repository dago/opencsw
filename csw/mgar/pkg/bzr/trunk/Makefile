# $Id: Makefile 19383 2012-10-05 10:07:53Z bilko50000 $
#

NAME = bzr
VERSION = 2.5.1
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = Next generation distributed version control
define BLURB
	Bazaar is a distributed revision control system. It allows team members
	to branch and merge upstream code very easily.
endef

MASTER_SITES = http://launchpad.net/bzr/2.5/$(VERSION)/\+download/
DISTFILES    = $(DISTNAME).tar.gz
LICENSE      = COPYRIGHT
PACKAGES     = CSWbzr

RUNTIME_DEP_PKGS  = CSWpython
RUNTIME_DEP_PKGS += CSWpy-crypto
RUNTIME_DEP_PKGS += CSWpy-paramiko

include gar/category.mk

