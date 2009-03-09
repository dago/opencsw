GARNAME = lzop
GARVERSION = 1.02
RELEASE = rc1
DISTVERSION = $(GARVERSION)$(RELEASE)
DISTNAME = $(GARNAME)-$(DISTVERSION)
CATEGORIES = utils

DESCRIPTION = LZO file compressor
define BLURB
  lzop is a file compressor which is very similar to gzip. lzop uses the LZO data
  compression library for compression services, and its main advantages over gzip are
  much higher compression and decompression speed (at the cost of some compression
  ratio).
endef

MASTER_SITES = http://www.lzop.org/download/
DISTFILES  = $(GARNAME)-$(GARVERSION)$(RELEASE).tar.gz

PACKAGES = CSWlzop
CATALOGNAME = lzop
SPKG_DESC = $(DESCRIPTION)
SPKG_SOURCEURL = http://www.lzop.org

REQUIRED_PKGS = CSWlzo

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

TEST_TARGET = check

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(RELEASE)

DOCS = AUTHORS NEWS README THANKS doc/magic
DOCDEST = $(DESTDIR)$(docdir)/$(GARNAME)

post-install-modulated:
	@echo " ==> Post-install for $(GARNAME) (custom)"
	@ginstall -d $(DOCDEST)
	@$(foreach DOC,$(DOCS),ginstall -m 644 $(WORKSRC)/$(DOC) $(DOCDEST);)
	@$(MAKECOOKIE)
