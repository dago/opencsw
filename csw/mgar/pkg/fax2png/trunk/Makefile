GARNAME = fax2png
GARVERSION = 1.0
CATEGORIES = utils

DESCRIPTION = 1-bit multipage TIFF (fax or scan) to PNG image converter
define BLURB
endef

MASTER_SITES = http://www.boutell.com/fax2png/
DISTFILES  = $(GARNAME).tar.gz
DISTFILES += $(call admfiles,CSWfax2png,depend)
WORKSRC = $(WORKDIR)/$(GARNAME)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

build-custom:
	@echo "==> Building fax2png in $(WORKSRC)"
	( cd $(WORKSRC); $(CC) $(CFLAGS) -c fax2png.c -o fax2png.o; $(CC) $(LDFLAGS) $(LD_OPTIONS) fax2png.o -o fax2png -lpng -lz -ltiff )
	@$(MAKECOOKIE)

install-custom:
	@echo "==> Installing fax2png in $(DESTDIR)"
	ginstall -D $(WORKSRC)/fax2png $(DESTDIR)$(bindir)/fax2png
	ginstall -D $(WORKSRC)/fax2png.1 $(DESTDIR)$(mandir)/man1/fax2png.1
	ginstall -D $(WORKSRC)/fax2png.pl $(DESTDIR)$(sharedstatedir)/doc/$(GARNAME)/fax2png.pl
	@$(MAKECOOKIE)
