GARNAME = scrollkeeper
GARVERSION = 0.3.14
CATEGORIES = utils

DESCRIPTION = a cataloging system for documentation on open systems
define BLURB
 ScrollKeeper is a cataloging system for documentation on open systems. It
 manages documentation metadata (as specified by the Open Source Metadata
 Framework(OMF)) and provides a simple API to allow help browsers to find,
 sort, and search the document catalog. It will also be able to communicate
 with catalog servers on the Net to search for documents which are not on the
 local system. 
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

SPKG_SOURCEURL = http://scrollkeeper.sourceforge.net/

LICENSE = COPYING

REQUIRED_PKGS = CSWggettextrt CSWiconv CSWlibxml2 CSWlibxslt CSWzlib

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=11543
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

PATCHFILES = Makefile.in.diff

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

include gar/category.mk

localstatedir = /var/$(prefix)
