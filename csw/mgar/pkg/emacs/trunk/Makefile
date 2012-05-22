# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME		=	emacs
VERSION		=	23.4
GARTYPE		=	v2
CATEGORIES	=	apps

DESCRIPTION = The GNU Emacs editor
define BLURB
  Emacs is the extensible, customizable, self-documenting real-time
  display editor.
endef

DISTFILES		=	$(DISTNAME).tar.bz2
MASTER_SITES	=	$(GNU_MIRROR)

CONFIGURE_ARGS	= $(DIRPATHS)

# this is necessary because GNU id options dialect is is used; BTW, I
# think that adding this systematically at the beginning of the PATH
# helps in packaging projects issued from the Linux steam.
INSTALL_ARGS		+=	\
						PATH="/opt/csw/gnu:$$PATH"

GARCOMPILER			=	GNU

BUILD_DEP_PKGS		=	\
						CSWcoreutils \
						CSWglib2devel \
						CSWlibatk-dev \
						CSWlibbz2-dev \
						CSWlibcairo-dev \
						CSWlibdatrie-dev \
						CSWlibdbus-dev \
						CSWlibdbus-glib-dev \
						CSWlibexpat-dev \
						CSWlibfreetype-dev \
						CSWlibgconf-dev \
						CSWlibgdk-pixbuf-dev \
						CSWlibgif-dev \
						CSWlibglib2-dev \
						CSWlibgtk2-dev \
						CSWlibiconv-dev \
						CSWlibjbig-dev \
						CSWlibjpeg-dev \
						CSWlibm17n-dev \
						CSWlibotf-dev \
						CSWlibpixman-dev \
						CSWlibpng-dev \
						CSWlibpthreadstubs \
						CSWlibrsvg-dev \
						CSWlibthai-dev \
						CSWlibtiff-dev \
						CSWlibx11devel \
						CSWlibxaudevel \
						CSWlibxcbdevel \
						CSWlibxdmcpdevel \
						CSWlibxft2devel \
						CSWlibxml2-dev \
						CSWlibxpmdevel \
						CSWlibz-dev \
						CSWpangodevel \
						CSWpkgconfig \
						CSWsunx11devel

PACKAGING_PLATFORMS	=	\
						solaris10-sparc \
						solaris10-i386

PATCHFILES			+=	0001-activate-Xft-for-configure.patch

include gar/category.mk

# this is private and not available publicly
mydependencies:
	$(HOME)/bin/ocswdeplist --package $(NAME)
