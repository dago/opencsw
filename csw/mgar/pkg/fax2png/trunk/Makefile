NAME = fax2png
VERSION = 1.0

DESCRIPTION = Multipage 1-bit TIFF (fax or scan) to PNG image converter
define BLURB
endef

MASTER_SITES = http://www.boutell.com/fax2png/
DISTNAME = $(NAME)
DISTFILES += $(DISTNAME).tar.gz
DISTFILES += COPYING

PACKAGES += CSWfax2png
SPKG_DESC_CSWfax2png = Multipage 1-bit TIFF (fax or scan) to PNG image converter
RUNTIME_DEP_PKGS_CSWfax2png += CSWlibtiff3
RUNTIME_DEP_PKGS_CSWfax2png += CSWlibpng12-0

# This is for the contributed CGI script, probably pull in when needed
CHECKPKG_OVERRIDES_CSWfax2png += missing-dependency|CSWperl

BUILD64 = 1
ISAEXEC = 1 $(WORKDIR)/$(NAME)

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
	ginstall -D $(WORKSRC)/fax2png.pl $(DESTDIR)$(sharedstatedir)/doc/$(NAME)/fax2png.