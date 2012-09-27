NAME = gimp
VERSION = 2.8.2
GARTYPE = v2
CATEGORIES = gnome

DESCRIPTION = The GNU Image Manipulation Program
define BLURB
	The GIMP is the GNU Image Manipulation Program. It is a freely distributed
	piece of software suitable for such tasks as photo retouching, image
	composition and image authoring. It can be used as a simple paint program,
	an expert quality photo retouching program, an online batch processing
	system, a mass production image renderer, a image format converter, etc.
endef

MASTER_SITES = ftp://ftp.gimp.org/pub/gimp/v$(shell echo $(VERSION) | cut -d . -f 1,2)/

DISTFILES = $(NAME)-$(VERSION).tar.bz2

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

VENDOR_URL = http://www.gimp.org/

PATCHFILES += 0001-studio-compiler-flags-configure.ac.patch
PATCHFILES += 0002-skip-backtrace-base-utils.c.patch
PATCHFILES += 0003-no-gcc-flags-Makefile.am.patch
PATCHFILES += 0004-no-gcc-flags-Makefile.am.patch
PATCHFILES += 0005-usr-local-sanity.c.patch

EXTRA_MERGE_EXCLUDE_FILES += /opt/csw/lib/gimp/2.0/python/.*py[co]

PACKAGES += CSWgimp
SPKG_DESC_CSWgimp = The GNU Image Manipulation Program
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWgimp += CSWlibgthread2-0-0
# RUNTIME_DEP_PKGS_CSWgimp += CSWlibwmflite0-2-7
RUNTIME_DEP_PKGS_CSWgimp += CSWlibgimpconfig2-0-0
RUNTIME_DEP_PKGS_CSWgimp += CSWlibgimpbase2-0-0
RUNTIME_DEP_PKGS_CSWgimp += CSWlibgimpmath2-0-0
# RUNTIME_DEP_PKGS_CSWgimp += CSWlibexif12
RUNTIME_DEP_PKGS_CSWgimp += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWgimp += CSWlibgimpcolor2-0-0
RUNTIME_DEP_PKGS_CSWgimp += CSWlibintl8
# RUNTIME_DEP_PKGS_CSWgimp += CSWlibwmf0-2-7
RUNTIME_DEP_PKGS_CSWgimp += CSWxpm
RUNTIME_DEP_PKGS_CSWgimp += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWgimp += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWgimp += CSWfconfig
RUNTIME_DEP_PKGS_CSWgimp += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgimp += CSWlibz1
RUNTIME_DEP_PKGS_CSWgimp += CSWpython
RUNTIME_DEP_PKGS_CSWgimp += CSWlibbabl0-1-0
RUNTIME_DEP_PKGS_CSWgimp += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgimp += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgimp += CSWpango
RUNTIME_DEP_PKGS_CSWgimp += CSWlibgimpui2-0-0
RUNTIME_DEP_PKGS_CSWgimp += CSWlibgimpmodule2-0-0
RUNTIME_DEP_PKGS_CSWgimp += CSWlibgimpwidgets2-0-0
# RUNTIME_DEP_PKGS_CSWgimp += CSWliblcms1
RUNTIME_DEP_PKGS_CSWgimp += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWgimp += CSWlibtiff3
# RUNTIME_DEP_PKGS_CSWgimp += CSWaalib
RUNTIME_DEP_PKGS_CSWgimp += CSWlibgimpthumb2-0-0
RUNTIME_DEP_PKGS_CSWgimp += CSWjasper
RUNTIME_DEP_PKGS_CSWgimp += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgimp += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWgimp += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgimp += CSWgs
RUNTIME_DEP_PKGS_CSWgimp += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWgimp += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWgimp += CSWlibgegl0-2-0
RUNTIME_DEP_PKGS_CSWgimp += CSWlibgimp2-0-0
RUNTIME_DEP_PKGS_CSWgimp += CSWlibxpm4

# cant find /usr/share in the bins
CHECKPKG_OVERRIDES_CSWgimp += file-with-bad-content|/usr/share|root/opt/csw/bin/amd64/gimp-2.8
CHECKPKG_OVERRIDES_CSWgimp += file-with-bad-content|/usr/share|root/opt/csw/bin/pentium_pro/gimp-2.8
CHECKPKG_OVERRIDES_CSWgimp += file-with-bad-content|/usr/share|root/opt/csw/share/man/man1/gimp-2.8.1

# OBSOLETED_BY_CSWgimp += CSWgimpminimal
# OBSOLETED_BY_CSWgimp += CSWgimpi18n
# OBSOLETED_BY_CSWgimp += CSWgimplibsdoc

PACKAGES += CSWlibgimp-dev
SPKG_DESC_CSWlibgimp-dev = Development files for libgimp*-2.0.so.0 libraries
PKGFILES_CSWlibgimp-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibgimp-dev += CSWlibgimpcolor2-0-0
RUNTIME_DEP_PKGS_CSWlibgimp-dev += CSWlibgimpbase2-0-0
RUNTIME_DEP_PKGS_CSWlibgimp-dev += CSWlibgimpconfig2-0-0
RUNTIME_DEP_PKGS_CSWlibgimp-dev += CSWlibgimpthumb2-0-0
RUNTIME_DEP_PKGS_CSWlibgimp-dev += CSWlibgimpmath2-0-0
RUNTIME_DEP_PKGS_CSWlibgimp-dev += CSWlibgimpui2-0-0
RUNTIME_DEP_PKGS_CSWlibgimp-dev += CSWlibgimpmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgimp-dev += CSWlibgimpwidgets2-0-0
RUNTIME_DEP_PKGS_CSWlibgimp-dev += CSWgimp
RUNTIME_DEP_PKGS_CSWlibgimp-dev += CSWlibgimp2-0-0
OBSOLETED_BY_CSWgimp-dev += CSWgimplibs

PACKAGES += CSWlibgimp2-0-0
SPKG_DESC_CSWlibgimp2-0-0 = GIMP library, libgimp-2.0.so.0
PKGFILES_CSWlibgimp2-0-0 += $(call pkgfiles_lib,libgimp-2.0.so.0)
RUNTIME_DEP_PKGS_CSWlibgimp2-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgimp2-0-0 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibgimp2-0-0 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibgimp2-0-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgimp2-0-0 += CSWlibgimpconfig2-0-0
RUNTIME_DEP_PKGS_CSWlibgimp2-0-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgimp2-0-0 += CSWlibgimpcolor2-0-0
RUNTIME_DEP_PKGS_CSWlibgimp2-0-0 += CSWlibgimpbase2-0-0
OBSOLETED_BY_CSWlibgimp2-0-0 += CSWgimplibs

PACKAGES += CSWlibgimpbase2-0-0
SPKG_DESC_CSWlibgimpbase2-0-0 = GIMP library, libgimpbase-2.0.so.0
PKGFILES_CSWlibgimpbase2-0-0 += $(call pkgfiles_lib,libgimpbase-2.0.so.0)
RUNTIME_DEP_PKGS_CSWlibgimpbase2-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgimpbase2-0-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgimpbase2-0-0 += CSWlibglib2-0-0
OBSOLETED_BY_CSWlibgimpbase2-0-0 += CSWgimplibs

PACKAGES += CSWlibgimpcolor2-0-0
SPKG_DESC_CSWlibgimpcolor2-0-0 = GIMP library, libgimpcolor-2.0.so.0
PKGFILES_CSWlibgimpcolor2-0-0 += $(call pkgfiles_lib,libgimpcolor-2.0.so.0)
RUNTIME_DEP_PKGS_CSWlibgimpcolor2-0-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgimpcolor2-0-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgimpcolor2-0-0 += CSWlibcairo2
OBSOLETED_BY_CSWlibgimpcolor2-0-0 += CSWgimplibs

PACKAGES += CSWlibgimpconfig2-0-0
SPKG_DESC_CSWlibgimpconfig2-0-0 = GIMP library, libgimpconfig-2.0.so.0
PKGFILES_CSWlibgimpconfig2-0-0 += $(call pkgfiles_lib,libgimpconfig-2.0.so.0)
RUNTIME_DEP_PKGS_CSWlibgimpconfig2-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgimpconfig2-0-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgimpconfig2-0-0 += CSWlibgimpbase2-0-0
RUNTIME_DEP_PKGS_CSWlibgimpconfig2-0-0 += CSWlibgimpmath2-0-0
RUNTIME_DEP_PKGS_CSWlibgimpconfig2-0-0 += CSWlibgimpcolor2-0-0
RUNTIME_DEP_PKGS_CSWlibgimpconfig2-0-0 += CSWlibglib2-0-0
OBSOLETED_BY_CSWlibgimpconfig2-0-0 += CSWgimplibs

PACKAGES += CSWlibgimpmath2-0-0
SPKG_DESC_CSWlibgimpmath2-0-0 = GIMP library, libgimpmath-2.0.so.0
PKGFILES_CSWlibgimpmath2-0-0 += $(call pkgfiles_lib,libgimpmath-2.0.so.0)
RUNTIME_DEP_PKGS_CSWlibgimpmath2-0-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgimpmath2-0-0 += CSWlibglib2-0-0
OBSOLETED_BY_CSWlibgimpmath2-0-0 += CSWgimplibs

PACKAGES += CSWlibgimpmodule2-0-0
SPKG_DESC_CSWlibgimpmodule2-0-0 = GIMP library, libgimpmodule-2.0.so.0
PKGFILES_CSWlibgimpmodule2-0-0 += $(call pkgfiles_lib,libgimpmodule-2.0.so.0)
RUNTIME_DEP_PKGS_CSWlibgimpmodule2-0-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgimpmodule2-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgimpmodule2-0-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgimpmodule2-0-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgimpmodule2-0-0 += CSWlibgimpbase2-0-0
OBSOLETED_BY_CSWlibgimpmodule2-0-0 += CSWgimplibs

PACKAGES += CSWlibgimpthumb2-0-0
SPKG_DESC_CSWlibgimpthumb2-0-0 = GIMP library, libgimpthumb-2.0.so.0
PKGFILES_CSWlibgimpthumb2-0-0 += $(call pkgfiles_lib,libgimpthumb-2.0.so.0)
RUNTIME_DEP_PKGS_CSWlibgimpthumb2-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgimpthumb2-0-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgimpthumb2-0-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgimpthumb2-0-0 += CSWlibgdk-pixbuf2-0-0
# OBSOLETED_BY_CSWlibgimpthumb2-0-0 += CSWgimplibs

PACKAGES += CSWlibgimpui2-0-0
SPKG_DESC_CSWlibgimpui2-0-0 = GIMP library, libgimpui-2.0.so.0
PKGFILES_CSWlibgimpui2-0-0 += $(call pkgfiles_lib,libgimpui-2.0.so.0)
RUNTIME_DEP_PKGS_CSWlibgimpui2-0-0 += CSWlibgimpcolor2-0-0
RUNTIME_DEP_PKGS_CSWlibgimpui2-0-0 += CSWlibgimpbase2-0-0
RUNTIME_DEP_PKGS_CSWlibgimpui2-0-0 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibgimpui2-0-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgimpui2-0-0 += CSWlibgimpmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgimpui2-0-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgimpui2-0-0 += CSWlibgimpwidgets2-0-0
RUNTIME_DEP_PKGS_CSWlibgimpui2-0-0 += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibgimpui2-0-0 += CSWlibgimp2-0-0
RUNTIME_DEP_PKGS_CSWlibgimpui2-0-0 += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibgimpui2-0-0 += CSWlibintl8
OBSOLETED_BY_CSWlibgimpui2-0-0 += CSWgimplibs

PACKAGES += CSWlibgimpwidgets2-0-0
SPKG_DESC_CSWlibgimpwidgets2-0-0 = GIMP library, libgimpwidgets-2.0.so.0
PKGFILES_CSWlibgimpwidgets2-0-0 += $(call pkgfiles_lib,libgimpwidgets-2.0.so.0)
RUNTIME_DEP_PKGS_CSWlibgimpwidgets2-0-0 += CSWlibgimpcolor2-0-0
RUNTIME_DEP_PKGS_CSWlibgimpwidgets2-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgimpwidgets2-0-0 += CSWlibgimpbase2-0-0
RUNTIME_DEP_PKGS_CSWlibgimpwidgets2-0-0 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibgimpwidgets2-0-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgimpwidgets2-0-0 += CSWlibgimpconfig2-0-0
RUNTIME_DEP_PKGS_CSWlibgimpwidgets2-0-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgimpwidgets2-0-0 += CSWpango
RUNTIME_DEP_PKGS_CSWlibgimpwidgets2-0-0 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibgimpwidgets2-0-0 += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibgimpwidgets2-0-0 += CSWlibgdk-x11-2-0-0
OBSOLETED_BY_CSWlibgimpwidgets2-0-0 += CSWgimplibs

BUILD64 = 1
ISAEXEC = 1

CONFIGURE_ARGS += $(DIRPATHS)
# No 64 bit Python yet
CONFIGURE_ARGS-64 += --disable-python
CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(MEMORYMODEL))
CONFIGURE_ARGS += --enable-mmx=no
CONFIGURE_ARGS += --enable-sse=no

CONFFILES += controllerrc
CONFFILES += gimprc
CONFFILES += gtkrc
CONFFILES += menurc
CONFFILES += ps-menurc
CONFFILES += sessionrc
CONFFILES += templaterc
CONFFILES += unitrc

PRESERVECONF = $(addprefix $(sysconfdir)/gimp/2.0/,$(CONFFILES))

PYCOMPILE = 1
# EXTRA_MERGE_EXCLUDE_FILES += .*.pyo .*.pyc

include gar/category.mk

pre-configure-modulated:
	cd $(WORKSRC) && rm ltmain.sh && libtoolize --copy --force
	cd $(WORKSRC) && aclocal
	cd $(WORKSRC) && autoconf --force
	cd $(WORKSRC) && automake -a -c -f
	cd $(WORKSRC) && autoheader
	$(MAKECOOKIE)

# For /opt/csw/gnu/xgettext
PATH := /opt/csw/gnu:$(PATH)
