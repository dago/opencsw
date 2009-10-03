# TODO
# - Move this to a pymodules/ subdirectory with the rest of the
#   python modules (similar to the cpan directory).
GARNAME = pysoappy
GARVERSION = 0.11.4
CATEGORIES = python

DESCRIPTION = SOAP library for python
define BLURB
  This package contains the SOAPpy Python module, which implements a high-
  level interface to Simple Object Access Protocol (SOAP) functions from
  Python. It includes functionality for acting as a SOAP server, client,
  or proxy, and includes both building and parsing functions. It has been
  tested against a wide array of other SOAP clients and servers, and is a
  very robust and well-rounded implementation of the SOAP protocol.
  
  SOAPpy is not actively supported by upstream anymore - please do not
  consider to use it in new projects! All functions were merged into ZSI
endef

SPKG_SOURCEURL = http://pywebsvcs.sourceforge.net/
MASTER_SITES = $(SF_MIRRORS)
SF_PROJ = pywebsvcs
DISTNAME = SOAPpy-$(GARVERSION)
DISTFILES = $(DISTNAME).tar.gz

ARCHALL = 1
PACKAGES = CSWpysoappy
CATALOGNAME = py_soappy
REQUIRED_PKGS = CSWpyfpconst CSWpyxml

# import __future__ statements need to occur first within a file
# SyntaxError: from __future__ imports must occur at the beginning of the file
PATCHFILES = 001-place-import-future-first.patch

# No tests available
TEST_SCRIPTS = 

include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(CATALOGNAME)
post-install-modulated:
	ginstall -d $(DOCDEST)
	cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	cp $(WORKSRC)/docs/* $(DOCDEST)
	@$(MAKECOOKIE)
