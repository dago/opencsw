# $Id: Makefile 14849 2011-06-21 09:07:58Z skayser $
# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! Remove /usr references in $(docdir) and drop overrides
# ! Determine how to run the integrated test suite (iptest/nose) and run it
# ! Package contains ipythonx which doesn't work w/o wxpython (can we skip
#   shipping ipythonx?)
# 
NAME    = ipython
VERSION = 0.12.1
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = Enhanced interactive python shell
define BLURB
endef

MASTER_SITES = http://archive.ipython.org/release/$(VERSION)/
DISTFILES    = $(NAME)-$(VERSION).tar.gz
ARCHALL      = 1
PACKAGES     = CSWipython
CATALOGNAME  = ipython

CHECKPKG_OVERRIDES_CSWipython += file-with-bad-content|/usr/share|root/opt/csw/lib/python/site-packages/IPython/core/usage.py
CHECKPKG_OVERRIDES_CSWipython += file-with-bad-content|/usr/share|root/opt/csw/lib/python/site-packages/IPython/external/mglob/_mglob.py
CHECKPKG_OVERRIDES_CSWipython += file-with-bad-content|/usr/local|root/opt/csw/lib/python/site-packages/IPython/core/magic.py
CHECKPKG_OVERRIDES_CSWipython += file-with-bad-content|/usr/local|root/opt/csw/lib/python/site-packages/IPython/utils/tests/test_path.py
CHECKPKG_OVERRIDES_CSWipython += file-with-bad-content|/usr/local|root/opt/csw/lib/python/site-packages/IPython/external/pexpect/_pexpect.py
CHECKPKG_OVERRIDES_CSWipython += file-with-bad-content|/usr/local|root/opt/csw/lib/python/site-packages/IPython/external/path/_path.py

SKIPTEST = 1

include gar/category.mk
