# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = xml2rfc
VERSION = 2.4.12
CATEGORIES = python

DESCRIPTION = Xml2rfc generates RFCs and IETF drafts from document source in XML

MASTER_SITES = $(PYPI_MIRROR)
DISTFILES += $(DISTNAME).tar.gz

# This is essentially an application, we don't need 2.6
MODULATIONS_PYTHON_VERSION = 2_7

PACKAGES += CSWxml2rfc
SPKG_DESC_CSWxml2rfc = Generates RFCs and IETF drafts from document source in XML
# PKGFILES is catchall
ARCHALL_CSWxml2rfc = 1
# This is a comment
CHECKPKG_OVERRIDES_CSWxml2rfc += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.7/site-packages/xml2rfc-2.4.12-py2.7.egg-info/PKG-INFO

# This is essentially an application
CHECKPKG_OVERRIDES_CSWxml2rfc += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWxml2rfc += catalogname-does-not-start-with-py_

# This is for /opt/csw/share/xml2rfc
REINPLACE_USRSHARE += xml2rfc/parser.py

include gar/category.mk
