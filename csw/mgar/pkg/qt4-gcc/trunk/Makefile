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
CONFIGURE_ARGS += -v -shared -stl -largefile -sm 
CONFIGURE_ARGS += -qt-libjpeg -qt-libpng -qt-libmng -qt-zlib 
CONFIGURE_ARGS += -I/usr/include -I/usr/X11/include 
CONFIGURE_ARGS += -I/usr/X11/share/include -I/usr/sfw/include
# CONFIGURE_ARGS_sparc += -big-endian -host-big-endian
# CONFIGURE_ARGS_i386 += -little-endian -host-big-endian
# CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GARCH))

# TEST_TARGET =

INSTALL_ROOT = $(DESTDIR)
EXTRA_INSTALL_EXPORTS = INSTALL_ROOT

PACKAGES += CSWqt4-gxx-dev
SPKG_DESC_CSWqt4-gxx-dev += $(DESCRIPTION), development files
PKGFILES_CSWqt4-gxx-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWqt4-gxx-dev += CSWlibqtscript4-gxx
RUNTIME_DEP_PKGS_CSWqt4-gxx-dev += CSWlibqtdesignercomponents4-gxx
RUNTIME_DEP_PKGS_CSWqt4-gxx-dev += CSWlibqtdesigner4-gxx
RUNTIME_DEP_PKGS_CSWqt4-gxx-dev += CSWlibqtxml4-gxx
RUNTIME_DEP_PKGS_CSWqt4-gxx-dev += CSWlibqthelp4-gxx
RUNTIME_DEP_PKGS_CSWqt4-gxx-dev += CSWlibqttest4-gxx
RUNTIME_DEP_PKGS_CSWqt4-gxx-dev += CSWlibqtnetwork4-gxx
RUNTIME_DEP_PKGS_CSWqt4-gxx-dev += CSWlibqtdbus4-gxx
RUNTIME_DEP_PKGS_CSWqt4-gxx-dev += CSWlibqtclucene4-gxx
RUNTIME_DEP_PKGS_CSWqt4-gxx-dev += CSWlibqtcore4-gxx
RUNTIME_DEP_PKGS_CSWqt4-gxx-dev += CSWlibqtscripttools4-gxx
RUNTIME_DEP_PKGS_CSWqt4-gxx-dev += CSWlibqtdeclarative4-gxx
RUNTIME_DEP_PKGS_CSWqt4-gxx-dev += CSWlibqtgui4-gxx
RUNTIME_DEP_PKGS_CSWqt4-gxx-dev += CSWlibqtopengl4-gxx
RUNTIME_DEP_PKGS_CSWqt4-gxx-dev += CSWlibqtmultimedia4-gxx
RUNTIME_DEP_PKGS_CSWqt4-gxx-dev += CSWlibqtsvg4-gxx
RUNTIME_DEP_PKGS_CSWqt4-gxx-dev += CSWlibphonon4-gxx
RUNTIME_DEP_PKGS_CSWqt4-gxx-dev += CSWlibqtsql4-gxx

PACKAGES += CSWqt4-gxx-doc
SPKG_DESC_CSWqt4-gxx-doc += $(DESCRIPTION), documentation
# Catch-all
RUNTIME_DEP_PKGS_CSWqt4-gxx-doc += CSWlibqtscript4-gxx
RUNTIME_DEP_PKGS_CSWqt4-gxx-doc += CSWlibqtdeclarative4-gxx
RUNTIME_DEP_PKGS_CSWqt4-gxx-doc += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWqt4-gxx-doc += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWqt4-gxx-doc += CSWlibqttest4-gxx
RUNTIME_DEP_PKGS_CSWqt4-gxx-doc += CSWlibsybdb5
RUNTIME_DEP_PKGS_CSWqt4-gxx-doc += CSWlibqtclucene4-gxx
RUNTIME_DEP_PKGS_CSWqt4-gxx-doc += CSWlibxrender
RUNTIME_DEP_PKGS_CSWqt4-gxx-doc += CSWlibqtdesignercomponents4-gxx
RUNTIME_DEP_PKGS_CSWqt4-gxx-doc += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWqt4-gxx-doc += CSWlibphonon4-gxx
RUNTIME_DEP_PKGS_CSWqt4-gxx-doc += CSWlibqtsql4-gxx
RUNTIME_DEP_PKGS_CSWqt4-gxx-doc += CSWlibintl8
RUNTIME_DEP_PKGS_CSWqt4-gxx-doc += CSWlibqtnetwork4-gxx
RUNTIME_DEP_PKGS_CSWqt4-gxx-doc += CSWlibqthelp4-gxx
RUNTIME_DEP_PKGS_CSWqt4-gxx-doc += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWqt4-gxx-doc += CSWlibqtscripttools4-gxx
RUNTIME_DEP_PKGS_CSWqt4-gxx-doc += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWqt4-gxx-doc += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWqt4-gxx-doc += CSWlibqtmultimedia4-gxx
RUNTIME_DEP_PKGS_CSWqt4-gxx-doc += CSWlibodbc2
RUNTIME_DEP_PKGS_CSWqt4-gxx-doc += CSWsqlite
RUNTIME_DEP_PKGS_CSWqt4-gxx-doc += CSWfconfig
RUNTIME_DEP_PKGS_CSWqt4-gxx-doc += CSWlibpq5
RUNTIME_DEP_PKGS_CSWqt4-gxx-doc += CSWlibqtxml4-gxx
RUNTIME_DEP_PKGS_CSWqt4-gxx-doc += CSWlibtiff3
RUNTIME_DEP_PKGS_CSWqt4-gxx-doc += CSWgstplugins
RUNTIME_DEP_PKGS_CSWqt4-gxx-doc += CSWmesa
RUNTIME_DEP_PKGS_CSWqt4-gxx-doc += CSWlibqtsvg4-gxx
RUNTIME_DEP_PKGS_CSWqt4-gxx-doc += CSWlibqtdesigner4-gxx
RUNTIME_DEP_PKGS_CSWqt4-gxx-doc += CSWlibqtdbus4-gxx
RUNTIME_DEP_PKGS_CSWqt4-gxx-doc += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWqt4-gxx-doc += CSWlibqtcore4-gxx
RUNTIME_DEP_PKGS_CSWqt4-gxx-doc += CSWgstreamer
RUNTIME_DEP_PKGS_CSWqt4-gxx-doc += CSWlibqtgui4-gxx
RUNTIME_DEP_PKGS_CSWqt4-gxx-doc += CSWlibqtopengl4-gxx
RUNTIME_DEP_PKGS_CSWqt4-gxx-doc += CSWlibgcc-s1
CHECKPKG_OVERRIDES_CSWqt4-gxx-doc += discouraged-path-in-pkgmap|/opt/csw/gxx/demos/shared/libdemo_shared.a
CHECKPKG_OVERRIDES_CSWqt4-gxx-doc += discouraged-path-in-pkgmap|/opt/csw/gxx/examples/tools/plugandpaint/plugins/libpnp_basictools.a

PACKGES += CSWlibqtgui4-gxx
PKGFILES_CSWlibqtgui4-gxx += $(call baseisadirs,$(libdir),libQtGui\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtgui4-gxx += $(DESCRIPTION), libQtGui.so.4
RUNTIME_DEP_PKGS_CSWlibqtgui4-gxx += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibqtgui4-gxx += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibqtgui4-gxx += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibqtgui4-gxx += CSWlibxrender
RUNTIME_DEP_PKGS_CSWlibqtgui4-gxx += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibqtgui4-gxx += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibqtgui4-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqtgui4-gxx += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibqtgui4-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibqtgui4-gxx += CSWlibqtcore4-gxx
CHECKPKG_OVERRIDES_CSWlibqtgui4-gxx += file-with-bad-content|/usr/local|root/opt/csw/gxx/lib/libQtGui.so.4.8.0
CHECKPKG_OVERRIDES_CSWlibqtgui4-gxx += file-with-bad-content|/usr/share|root/opt/csw/gxx/lib/libQtGui.so.4.8.0

PACKAGES += CSWlibqthelp4-gxx
PKGFILES_CSWlibqthelp4-gxx += $(call baseisadirs,$(libdir),libQtHelp\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqthelp4-gxx += $(DESCRIPTION), libQtHelp.so.4
RUNTIME_DEP_PKGS_CSWlibqthelp4-gxx += CSWlibqtnetwork4-gxx
RUNTIME_DEP_PKGS_CSWlibqthelp4-gxx += CSWqt4-gxx-doc
RUNTIME_DEP_PKGS_CSWlibqthelp4-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqthelp4-gxx += CSWlibqtgui4-gxx
RUNTIME_DEP_PKGS_CSWlibqthelp4-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibqthelp4-gxx += CSWlibqtcore4-gxx
RUNTIME_DEP_PKGS_CSWlibqthelp4-gxx += CSWlibqtsql4-gxx

PACKAGES += CSWlibqtmultimedia4-gxx
PKGFILES_CSWlibqtmultimedia4-gxx += $(call baseisadirs,$(libdir),libQtMultimedia\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtmultimedia4-gxx += $(DESCRIPTION), libQtMultimedia.so.4
RUNTIME_DEP_PKGS_CSWlibqtmultimedia4-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibqtmultimedia4-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqtmultimedia4-gxx += CSWlibqtgui4-gxx
RUNTIME_DEP_PKGS_CSWlibqtmultimedia4-gxx += CSWlibqtcore4-gxx

PACKAGES += CSWlibqtnetwork4-gxx
PKGFILES_CSWlibqtnetwork4-gxx += $(call baseisadirs,$(libdir),libQtNetwork\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtnetwork4-gxx += $(DESCRIPTION), libQtNetwork.so.4
RUNTIME_DEP_PKGS_CSWlibqtnetwork4-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibqtnetwork4-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqtnetwork4-gxx += CSWlibqtcore4-gxx
CHECKPKG_OVERRIDES_CSWlibqtnetwork4-gxx += file-with-bad-content|/usr/local|root/opt/csw/gxx/lib/libQtNetwork.so.4.8.0
CHECKPKG_OVERRIDES_CSWlibqtnetwork4-gxx += file-with-bad-content|/usr/share|root/opt/csw/gxx/lib/libQtNetwork.so.4.8.0

PACKAGES += CSWlibqtopengl4-gxx
PKGFILES_CSWlibqtopengl4-gxx += $(call baseisadirs,$(libdir),libQtOpenGL\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtopengl4-gxx += $(DESCRIPTION), libQtOpenGL.so.4
RUNTIME_DEP_PKGS_CSWlibqtopengl4-gxx += CSWlibxrender
RUNTIME_DEP_PKGS_CSWlibqtopengl4-gxx += CSWlibqtcore4-gxx
RUNTIME_DEP_PKGS_CSWlibqtopengl4-gxx += CSWmesa
RUNTIME_DEP_PKGS_CSWlibqtopengl4-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqtopengl4-gxx += CSWlibqtgui4-gxx
RUNTIME_DEP_PKGS_CSWlibqtopengl4-gxx += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibqtopengl4-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibqtopengl4-gxx += CSWfconfig

PACKAGES += CSWlibqtscript4-gxx
PKGFILES_CSWlibqtscript4-gxx += $(call baseisadirs,$(libdir),libQtScript\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtscript4-gxx += $(DESCRIPTION), libQtScript.so.4
RUNTIME_DEP_PKGS_CSWlibqtscript4-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibqtscript4-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqtscript4-gxx += CSWlibqtcore4-gxx

PACKAGES += CSWlibqtscripttools4-gxx
PKGFILES_CSWlibqtscripttools4-gxx += $(call baseisadirs,$(libdir),libQtScriptTools\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtscripttools4-gxx += $(DESCRIPTION), libQtScriptTools.so.4
RUNTIME_DEP_PKGS_CSWlibqtscripttools4-gxx += CSWlibqtscript4-gxx
RUNTIME_DEP_PKGS_CSWlibqtscripttools4-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibqtscripttools4-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqtscripttools4-gxx += CSWlibqtgui4-gxx
RUNTIME_DEP_PKGS_CSWlibqtscripttools4-gxx += CSWlibqtcore4-gxx

PACKAGES += CSWlibqtsql4-gxx
PKGFILES_CSWlibqtsql4-gxx += $(call baseisadirs,$(libdir),libQtSql\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtsql4-gxx += $(DESCRIPTION), libQtSql.so.4
RUNTIME_DEP_PKGS_CSWlibqtsql4-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibqtsql4-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqtsql4-gxx += CSWlibqtcore4-gxx

PACKAGES += CSWlibqtsvg4-gxx
PKGFILES_CSWlibqtsvg4-gxx += $(call baseisadirs,$(libdir),libQtSvg\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtsvg4-gxx += $(DESCRIPTION), libQtSvg.so.4
RUNTIME_DEP_PKGS_CSWlibqtsvg4-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibqtsvg4-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqtsvg4-gxx += CSWlibqtgui4-gxx
RUNTIME_DEP_PKGS_CSWlibqtsvg4-gxx += CSWlibqtcore4-gxx

PACKAGES += CSWlibqttest4-gxx
PKGFILES_CSWlibqttest4-gxx += $(call baseisadirs,$(libdir),libQtTest\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqttest4-gxx += $(DESCRIPTION), libQtTest.so.4
RUNTIME_DEP_PKGS_CSWlibqttest4-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibqttest4-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqttest4-gxx += CSWlibqtcore4-gxx

PACKAGES += CSWlibphonon4-gxx
PKGFILES_CSWlibphonon4-gxx += $(call baseisadirs,$(libdir),libphonon\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibphonon4-gxx += $(DESCRIPTION), libphonon.so.4
RUNTIME_DEP_PKGS_CSWlibphonon4-gxx += CSWlibqtxml4-gxx
RUNTIME_DEP_PKGS_CSWlibphonon4-gxx += CSWlibqtdbus4-gxx
RUNTIME_DEP_PKGS_CSWlibphonon4-gxx += CSWlibqtcore4-gxx
RUNTIME_DEP_PKGS_CSWlibphonon4-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibphonon4-gxx += CSWlibqtgui4-gxx
RUNTIME_DEP_PKGS_CSWlibphonon4-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibqtdbus4-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibqtdbus4-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqtdbus4-gxx += CSWlibqtxml4-gxx
RUNTIME_DEP_PKGS_CSWlibqtdbus4-gxx += CSWlibqtcore4-gxx

PACKAGES += CSWlibqtclucene4-gxx
PKGFILES_CSWlibqtclucene4-gxx += $(call baseisadirs,$(libdir),libQtCLucene\.so\.4\.8\.0)
SPKG_DESC_CSWlibqtclucene4-gxx += $(DESCRIPTION), libQtCLucene.so.4
RUNTIME_DEP_PKGS_CSWlibqtclucene4-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibqtclucene4-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqtclucene4-gxx += CSWlibqtcore4-gxx

PACKAGES += CSWlibqtcore4-gxx
PKGFILES_CSWlibqtcore4-gxx += $(call baseisadirs,$(libdir),libQtCore\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtcore4-gxx += $(DESCRIPTION), libQtCore.so.4
RUNTIME_DEP_PKGS_CSWlibqtcore4-gxx += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibqtcore4-gxx += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibqtcore4-gxx += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibqtcore4-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqtcore4-gxx += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibqtcore4-gxx += CSWlibgcc-s1

PACKAGES += CSWlibqtdbus4-gxx
PKGFILES_CSWlibqtdbus4-gxx += $(call baseisadirs,$(libdir),libQtDBus\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtdbus4-gxx += $(DESCRIPTION), libQtDBus.so.4

PACKAGES += CSWlibqtdeclarative4-gxx
PKGFILES_CSWlibqtdeclarative4-gxx += $(call baseisadirs,$(libdir),libQtDeclarative\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtdeclarative4-gxx += $(DESCRIPTION), libQtDeclarative.so.4
RUNTIME_DEP_PKGS_CSWlibqtdeclarative4-gxx += CSWlibqtscript4-gxx
RUNTIME_DEP_PKGS_CSWlibqtdeclarative4-gxx += CSWlibqtnetwork4-gxx
RUNTIME_DEP_PKGS_CSWlibqtdeclarative4-gxx += CSWlibqtcore4-gxx
RUNTIME_DEP_PKGS_CSWlibqtdeclarative4-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqtdeclarative4-gxx += CSWlibqtgui4-gxx
RUNTIME_DEP_PKGS_CSWlibqtdeclarative4-gxx += CSWlibqtsvg4-gxx
RUNTIME_DEP_PKGS_CSWlibqtdeclarative4-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibqtdeclarative4-gxx += CSWlibqtsql4-gxx

PACKAGES += CSWlibqtdesigner4-gxx
PKGFILES_CSWlibqtdesigner4-gxx += $(call baseisadirs,$(libdir),libQtDesigner\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtdesigner4-gxx += $(DESCRIPTION), libQtDesigner.so.4
RUNTIME_DEP_PKGS_CSWlibqtdesigner4-gxx += CSWlibqtscript4-gxx
RUNTIME_DEP_PKGS_CSWlibqtdesigner4-gxx += CSWlibqtxml4-gxx
RUNTIME_DEP_PKGS_CSWlibqtdesigner4-gxx += CSWlibqtcore4-gxx
RUNTIME_DEP_PKGS_CSWlibqtdesigner4-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqtdesigner4-gxx += CSWlibqtgui4-gxx
RUNTIME_DEP_PKGS_CSWlibqtdesigner4-gxx += CSWlibgcc-s1

PACKAGES += CSWlibqtdesignercomponents4-gxx
PKGFILES_CSWlibqtdesignercomponents4-gxx += $(call baseisadirs,$(libdir),libQtDesignerComponents\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtdesignercomponents4-gxx += $(DESCRIPTION), libQtDesignerComponents.so.4
RUNTIME_DEP_PKGS_CSWlibqtdesignercomponents4-gxx += CSWlibqtscript4-gxx
RUNTIME_DEP_PKGS_CSWlibqtdesignercomponents4-gxx += CSWlibqtdesigner4-gxx
RUNTIME_DEP_PKGS_CSWlibqtdesignercomponents4-gxx += CSWlibqtxml4-gxx
RUNTIME_DEP_PKGS_CSWlibqtdesignercomponents4-gxx += CSWlibqtcore4-gxx
RUNTIME_DEP_PKGS_CSWlibqtdesignercomponents4-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqtdesignercomponents4-gxx += CSWlibqtgui4-gxx
RUNTIME_DEP_PKGS_CSWlibqtdesignercomponents4-gxx += CSWlibgcc-s1

PACKAGES += CSWlibqtgui4-gxx
PKGFILES_CSWlibqtgui4-gxx += $(call baseisadirs,$(libdir),libQtGui\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtgui4-gxx += $(DESCRIPTION), libQtGui.so.4

PACKAGES += CSWlibqtxml4-gxx
PKGFILES_CSWlibqtxml4-gxx += $(call baseisadirs,$(libdir),libQtXml\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtxml4-gxx += $(DESCRIPTION), libQtXml.so.4
RUNTIME_DEP_PKGS_CSWlibqtxml4-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibqtxml4-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqtxml4-gxx += CSWlibqtcore4-gxx

# These are code examples.
CHECKPKG_OVERRIDES_CSWqt4-gxx-doc += binary-architecture-does-not-match-placement
CHECKPKG_OVERRIDES_CSWqt4-gxx-doc += file-with-bad-content

include gar/category.mk
