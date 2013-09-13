# $Id$

NAME = qt
VERSION = 4.8.5
GARTYPE = v2
MAJOR = $(basename $(basename $(VERSION)))
CATEGORIES = lib

DESCRIPTION = TrollTech C++ application framework
define BLURB
  It contains a C++ class library as well as tools for cross-platform GUI
  development and internationaRCOMPILER = GNUhttp://download.qt-project.org/official_releases/qt/$(basename $(VERSION))/$(VERSION)kia.com/qt/source/
DISTNAME = qt-everywhere-opensource-src-$(VERSION)
DISTFILES = $(DISTNAME).tar.gz

L#NOGITPATCH = 1
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

GARCOMPILER = GNU
# GARFLAVOR = DBG

REINPLACE_USRLOCAL += src/gui/kernel/qguiplatformplugin.cpp 
REINPLACE_USRLOCAL += src/network/ssl/qsslsocket_openssl_symbols.cpp
REINPLACE_USRLOCAL += src/network/ssl/qsslsocket_openssl.cpp
# replace SSL cert location
REINPLACE_USRLOCAL += src/network/ssl/qsslsocket.cpp
REINPLACE_USRLOCAL += src/3rdparty/webkit/Source/WebCore/plugins/PluginDatabase.cpp

PATCHFILES += mkspec-csw.patch
# bug in 4.8.1, see: https//bugreports.qt-project.org/browse/QTBUG-25281
# PATCHFILES += 0001-shapeinput.patch
PATCHFILES += 0003-configure-must-use-bash.patch
PATCHFILES += 0004-webkit-port.patch
=BUILD_DEP_PKGS += CSWlibssl-dev
BUILD_DEP_PKGS += CSWunixodbc-dev
BUILD_DEP_PKGS += CSWpostgresql-dev
BUILD_DEP_PKGS += CSWfreetds-devsBUILD_DEP_PKGS += CSWmysql-devsBUILD_DEP_PKGS += CSWcups-dev
BUILD_DEP_PKGS += CSWgstplugins-dev
BUILD_DEP_PKGS += CSWgstreamer-dev
BUILD_DEP_PKGS += CSWlibiconv-dev
BUILD_DEP_PKGS += CSWlibglib2-dev
BUILD_DEP_PKGS += CSWlibxml2-devsl/qsslsocket.cpp

# http://wiki.opencsw.org/porting-faq#toc9
EXTRA_CFLAGS = -DSUN_OGL_NO_VERTEX_MACROS
EXTRA_CXXFLAGS = -DSUN_OGL_# override -O2 because of core dumps of designer, qmlplugindump and other in libQtDeclarative.so.4?
CXXFLAGS = -pipe $(ARCHFLAGS_$(GARCOMPILER)_$(ISA)) $(EXTRA_CXXFLAGS)

platform_arg = solaris-g++

CONFIGURE_ARGS_DBG += -debug
CONFIGURE_ARGS_OPT += -releaseGS += -opensource
COconfirm-licensRGS += -opensource
CONFIGURE_ARGS += -prefix $(prefix)
COdocdir $(sharedstatedir)/$(NAME)$(MAJOR)/doc
CONFIGURE_ARGS += -datadir $(sharedstatedir)/$(NAME)$(MAJOR -prefix $(prefix)
COplugindir $(libdir)/$(NAME)$(MAJOR)/plugins
CONFIGURE_ARGS += -importdir $(libdir)/$(NAME)$(MAJOR)/imports
CONFIGURE_ARGS += -translationdir $(sharedstatedir)/$(NAME)$(MAJOR)/translations
# CONFIGURE_ARGS += -sysconfdir $(syconfdir)/$(NAME)$(MAJOR -prefix $(prefix)
COsysconfdir /etc/xdg
CONFIGURE_ARGS += -demosdir $(libdir)/$(NAME)$(MAJOR)/demos
CONFIGURE_ARGS += -examplesdir $(libdir)/$(NAME)$(MAJOR)/examples
CONFIGURE_ARGS += -opensource
#debain args -- without windows only options, defaults, undocumented options
CONFIGURE_ARGS += -fast
CONFIGURE_ARGS += -plugin-sql-mysql
CONFIGURE_ARGS += -plugin-sql-odbc
CONFIGURE_ARGS += -plugin-sql-psql
CONFIGURE_ARGS += -plugin-sql-sqlite
CONFIGURE_ARGS += -plugin-sql-tds
CONFIGURE_ARGS += -system-sqlite
CONFIGURE_ARGS += -platform $(platform_arg)
CONFIGURE_ARGS += -system-zlib
CONFIGURE_ARGS += -system-libtiff
CONFIGURE_ARGS += -system-libpng
CONFIGURE_ARGS += -system-libjpeg
CONFIGURE_ARGS += -no-rpath
CONFIGURE_ARGS += -reduce-relocations
# CONFIGURE_ARGS += -no-separate-debug-info
CONFIGURE_ARGS += -verbose
CONFIGURE_ARGS += -lfontconfig
CONFIGURE_ARGS += -I$(includedir)/freetype2
#endof debian args-prefix $(prefix)
CONFIGURE_ARGS += -no-qt3support
COno-xshape+= -no-qt3support
COv 
CONFIGURE_ARGS += -shared
CONFIGURE_ARGS += -stl
CONFIGURE_ARGS += -largefile
CONFIGURE_ARGS += -sm 
CONFIGURE_ARGS += -qt-libjpeg
CONFIGURE_ARGS += -qt-libpng
CONFIGURE_ARGS += -qt-libmng
CONFIGURE_ARGS +=libpng -qt-CONFIGURE_ARGS += -xmlpatterns
CONFIGURE_ARGS += -webkit-# compile error: error: 'QGtkStyle' has not been declared ??? since 10.12.2012
CONFIGURE_ARGS += -no-gtkstyle-libmng -qt-zlib 
CON$(includedir)/glib-2.0
CONFIGURE_ARGS += -I$(libdir)/glib-2.0/include
CONFIGURE_ARGS += -I$(includedir)/gtk-2.0
CONFIGURE_ARGS += -I$(includedir)/gstreamer-0.10
CONFIGURE_ARGS += -I$(includedir)/libxml2
CONFIGURE_ARGS +=+= -I/usr/include -I/usr/X11/include 
CONFIGURE_ARGS += -I/usr/XGS += -no-xshape
CONFIGURE_ARGS_sparc += -big-endian 

# not build for Sparc because core dump in designer, qmlplugindump, ..
# not built for i386 because of cti_vm_throw referenced in JITStubs
CONFIGURE_ARGS += -no-javascript-jit
CONFIGURE_ARGS_sparc += -no-script

# CONFIGURE_ARGS_i386 += -little-endian -host-big-endian
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GARCH))
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GARFLAVORGUREINSTALL_ROOT = $(DESTDIR)
EXTRA_INSTALL_EXPORTS = INSTALL_ROOT

# skip this if you are not connected to as X Windows server
TEST_SCRIPTS		=	customS = INSTALL_ROOT


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
RUNTIME_DEP_PKGS_CSWlibqtgui4 += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWlibqtgui4 += CSWlibfreetype6
CHECKPKG_OVERRIDES_CSWlibqtgui4 += file-with-bad-content|/usr/share|root/opt/csw/lib/libQtGui.so.$(VERSION)

PACKAGES						+=	CSWqt4-private-dev
CATALOGNAME_CSWqt4-private-dev	=	qt4_private_dev
SPKG_DESC_CSWqt4-private-dev	=	$(DESCRIPTION), private development files
PKGFILES_CSWqt4-private-dev		+=	$(includedir)/QtCore/private/.*
PKGFILES_CSWqt4-private-dev		+=	$(includedir)/QtDeclarative/private/.*
PKGFILES_CSWqt4-private-dev		+=	$(includedir)/QtGui/private/.*
PKGFILES_CSWqt4-private-dev		+=	$(includedir)/QtScript/private/.*
PKGFILES_CSWqt4-private-dev		+=	$(includedir)/src/.*
ARCHALL_CSWqt4-private-dev		=	1
RUNTIME_DEP_PKGS_CSWqt4-private-dev += CSWqt4-dev
CHECKPKG_OVERRIDES_CSWqt4-private-dev += surplus-dependency|CSWqt4-dev
CHECKPKG_OVERRIDES_CSWqt4-private-dev += archall-devel-package

PACKAGES += CSWqt4-dev
SPKG_DESC_CSWqt4-dev += $(DESCRIPTION), development files
PKGFILES_CSWqt4-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWqt4-dev += $(call baseisadirs,$(bindir),.*)
PKGFILES_CSWqt4-dev += $(libdir)/libQt.*\.prl
PKGFILES_CSWqt4-dev += $(libdir)/$(NAME)$(MAJOR)/examples/.*
PKGFILES_CSWqt4-dev += $(libdir)/$(NAME)$(MAJOR)/plugins/.*
PKGFILES_CSWqt4-dev += $(libdir)/$(NAME)$(MAJOR)/demos/.*
PKGFILES_CSWqt4-dev += $(libdir)/$(NAME)$(MAJOR)/imports/.*
PKGFILES_CSWqt4-dev += $(sharedstatedir)/$(NAME)$(MAJOR)/mkspecs/.*
EXTRA_PKGFILES_EXCLUDED_CSWqt4-dev += $(PKGFILES_CSWqt4-private-dev)
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
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibqtgui4
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibqtopengl4
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibqtmultimedia4
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibqtxmlpatterns4
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibqtwebkit4
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibqtsvg4
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibphonon4
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibqtsql4
# RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibgthread2-0-0
# RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibgmodule2-0-0
# RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibintl8
# RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibxrender
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWmesa
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibglib2-0-0
# RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWsqlite
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibtiff5
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibicui18n50
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibodbc2
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibpq5
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibsybdb5
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibmysqlclient18
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibgstbase0-10-0
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibgstinterfaces0-10-0
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibgstreamer0-10-0
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibgstvideo0-10-0
RUNTIME_DEP_PKGS_CSWqt4-dev += CSWlibgstaudio0-10-0

CHECKPKG_OVERRIDES_CSWqt4-dev += surplus-dependency|CSWlibicui18n50
CHECKPKG_OVERRIDES_CSWqt4-dev_i386 += file-with-bad-content|/usr/share|root/opt/csw/lib/qt4/demos/declarative/twitter/twitter_harmattan.desktop
CHECKPKG_OVERRIDES_CSWqt4-dev_i386 += file-with-bad-content|/usr/share|root/opt/csw/lib/qt4/demos/declarative/flickr/flickr_harmattan.desktop
CHECKPKG_OVERRIDES_CSWqt4-dev_i386 += file-with-bad-content|/usr/share|root/opt/csw/lib/qt4/demos/declarative/samegame/samegame_harmattan.desktop
CHECKPKG_OVERRIDES_CSWqt4-dev_i386 += file-with-bad-content|/usr/share|root/opt/csw/lib/qt4/demos/declarative/rssnews/rssnews_harmattan.desktop
CHECKPKG_OVERRIDES_CSWqt4-dev_i386 += file-with-bad-content|/usr/share|root/opt/csw/lib/qt4/demos/declarative/photoviewer/photoviewer_harmattan.desktop
CHECKPKG_OVERRIDES_CSWqt4-dev_i386 += file-with-bad-content|/usr/share|root/opt/csw/lib/qt4/demos/declarative/calculator/calculator_harmattan.desktop
CHECKPKG_OVERRIDES_CSWqt4-dev_i386 += file-with-bad-content|/usr/share|root/opt/csw/lib/qt4/demos/declarative/snake/snake_harmattan.desktop
CHECKPKG_OVERRIDES_CSWqt4-dev_i386 += file-with-bad-content|/usr/share|root/opt/csw/lib/qt4/demos/helper/qmlapplicationviewer/qmlapplicationviewer.pri
CHECKPKG_OVERRIDES_CSWqt4-dev_i386 += file-with-bad-content|/usr/share|root/opt/csw/lib/qt4/examples/helper/qmlapplicationviewer/qmlapplicationviewer.pri
d-path-in-pkgmap
# because libdbus needs /etc/machine-id which can generated with a tool of CSWdbus
CHECKPKG_dev += surplus-dependency|CSWdbus
CHECKPKG_OVERRIDES_CSWqt4-dev += $(CHECKPKG_OVERRIDES_CSWqt4-dev_$(GARCH))

#
# temporary special packaging for Sprac build without script
#
RUNTIME_DEP_PKGS_CSWqt4-dev_i386 += CSWlibqtscript4
RUNTIME_DEP_PKGS_CSWqt4-dev_i386 += CSWlibqtscripttools4
RUNTIME_DEP_PKGS_CSWqt4-dev_i386 += CSWlibqtdeclarative4
RUNTIME_DEP_PKGS_CSWqt4-dev += $(RUNTIME_DEP_PKGS_CSWqt4-dev_$(GARCH))

PACKAGES += CSWlibqtscript4
PKGFILES_CSWlibqtscript4 += $(call baseisadirs,$(libdir),libQtScript\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtscript4 += $(DESCRIPTION), libQtScript.so.4
RUNTIME_DEP_PKGS_CSWlibqtscript4_i386 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibqtscript4_i386 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqtscript4_i386 += CSWlibqtcore4
RUNTIME_DEP_PKGS_CSWlibqtscript4 += $(RUNTIME_DEP_PKGS_CSWlibqtscript4_$(GARCH))

PACKAGES += CSWlibqtscripttools4
PKGFILES_CSWlibqtscripttools4 += $(call baseisadirs,$(libdir),libQtScriptTools\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtscripttools4 += $(DESCRIPTION), libQtScriptTools.so.4
RUNTIME_DEP_PKGS_CSWlibqtscripttools4_i386 += CSWlibqtscript4
RUNTIME_DEP_PKGS_CSWlibqtscripttools4_i386 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibqtscripttools4_i386 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqtscripttools4_i386 += CSWlibqtgui4
RUNTIME_DEP_PKGS_CSWlibqtscripttools4_i386 += CSWlibqtcore4
RUNTIME_DEP_PKGS_CSWlibqtscripttools4 += $(RUNTIME_DEP_PKGS_CSWlibqtscripttools4_$(GARCH))

PACKAGES += CSWlibqtdeclarative4
PKGFILES_CSWlibqtdeclarative4 += $(call baseisadirs,$(libdir),libQtDeclarative\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtdeclarative4 += $(DESCRIPTION), libQtDeclarative.so.4
RUNTIME_DEP_PKGS_CSWlibqtdeclarative4_i386 += CSWlibqtscript4
RUNTIME_DEP_PKGS_CSWlibqtdeclarative4_i386 += CSWlibqtnetwork4
RUNTIME_DEP_PKGS_CSWlibqtdeclarative4_i386 += CSWlibqtcore4
RUNTIME_DEP_PKGS_CSWlibqtdeclarative4_i386 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqtdeclarative4_i386 += CSWlibqtgui4
# RUNTIME_DEP_PKGS_CSWlibqtdeclarative4 += CSWlibqtsvg4
RUNTIME_DEP_PKGS_CSWlibqtdeclarative4_i386 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibqtdeclarative4_i386 += CSWlibqtsql4
RUNTIME_DEP_PKGS_CSWlibqtdeclarative4 += $(RUNTIME_DEP_PKGS_CSWlibqtdeclarative4_$(GARCH))
#
# end temporay packaging
#

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
CHECKPKG_OVERRIDES_CSWlibqtnetwork4libqtnetwork4-gxx += file-with-bad-content|/usr/shroot/opt/csw/gxx/lib$(VERSION)
tNetwork.so.4.8.1

PACKAGES +
PKGFILES_CSWlibqtopengl4Wlibqtopengl4-gxx += $(call baseisadirs,$(libdir),libQtOpenGL\.so\.4(\.\d+)*)
SPKG_DES += $(DESCRIPTION), libQtOpenGL.so.4
RUNTIME_DEP_PKGS_CSWlibqtopengl4 += CSWlibxrender
RUNTIME_DEP_PKGS_CSWlibqtopengl4 += CSWlibqtcore4
RUNTIME_DEP_PKGS_CSWlibqtopengl4 += CSWmesa
RUNTIME_DEP_PKGS_CSWlibqtopengl4 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqtopengl4 += CSWlibqtgui4
RUNTIME_DEP_PKGS_CSWlibqtopengl4 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibqtopengl4 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibqtopengl4 += $(RUNTIME_DEP_PKGS_CSWlibqtopengl4_$(GARCH))

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

PACKAGES += CSWlibqtdesigner4
PKGFILES_CSWlibqtdesigner4 += $(call baseisadirs,$(libdir),libQtDesigner\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtdesigner4 += $(DESCRIPTION), libQtDesigner.so.4
RUNTIME_DEP_PKGS_CSWlibqtdesigner4_i386 += CSWlibqtscript4
RUNTIME_DEP_PKGS_CSWlibqtdesigner4 += CSWlibqtxml4
RUNTIME_DEP_PKGS_CSWlibqtdesigner4 += CSWlibqtcore4
RUNTIME_DEP_PKGS_CSWlibqtdesigner4 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqtdesigner4 += CSWlibqtgui4
RUNTIME_DEP_PKGS_CSWlibqtdesigner4 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibqtdesigner4 += $(RUNTIME_DEP_PKGS_CSWlibqtdesigner4_$(GARCH))

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

PACKAGES += CSWlibqtwebkit4
CATALOGNAME_CSWlibqtwebkit4 = libqtwebkit4
PKGFILES_CSWlibqtwebkit4 += $(call baseisadirs,$(libdir),libQtWebKit\.so\.4\.9\.4)
PKGFILES_CSWlibqtwebkit4 += $(call baseisadirs,$(libdir),libQtWebKit\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtwebkit4 += $(DESCRIPTION), libQtWebKit.so.4
RUNTIME_DEP_PKGS_CSWlibqtwebkit4 += CSWlibqtcore4
RUNTIME_DEP_PKGS_CSWlibqtwebkit4 += CSWlibxrender
RUNTIME_DEP_PKGS_CSWlibqtwebkit4 += CSWlibqtnetwork4
RUNTIME_DEP_PKGS_CSWlibqtwebkit4 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqtwebkit4 += CSWlibqtgui4
RUNTIME_DEP_PKGS_CSWlibqtwebkit4 += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWlibqtwebkit4 += CSWlibgcc-s1

PACKAGES += CSWlibqtxmlpatterns4
CATALOGNAME_CSWlibqtxmlpatterns4 = libqtxmlpatterns4
PKGFILES_CSWlibqtxmlpatterns4 += $(call baseisadirs,$(libdir),libQtXmlPatterns\.so\.4\.8\.5)
PKGFILES_CSWlibqtxmlpatterns4 += $(call baseisadirs,$(libdir),libQtXmlPatterns\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibqtxmlpatterns4 += $(DESCRIPTION), libQtXmlPatterns.so.4
RUNTIME_DEP_PKGS_CSWlibqtxmlpatterns4 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibqtxmlpatterns4 += CSWlibqtcore4
RUNTIME_DEP_PKGS_CSWlibqtxmlpatterns4 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqtxmlpatterns4 += CSWlibqtnetwork4

PACKAGES += CSWqt4-doc
SPKG_DESC_CSWqt4G_DESC_CSWqt4-gxx-doc += $(DESCRIPTION), documentation
# Catch-aldoc = 1
CHECKPKG_OVERRIDES_CSWqt4RRIDES_CSWqt4-gxx-doc += file-winclude gar/category.mk

PATH:=:/opt/csw/gnu:$(PATH)e libraries4test=$(shell pwd)/$(WORKSRC)/lib
test-custom:
	cd $(WORKSRC) && /usr/bin/env -i $(BUILD_ENV) LD_LIBRARY_PATH=$(libraries4test) && $(MAKE) -i -k -C $(OBJDIR) TESTRUNNER='LD_LIBRARY_PATH=$(libraries4test)' check
	$(MAKECOOKIE)e gar/category.mk

# pre-reconfigure-modulated:
# 	cd $(WORKSRC) && gmake confclean
# 
# Ship private headers - ugly hack to build Qt Creator QML Designer;
# adapted from Debian rules
# and
# prune tests from the destination directory (we don't want them in
# our packages isn't it?)
post-install:
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)$(includedir)/QtCore
	gtar --directory=$(WORKSRC)/include/QtCore --create --file=- private | gtar --directory=$(DESTDIR)$(includedir)/QtCore --extract --file=-
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)$(includedir)/QtDeclarative
	gtar --directory=$(WORKSRC)/include/QtDeclarative --create --file=- private | gtar --directory=$(DESTDIR)$(includedir)/QtDeclarative --extract --file=-
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)$(includedir)/QtGui
	gtar --directory=$(WORKSRC)/include/QtGui --create --file=- private | gtar --directory=$(DESTDIR)$(includedir)/QtGui --extract --file=-
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)$(includedir)/QtScript
	gtar --directory=$(WORKSRC)/include/QtScript --create --file=- private | gtar --directory=$(DESTDIR)$(includedir)/QtScript --extract --file=-
	cd $(WORKSRC) && gtar --create --file=- src/corelib/*/*_p.h src/declarative/*/*_p.h src/gui/*/*_p.h src/script/*/*_p.h | gtar --directory=$(DESTDIR)$(includedir) --extract --file=-
	rm -rf $(DESTDIR)/$(prefix)/tests
	$(MAKECOOKIE)
