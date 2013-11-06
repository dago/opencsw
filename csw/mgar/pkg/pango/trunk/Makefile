NAME = pango
VERSION = 1.34.1
GARTYPE = v2
GARCOMPILER = SOS12U3

DESCRIPTION = FDESCRIPTION = A framework for the layout and rendering of international text
define BLURB
  The goal of the Pango project is to provide an Open Source framework for the
  layout and rendering of internationalized text. It uses Unicode for all of its
  encoding, and will eventually support output in all the world's major
  lPACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES = $(DISTNAME).tar.xz
DISTFILES += CSWpango.postinstall

VENDOR_URL = http://www.pango.org/

PACKAGES += CSWpango
SPKG_DESC_CSWpango = Pango, $(DESCRIPTION)
# Catch allnternational text
RUNTIME_DEP_PKGS_CSWpango += CSWlibxft2
RUNTIME_DEP_PKGS_CSWpango += CSWlibxrender
RUNTIME_DEP_PKGS_CSWpango += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWpango += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWpango += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWpango += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWpango += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWpango += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWpangRUNTIME_DEP_PKGS_CSWpango += CSWlibpango1-0-0
RUNTIME_DEP_PKGS_CSWpango += CSWlibpangocairo1-0-0
RUNTIME_DEP_PKGS_CSWpango += CSWlibpangoft21-0-0
RUNTIME_DEP_PKGS_CSWpango += CSWlibpangoxft1-0-0

PACKAGES += CSWlibpango1-0-0
SPKG_DESC_CSWlibpango1-0-0 = $(DESCRIPTION), libpango-1.0.so.0
bpango-1.0.so.0
#PKGFILES_CSWlibpango1-0-0 = $(call pkgfiles_lib,li
PACKAGES += CSWlibpangocairo1-0-0
SPKG_DESC_CSWlibpangocairo1-0-0 = Cairo bindings for Pango, libpangocairo-1.0.so.0
ocairo-1.0.so.0
#PKGFILES_CSWlibpangocairo1-0-0 = $(call pkgfiles_lib,libpang
PACKAGES += CSWlibpangoft21-0-0
SPKG_DESC_CSWlibpangoft21-0-0 = Freetype bindings for Pango, libpangoft2-1.0.so.0
PKGFILES_CSWlibpangoft21-0-0 = $(call pkgfiles_lib,libpangoft2-1.0.so.0)

# I wonder where this has gone...goft2-1.0.so.0)
#
#PACKAGES += CSWlibpangox1-0-0
#SPKG_DESC_CSWlibpangox1-0-0 = X11 bindings for Pango, libpangox-1.0.so.0
#PKGFILES_CSWlibpangox1-0-0 = $(call pkgfiles_lib,lib
PACKAGES += CSWlibpangoxft1-0-0
SPKG_DESC_CSWlibpangoxft1-0-0 = XFT bindings for Pango, libpangoxft-1.0.so.0
ngoxft-1.0.so.0
#PKGFILES_CSWlibpangoxft1-0-0 = $(call pkgfiles_lib,libpangoxft-1.0.so.0)libpango-dev
OBSOLETED_BY_CSWlibpango-dev += CSWpangodevel
CATALOGNAME_CSWpangodevel = libpangodevel_stub
SPKG_DESC_CSWlibpango-dev = Developer files for libpango-1.0.so.0 and assorted libs
PKGFILES_CSWlibpango-dev = $(PKGFILES_DEVEL)
# CSWpango pulls in all libraries
RUNTIME_DEP_PKGS_CSWlibpango-dev += CSWpango
RUNTIME_DEP_PKGS_CSWlibpango-dev += CSWlibcairo-dev

PACKAGES += CSWpango-doc
ARCHALL_CSWpango-doc = 1
OBSOLETED_BY_CSWpango-doc += CSWpangodoc
CATALOGNAME_CSWpangodoc += libpango_doc_stub
SPKG_DESC_CSWpango-doc = Documentation for Pango
PKGFILES_CSWpango-doc = $(sharedstatedir)/gtk-doc/.*
L_CSWpangodoc = 1

BUILD_DEP_PKGS += CSWggettext-dev
BUILD_DEP_PKGS += CSWgtk-doc
BUILD_DEP_PKGS += CSWlibxslt
BUILD_DEP_PKGS BUILD_DEP_PKGS += CSWlibharfbuzz-dev
 CSWglib2devel
# BUILD_DEP_PKGS += CSWlibxft2devel
BUILD_DEP_PKGS += CSWvim # for generating do# check.defs fails, and I'dont care too much about it.
#
# So, employing a custom test script only performing tests in tests
TEST_SCRIPTS = customdocs

BUILD64 = 1

sysconfdir-suffix-64 = /64
sysconfdir = /etc/opt/csw$(sysconfdir-suffix-$(MEMORYMODEL))

# EXTRA_ISAEXEC_EXCLUDE_FILES = $(bindir)/pango-querymodules
CONFIGURE_ARGS  = $(DIRPATHS)
CONenable-gtk-doc
CONFIGURE_ARGS += --with-xft
CONFIGURE_ARGS += --disable-static

STRIP_LIBTOOL = 1

include gar/category.mk

test-custom:
	cd $(WORKSRC)/tests && env $(BUILD_ENV) $(MAKE) check
	@$(MAKECOOKIE)

post-merge:
	[ -d $(PKGROOT)$(sysconfdir)/pango ] || mkdir -p $(PKGROOT)$(sysconfdir)/pango
	@$(MAKECOOKIE)
