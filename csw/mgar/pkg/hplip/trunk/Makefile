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

PACKAGING_PLATFORMS = solaris10-i386  += CSWlibjpeg7

PATCHFILES += 0001-add-strnlen.patch
PATCHFILES += 0002-set-csw-path-hpijs.cpp.patch
PATCHFILES += 0004-set-csw-path-foomatPATCHFILES += 0005-set-csw-path-utils.h.patch
PATCHFILES += 0006-set-csw-path-hpps.patch
PATCHFILES += 0007-swap-ldflags-Makefile.in.patch
PATCHFILES += 0008-add-strcasestr-hp.c.patch
PATCHFILES += 0009-add-getdomainname-def-HPCupsFilter.cpp.patch
PATCHFILES += 0010-include-math.h.ErnieFilter.cpp.patch

PACKAGES += CSWlibhpip0
CATALOGNAME_CSWlibhpip0 = libhpip0
SPKG_DESC_CSWlibhpip0 += $(DESCRIPTION), libhpip
PKGFILES_CSWlibhpip0 += $(call baseisadirs,$(libdir),libhpip\.so\.0\.0\.1)
PKGFILES_CSWlibhpip0 += $(call baseisadirs,$(libdir),libhpip\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibhpip0 += $(DESCRIPTION), libhpip.so.0
CHECKPKG_OVERRIDES_CSWlibhpip0 += bad-rpath-entry

PACKAGES += CSWlibhpmud0
CATALOGNAME_CSWlibhpmud0 = libhpmud0
SPKG_DESC_CSWlibhpmud0 += $(DESCRIPTION), libhpmud
PKGFILES_CSWlibhpmud0 += $(call baseisadirs,$(libdir),libhpmud\.so\.0\.0\.6)
PKGFILES_CSWlibhpmud0 += $(call baseisadirs,$(libdir),libhpmud\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibhpmud0 += $(DESCRIPTION), libhpmud.so.0
# need /usr/sfw/lib/libusb.so
CHECKPKG_OVERRIDES_CSWlibhpmud0 += bad-rpath-entry

PACKAGES += CSWhplip-dev
CATALOGNAME_CSWhplip-dev = hplip_dev
SPKG_DESC_CSWhplip-dev += $(DESCRIPTION), development files
PKGFILES_CSWhplip-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWhplip-dev += CSWlibhpmud0
RUNTIME_DEP_PKGS_CSWhplip-dev += CSWlibhpip0

PACKAGES +10-sparc

P# ACKAGES = CSWhplip
OBSOLETED_BY_CSWhplip = CSWhpijs
SPKG_DESC_CSWhplip = $(DESCRIPTION) Inkjet driver
RUNTIME_DEP_PKGS_CSWhpRUNTIME_DEP_PKGS_CSWhplip += CSWlibcups2
RUNTIME_DEP_PKGS_CSWhplip += CSWlibcupsimage2
RUNTIME_DEP_PKGS_CSWhplip += CSWlibsane1
RUNTIME_DEP_PKGS_CSWhplip += CSWlibdbus1-3
RUNTIME_DEP_PKGS_CSWhplip += CSWlibhpmud0
RUNTIME_DEP_PKGS_CSWhplip += CSWlibhpip012.2/upgrading.html
CHECKPKG_OVERRIDES_CSWhplip += file-with-bad-content|/usr/share|root$(NAME)-$(VERSION)/u/doc/hplip-3.12.2/upgrading.html
CHECKPKG_OVERRIDES_CSWhplip += file-with-bad-content|/usr/share|root$(NAME)-$(VERSION)/uninstalling.html
CHECKPKG_OVERRIDES_CSWhplip += bad-rpath-entry
CHECKPKG_OVERRIDES_CSWhplip += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWhplip += catalogname-does-not-start-with-py_


# not interested in dll.conf
EXTRA_MERGE_EXCLUDE_FILES += /etc/sane.d.*
# not interested in 56-hpmud.rules
EXTRA_MERGE_EXCLUDE_FILES += /etc/udev.*
# not interested in systemd stuff
EXTRA_MERGE_EXCLUDE_FILES += /usr/lib.*
# not interested in hal stuff
EXTRA_MERGE_EXCLUDE_FILES += /usr/share.*

EXTRA_LINKER_FLAGS_SOS12U3 += -norunpath -xnorunpath
EXTRA_LINKER_FLAGS += $(EXTRA_LINKER_FLAGS_$(GARCOMPILER))
EXTRA_INC += /usr/sfw/include
EXTRA_LIB += /usr/sfw/lib
EXTRA_CPPFLAGS_SOS12U3 += -features=extensions
EXTRA_CPPFLAGS += $(EXTRA_CPPFLAGS_$(GARCOMPILER))
STRIP_LIBTOOL = 1
EXTRAC_CONFIGURE_ENV += hplip_confdir=$(sysconfdir)/hp

CONFIGURE_ARGS = $(DIRPATHS)
# CONFIGURE_ARGS += --enable-hpijs-only-build
# e-hpijs-only-build
CONFIGURE_ARGS += --enable-hpijs-install
CONFIGURE_ARGS += --with-hpppddir=/opt/csw/share/cups/model/HP
# CONFIGURE_ARGS += --enableCONFIGURE_ARGS += --disable-network-build
# CONFIGURE_ARGS += --disable-scan-build
# CONFIGURE_ARGS += --disable-gui-build
# CONFIGURE_ARGS += --disable-fax-build
CONFIGURE_ARGS += --enable-libusb01_enableCONFIGURE_ARGS += --with-systraydir=$(sysconfdir)/xdg/autostart
CONFIGURE_ARGS += --with-icondir=$(datadir)/icons/hp
CONFIGURE_ARGS +=  --with-mimedir=$(sysconfdir)/cups
CONFIGURE_ARGS +=  --with-cupsbackenddir=$(libdir)/cups/backend
CONFIGURE_ARGS +=  --with-cupsfilterdir=$(libdir)/cups/filter
CONFIGURE_ARGS +=  --with-drvdir=$(libdir)/cups/drv/hp

include gar/category.mk

post-install:
	ginstall -m 755 -d $(DESTDIR)$(libdir)/cups/filter
	ginstall -m 755 -d $(DESTDIR)$(sysconfdir)/hp
	ginstall -m 755 $(WORKSRC)/prnt/filters/hpps $(DESTDIR)$(libdir)/cups/filter
	ginstall -m 644 $(WORKSRC)/hplip.conf $(DESTDIR)$(sysconfdir)/hp
	$(MAKECOOKIES)
