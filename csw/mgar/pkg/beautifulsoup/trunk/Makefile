GARNAME = beautifulsoup
GARVERSION = 3.1.0.1
CATEGORIES = lib

EXT_NAME = BeautifulSoup

DESCRIPTION = A Python HTML/XML parser
define BLURB
  Beautiful Soup is a Python HTML/XML parser designed for quick turnaround
  projects like screen-scraping. Three features make it powerful:

  1. Beautiful Soup won't choke if you give it bad markup. It yields a parse
     tree that makes approximately as much sense as your original document. This
     is usually good enough to collect the data you need and run away.
  2. Beautiful Soup provides a few simple methods and Pythonic idioms for
     navigating, searching, and modifying a parse tree: a toolkit for dissecting a
     document and extracting what you need. You don't have to create a custom
     parser for each application.
  3. Beautiful Soup automatically converts incoming documents to Unicode and
     outgoing documents to UTF-8. You don't have to think about encodings, unless
     the document doesn't specify an encoding and Beautiful Soup can't autodetect
     one. Then you just have to specify the original encoding.
endef

MASTER_SITES = http://www.crummy.com/software/$(EXT_NAME)/download/
DISTFILES  = $(EXT_NAME).tar.gz
WORKSRC = $(WORKDIR)/$(EXT_NAME)-$(GARVERSION)

SPKG_CLASSES = none cswpycompile

ARCHALL = 1
CONFIGURE_SCRIPTS = 
BUILD_SCRIPTS = beautifulsoup
TEST_SCRIPTS = 
INSTALL_SCRIPTS = beautifulsoup

PACKAGES = CSWbeautifulsoup
REQUIRED_PKGS_CSWbeautifulsoup = CSWpython CSWcswclassutils

PROTOTYPE_FILTER = awk ' \
  $$$$3 ~/.*\.py$$$$/ { $$$$2 = "pycompile" } \
  { print }'

build-beautifulsoup:
	(cd $(WORKSRC); python setup.py build)

install-beautifulsoup:
	(cd $(WORKSRC); python setup.py install --root=$(DESTDIR))

include gar/category.mk
