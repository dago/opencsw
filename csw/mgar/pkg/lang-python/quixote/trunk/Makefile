# $Id$
NAME = quixote
VERSION = 2.7
CATEGORIES = python

DESCRIPTION = Web framework targeted at flexibility and high-performance
define BLURB
  Quixote is a framework for writing Web-based applications using Python.
  Its goals are flexibility and high-performance, in that order. The two
  major versions of Quixote, version 1 and version 2, are simliar but
  incompatible with each other. Both are actively maintained and are used
  by numerous public sites.
endef

VENDOR_URL   = http://quixote.ca/
MASTER_SITES = http://quixote.ca/releases/
DISTNAME     = $(subst q,Q,$(NAME))-$(VERSION)
DISTFILES    = $(DISTNAME).tar.gz

PACKAGES     = CSWpy-quixote
CATALOGNAME  = py_quixote

TEST_SCRIPTS = 

include gar/category.mk

post-install-modulated:
	mkdir -p $(DESTDIR)$(docdir)/$(PACKAGES)
	gcp -r $(WORKSRC)/doc/* $(DESTDIR)$(docdir)/$(PACKAGES)
	@$(MAKECOOKIE)

# Install changelog.CSW
post-merge: $(foreach P,$(_PKG_SPECS),install-changelog-$P)
install-changelog-%:
	ginstall -D $(FILEDIR)/changelog.CSW \
		$(PKGROOT)$(docdir)/$(call catalogname,$*)/changelog.CSW
	@$(MAKECOOKIE)
