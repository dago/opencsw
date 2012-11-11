# : Makefile 9089 2010-03-11 08:34:46Z wahwah $
NAME = xfig
VERSION = 3.2.5b
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = An interactive drawing tool
define BLURB
  The purpose of this site is to provide a central Xfig repository for the
  diverse documentation and programs available on the web. All the components
  and libraries will be available at this site, in addition to Xfig drawiECTngs.
endef

SF_PROJ = mcj
MASTER_SITES = $(SF_MIRROR)
DISTNAME = $(NAME).$(VERSION)
DISTFILES  = $(DISTNAME).full.tar.gz

PATCHFILES = 0001-Add-missing-define-for-REG_NOERROR.patch

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).full.tar.gz

VENOR_URL = http://www.xfig.org/

LICENSE = Libraries/GUI/LICENSE

DEP_PKGS = CSWxpm CSWzlib CSWjpeg CSWpng CSWxaw3d

CONFIGURE_SCRIPTS = $(WORKSRC)/Imakefile

BUILD_OVERRIDE_VARS  = PNGLIBDIR PNGINC ZLIBDIR
BUILD_OVERRIDE_VARS += JPEGLIBDIR JPEGINC
BUILD_OVERRIDE_VARS += XPMLIBDIR XPMINC
BUILD_OVERRIDE_VARS += XFIGLIBDIR XFIGDOCDIR XAPPLOADDIR

BUILD_OVERRIDE_VAR_PNGLIBDIR = $(libdir)
BUILD_OVERRIDE_VAR_PNGINC = -I$(includedir)
BUILD_OVERRIDE_VAR_ZLIBDIR = $(libdir)
BUILD_OVERRIDE_VAR_JPEGLIBDIR = $(libdir)
BUILD_OVERRIDE_VAR_JPEGINC = -I$(includedir)
BUILD_OVERRIDE_VAR_XPMLIBDIR = /usr/openwin/lib
BUILD_OVERRIDE_VAR_XPMINC = -I/usr/openwin/include/X11

BUILD_OVERRIDE_VAR_XFIGLIBDIR = $(libdir)/X11/xfig
BUILD_OVERRIDE_VAR_XFIGDOCDIR = $(docdir)/xfig
BUILD_OVERRIDE_VAR_XAPPLOADDIR = $(libdir)/X11/app-defaults

# -DXFIGLIBDIR=\"/usr/openwin/lib/X11/xfig\" -DXFIGDOCDIR=\"/usr/local/xfig/doc\" -DPRINTCAP=\"/etc/printcap\"

TEST_SCRIPTS =

INSTALL_ARGS = install.man install.html install.libs

INSTALL_OVERRIDE_VARS = BINDIR MANPATH LIBDIR XFIGLIBDIR XFIGDOCDIR XAPPLOADDIR
INSTALL_OVERRIDE_VAR_BINDIR = $(bindir)
INSTALL_OVERRIDE_VAR_MANPATH = $(mandir)
INSTALL_OVERRIDE_VAR_LIBDIR = $(libdir)
INSTALL_OVERRIDE_VAR_XFIGLIBDIR = $(libdir)/X11/xfig
INSTALL_OVERRIDE_VAR_XFIGDOCDIR = $(docdir)/xfig
INSTALL_OVERRIDE_VAR_XAPPLOADDIR = $(libdir)/X11/app-defaults

include gar/category.mk

post-extract-modulated:
	-find $(WORKSRC) -type d -exec chmod 755 \{\} \;
	-find $(WORKSRC) -type f -exec chmod ugo+r \{\} 