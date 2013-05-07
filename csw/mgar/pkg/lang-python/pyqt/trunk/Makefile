# $Id$

NAME		=	pyqt
VERSION		=	4.10.1
CATEGORIES	=	python
GARTYPE		=	v2

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

BUILD_DEPS_PKG	+=	CSWqt4-dev
BUILD_DEPS_PKG	+=	CSWpy-sip

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

PACKAGES				+=	CSWpy-pyqt
CATALOGNAME_CSWpy-pyqt	=	py_pyqt
SPKG_DESC_CSWpy-pyqt	=	$(DESCRIPTION)
PKGFILES_CSWpy-pyqt		+=	/opt/csw/bin/pylupdate4
PKGFILES_CSWpy-pyqt		+=	/opt/csw/bin/pyrcc4
PKGFILES_CSWpy-pyqt		+=	/opt/csw/lib/python/site-packages/PyQt4/.*[.]so
PKGFILES_CSWpy-pyqt		+=	/opt/csw/plugins/designer/libpythonplugin.so

include gar/category.mk

PATH := /opt/csw/gnu:/opt/csw/libexec/flex-2.5.35/bin:$(PATH)

# assume share because QT_SHARED doesn't get defined in the
# configuration environment (TODO: explore issue in depth)
configure-custom:
	cd $(WORKSRC) && \
	 	/usr/bin/env -i \
		  $(CONFIGURE_ENV) \
			python configure-ng.py \
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
	@$(MAKECOOKIE)
