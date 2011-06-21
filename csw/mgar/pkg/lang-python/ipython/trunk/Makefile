# $Id: Makefile 14849 2011-06-21 09:07:58Z skayser $
# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! Remove /usr references in $(docdir)
# ! Determine how to run the integrated test suite (iptest/nose) and run it
# 
NAME    = ipython
VERSION = 0.10.2
CATEGORIES = python

DESCRIPTION = Enhanced interactive python shell
define BLURB
endef

MASTER_SITES = http://ipython.scipy.org/dist/$(VERSION)/
DISTFILES    = $(NAME)-$(VERSION).tar.gz
ARCHALL      = 1

# /opt/csw/share/doc/ipython/ contains plenty of references, override
# them for now and focus on whether ipython actually stops segfaulting
CHECKPKG_OVERRIDES += file-with-bad-content|/usr/local
CHECKPKG_OVERRIDES += file-with-bad-content|/usr/local

SKIPTEST = 1

include gar/category.mk
