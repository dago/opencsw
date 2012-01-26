NAME = String-CRC32
VERSION = 1.4
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = SOENKE

DESCRIPTION = Interface for cyclic redundency check generation
define BLURB
  The CRC32 module calculates CRC sums of 32 bit lenghts. It generates the
  same CRC values as ZMODEM, PKZIP, PICCHECK and many others.  Despite its
  name, this module is able to compute the checksum of strings as well as of
  files.
endef

DISTFILES += COPYING

PACKAGES = CSWpmstringcrc32
CATALOGNAME = pm_stringcrc32

include gar/category.mk

post-install-modulated:
	@echo " ==> Post-install for $(NAME) (custom)"
	@( cd $(WORKSRC) ; \
	  gmake metafile ; \
	  cp $(NAME)-$(VERSION)/META.yml . )
	@$(MAKECOOKIE)
