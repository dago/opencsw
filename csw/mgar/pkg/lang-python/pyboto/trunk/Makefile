NAME = pyboto
VERSION = 1.9b
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = Python interfaces to Amazon Web Services
define BLURB
  An integrated interface to current and future infrastructural services
  offered by Amazon Web Services. The goal of boto is to provide a very
  simple, easy to use, lightweight wrapper around the Amazon services.
endef

PACKAGES = CSWpy-boto
CATALOGNAME = py_boto

VENDOR_URL     = http://code.google.com/p/boto/
MASTER_SITES   = $(GOOGLE_MIRROR)
GOOGLE_PROJECT = boto
DISTNAME       = $(GOOGLE_PROJECT)-$(VERSION)
DISTFILES      = $(DISTNAME).tar.gz
UFILES_REGEX   = $(GOOGLE_PROJECT)-(\d+(?:\.\d+)*).tar.gz

LICENSE = files/COPYING
ARCHALL = 1

include gar/category.mk

post-install-modulated:
	ginstall -D $(WORKSRC)/README \
		$(DESTDIR)$(docdir)/$(CATALOGNAME)/README
	@$(MAKECOOKIE)

# Install changelog.CSW
post-merge: $(foreach P,$(_PKG_SPECS),install-changelog-$P)
install-changelog-%:
	ginstall -D $(FILEDIR)/changelog.CSW \
		$(PKGROOT)$(docdir)/$(call catalogname,$*)/changelog.CSW
	@$(MAKECOOKIE)
