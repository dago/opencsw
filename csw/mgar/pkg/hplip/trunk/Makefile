NAME = hplip
VERSION = 3.13.3
GARTYPE = v2

MASTER_SITES = http://prdownloads.sourceforge.net/hplip/urceforge.net/hplip
DISTFILES = $(NAME)-$(VERSION).tar.gz


DESCRIPTION = HP Cups Printing and Imaging
define BLURB
	Cups printer drivers for HP non postsript printers
endef

# GARCOMPILER = GNU
GARCOMPILER = SOS12U3

PACKAGING_PLATFORMS = solaris10-i386 solaris10-sparc

P# ACKAGES = CSWhplip
OBSOLETED_BY_CSWhplip = CSWhpijs
SPKG_DESC_CSWhplip = $(DESCRIPTION) Inkjet driver
RUNTIME_DEP_PKGS_CSWhplip += CSWlibjpeg7

PATCHFILES += 0001-add-strnlen.patch
PATCHFILES += 0002-set-csw-path-hpijs.cpp.patch
PATCHFILES += 0004-set-csw-path-foomatic-rip-hplip.patch

EXTRA_LINKER_FLAGS += -norunpath -xnorunpath

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-hpijs-only-build
CONFIGURE_ARGS += --enable-hpijs-install
CONFIGURE_ARGS += --with-hpppddir=/opt/csw/share/cups/model/HP
# CONFIGURE_ARGS += --enable-hpcups-only-build

CHECKPKG_OVERRIDES_CSWhplip += file-with-bad-content|/usr/share|root$(NAME)-$(VERSION)re/doc/hplip-3.12.2/upgrading.html
CHECKPKG_OVERRIDES_CSWhplip += file-with-bad-content|/usr/share|root$(NAME)-$(VERSION)/uninstalling.html

include gar/category.mk

post-install:
	ginstall -m 755 -d $(DESTDIR)$(libdir)/cups/filter
	ginstall -m 755 $(WORKSRC)/prnt/filters/hpps $(DESTDIR)$(libdir)/cups/filter
	ginstall -m 755 $(WORKSRC)/prnt/filters/hpcac $(DESTDIR)$(libdir)/cups/filter
	$(MAKECOOKIES)
