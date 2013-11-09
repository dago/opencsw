# $Id$

NAME = poppler
VERSION = 0.24.0
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
RUNTIME_DEP_PKGS_CSWlibpoppler-cpp043
RUNTIME_DEP_PKGS_CSWlibpoppler-cpp0 += CSWlibiconv2

PACKAGES += CSWlibpoppler-glib8
PKGFILES_CSWlibpoppler-glib8 += $(call baseisadirs,$(libdir),libpoppler-glib\.so\.8\.6\.0)
PKGFILES_CSWlibpoppler-glib8 += $(call baseisadirs,$(libdir),libpoppler-glib\.so\.8(\.\d+)*)
SPKG_DESC_CSWlibpoppler-glib8 += $(DESCRIPTION), libpoppler-glib.so.8
RUNTIME_DEP_PKGS_CSWlibpoppler-glib8 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibpoppler-glib8 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibpoppler-glib8 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibpoppler-glib8 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibpoppler-glib8 += CSWlibpoppler43
RUNTIME_DEP_PKGS_CSWlibpoppler-glib8 += CSWlibgio2-0-0

PACKAGES += CSWlibpoppler43
PKGFILES_CSWlibpoppler43 += $(call baseisadirs,$(libdir),libpoppler\.so\.43\.0\.0)
PKGFILES_CSWlibpoppler43 += $(call baseisadirs,$(libdir),libpoppler\.so\.43(\.\d+)*)
SPKG_DESC_CSWlibpoppler43 += $(DESCRIPTION), libpoppler.so.43
RUNTIME_DEP_PKGS_CSWlibpoppler43 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibpoppler43 += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWlibpoppler43 += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWlibpoppler43 += CSWliblcms2-2
RUNTIME_DEP_PKGS_CSWlibpoppler43 += CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWlibpoppler43 += CSWlibtiff5

PACKAGES += CSWpoppler-er-dev = poppler_dev
SPKG_DESC_CSWpoppler-dev += $(DESCRIPTION), development files
PKGFILES_CSWpoppler-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWpoppler-dev43+= CSWlibpoppler7
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
RUNTIME_DEP_PKGS_CSWpoppler43
RUNTIME_DEP_PKGS_CSWpoppler += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWpoppler += CSWliblcms2-2
RUNTIME_DEP_PKGS_CSWpoppler += CSWlibcairo2er += CSWliblcms1

# Fix for making sure libtool doesn't pick up libpoppler.so from /opt/csw/lib
# when relinking libpoppler-glib during install phaze
EXTRA_SOS_LD_FLAGS += -L$(abspath $(WORKSRC)/poppler/.libs)
# EXTRA_CXXFLAGS += path -xnorunpath

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