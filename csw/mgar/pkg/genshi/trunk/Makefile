NAME    = Genshi
VERSION = 0.7
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = Python toolkit for generation of output for the web
define BLURB
	Genshi is a Python library that provides an integrated set of 
	components for parsing, generating, and processing HTML, XML 
	or other textual content for output generation on the web
endef

MASTER_SITES = http://ftp.edgewall.com/pub/genshi/
DISTFILES = $(NAME)-$(VERSION).tar.gz

UFILES_REGEX = (\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWgenshi
CATALOGNAME = genshi
RUNTIME_DEP_PKGS_CSWgenshi += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWgenshi += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWgenshi += CSWlibpython2-7-1-0

VENDOR_URL = http://genshi.edgewall.org/

TEST_SCRIPTS =

# This is a legacy name, don't change for now
CHECKPKG_OVERRIDES_CSWgenshi += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWgenshi += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWgenshi += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.7/site-packages/genshi/template/tests/plugin.py
CHECKPKG_OVERRIDES_CSWgenshi += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.6/site-packages/genshi/template/tests/plugin.py
CHECKPKG_OVERRIDES_CSWgenshi += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.7/site-packages/genshi/template/tests/plugin.py
CHECKPKG_OVERRIDES_CSWgenshi += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.6/site-packages/genshi/template/tests/plugin.py


include gar/category.mk

