# TODO
# - Move this to a pymodules/ subdirectory with the rest of the
#   python modules (similar to the cpan directory).
NAME = pylxml
VERSION = 2.2.4
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = Easy to use and powerful libxml2/libxslt binding for Python
define BLURB
  lxml is a Pythonic binding for the libxml2 and libxslt libraries. It is
  unique in that it combines the speed and feature completeness of these
  libraries with the simplicity of a native Python API, mostly compatible
  but superior to the well-known ElementTree API.
endef

VENDOR_URL   = http://codespeak.net/lxml/
MASTER_SITES = http://pypi.python.org/packages/source/l/lxml/
DISTNAME     = lxml-$(VERSION)
DISTFILES    = $(DISTNAME).tar.gz
UFILES_REGEX = lxml-(\d+(?:\.\d+)*).tar.gz

# See http://codespeak.net/lxml/index.html#license
LICENSE = doc/licenses/BSD.txt

PACKAGES = CSWpy-lxml
CATALOGNAME = py_lxml

RUNTIME_DEP_PKGS = CSWlibxml2 CSWlibxslt CSWzlib

EXTRA_PAX_ARGS = '-s,CHANGES.txt,changelog,p'

include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(CATALOGNAME)
post-install-modulated: DOCS=CHANGES.txt CREDITS.txt IDEAS.txt
post-install-modulated:
	ginstall -d $(DOCDEST)
	cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	cp $(addprefix $(WORKSRC)/,$(DOCS)) $(DOCDEST)
	@$(MAKECOOKIE)
