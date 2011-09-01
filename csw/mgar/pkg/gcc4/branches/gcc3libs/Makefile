# $Id$

NAME      = gcc
VERSION   = 3.4.6
CATEGORIES   = lang
GARTYPE = v2

DESCRIPTION  = The GNU Compiler Collection
define BLURB
  Repackaging of legacy gcc3 libraries.
endef

DISTFILES    += COPYING
DISTFILES    += libstdc++.so.5.0.5-i386
DISTFILES    += libstdc++.so.5.0.5-sparcv8
DISTFILES    += libstdc++.so.5.0.5-sparcv9
DISTFILES    += libstdc++.so.6.0.3-i386
DISTFILES    += libstdc++.so.6.0.3-sparcv8
DISTFILES    += libstdc++.so.6.0.3-sparcv9
# There is no amd64 file libstdc++ from gcc3. There will be one from gcc4

MASTER_SITES =

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS =
TEST_SCRIPTS = 

LICENSE = COPYING
VENDOR_URL = http://gcc.gnu.org

PACKAGES += CSWlibstdc++5
CATALOGNAME_CSWlibstdc++5 = libstdc++5
PKGFILES_CSWlibstdc++5 += $(call baseisadirs,$(libdir),libstdc\+\+\.so\.5(\.\d+)*)
SPKG_DESC_CSWlibstdc++5 += GCC shared library, libstdc++.so.5
OBSOLETED_BY_CSWlibstdc++5  += CSWgcc3g++rt
RUNTIME_DEP_PKGS_CSWlibstdc++5 += CSWgcc3corert
# This is necessary when uploading the gcc3libs + gcc4 combo, because the
# updated gcc3corert stub built from gcc4 sources does not include any shared
# libraries.
CHECKPKG_OVERRIDES_CSWlibstdc++5 += surplus-dependency|CSWgcc3corert

PACKAGES += CSWlibstdc++6
SPKG_DESC_CSWlibstdc++6 = GCC shared library libstdc++.so.6
PKGFILES_CSWlibstdc++6 = $(call baseisadirs,$(libdir),libstdc\+\+\.so\.6(\.\d+)*)
OBSOLETED_BY_CSWlibstdc++6 += CSWgcc3g++rt
RUNTIME_DEP_PKGS_CSWlibstdc++6 += CSWgcc3corert

# It's a legacy shared library which we will not rebuild.
CHECKPKG_OVERRIDES_CSWlibstdc++5 += soname-not-found|libgcc_s.so.1|is|needed|by|opt/csw/lib/sparcv9/libstdc++.so.5.0.5
CHECKPKG_OVERRIDES_CSWlibstdc++5 += soname-not-found|libgcc_s.so.1|is|needed|by|opt/csw/lib/libstdc++.so.5.0.5

STDC5_FILE = libstdc++.so.5.0.5
STDC6_FILE = libstdc++.so.6.0.3

ARCH_32_sparc = sparcv8
ARCH_64_sparc = sparcv9
ARCH_32_i386 = i386
ARCH_64_i386 = amd64

ARCH_32 = $(ARCH_32_$(GARCH))
ARCH_64 = $(ARCH_64_$(GARCH))

include gar/category.mk

post-merge:
	ginstall -m 755 -d $(PKGROOT)$(libdir)
	ginstall -m 755 -d $(PKGROOT)$(libdir)/$(ARCH_64)
	ginstall -m 755 \
		$(FILEDIR)/$(STDC5_FILE)-$(ARCH_32) \
		$(PKGROOT)$(libdir)/$(STDC5_FILE)
	gln -s $(STDC5_FILE) $(PKGROOT)$(libdir)/libstdc++.so.5
	if [ -r $(FILEDIR)/$(STDC5_FILE)-$(ARCH_64) ]; then \
		ginstall -m 755 \
			$(FILEDIR)/$(STDC5_FILE)-$(ARCH_64) \
			$(PKGROOT)$(libdir)/$(ARCH_64)/$(STDC5_FILE); \
		gln -s $(STDC5_FILE) $(PKGROOT)$(libdir)/$(ARCH_64)/libstdc++.so.5; \
	fi
	ginstall -m 755 \
		$(FILEDIR)/$(STDC6_FILE)-$(ARCH_32) \
		$(PKGROOT)$(libdir)/$(STDC6_FILE)
	gln -s $(STDC6_FILE) $(PKGROOT)$(libdir)/libstdc++.so.6
	if [ -r $(FILEDIR)/$(STDC6_FILE)-$(ARCH_64) ]; then \
		ginstall -m 755 \
			$(FILEDIR)/$(STDC6_FILE)-$(ARCH_64) \
			$(PKGROOT)$(libdir)/$(ARCH_64)/$(STDC6_FILE); \
		gln -s $(STDC6_FILE) $(PKGROOT)$(libdir)/$(ARCH_64)/libstdc++.so.6; \
	fi
	@$(MAKECOOKIE)
