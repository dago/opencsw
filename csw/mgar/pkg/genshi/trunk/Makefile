GARNAME    = Genshi
GARVERSION = 0.5.1
CATEGORIES = python

DESCRIPTION = Python toolkit for generation of output for the web
define BLURB
	Genshi is a Python library that provides an integrated set of 
	components for parsing, generating, and processing HTML, XML 
	or other textual content for output generation on the web
endef

MASTER_SITES           = http://ftp.edgewall.com/pub/genshi/
SPKG_SOURCEURL         = http://genshi.edgewall.org/wiki/TracDownload
DISTFILES              = $(GARNAME)-$(GARVERSION).tar.bz2
# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX           = (\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWgenshi
ARCHALL_CSWtrac = 1

CATALOGNAME_CSWgenshi  = genshi
SPKG_DESC_CSWgenshi    = $(DESCRIPTION)

TEST_SCRIPTS           =

include gar/category.mk

