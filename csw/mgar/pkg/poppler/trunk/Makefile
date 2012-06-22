# $Id$

NAME = poppler
VERSION = 0.14.4
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Poppler is a PDF rendering library based on the xpdf-3.0 code base
define BLURB
endef

SPKG_SOURCEURL = http://poppler.freedesktop.org/
MASTER_SITES = http://poppler.freedesktop.org/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += old_libs_i386.tar.bz2
DISTFILES += old_libs_sparc.tar.bz2

GARCOMPILER = SOS12U3
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

PATCHFILES += missing-includes.patch
PATCHFILES += ltmain.patch

# UPSTREAM_MASTER_SITES = 
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# BUILD64_LIBS_ONLY = 1

PACKAGES += CSWlibpoppler-cpp0
CATALOGNAME_CSWlibpoppler-cpp0 = libpoppler_cpp0
PKGFILES_CSWlibpoppler-cpp0 += $(call baseisadirs,$(libdir),libpoppler-cpp\.so\.0\.1\.0)
PKGFILES_CSWlibpoppler-cpp0 += $(call baseisadirs,$(libdir),libpoppler-cpp\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibpoppler-cpp0 += $(DESCRIPTION), libpoppler-cpp.so.0
RUNTIME_DEP_PKGS_CSWlibpoppler-cpp0 += CSWlibpoppler7
RUNTIME_DEP_PKGS_CSWlibpoppler-cpp0 += CSWlibiconv2

PACKAGES += CSWlibpoppler-glib5
CATALOGNAME_CSWlibpoppler-glib5 = libpoppler_glib5
PKGFILES_CSWlibpoppler-glib5 += $(call baseisadirs,$(libdir),libpoppler-glib\.so\.5\.0\.0)
PKGFILES_CSWlibpoppler-glib5 += $(call baseisadirs,$(libdir),libpoppler-glib\.so\.5(\.\d+)*)
SPKG_DESC_CSWlibpoppler-glib5 += $(DESCRIPTION), libpoppler-glib.so.5
RUNTIME_DEP_PKGS_CSWlibpoppler-glib5 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibpoppler-glib5 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibpoppler-glib5 += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibpoppler-glib5 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibpoppler-glib5 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibpoppler-glib5 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibpoppler-glib5 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibpoppler-glib5 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibpoppler-glib5 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibpoppler-glib5 += CSWpango
RUNTIME_DEP_PKGS_CSWlibpoppler-glib5 += CSWlibpoppler7
RUNTIME_DEP_PKGS_CSWlibpoppler-glib5 += CSWlibfontconfig1

PACKAGES += CSWlibpoppler7
CATALOGNAME_CSWlibpoppler7 = libpoppler7
PKGFILES_CSWlibpoppler7 += $(call baseisadirs,$(libdir),libpoppler\.so\.7\.0\.0)
PKGFILES_CSWlibpoppler7 += $(call baseisadirs,$(libdir),libpoppler\.so\.7(\.\d+)*)
SPKG_DESC_CSWlibpoppler7 += $(DESCRIPTION), libpoppler.so.7
RUNTIME_DEP_PKGS_CSWlibpoppler7 += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWlibpoppler7 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibpoppler7 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibpoppler7 += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWlibpoppler7 += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWlibpoppler7 += CSWliblcms1

PACKAGES += CSWpoppler-dev
CATALOGNAME_CSWpoppler-dev = poppler_dev
SPKG_DESC_CSWpoppler-dev += $(DESCRIPTION), development files
PKGFILES_CSWpoppler-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWpoppler-dev += CSWlibpoppler7
RUNTIME_DEP_PKGS_CSWpoppler-dev += CSWlibpoppler-cpp0
RUNTIME_DEP_PKGS_CSWpoppler-dev += CSWlibpoppler-glib5

PACKAGES += CSWpoppler
SPKG_DESC_CSWpoppler += $(DESCRIPTION), utils
PKGFILES_CSWpoppler += $(call baseisadirs,$(bindir),.*)
PKGFILES_CSWpoppler += $(call baseisadirs,$(datadir)/man,.*)
# CSWxpdf provides the same tools, but should use this package instead
# interims solution until rework xpdf
INCOMPATIBLE_PKGS_CSWpoppler = CSWxpdf
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
RUNTIME_DEP_PKGS_CSWpoppler += CSWlibpoppler7
RUNTIME_DEP_PKGS_CSWpoppler += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWpoppler += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWpoppler += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWpoppler += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWpoppler += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWpoppler += CSWliblcms1

# Fix for making sure libtool doesn't pick up libpoppler.so from /opt/csw/lib
# when relinking libpoppler-glib during install phaze
EXTRA_SOS_LD_FLAGS += -L$(abspath $(WORKSRC)/poppler/.libs)
# EXTRA_CXXFLAGS += -D__EXTENSIONS__
EXTRA_LINKER_FLAGS = -norunpath -xnorunpath

CONFIGURE_ARGS = $(DIRPATHS)
### Install unsupported xpdf headers.
CONFIGURE_ARGS += --enable-xpdf-headers 

include gar/category.mk

post-install-isa-sparcv8:
	(cd $(INSTALLISADIR)$(libdir);bzip2 -dc $(CURDIR)/$(DOWNLOADDIR)/old_libs_sparc.tar.bz2|tar xf -)
	$(MAKECOOKIE)

post-install-isa-i386:
	(cd $(INSTALLISADIR)$(libdir);bzip2 -dc $(CURDIR)/$(DOWNLOADDIR)/old_libs_i386.tar.bz2|tar xf -)
	$(MAKECOOKIE)
