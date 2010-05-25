GARNAME = pyboto
GARVERSION = 1.9b
CATEGORIES = python

DESCRIPTION = Python interfaces to Amazon Web Services
define BLURB
  An integrated interface to current and future infrastructural services
  offered by Amazon Web Services. The goal of boto is to provide a very
  simple, easy to use, lightweight wrapper around the Amazon services.
endef

VENDOR_URL     = http://code.google.com/p/boto/
MASTER_SITES   = $(GOOGLE_MIRROR)
GOOGLE_PROJECT = boto
DISTNAME       = $(GOOGLE_PROJECT)-$(GARVERSION)
DISTFILES      = $(DISTNAME).tar.gz
UFILES_REGEX   = $(GOOGLE_PROJECT)-(\d+(?:\.\d+)*).tar.gz

ARCHALL = 1

include gar/category.mk
