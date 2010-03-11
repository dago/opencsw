# $Id$

GARNAME = poppler
GARVERSION = 0.10.6
CATEGORIES = lib

DESCRIPTION = Poppler is a PDF rendering library based on the xpdf-3.0 code base
define BLURB
endef

SPKG_SOURCEURL = http://poppler.freedesktop.org/
MASTER_SITES = http://poppler.freedesktop.org/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += old_libs_i386.tar.bz2
DISTFILES += old_libs_sparc.tar.bz2

RUNTIME_DEP_PKGS_CSWpoppler += CSWgtk2
RUNTIME_DEP_PKGS_CSWpoppler += CSWiconv
RUNTIME_DEP_PKGS_CSWpoppler += CSWlibcairo
RUNTIME_DEP_PKGS_CSWpoppler += CSWpango
RUNTIME_DEP_PKGS_CSWpoppler += CSWzlib
RUNTIME_DEP_PKGS_CSWpoppler += CSWfconfig
RUNTIME_DEP_PKGS_CSWpoppler += CSWftype2
RUNTIME_DEP_PKGS_CSWpoppler += CSWggettextrt
RUNTIME_DEP_PKGS_CSWpoppler += CSWglib2
RUNTIME_DEP_PKGS_CSWpoppler += CSWjpeg
RUNTIME_DEP_PKGS_CSWpoppler += CSWlibxml2

#PATCHFILES += missing-includes.patch

# UPSTREAM_MASTER_SITES = 
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1

# Fix for making sure libtool doesn't pick up libpoppler.so from /opt/csw/lib
# when relinking libpoppler-glib during install phaze
EXTRA_SOS_LD_FLAGS += -L$(abspath $(WORKSRC)/poppler/.libs)

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

post-install-isa-sparcv8:
	(cd $(INSTALLISADIR)$(libdir);bzip2 -dc $(CURDIR)/$(DOWNLOADDIR)/old_libs_sparc.tar.bz2|tar xf -)
	$(MAKECOOKIE)

post-install-isa-i386:
	(cd $(INSTALLISADIR)$(libdir);bzip2 -dc $(CURDIR)/$(DOWNLOADDIR)/old_libs_i386.tar.bz2|tar xf -)
	$(MAKECOOKIE)
