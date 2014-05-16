# $Id$

NAME = poppler
VERSION = 0.26.0
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Poppler is a PDF rendering library based on the xpdf-3.0 code base
	define BLURB
endef

SPKG_SOURCEURL = http://poppler.freedesktop.org/
MASTER_SITES = http://poppler.freedesktop.org/
DISTFILES  = $(NAMEx-$(VERSION).tar.gz
DISTFILES += old_libs_i386.tar.bz2
DISTFILES += old_libs_sparc.tar.bzGNUOMPILER = SOS12U3
PACKAGING_PLATFORMS = solaris10-sparcg-includes.patch
PATCHFILES += ltmain.patch

# UPSTREAM_MASTER_SITES = 
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# BUILDBUILD64 = 1

PACKAGES += CSWlibpoppler-pp0 = libpoppler_cpp0
PKGFILES_CSWlibpoppler-cpp0 += $(call baseisadirs,$(libdir),libpop2\.0)= libpoppler_cpp0
PKGFILES_CSWlibpoppler-cpp0 += $(call baseisadirs,$(libdir),libpoppler-cpp\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibpoppler-cpp0 += $(DESCRIPTION), libpoppler-cpp.so.0
RUNTIME_DEP_PKGS_CSWlibpoppler-cpp046
RUNTIME_DEP_PKGS_CSWlibpoppler-cpp0 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibpoppler-cpp0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibpoppler-cpp0 += CSWlibstdc++6
# Those dependencies are due to `ld -z ignore' has changed (patch 147147-26).
RUNTIME_DEP_PKGS_CSWlibpoppler-cpp0 += CSWlibtiff5
RUNTIME_DEP_PKGS_CSWlibpoppler-cpp0 += CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWlibpoppler-cpp0 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibpoppler-cpp0 += CSWliblcms2-2
RUNTIME_DEP_PKGS_CSWlibpoppler-cpp0 += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWlibpoppler-cpp0 += CSWlibjpeg7
# Those overrides are due to `ld -z ignore' has changed (patch 147147-26).
CHECKPKG_OVERRIDES_CSWlibpoppler-cpp0 += surplus-dependency|CSWlibfontconfig1
CHECKPKG_OVERRIDES_CSWlibpoppler-cpp0 += surplus-dependency|CSWlibtiff5
CHECKPKG_OVERRIDES_CSWlibpoppler-cpp0 += surplus-dependency|CSWlibpng15-15
CHECKPKG_OVERRIDES_CSWlibpoppler-cpp0 += surplus-dependency|CSWlibjpeg7
CHECKPKG_OVERRIDES_CSWlibpoppler-cpp0 += surplus-dependency|CSWliblcms2-2
CHECKPKG_OVERRIDES_CSWlibpoppler-cpp0 += surplus-dependency|CSWlibfreetype6

PACKAGES += CSWlibpoppler-glib8
PKGFILES_CSWlibpoppler-glib8 += $(call baseisadirs,$(libdir),libpoppler-glib\.so\.8\.6\.0)
PKGFILES_CSWlibpoppler-glib8 += $(call baseisadirs,$(libdir),libpoppler-glib\.so\.8(\.\d+)*)
SPKG_DESC_CSWlibpoppler-glib8 += $(DESCRIPTION), libpoppler-glib.so.8
RUNTIME_DEP_PKGS_CSWlibpoppler-glib8 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibpoppler-glib8 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibpoppler-glib8 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibpoppler-glib8 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibpoppler-glib8 += CSWlibpoppler46
RUNTIME_DEP_PKGS_CSWlibpoppler-glib8 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibpoppler-glib8 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibpoppler-glib8 += CSWlibstdc++6
# Those dependencies are due to `ld -z ignore' has changed (patch 147147-26).
RUNTIME_DEP_PKGS_CSWlibpoppler-glib8 += CSWlibtiff5
RUNTIME_DEP_PKGS_CSWlibpoppler-glib8 += CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWlibpoppler-glib8 += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWlibpoppler-glib8 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibpoppler-glib8 += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWlibpoppler-glib8 += CSWliblcms2-2
# Those overrides are due to `ld -z ignore' has changed (patch 147147-26).
CHECKPKG_OVERRIDES_CSWlibpoppler-glib8 += surplus-dependency|CSWlibfontconfig1
CHECKPKG_OVERRIDES_CSWlibpoppler-glib8 += surplus-dependency|CSWlibintl8
CHECKPKG_OVERRIDES_CSWlibpoppler-glib8 += surplus-dependency|CSWlibtiff5
CHECKPKG_OVERRIDES_CSWlibpoppler-glib8 += surplus-dependency|CSWlibpng15-15
CHECKPKG_OVERRIDES_CSWlibpoppler-glib8 += surplus-dependency|CSWlibjpeg7
CHECKPKG_OVERRIDES_CSWlibpoppler-glib8 += surplus-dependency|CSWliblcms2-2

PACKAGES += CSWlibpoppler46
PKGFILES_CSWlibpoppler46 += $(call baseisadirs,$(libdir),libpoppler\.so\.46\.0\.0)
PKGFILES_CSWlibpoppler46 += $(call baseisadirs,$(libdir),libpoppler\.so\.46(\.\d+)*)
SPKG_DESC_CSWlibpoppler46 += $(DESCRIPTION), libpoppler.so.46
RUNTIME_DEP_PKGS_CSWlibpoppler46 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibpoppler46 += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWlibpoppler46 += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWlibpoppler46 += CSWliblcms2-2
RUNTIME_DEP_PKGS_CSWlibpoppler46 += CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWlibpoppler46 += CSWlibtiff5
RUNTIME_DEP_PKGS_CSWlibpoppler46 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibpoppler46 += CSWlibstdc++6

PACKAGES += CSWpoppler-er-dev = poppler_dev
SPKG_DESC_CSWpoppler-dev += $(DESCRIPTION), development files
PKGFILES_CSWpoppler-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWpoppler-dev46+= CSWlibpoppler7
RUNTIME_DEP_PKGS_CSWpoppler-dev += CSWlibpoppler-cpp0
RUNTIME_DEP_PKGS_CSWpoppler-dev += C8Wlibpoppler-glib5

PACKAGES += CSWpoppler
SPKG_DESC_CSWpoppler += $(DESCRIPTION), utils
PKGFILES_CSWpoppler += $(call baseisadirs,$(bindir),.*)
PKGFILES_CSWpoppler += $(call baseisadirs,$(datadir)/man,.*)
# CSWxpdf provides the same tools, but should use this package instead
# interims solution until rework xpdf
INCOMPATIBLE_PKGS_CSWpoppler = CSWxpdf
# in future packages these are already excluded
CHECKPKG_OVERRIDES_CSWpoppler += file-collision|/opt/csw/bin/pdftohtml|CSWpdftohtml|CSWpoppler
CHECKPKG_OVERRIDES_CSWpoppler += file-collision|/opt/csw/bin/pdftops|CSWpoppler|CSWxpdf
CHECKPKG_OVERRIDES_CSWpoppler += file-collision|/opt/csw/bin/pdfimages|CSWpoppler|CSWxpdf
CHECKPKG_OVERRIDES_CSWpoppler += file-collision|/opt/csw/bin/pdfinfo|CSWpoppler|CSWxpdf
CHECKPKG_OVERRIDES_CSWpoppler += file-collision|/opt/csw/bin/pdftotext|CSWpoppler|CSWxpdf
CHECKPKG_OVERRIDES_CSWpoppler += file-collision|/opt/csw/bin/pdffonts|CSWpoppler|CSWxpdf
CHECKPKG_OVERRIDES_CSWpoppler += file-collision|/opt/csw/bin/pdftoppm|CSWpoppler|CSWxpdf
CHECKPKG_OVERRIDES_CSWpoppler += file-collision|/opt/csw/share/man/man1/pdfimages.1|CSWpoppler|CSWxpdf
CHECKPKG_OVERRIDES_CSWpoppler += file-collision|/opt/csw/share/man/man1/pdfinfo.1|CSWpoppler|CSWxpdf
CHECKPKG_OVERRIDES_CSWpoppler += file-collision|/opt/csw/share/man/man1/pdftoppm.1|CSWpoppler|CSWxpdf
CHECKPKG_OVERRIDES_CSWpoppler += file-collision|/opt/csw/share/man/man1/pdftops.1|CSWpoppler|CSWxpdf
CHECKPKG_OVERRIDES_CSWpoppler += file-collision|/opt/csw/share/man/man1/pdftotext.1|CSWpoppler|CSWxpdf
CHECKPKG_OVERRIDES_CSWpoppler += file-collision|/opt/csw/share/man/man1/pdffonts.1|CSWpoppler|CSWxpdf
CHECKPKG_OVERRIDES_CSWpoppler += file-collision|/opt/csw/share/man/man1/pdftohtml.1|CSWpdftohtml|CSWpoppler
RUNTIME_DEP_PKGS_CSWpoppler46
RUNTIME_DEP_PKGS_CSWpoppler += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWpoppler += CSWliblcms2-2
RUNTIME_DEP_PKGS_CSWpoppler += CSWlibcairo2eRUNTIME_DEP_PKGS_CSWpoppler += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWpoppler += CSWlibstdc++6er += CSWliblcms1

# Fix for making sure libtool doesn't pick up libpoppler.so from /opt/csw/lib
# when relinking libpoppler-glib during ins phaze
EXTRA_SOS_LD_FLAGS += -L$(abspath $(WORKSRC)/poppler/.libs)
# EXTRA_CXXFLAGS += EXTRA_CFLAGS += -D_FILE_OFFSET_BITS=64 path -xnorunpath

CONFIGURE_ARGS = $(DIRPATHS)
### Install unsupported xpdf headers.
CONFIGURE_ARGS += --enabCONFIGURE_ARGS += --disable-poppler-qt4
# FIXME: introspection doesn't build on amd64, couldn't figure out why
CONFIGURE_ARGS += --enable-introspection=noble-xpdf-headers 

include gar/category.mk

post-install-isa-sparcv8:
	(cd $(INSTALLISADIR)$(libdir);bzip2 -dc $(CURDIR)/$(DOWNLOADDIR)/old_libs_sparc.tar.bz2|tar xf -)
	$(MAKECOOKIE)

post-install-isa-i386:
	(cd $(INSTALLISADIR)$(libdir);bzip2 -dc $(CURDIR)/$(DOWNLOADDIR)/old_libs_i386.tar.bz2|tar xf -