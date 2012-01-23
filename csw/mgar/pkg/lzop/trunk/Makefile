NAME = lzop
VERSION = 1.03
#RELEASE = rc1
#DISTVERSION = $(VERSION)$(RELEASE)
#DISTNAME = $(NAME)-$(DISTVERSION)
CATEGORIES = utils

DESCRIPTION = LZO file compressor
define BLURB
  lzop is a file compressor which is very similar to gzip. lzop uses the LZO
  data compression library for compression services, and its main advantages
  over gzip are much higher compression and decompression speed (at the cost
  of some compression ratio).
endef

MASTER_SITES = http://www.lzop.org/download/
DISTFILES  = $(NAME)-$(VERSION)$(RELEASE).tar.gz

PACKAGES = CSWlzop
CATALOGNAME = lzop
SPKG_DESC = $(DESCRIPTION)
SPKG_SOURCEURL = http://www.lzop.org

RUNTIME_DEP_PKGS = CSWlzo

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

NOISALIST = 1

include gar/category.mk

#SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(RELEASE)

DOCS = AUTHORS NEWS README THANKS doc/magic
DOCDEST = $(DESTDIR)$(docdir)/$(NAME)

post-install-modulated:
	@echo " ==> Post-install for $(NAME) (custom)"
	@ginstall -d $(DOCDEST)
	@$(foreach DOC,$(DOCS),ginstall -m 644 $(WORKSRC)/$(DOC) $(DOCDEST);)
	@$(MAKECOOKIE)
