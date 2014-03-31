NAME = hplip
VERSION = 3.14.3
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
PATCHFILES += 0004-set-csw-path-foomatPATCHFILES += 0005-set-csw-path-utils.h.patch
PATCHFILES += 0006-set-csw-path-hpps.patch
PATCHFILES += 0007-swap-ldflags-Makefile.in.patch
PATCHFILES += 0008-add-strcasestr-hp.c.patch
PATCHFILES += 0009-add-getdomainname-def-HPCupsFilter.cpp.patch
PATCHFILES += 0010-include-math.h.ErnieFilter.cpp.patch

EXTRA_LINKER_FLAGS_SOS12U3 += -norunpath -xnorunpath
EXTRA_LINKER_FLAGS += $(EXTRA_LINKER_FLAGS_$(GARCOMPILER))
EXTRA_INC += /usr/sfw/include
EXTRA_LIB += /usr/sfw/lib
EXTRA_CPPFLAGS_SOS12U3 += -features=extensions
EXTRA_CPPFLAGS += $(EXTRA_CPPFLAGS_$(GARCOMPILER))
STRIP_LIBTOOL = 1

CONFIGURE_ARGS = $(DIRPATHS)
# CONFIGURE_ARGS += --enable-hpijs-only-build
# e-hpijs-only-build
CONFIGURE_ARGS += --enable-hpijs-install
CONFIGURE_ARGS += --with-hpppddir=/opt/csw/share/cups/model/HP
# CONFIGURE_ARGS += --enableCONFIGURE_ARGS += --disable-network-build
# CONFIGURE_ARGS += --disable-scan-build
# CONFIGURE_ARGS += --disable-gui-build
# CONFIGURE_ARGS += --disable-fax-build
CONFIGURE_ARGS += --enable-libusb01_enable-hpcups-only-build

CHECKPKG_OVERRIDES_CSWhplip += file-with-bad-content|/usr/share|root$(NAME)-$(VERSION)re/doc/hplip-3.12.2/upgrading.html
CHECKPKG_OVERRIDES_CSWhplip += file-with-bad-content|/usr/share|root$(NAME)-$(VERSION)/uninstalling.html

include gar/category.mk

post-install:
	ginstall -m 755 -d $(DESTDIR)$(libdir)/cups/filter
	ginstall -m 755 -d $(DESTDIR)$(sysconfdir)/hp
	ginstall -m 755 $(WORKSRC)/prnt/filters/hpps $(DESTDIR)$(libdir)/cups/filter
	ginstall -m 644 $(WORKSRC)/hplip.conf $(DESTDIR)$(sysconfdir)/hp
	$(MAKECOOKIES)
