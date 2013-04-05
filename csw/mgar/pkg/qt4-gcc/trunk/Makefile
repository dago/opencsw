# $Id$

NAME = qt
VERSION = 4.8.1
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = TrollTech C++ application framework
define BLURB
  It contains a C++ class library as well as tools for cross-platform GUI
  development and internationaUILD_PREFIX)/gxx
GARCOMPILER = GNUftp://ftp.qt-project.org/get.qt.nokia.com/qt/source/
DISTNAME = qt-everywhere-opensource-src-$(VERSION)
DISTFILES = $(DISTNAME).tar.gz

LNOGITPATCH = 1
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

REINPLACE_USRLOCAL += src/gui/kernel/qguiplatformplugin.cpp 
REINPLACE_USRLOCAL += src/network/ssl/qsslsocket_openssl_symbols.cpp
REINPLACE_USRLOCAL += src/network/ssl/qsslsocket_openssl.cpp
REINPLACE_USRLOCAL += src/network/ssl/qsslsocket.cpp
REINPLACE_USRLOCAL += src/3rdparty/webkit/Source/WebCore/plugins/PluginDatabase.cpp
PATCHFILES += mkspec-csw.patch
# bug in 4.8.1, see: https//bugreports.qt-project.org/browse/QTBUG-25281
PATCHFILES += 0001-shapeinputILES += no-xshape.patch

REINPLACE_USRLOCAL += src/gui/kernel/qguiplatformplugin.cpp
REINPLACE_USRLOCAL += src/network/ssl/qsslsocket_openssl_symbols.cpp
# replace SSL cert location
REINPLACE_USRLOCAL += src/network/ssl/qsslsocket.cpp

# http://wiki.opencsw.org/porting-faq#toc9
EXTRA_CFLAGS = -DSUN_OGL_NO_VERTEX_MACROS
EXTRA_CXXFLAGS = -DSUN_OGL_NO_VERTEX_MACROS

CONFIGURE_ARGS += -platform solaris-g++
CONFIGURE_ARGS += -opensource
COconfirm-licensRGS += -opensource
CONFIGURE_ARGS += -prefix $(prefix)
CONFIGURE_ARGS += -no-qt3support
COno-xshape+= -no-qt3support
CONFIGURE_ARGS += -webkit
CONFIGURE_ARGS += -v -shared -stl -largefile -sm 
CONFIGURE_ARGS += -qt-libjpeg -qt-libpng -qt-# compile error: error: 'QGtkStyle' has not been declared ??? since 10.12.2012
CONFIGURE_ARGS += -no-gtkstyle-libmng -qt-zlib 
CON$(BUILD_PREFIX)/include/gtk-2.0
CONFIGURE_ARGS +=+= -I/usr/include -I/usr/X11/include 
CONFIGURE_ARGS += -I/usr/XGS += -no-xshape
CONFIGURE_ARGS_sparc += -big-endian -host-big-endian
# CONFIGURE_ARGS_i386 += -little-endian -host-big-endian
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GARCH))

# TEST_TARGET =

INSTALL_ROOT = $(DESTDIR)
EXTRA_INSTALL_EXPORTS = INSTALL_ROOT


PACKAGES
PKGFILES_CSWlibqtcore4 += $(call baseisadirs,$(libdir),libQtCore\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtcore4CSWlibqtcore4-gxx += $(DESCRIPTION), libQtCore.so.4
# RUNTIME_DEP_P += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibqtcore4 += CSWlibiconv2
# RUNTIME_DEP_PKGS_CSWlibqtcore4 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibqtcore4 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqtcore4 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibqtcore4 += CSWlibgcc-s1

PACKAGES += CSWlibqtgui4
PKGFILES_CSWlibqtgui4 += $(call baseisadirs,$(libdir),libQtGui\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtgui4 += $(DESCRIPTION), libQtGui.so.4
# RUNTIME_DEP_PKGS_CSWlibqtgui4 += CSWlibgthread2-0-0
# RUNTIME_DEP_PKGS_CSWlibqtgui4 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibqtgui4 += CSWlibxrender
RUNTIME_DEP_PKGS_CSWlibqtgui4 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqtgui4 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibqtgui4 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibqtgui4 += CSWlibqtcore4
# RUNTIME_DEP_PKGS_CSWlibqtgui4_sparc += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibqtgui4 += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWlibqtgui4 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibqtgui4 += $(RUNTIME_DEP_PKGS_CSWlibqtgui4_$(GARCH))
CHECKPKG_OVERRIDES_CSWlibqtgui4 += file-with-bad-content|/usr/share|root/opt/csw/lib/libQtGui.so.4.8.1

PACKAGES += CSWqt4-dev
SPKG_DESC_CSWqt4-dev += $(DESCRIPTION), development files
PKGFILES_CSWqt4-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWqt4-dev += $(call baseisadirs,$(bindir),.*)
PKGFILES_CSWqt4-dev += $(prefix)/examples/.*
PKGFILES_CSWqt4-dev += $(prefix)/plugins/.*
PKGFILES_CSWqt4-dev += $(prefix)/demos/.*
PKGFILES_CSWqt4-dev += $(prefix)/imports/.*
PKGFILES_CSWqt4-dev += $(prefix)/mkspecs/.*
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibqtscript4
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibqtdesignercomponents4
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibqtdesigner4
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibqtxml4
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibqthelp4
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibqttest4
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibqtnetwork4
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibqtdbus4
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWdbus
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibqtclucene4
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibqtcore4
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibqtscripttools4
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibqtdeclarative4
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibqtgui4
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibqtopengl4
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibqtmultimedia4
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibqtsvg4
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibphonon4
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibqtsql4
# RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibgthread2-0-0
# RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibgmodule2-0-0
# RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibintl8
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWgstreamer
# RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibxrender
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWmesa
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibglib2-0-0
# RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWgstplugins
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibsybdb5
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWsqlite
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibpq5
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibodbc2
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibtiff3
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibmysqlclient18
# RUNTIME_DEP_PKGS_CSWqt4-dev_sparc += CSWlibfontconfig1
# RUNTIME_DEP_PKGS_CSWqt4-dev_sparc += CSWlibfreetype6
# RUNTIME_DEP_PKGS_CSWqt4-dev += $(RUNTIME_DEP_PKGS_CSWqt4-dev_$(GARCH))
# These are code examples.
CHECKPKG_OVERRIDES_CSWqt4-dev += binary-architecture-does-not-match-placement

# REFINE this later!
CHECKPKG_OVERRIDES_CSWqt4-dev += file-with-bad-content
CHECKPKG_OVERRIDES_CSWqt4RRIDES_CSWqt4-gxx-dev += discouraged-path-in-pkgmap
# because libdbus needs /etc/machine-id which can generated with a tool of CSWdbus
CHECKPKG_dev += surplus-dependency|CSWdbus

PACKAGES += CSWlibqthelp4
PKGFILES_CSWlibqthelp4 += $(call baseisadirs,$(libdir),libQtHelp\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqthelp4 += $(DESCRIPTION), libQtHelp.so.4
RUNTIME_DEP_PKGS_CSWlibqthelp4 += CSWlibqtnetwork4
RUNTIME_DEP_PKGS_CSWlibqthelp4 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqthelp4 += CSWlibqtgui4
RUNTIME_DEP_PKGS_CSWlibqthelp4 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibqthelp4 += CSWlibqtcore4
RUNTIME_DEP_PKGS_CSWlibqthelp4 += CSWlibqtsql4
RUNTIME_DEP_PKGS_CSWlibqthelp4 += CSWlibqtclucene4

PACKAGES += CSWlibqtmultimedia4
PKGFILES_CSWlibqtmultimedia4qtmultimedia4-gxx += $(call baseisadirs,$(libdir),libQtMultimedia\.so\.4(\.\d+)*)
SPKG_DESC_CS += $(DESCRIPTION), libQtMultimedia.so.4
RUNTIME_DEP_PKGS_CSWlibqtmultimedia4 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibqtmultimedia4 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqtmultimedia4 += CSWlibqtgui4
RUNTIME_DEP_PKGS_CSWlibqtmultimedia4 += CSWlibqtcore4

PACKAGES += CSWlibqtnetwork4
PKGFILES_CSWlibqtnetwork4 += $(call baseisadirs,$(libdir),libQtNetwork\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtnetwork4libqtnetwork4-gxx += $(DESCRIPTION), libQtNetwork.so.4
RUNTIME_DEP_PKGS += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibqtnetwork4 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqtnetwork4 += CSWlibqtcore4
CHECKPKG_OVERRIDES_CSWlibqtnetwork4libqtnetwork4-gxx += file-with-bad-content|/usr/shroot/opt/csw/gxx/lib/libQtNetwork.so.4.8.1

PACKAGES +
PKGFILES_CSWlibqtopengl4Wlibqtopengl4-gxx += $(call baseisadirs,$(libdir),libQtOpenGL\.so\.4(\.\d+)*)
SPKG_DES += $(DESCRIPTION), libQtOpenGL.so.4
RUNTIME_DEP_PKGS_CSWlibqtopengl4 += CSWlibxrender
RUNTIME_DEP_PKGS_CSWlibqtopengl4 += CSWlibqtcore4
RUNTIME_DEP_PKGS_CSWlibqtopengl4 += CSWmesa
RUNTIME_DEP_PKGS_CSWlibqtopengl4 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqtopengl4 += CSWlibqtgui4
RUNTIME_DEP_PKGS_CSWlibqtopengl4 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibqtopengl4_sparc += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWlibqtopengl4 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibqtopengl4 += $(RUNTIME_DEP_PKGS_CSWlibqtopengl4_$(GARCH))


PACKAGES += CSWlibqtscript4
PKGFILES_CSWlibqtscript4 += $(call baseisadirs,$(libdir),libQtScript\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtscript4 += $(DESCRIPTION), libQtScript.so.4
RUNTIME_DEP_PKGS_CSWlibqtscript4 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibqtscript4 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqtscript4 += CSWlibqtcore4

PACKAGES += CSWlibqtscripttools4
PKGFILES_CSWlibqtscripttools4 += $(call baseisadirs,$(libdir),libQtScriptTools\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtscripttools4 += $(DESCRIPTION), libQtScriptTools.so.4
RUNTIME_DEP_PKGS_CSWlibqtscripttools4 += CSWlibqtscript4
RUNTIME_DEP_PKGS_CSWlibqtscripttools4 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibqtscripttools4 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqtscripttools4 += CSWlibqtgui4
RUNTIME_DEP_PKGS_CSWlibqtscripttools4 += CSWlibqtcore4

PACKAGES += CSWlibqtsql4
PKGFILES_CSWlibqtsql4_CSWlibqtsql4-gxx += $(call baseisadirs,$(libdir),libQtSql\.so\.4(\.\d+)*)
SPKG_ += $(DESCRIPTION), libQtSql.so.4
RUNTIME_DEP_PKGS_CSWlibqtsql4 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibqtsql4 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqtsql4 += CSWlibqtcore4

PACKAGES += CSWlibqtsvg4
PKGFILES_CSWlibqtsvg4 += $(call baseisadirs,$(libdir),libQtSvg\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtsvg4 += $(DESCRIPTION), libQtSvg.so.4
RUNTIME_DEP_PKGS_CSWlibqtsvg4 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibqtsvg4 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqtsvg4 += CSWlibqtgui4
RUNTIME_DEP_PKGS_CSWlibqtsvg4 += CSWlibqtcore4

PACKAGES += CSWlibqttest4
PKGFILES_CSWlibqttest4 += $(call baseisadirs,$(libdir),libQtTest\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqttest4 += $(DESCRIPTION), libQtTest.so.4
RUNTIME_DEP_PKGS_CSWlibqttest4 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibqttest4 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqttest4 += CSWlibqtcore4

PACKAGES += CSWlibphonon4
PKGFILES_CSWlibphonon4 += $(call baseisadirs,$(libdir),libphonon\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibphonon4 += $(DESCRIPTION), libphonon.so.4
# RUNTIME_DEP_PKGS_CSWlibphonon4 += CSWlibqtxml4
RUNTIME_DEP_PKGS_CSWlibphonon4 += CSWlibqtdbus4
RUNTIME_DEP_PKGS_CSWlibphonon4 += CSWlibqtcore4
RUNTIME_DEP_PKGS_CSWlibphonon4 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibphonon4 += CSWlibqtgui4
RUNTIME_DEP_PKGS_CSWlibphonon4 += CSWlibgcc-s1

PACKAGES += CSWlibqtclucene4
PKGFILES_CSWlibqtclucene4 += $(call baseisadirs,$(libdir),libQtCLucene\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtclucene4 += $(DESCRIPTION), libQtCLucene.so.4
RUNTIME_DEP_PKGS_CSWlibqtclucene4 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibqtclucene4 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqtclucene4 += CSWlibqtcore4
# RUNTIME_DEP_PKGS_CSWlibqtclucene4 += CSWlibqtdbus4

PACKAGES += CSWlibqtdbus4
PKGFILES_CSWlibqtdbus4CSWlibqtdbus4-gxx += $(call baseisadirs,$(libdir),libQtDBus\.so\.4(\.\d+)*)
SPKG_D += $(DESCRIPTION), libQtDBus.so.4
RUNTIME_DEP_PKGS_CSWlibqtdbus4 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibqtdbus4 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqtdbus4 += CSWlibqtxml4
RUNTIME_DEP_PKGS_CSWlibqtdbus4 += CSWlibqtcore4

PACKAGES += CSWlibqtdeclarative4
PKGFILES_CSWlibqtdeclarative4 += $(call baseisadirs,$(libdir),libQtDeclarative\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtdeclarative4 += $(DESCRIPTION), libQtDeclarative.so.4
RUNTIME_DEP_PKGS_CSWlibqtdeclarative4 += CSWlibqtscript4
RUNTIME_DEP_PKGS_CSWlibqtdeclarative4 += CSWlibqtnetwork4
RUNTIME_DEP_PKGS_CSWlibqtdeclarative4 += CSWlibqtcore4
RUNTIME_DEP_PKGS_CSWlibqtdeclarative4 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqtdeclarative4 += CSWlibqtgui4
# RUNTIME_DEP_PKGS_CSWlibqtdeclarative4 += CSWlibqtsvg4
RUNTIME_DEP_PKGS_CSWlibqtdeclarative4 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibqtdeclarative4 += CSWlibqtsql4

PACKAGES += CSWlibqtdesigner4
PKGFILES_CSWlibqtdesigner4 += $(call baseisadirs,$(libdir),libQtDesigner\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtdesigner4 += $(DESCRIPTION), libQtDesigner.so.4
RUNTIME_DEP_PKGS_CSWlibqtdesigner4 += CSWlibqtscript4
RUNTIME_DEP_PKGS_CSWlibqtdesigner4 += CSWlibqtxml4
RUNTIME_DEP_PKGS_CSWlibqtdesigner4 += CSWlibqtcore4
RUNTIME_DEP_PKGS_CSWlibqtdesigner4 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqtdesigner4 += CSWlibqtgui4
RUNTIME_DEP_PKGS_CSWlibqtdesigner4 += CSWlibgcc-s1

PACKAGES += CSWlibqtdesignercomponents4
PKGFILES_CSWlibqtdesignercomponents4ercomponents4-gxx += $(call baseisadirs,$(libdir),libQtDesignerComponents\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtdeercomponents4-gxx += $(DESCRIPTION), libQtDesigne# rComponents.so.4
RUNTIME_DEP_PKGS_CSWlibqtde += CSWlibqtscript4
RUNTIME_DEP_PKGS_CSWlibqtdesignercomponents4 += CSWlibqtdesigner4
RUNTIME_DEP_PKGS_CSWlibqtdesignercomponents4 += CSWlibqtxml4
RUNTIME_DEP_PKGS_CSWlibqtdesignercomponents4 += CSWlibqtcore4
RUNTIME_DEP_PKGS_CSWlibqtdesignercomponents4 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqtdesignercomponents4 += CSWlibqtgui4
RUNTIME_DEP_PKGS_CSWlibqtdesignercomponents4 += CSWlibgcc-s1

PACKAGES += CSWlibqtxml4
PKGFILES_CSWlibqtxml4_CSWlibqtxml4-gxx += $(call baseisadirs,$(libdir),libQtXml\.so\.4(\.\d+)*)
SPKG_ += $(DESCRIPTION), libQtXml.so.4
RUNTIME_DEP_PKGS_CSWlibqtxml4 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibqtxml4 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqtxml4 += CSWlibqtcore4

PACKAGES += CSWqt4-doc
SPKG_DESC_CSWqt4G_DESC_CSWqt4-gxx-doc += $(DESCRIPTION), documentation
# Catch-aldoc = 1
CHECKPKG_OVERRIDES_CSWqt4RRIDES_CSWqt4-gxx-doc += file-with-bad-content

include gar/category.mk

# pre-reconfigure-modulated:
# 	cd $(WORKSRC) && gmake confclean
# 	@$(MAKECOOKIE)

PATH:=$(PATH):/