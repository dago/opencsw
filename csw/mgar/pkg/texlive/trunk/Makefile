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
DISTFILES		+=	$(DISTNAMEPREFIX)-texmf.tar.xz
PATCHFILES		+=	0001-Fix-lacheck-buffer-overflow.patch
PATCHFILES		+=	0002-Fix-ICU-link-edit.patch

PACKAGING_PLATFORMS	=	solaris10-sparc
PACKAGING_PLATFORMS	+=	solaris10-i386

BUILD_DEP_PKGS	+=	CSWpoppler-dev
BUILD_DEP_PKGS	+=	CSWpoppler-dev
BUILD_DEP_PKGS	+=	CSWclisp
# when this is installed, raises undefined symbols when linking
# tools/genrb; this is the reason form 0002-Fix-ICU-link-edit.patch
# BUILD_DEP_PKGS += CSWlibicu-dev

EXTRA_CFLAGS	+=	-std=gnu99 -D_XPG6
EXTRA_CXXFLAGS	+=	-D_XPG6

STRIP_LIBTOOL	=	1

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
# cannot be used as ICU delivered by OpenCSW is compiled with Sun Studio C++
#CONFIGURE_ARGS	+=	--with-system-icu
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

RUNTIME_DEP_PKGS	+=	CSWps2eps

# EXTRA_MERGE_EXCLUDE_FILES	+=	

include gar/category.mk

PATH := /opt/csw/gnu:/opt/csw/libexec/flex-2.5.35/bin:$(PATH)

# we build in a directory outside the source tree and gather the
# licenses from the extra archive into one file:
pre-configure-modulated:
	mkdir -p $(OBJDIR)
	cat $(WORKDIR)/$(DISTNAMEPREFIX)-extra/LICENSE.TL $(WORKDIR)/$(DISTNAMEPREFIX)-extra/LICENSE.CTAN > $(WORKSRC)/COPYING
	$(MAKECOOKIE)

# this is necessary to link texk/ptexenc (libtool --mode=install) when
# the kpathsea from teTeX is installed on the build system; this will
# probably go away when teTeX is decommissioned.
pre-install-modulated:
	cd $(OBJDIR)/texk/ptexenc && gsed --in-place --expression='s;-L/opt/csw/lib;;g' libptexenc.la
	$(MAKECOOKIE)

# install the texmf and texmf-dist but exclude those components
# provided by the source archive:
post-install-modulated: xdup = --exclude=texmf/doc/xindy/alphabets-doc.pdf
post-install-modulated: xdup += --exclude=texmf/doc/xindy/tex2xindy.pdf
post-install-modulated: xdup += --exclude=texmf/doc/xindy/texindy.pdf
post-install-modulated: xdup += --exclude=texmf/doc/xindy/xindy.pdf
post-install-modulated: xdup += --exclude=texmf/dvipdfmx/dvipdfmx.cfg
post-install-modulated: xdup += --exclude=texmf/xindy/modules/tex/inputenc/cp1250.xdy
post-install-modulated: xdup += --exclude=texmf/xindy/modules/tex/inputenc/cp437.xdy
post-install-modulated: xdup += --exclude=texmf/xindy/modules/tex/inputenc/cp850.xdy
post-install-modulated:
	gtar --directory=$(WORKDIR)/$(DISTNAMEPREFIX)-texmf --create $(xdup) --file=- . | gtar --directory=$(DESTDIR)/$(datadir) --extract --file=-
	$(MAKECOOKIE)

# this is private and not available publicly
mydependencies:
	for package in $(PACKAGES); do echo '___' $${package}; $(HOME)/bin/ocswdeplist --depth 1 --dependencies --packaging --csw --prototype $(HOME)/opencsw/$(NAME)/trunk/work/build-global/$${package}.prototype --target $(HOME)/opencsw/$(NAME)/trunk/work/pkgroot; done
