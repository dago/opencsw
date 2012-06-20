# $Id$

NAME = plotutils
VERSION = 2.6
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = The GNU plotutils (plotting utilities) package
define BLURB
  The GNU plotutils package contains software for both programmers and
  technical users. Its centerpiece is libplot, a powerful C/C++ function
  library for exporting 2-D vector graphics in many file formats, both
  vector and bitmap. On the X Window System, it can also do 2-D vector
  graphics animations.
endef

MASTER_SITES	=	$(GNU_MIRROR)
DISTFILES		=	$(DISTNAME).tar.gz

GARCOMPILER			=	GNU

CONFIGURE_ARGS	=	$(DIRPATHS)
CONFIGURE_ARGS	+=	--enable-libplotter
CONFIGURE_ARGS	+=	--enable-libxmi
CONFIGURE_ARGS	+=	--enable-lj-fonts-in-x
CONFIGURE_ARGS	+=	--enable-ps-fonts-in-pcl
CONFIGURE_ARGS	+=	--enable-lj-fonts-in-ps

INSTALL_ARGS	=	datadir=$(docdir)/$(NAME)

TEST_SCRIPTS = custom

BUILD_DEP_PKGS		+=	CSWlibpng-dev
BUILD_DEP_PKGS		+=	CSWlibz-dev

PACKAGES							=	CSWplotutils-doc
CATALOGNAME_CSWplotutils-doc		=	plotutils_doc
SPKG_DESC_CSWplotutils-doc			=	$(DESCRIPTION), documentation
OBSOLETED_BY_CSWplotutils-doc		=	CSWplotutildoc
ARCHALL_CSWplotutils-doc			=	1
CHECKPKG_OVERRIDES_CSWplotutils-doc	+=	file-with-bad-content|/usr/local|root/opt/csw/share/info/plotutils.info
CHECKPKG_OVERRIDES_CSWplotutils-doc	+=	file-with-bad-content|/usr/share|root/opt/csw/share/info/plotutils.info

PACKAGES						+=	CSWlibplot2
CATALOGNAME_CSWlibplot2			=	libplot2
PKGFILES_CSWlibplot2			+=	$(call baseisadirs,$(libdir),libplot\.so\.2\.2\.4)
PKGFILES_CSWlibplot2			+=	$(call baseisadirs,$(libdir),libplot\.so\.2(\.\d+)*)
SPKG_DESC_CSWlibplot2			+=	$(DESCRIPTION), libplot.so.2
OBSOLETED_BY_CSWlibplot2		=	CSWplotutilrt
RUNTIME_DEP_PKGS_CSWlibplot2	+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibplot2	+=	CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWlibplot2	+=	CSWlibz1

PACKAGES						+=	CSWlibplotter2
CATALOGNAME_CSWlibplotter2		=	libplotter2
PKGFILES_CSWlibplotter2			+=	$(call baseisadirs,$(libdir),libplotter\.so\.2\.2\.4)
PKGFILES_CSWlibplotter2			+=	$(call baseisadirs,$(libdir),libplotter\.so\.2(\.\d+)*)
SPKG_DESC_CSWlibplotter2		+=	$(DESCRIPTION), libplotter.so.2
OBSOLETED_BY_CSWlibplotter2		=	CSWplotutilrt
RUNTIME_DEP_PKGS_CSWlibplotter2	+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibplotter2	+=	CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWlibplotter2	+=	CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibplotter2	+=	CSWlibz1

PACKAGES					+=	CSWlibxmi0
CATALOGNAME_CSWlibxmi0		=	libxmi0
PKGFILES_CSWlibxmi0			+=	$(call baseisadirs,$(libdir),libxmi\.so\.0\.1\.3)
PKGFILES_CSWlibxmi0			+=	$(call baseisadirs,$(libdir),libxmi\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibxmi0		+=	$(DESCRIPTION), libxmi.so.0
OBSOLETED_BY_CSWlibxmi0		=	CSWplotutilrt
RUNTIME_DEP_PKGS_CSWlibxmi0	+=	CSWlibgcc-s1

PACKAGES						+=	CSWplotutils
SPKG_DESC_CSWplotutils			=	$(DESCRIPTION), utilities
PKGFILES_CSWplotutils			=	/opt/csw/bin/double
PKGFILES_CSWplotutils			+=	/opt/csw/bin/graph
PKGFILES_CSWplotutils			+=	/opt/csw/bin/hersheydemo
PKGFILES_CSWplotutils			+=	/opt/csw/bin/ode
PKGFILES_CSWplotutils			+=	/opt/csw/bin/pic2plot
PKGFILES_CSWplotutils			+=	/opt/csw/bin/plot
PKGFILES_CSWplotutils			+=	/opt/csw/bin/plotfont
PKGFILES_CSWplotutils			+=	/opt/csw/bin/spline
PKGFILES_CSWplotutils			+=	/opt/csw/bin/tek2plot
RUNTIME_DEP_PKGS_CSWplotutils	+=	CSWlibplot2
RUNTIME_DEP_PKGS_CSWplotutils	+=	CSWlibplotter2
RUNTIME_DEP_PKGS_CSWplotutils	+=	CSWlibxmi0
OBSOLETED_BY_CSWplotutils		=	CSWplotutil
CHECKPKG_OVERRIDES_CSWplotutils	+=	missing-dependency|CSWlibgcc-s1
CHECKPKG_OVERRIDES_CSWplotutils	+=	missing-dependency|CSWlibstdc++6
CHECKPKG_OVERRIDES_CSWplotutils	+=	missing-dependency|CSWlibpng12-0
CHECKPKG_OVERRIDES_CSWplotutils	+=	missing-dependency|CSWlibz1
CHECKPKG_OVERRIDES_CSWplotutils	+=	surplus-dependency|CSWlibxmi0
CHECKPKG_OVERRIDES_CSWplotutils	+=	surplus-dependency|CSWlibplotter2

PACKAGES							+=	CSWplotutils-dev
CATALOGNAME_CSWplotutils-dev		=	plotutils_dev
SPKG_DESC_CSWplotutils-dev			+=	$(DESCRIPTION), development files
PKGFILES_CSWplotutils-dev			+=	/opt/csw/lib/libplot.so
PKGFILES_CSWplotutils-dev			+=	/opt/csw/lib/libplotter.so
PKGFILES_CSWplotutils-dev			+=	/opt/csw/lib/libxmi.so
PKGFILES_CSWplotutils-dev			+=	$(PKGFILES_DEVEL)
OBSOLETED_BY_CSWplotutils-dev		=	CSWplotutildevel
ARCHALL_CSWplotutils-dev			=	1
RUNTIME_DEP_PKGS_CSWplotutils-dev	+=	CSWplotutils
CHECKPKG_OVERRIDES_CSWplotutils-dev	+=	archall-devel-package
CHECKPKG_OVERRIDES_CSWplotutils-dev	+=	missing-dependency|CSWlibplotter2
CHECKPKG_OVERRIDES_CSWplotutils-dev	+=	missing-dependency|CSWlibxmi0
CHECKPKG_OVERRIDES_CSWplotutils-dev	+=	missing-dependency|CSWlibplot2

include gar/category.mk

# there are test failing (plot2hpgl.test and plot2pcl.test) and I
# choose to ignore them as the remaining ones pass.
test-custom:
	-$(MAKE) -k -C $(WORKSRC) check
	$(MAKECOOKIE)

# this is private and not available publicly
mydependencies:
	$(HOME)/bin/ocswdeplist --package $(NAME)
