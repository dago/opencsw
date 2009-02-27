GARNAME = axel
GARVERSION = 2.3
CATEGORIES = utils

DESCRIPTION = Download accelerator
define BLURB
  Axel tries to accelerate downloads by using multiple connections (possibly 
  to multiple servers) for one download. Because of its size, it might be 
  very useful on bootdisks or other small systems as a wget replacement
endef

MASTER_SITES = http://alioth.debian.org/frs/download.php/2717/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = http://alioth.debian.org/frs/?group_id=100070
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

PROTOTYPE_FILTER = awk '\
	$$$$3 ~ /axelrc.CSW$$$$/ { $$$$2 = "cswcpsampleconf" } \
	 { print }'

include gar/category.mk

pre-build-modulated:
	@perl -pi -e 's/-Wall//g' $(WORKSRC)/Makefile

post-install-modulated:
	@mv $(DESTDIR)$(sysconfdir)/axelrc \
		$(DESTDIR)$(sysconfdir)/axelrc.CSW
