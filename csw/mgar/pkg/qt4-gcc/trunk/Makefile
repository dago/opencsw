# $Id$

NAME = qt
VERSION = 4.8.0
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = TrollTech C++ application framework
define BLURB
  It contains a C++ class library as well as tools for cross-platform GUI
  development and internationalization.
endef

prefix = $(BUILD_PREFIX)/gxx
GARCOMPILER = GNU

MASTER_SITES = http://get.qt.nokia.com/qt/source/
DISTNAME = qt-everywhere-opensource-src-$(VERSION)
DISTFILES = $(DISTNAME).tar.gz

LICENSE = README

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

# http://wiki.opencsw.org/porting-faq#toc9
EXTRA_CFLAGS = -DSUN_OGL_NO_VERTEX_MACROS
EXTRA_CXXFLAGS = -DSUN_OGL_NO_VERTEX_MACROS

CONFIGURE_ARGS += -platform solaris-g++
CONFIGURE_ARGS += -opensource
CONFIGURE_ARGS += -prefix $(prefix)
CONFIGURE_ARGS += -no-qt3support
CONFIGURE_ARGS += -webkit
CONFIGURE_ARGS_sparc += -big-endian -host-big-endian
CONFIGURE_ARGS_i386 += -little-endian -host-big-endian
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GARCH))

# TEST_TARGET =

INSTALL_ROOT = $(DESTDIR)
EXTRA_INSTALL_EXPORTS = INSTALL_ROOT

PACKAGES += CSWqt4-gxx-dev
SPKG_DESC_CSWqt4-gxx-dev += $(DESCRIPTION), development files
PKGFILES_CSWqt4-gxx-dev += $(PKGFILES_DEVEL)

PACKAGES += CSWqt4-gxx-doc
SPKG_DESC_CSWqt4-gxx-doc += $(DESCRIPTION), documentation
# Catch-all

PACKGES += CSWlibqtgui4-gxx
PKGFILES_CSWlibqtgui4-gxx += $(call baseisadirs,$(libdir),libQtGui\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtgui4-gxx += $(DESCRIPTION), libQtGui.so.4

PACKAGES += CSWlibqthelp4-gxx
PKGFILES_CSWlibqthelp4-gxx += $(call baseisadirs,$(libdir),libQtHelp\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqthelp4-gxx += $(DESCRIPTION), libQtHelp.so.4

PACKAGES += CSWlibqtmultimedia4-gxx
PKGFILES_CSWlibqtmultimedia4-gxx += $(call baseisadirs,$(libdir),libQtMultimedia\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtmultimedia4-gxx += $(DESCRIPTION), libQtMultimedia.so.4

PACKAGES += CSWlibqtnetwork4-gxx
PKGFILES_CSWlibqtnetwork4-gxx += $(call baseisadirs,$(libdir),libQtNetwork\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtnetwork4-gxx += $(DESCRIPTION), libQtNetwork.so.4

PACKAGES += CSWlibqtopengl4-gxx
PKGFILES_CSWlibqtopengl4-gxx += $(call baseisadirs,$(libdir),libQtOpenGL\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtopengl4-gxx += $(DESCRIPTION), libQtOpenGL.so.4

PACKAGES += CSWlibqtscript4-gxx
PKGFILES_CSWlibqtscript4-gxx += $(call baseisadirs,$(libdir),libQtScript\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtscript4-gxx += $(DESCRIPTION), libQtScript.so.4

PACKAGES += CSWlibqtscripttools4-gxx
PKGFILES_CSWlibqtscripttools4-gxx += $(call baseisadirs,$(libdir),libQtScriptTools\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtscripttools4-gxx += $(DESCRIPTION), libQtScriptTools.so.4

PACKAGES += CSWlibqtsql4-gxx
PKGFILES_CSWlibqtsql4-gxx += $(call baseisadirs,$(libdir),libQtSql\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtsql4-gxx += $(DESCRIPTION), libQtSql.so.4

PACKAGES += CSWlibqtsvg4-gxx
PKGFILES_CSWlibqtsvg4-gxx += $(call baseisadirs,$(libdir),libQtSvg\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtsvg4-gxx += $(DESCRIPTION), libQtSvg.so.4

PACKAGES += CSWlibqttest4-gxx
PKGFILES_CSWlibqttest4-gxx += $(call baseisadirs,$(libdir),libQtTest\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqttest4-gxx += $(DESCRIPTION), libQtTest.so.4

PACKAGES += CSWlibphonon4-gxx
PKGFILES_CSWlibphonon4-gxx += $(call baseisadirs,$(libdir),libphonon\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibphonon4-gxx += $(DESCRIPTION), libphonon.so.4

PACKAGES += CSWlibqtclucene4-gxx
PKGFILES_CSWlibqtclucene4-gxx += $(call baseisadirs,$(libdir),libQtCLucene\.so\.4\.8\.0)
SPKG_DESC_CSWlibqtclucene4-gxx += $(DESCRIPTION), libQtCLucene.so.4

PACKAGES += CSWlibqtcore4-gxx
PKGFILES_CSWlibqtcore4-gxx += $(call baseisadirs,$(libdir),libQtCore\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtcore4-gxx += $(DESCRIPTION), libQtCore.so.4

PACKAGES += CSWlibqtdbus4-gxx
PKGFILES_CSWlibqtdbus4-gxx += $(call baseisadirs,$(libdir),libQtDBus\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtdbus4-gxx += $(DESCRIPTION), libQtDBus.so.4

PACKAGES += CSWlibqtdeclarative4-gxx
PKGFILES_CSWlibqtdeclarative4-gxx += $(call baseisadirs,$(libdir),libQtDeclarative\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtdeclarative4-gxx += $(DESCRIPTION), libQtDeclarative.so.4

PACKAGES += CSWlibqtdesigner4-gxx
PKGFILES_CSWlibqtdesigner4-gxx += $(call baseisadirs,$(libdir),libQtDesigner\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtdesigner4-gxx += $(DESCRIPTION), libQtDesigner.so.4

PACKAGES += CSWlibqtdesignercomponents4-gxx
PKGFILES_CSWlibqtdesignercomponents4-gxx += $(call baseisadirs,$(libdir),libQtDesignerComponents\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtdesignercomponents4-gxx += $(DESCRIPTION), libQtDesignerComponents.so.4

PACKAGES += CSWlibqtgui4-gxx
PKGFILES_CSWlibqtgui4-gxx += $(call baseisadirs,$(libdir),libQtGui\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtgui4-gxx += $(DESCRIPTION), libQtGui.so.4

PACKAGES += CSWlibqtxml4-gxx
PKGFILES_CSWlibqtxml4-gxx += $(call baseisadirs,$(libdir),libQtXml\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtxml4-gxx += $(DESCRIPTION), libQtXml.so.4

# These are code examples.
CHECKPKG_OVERRIDES_CSWqt4-gxx-doc += binary-architecture-does-not-match-placement
CHECKPKG_OVERRIDES_CSWqt4-gxx-doc += file-with-bad-content

include gar/category.mk
