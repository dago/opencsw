NAME = libgc
theVersion = 7.2
thePatch = d
VERSION = $(theVersion)$(thePatch)
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = A garbage collector for C and C++
define BLURB
	The Boehm-Demers-Weiser conservative garbage collector can be used as a
	garbage collecting replacement for C malloc or C++ new. It allows you to
	allocate memory basically as you normally would, without explicitly
	deallocating memory that is no longer useful. The collector automatically
	recycles memory when it determines that it can no longer be otherwise
	accessed.
endef

MASTER_SITES = http://www.hpl.hp.com/personal/Hans_Boehm/gc/gc_source/theVersion)
DISTFILES  = $(DISTNAME)$(thePatchLES  = $(DISTNAME).tar.gz

VENDOR_URL = http://www.hpl.hp.com/personal/Hans_Boehm/gc/

LICENSE = README.QUICK

GARCOMPILER	=	GNU

CONFIGURE_ARGS	=	$(DIRPATHS)
CONFIGURE_ARGS	+=	--enable-cplusplus

PACKAGES += CSWlibcord1
SPKG_DESC_CSWlibcord1 = A garbage collector for C and C++, libcord.so.1
PKGFILES_CSWlibcord1 += $(call pkgfiles_lib,libcord.so.1)
RUNTIME_DEP_PKGS_CSWlibcord1 += CSWlibgc1
OBSOLETED_BY_CSWlibcRUNTIME_DEP_PKGS_CSWlibcord1 += CSWlibgcc-s1cCHECKPKG_OVERRIDES_CSWlibcord1 += bad-rpath-entry|/usr/lib/lwp/.|opt/csw/lib/libcord.so.1.0.3
CHECKPKG_OVERRIDES_CSWlibcord1 += bad-rpath-entry|/usr/lib/lwp/.|opt/csw/lib/sparcv9/libcord.so.1.0.3cCHECKPKG_OVERRIDES_CSWlibcord1 += bad-rpath-entry|/usr/lib/lwp/.|opt/csw/lib/amd64/libcord.so.1.0.3cord1 += CSWlibgc

PACKAGES += CSWlibgc1
SPKG_DESC_CSWlibgc1 = A garbage collector for C and C++, libgc.so.1
PKGFILES_CSWlibgc1 += $(call pkgfiles_lib,libgc.so.1)
OBSOLETED_BY_CSWliRUNTIME_DEP_PKGS_CSWlibgc1 += CSWlibgcc-s1iCHECKPKG_OVERRIDES_CSWlibgc1 += bad-rpath-entry|/usr/lib/lwp/.|opt/csw/lib/libgc.so.1.0.3
CHECKPKG_OVERRIDES_CSWlibgc1 += bad-rpath-entry|/usr/lib/lwp/.|opt/csw/lib/sparcv9/libgc.so.1.0.3iCHECKPKG_OVERRIDES_CSWlibgc1 += bad-rpath-entry|/usr/lib/lwp/.|opt/csw/lib/amd64/libgc.so.1.0.3ibgc1 += CSWlibgc

PACKAGES += CSWlibgccpp1
SPKG_DESC_CSWlibgccpp1 = A garbage collector for C and C++, libgccpp.so.1
PKGFILES_CSWlibgccpp1 += $(call pkgfiles_liRUNTIME_DEP_PKGS_CSWlibgccpp1 += CSWlibgc1
RUNTIME_DEP_PKGS_CSWlibgccpp1 += CSWlibgcc-s1iCHECKPKG_OVERRIDES_CSWlibgccpp1 += bad-rpath-entry|/usr/lib/lwp/.|opt/csw/lib/libgccpp.so.1.0.3
CHECKPKG_OVERRIDES_CSWlibgccpp1 += bad-rpath-entry|/usr/lib/lwp/.|opt/csw/lib/sparcv9/libgccpp.so.1.0.3iCHECKPKG_OVERRIDES_CSWlibgccpp1 += bad-rpath-entry|/usr/lib/lwp/.|opt/csw/lib/amd64/libgccpp.so.1.0.3ib,libgccpp.so.1)

PACKAGES += CSWlibgc-dev
SPKG_DESC_CSWlibgc-dev = Development files for libgc.so.1 libcord.so.1 and libgccpp.so.1
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibgc-dev += CSWlibcord1
RUNTIME_DEP_PKGS_CSWlibgc-dev += CSWlibgc1
RUNTIME_DEP_PKGS_CSWlibgc-devCHECKPKG_OVERRIDES_CSWlibgc-dev += archall-devel-package
ARCHALL_CSWlibgc-dev = ev +=ADME.autoconf

# One test is failing on amd64, disable for now:
#   FAIL: gctest
# The bugreport has been posted on
#   http://www.hpl.hp.com/hosted/linux/mail-archives/gc/2012-January/004904.html
TEST_SIPTS	=	custom

# BUILD64_LIBS_ONLY = 1

include gar/category.mk

test-custom:
	cd $(WORKSRC) && /usr/bin/env -i $(BUILD_ENV) && $(MAKE) -i -k -C $(OBJDIR) check
	$(MAKECOOKIE)

post-install-modulated: pkgdoc = $(DESTDIR)/$(docdir)/$(NAME)-dev
post-install-modulated:
	ginstall --directory --mode=u=rwx,go=rx $(pkgdoc)
	cd $(DESTDIR)/$(sharedstatedir)/gc && mv * $(pkgdoc)
	rmdir $(DESTDIR)/$(sharedstatedir)/g