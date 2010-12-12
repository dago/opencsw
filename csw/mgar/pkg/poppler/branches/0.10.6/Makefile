# $Id$

NAME = poppler
VERSION = 0.10.6
CATEGORIES = lib

DESCRIPTION = Poppler is a PDF rendering library based on the xpdf-3.0 code base
define BLURB
endef

SPKG_SOURCEURL = http://poppler.freedesktop.org/
MASTER_SITES = http://poppler.freedesktop.org/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += old_libs_i386.tar.bz2
DISTFILES += old_libs_sparc.tar.bz2

PACKAGES = CSWpoppler CSWlibpoppler CSWlibpopplerdev CSWlibpopplerdoc
CATALOGNAME_CSWpoppler = poppler
CATALOGNAME_CSWlibpoppler = libpoppler
CATALOGNAME_CSWlibpopplerdev = libpoppler_devel
CATALOGNAME_CSWlibpopplerdoc = libpoppler_doc
SPKG_DESC_CSWpoppler = $(DESCRIPTION) - utilities
SPKG_DESC_CSWlibpoppler = $(DESCRIPTION)
SPKG_DESC_CSWlibpopplerdev = $(DESCRIPTION) - developer package
SPKG_DESC_CSWlibpopplerdoc = $(DESCRIPTION) - documentation

PKGFILES_CSWlibpoppler= $(PKGFILES_RT)
PKGFILES_CSWlibpopplerdev = $(PKGFILES_DEVEL)
PKGFILES_CSWlibpopplerdoc = $(sharedstatedir)/gtk-doc/.*

INCOMPATIBLE_PKGS_CSWpoppler = CSWxpdf

RUNTIME_DEP_PKGS_CSWpoppler += CSWfconfig
RUNTIME_DEP_PKGS_CSWpoppler += CSWftype2
RUNTIME_DEP_PKGS_CSWpoppler += CSWjpeg
RUNTIME_DEP_PKGS_CSWpoppler += CSWlibpoppler
RUNTIME_DEP_PKGS_CSWpoppler += CSWlibxml2

RUNTIME_DEP_PKGS_CSWlibpoppler += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibpoppler += CSWftype2
RUNTIME_DEP_PKGS_CSWlibpoppler += CSWggettextrt
RUNTIME_DEP_PKGS_CSWlibpoppler += CSWglib2
RUNTIME_DEP_PKGS_CSWlibpoppler += CSWgtk2
RUNTIME_DEP_PKGS_CSWlibpoppler += CSWiconv
RUNTIME_DEP_PKGS_CSWlibpoppler += CSWjpeg
RUNTIME_DEP_PKGS_CSWlibpoppler += CSWlibcairo
RUNTIME_DEP_PKGS_CSWlibpoppler += CSWlibxml2
RUNTIME_DEP_PKGS_CSWlibpoppler += CSWpango
RUNTIME_DEP_PKGS_CSWlibpoppler += CSWzlib

RUNTIME_DEP_PKGS_CSWlibpopplerdev += CSWlibpoppler

ARCHALL_CSWlibpopplerdoc = 1

#PATCHFILES += missing-includes.patch

# UPSTREAM_MASTER_SITES = 
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

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
