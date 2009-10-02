# TODO
# - Move this to a pymodules/ subdirectory with the rest of the
#   python modules (similar to the cpan directory).
GARNAME = pylxml
GARVERSION = 2.2.2
CATEGORIES = python

DESCRIPTION = Pythonic binding for the libxml2 and libxslt libraries
define BLURB
  lxml is a Pythonic binding for the libxml2 and libxslt libraries. It is
  unique in that it combines the speed and feature completeness of these
  libraries with the simplicity of a native Python API, mostly compatible
  but superior to the well-known ElementTree API.
endef

SPKG_SOURCEURL = http://codespeak.net/lxml/
MASTER_SITES = http://pypi.python.org/packages/source/l/lxml/
DISTNAME = lxml-$(GARVERSION)
DISTFILES  = $(DISTNAME).tar.gz
UFILES_REGEX = lxml-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWpylxml
CATALOGNAME = py_lxml

REQUIRED_PKGS = CSWlibxml2 CSWlibxslt CSWzlib

EXTRA_PAX_ARGS = '-s,CHANGES.txt,changelog,p'

include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(CATALOGNAME)
post-install-modulated: DOCS=CHANGES.txt CREDITS.txt IDEAS.txt
post-install-modulated:
	ginstall -d $(DOCDEST)
	cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	cp $(addprefix $(WORKSRC)/,$(DOCS)) $(DOCDEST)
	@$(MAKECOOKIE)
