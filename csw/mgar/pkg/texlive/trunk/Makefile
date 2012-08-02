# $Id$

NAME		=	texlive
YEAR		=	2012
VERSION		=	$(YEAR)0701
GARTYPE		=	v2
CATEGORIES	=	apps

DESCRIPTION = TeX Live
define BLURB
  TeX Live is an easy way to get up and running with the TeX document
  production system. It provides a comprehensive TeX system with binaries
  for most flavors of Unix, including GNU/Linux, and also Windows. It includes
  all the major TeX-related programs, macro packages, and fonts that are free
  software, including support for many languages around the world. 
endef

VENDOR_URL		=	http://www.tug.org/texlive/
MASTER_SITES	=	ftp://tug.org/texlive/historic/$(YEAR)/
DISTNAMEPREFIX	=	$(NAME)-$(VERSION)
DISTNAME		=	$(DISTNAMEPREFIX)-source
DISTFILES		=	$(DISTNAME).tar.xz
DISTFILES		+=	$(DISTNAMEPREFIX)-extra.tar.xz
NOEXTRACT		+=	$(DISTNAMEPREFIX)-extra.tar.xz
DISTFILES		+=	$(DISTNAMEPREFIX)-texmf.tar.xz
NOEXTRACT		+=	$(DISTNAMEPREFIX)-texmf.tar.xz

BUILD_DEP_PKGS	+=	CSWpoppler-dev
BUILD_DEP_PKGS	+=	CSWpoppler-dev
BUILD_DEP_PKGS	+=	CSWclisp

EXTRA_CFLAGS	+=	-std=gnu99 -D_XPG6
EXTRA_CXXFLAGS	+=	-D_XPG6

GARCOMPILER		=	GNU

# must be a absolute path name if we don't want to have the object
# directory created relatively in the working source
OBJDIR			=	$(abspath $(WORKDIR)/objdir)

CONFIGURE_ARGS	=	$(DIRPATHS)
CONFIGURE_ARGS	+=	--disable-debug
CONFIGURE_ARGS	+=	--disable-devnag
CONFIGURE_ARGS	+=	--disable-libtool-hack
CONFIGURE_ARGS	+=	--disable-missing
CONFIGURE_ARGS	+=	--disable-multiplatform
CONFIGURE_ARGS	+=	--disable-native-texlive-build
CONFIGURE_ARGS	+=	--disable-pmx
CONFIGURE_ARGS	+=	--disable-ps2eps
CONFIGURE_ARGS	+=	--disable-psutils
CONFIGURE_ARGS	+=	--enable-ipc
CONFIGURE_ARGS	+=	--enable-shared
CONFIGURE_ARGS	+=	--enable-xindy
CONFIGURE_ARGS	+=	--enable-xindy-docs
CONFIGURE_ARGS	+=	--enable-xindy-rules
CONFIGURE_ARGS	+=	--with-banner-add='/OpenCSW'
CONFIGURE_ARGS	+=	--with-freetype2-include=$(includedir)/freetype2
CONFIGURE_ARGS	+=	--with-mf-x-toolkit
CONFIGURE_ARGS	+=	--with-system-freetype2
CONFIGURE_ARGS	+=	--with-system-gd
CONFIGURE_ARGS	+=	--with-system-libgs
CONFIGURE_ARGS	+=	--with-system-libpng
# poppler, C++, is compiled with Sun Studio
# CONFIGURE_ARGS	+=	--with-system-poppler
# CONFIGURE_ARGS	+=	--with-system-xpdf
CONFIGURE_ARGS	+=	--with-system-t1lib
CONFIGURE_ARGS	+=	--with-system-zlib
CONFIGURE_ARGS	+=	--with-system-zzlib
CONFIGURE_ARGS	+=	--with-x
CONFIGURE_ARGS	+=	--with-xdvi-x-toolkit=xaw

TEST_SCRIPTS	=	custom

RUNTIME_DEP_PKGS	+=	CSWps2eps

include gar/category.mk

PATH := /opt/csw/gnu:/opt/csw/libexec/flex-2.5.35/bin:$(PATH)

pre-configure-modulated:
	mkdir -p $(OBJDIR)
	$(MAKECOOKIE)

# this is needed only because the lacheck test fails:
test-custom:
	cd $(WORKSRC) && /usr/bin/env -i $(BUILD_ENV) && $(MAKE) -i -k -C $(OBJDIR) check
	$(MAKECOOKIE)

# this is private and not available publicly
mydependencies:
	for package in $(PACKAGES); do echo '___' $${package}; $(HOME)/bin/ocswdeplist --depth 1 --dependencies --packaging --csw --prototype $(HOME)/opencsw/$(NAME)/trunk/work/build-global/$${package}.prototype --target $(HOME)/opencsw/$(NAME)/trunk/work/pkgroot; done
