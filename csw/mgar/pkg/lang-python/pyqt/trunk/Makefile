# $Id$

NAME			=	pyqt
VERSION			=	4.10.2
CATEGORIES		=	python
PYTHON_VERSION	=	2_7
GARTYPE			=	v2

DESCRIPTION	=	Python bindings for Qt
define BLURB
  PyQt is the Python bindings for Qt cross-platform application development
  framework.
endef

MASTER_SITES	=	$(SF_MIRRORS)
SF_PROJECT		=	pyqt
SPKG_SOURCEURL	=	$(MASTER_SITES)
DISTNAME		=	PyQt-x11-gpl-$(VERSION)
DISTFILES 		=	$(DISTNAME).tar.gz
LICENSE			=	LICENSE.GPL3
PATCHFILES		+=	0001-disable-ocsw-unsupported-modules.patch
PATCHFILES		+=	0002-force-xpg6-where-not-set-by-configure.patch

BUILD_DEP_PKGS	+=	CSWqt4-dev
BUILD_DEP_PKGS	+=	CSWpy-sip

GARCOMPILER		=	GNU
EXTRA_CFLAGS	+=	-std=gnu99 -D_XPG6
EXTRA_CXXFLAGS	+=	-D_XPG6
CONFIGURE_ARGS	=	$(DIRPATHS)
CONFIGURE_SCRIPTS	=	custom

BUILD_SCRIPTS	=	custom

TEST_SCRIPTS	=

INSTALL_SCRIPTS	=	custom

PACKAGES						+=	CSWpy-pyqt-common
CATALOGNAME_CSWpy-pyqt-common	=	py_pyqt_common
SPKG_DESC_CSWpy-pyqt-common		=	$(DESCRIPTION), common files
ARCHALL_CSWpy-pyqt-common		=	1

PACKAGES						+=	CSWpy-pyqt
CATALOGNAME_CSWpy-pyqt			=	py_pyqt
SPKG_DESC_CSWpy-pyqt			=	$(DESCRIPTION)
PKGFILES_CSWpy-pyqt				+=	/opt/csw/bin/pylupdate4
PKGFILES_CSWpy-pyqt				+=	/opt/csw/bin/pyrcc4
PKGFILES_CSWpy-pyqt				+=	/opt/csw/lib/python/site-packages/PyQt4/.*[.]so
PKGFILES_CSWpy-pyqt				+=	/opt/csw/plugins/designer/libpythonplugin.so
PKGFILES_CSWpy-pyqt				+=	/opt/csw/lib/python/site-packages/dbus/mainloop/qt.so
RUNTIME_DEP_PKGS_CSWpy-pyqt		+=	CSWlibdbus1-3
RUNTIME_DEP_PKGS_CSWpy-pyqt		+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWpy-pyqt		+=	CSWlibphonon4
RUNTIME_DEP_PKGS_CSWpy-pyqt		+=	CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-pyqt		+=	CSWlibqtcore4
RUNTIME_DEP_PKGS_CSWpy-pyqt		+=	CSWlibqtdbus4
RUNTIME_DEP_PKGS_CSWpy-pyqt		+=	CSWlibqtdeclarative4
RUNTIME_DEP_PKGS_CSWpy-pyqt		+=	CSWlibqtdesigner4
RUNTIME_DEP_PKGS_CSWpy-pyqt		+=	CSWlibqtgui4
RUNTIME_DEP_PKGS_CSWpy-pyqt		+=	CSWlibqthelp4
RUNTIME_DEP_PKGS_CSWpy-pyqt		+=	CSWlibqtmultimedia4
RUNTIME_DEP_PKGS_CSWpy-pyqt		+=	CSWlibqtnetwork4
RUNTIME_DEP_PKGS_CSWpy-pyqt		+=	CSWlibqtopengl4
RUNTIME_DEP_PKGS_CSWpy-pyqt		+=	CSWlibqtscript4
RUNTIME_DEP_PKGS_CSWpy-pyqt		+=	CSWlibqtscripttools4
RUNTIME_DEP_PKGS_CSWpy-pyqt		+=	CSWlibqtsql4
RUNTIME_DEP_PKGS_CSWpy-pyqt		+=	CSWlibqtsvg4
RUNTIME_DEP_PKGS_CSWpy-pyqt		+=	CSWlibqttest4
RUNTIME_DEP_PKGS_CSWpy-pyqt		+=	CSWlibqtxml4
RUNTIME_DEP_PKGS_CSWpy-pyqt		+=	CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWpy-pyqt		+=	CSWpy-pyqt-common
CHECKPKG_OVERRIDES_CSWpy-pyqt	+=	surplus-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWpy-pyqt	+=	surplus-dependency|CSWpy-pyqt-common
CHECKPKG_OVERRIDES_CSWpy-pyqt	+=	binary-architecture-does-not-match-placement|file=opt/csw/plugins/designer/libpythonplugin.so|arch_id=18|arch_name=sparcv8+
CHECKPKG_OVERRIDES_CSWpy-pyqt	+=	binary-architecture-does-not-match-placement|file=opt/csw/plugins/designer/libpythonplugin.so|arch_id=3|arch_name=i386

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

# all this hoopla to obtain the file required by projects based on the
# old PyQt build system providing this script
$(WORKSRC)/pyqtconfig.py:
	cd $(WORKSRC) && \
		rm -f reference && \
		touch reference && \
	 	/usr/bin/env -i \
		  $(CONFIGURE_ENV) \
			$(PYTHON_EXECUTABLE) configure.py \
				--verbose \
				--confirm-license \
				--assume-shared \
				CFLAGS="${CFLAGS} ${CPPFLAGS}" \
				CXXFLAGS="${CXXFLAGS} ${CPPFLAGS}" \
				LFLAGS="${LDFLAGS}" \
			&& \
		gfind . -type f -newer reference | \
			ggrep -v '^[.]/pyqtconfig.py$$' | \
			xargs rm \
			&& \
		rmdir \
			./phonon \
			./Qt \
			./QtCore \
			./QtDBus \
			./QtDeclarative \
			./QtDesigner \
			./QtGui \
			./QtHelp \
			./QtMultimedia \
			./QtNetwork \
			./QtOpenGL \
			./QtScript \
			./QtScriptTools \
			./QtSql \
			./QtSvg \
			./QtTest \
			./QtXml \
			./sip/Qt \
			&& \
		rm reference

# assume share because QT_SHARED doesn't get defined in the
# configuration environment (TODO: explore issue in depth)
configure-custom: $(WORKSRC)/pyqtconfig.py
	cd $(WORKSRC) && \
	 	/usr/bin/env -i \
		  $(CONFIGURE_ENV) \
			$(PYTHON_EXECUTABLE) configure-ng.py \
				--verbose \
				--confirm-license \
				--assume-shared \
				CFLAGS="${CFLAGS} ${CPPFLAGS}" \
				CXXFLAGS="${CXXFLAGS} ${CPPFLAGS}" \
				LFLAGS="${LDFLAGS}" \
				QMAKE_CFLAGS+="${CFLAGS} ${CPPFLAGS}" \
				QMAKE_CXXFLAGS+="${CXXFLAGS} ${CPPFLAGS}" \
				QMAKE_LFLAGS+="${LDFLAGS}"
	@$(MAKECOOKIE)

build-custom:
	cd $(WORKSRC) && \
	 	/usr/bin/env -i \
		  $(BUILD_ENV) \
			$(MAKE)
	@$(MAKECOOKIE)

install-custom:
	cd $(WORKSRC) && \
	 	/usr/bin/env -i \
		  $(INSTALL_ENV) \
			$(MAKE) DESTDIR=$(DESTDIR) INSTALL_ROOT=$(DESTDIR) install
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/pyqtconfig.py $(DESTDIR)/$(PYTHON_SITE_PACKAGES)/PyQt4

	@$(MAKECOOKIE)
