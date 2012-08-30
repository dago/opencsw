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
TEXMFARPREFIX	=	$(DISTNAMEPREFIX)-texmf
TEXMFAR			=	$(TEXMFARPREFIX).tar.xz
DISTFILES		+=	$(TEXMFAR)
NOEXTRACT		+=	$(TEXMFAR)
PATCHFILES		+=	0001-Fix-lacheck-buffer-overflow.patch
PATCHFILES		+=	0002-Fix-ICU-link-edit.patch
PATCHFILES		+=	0003-Adapt-texmf-configuration.patch
PATCHFILES		+=	0004-Activate-formats.patch

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

# install the texmf and texmf-dist
post-install-modulated:
	: merge source and distributed texmf tree
	gtar --directory=$(DESTDIR)/$(datadir) --extract --file=$(DOWNLOADDIR)/$(TEXMFAR)
	gtar --directory=$(DESTDIR)/$(datadir) --create --file=- texmf texmf-dist | gtar --directory=$(DESTDIR)/$(datadir)/$(TEXMFARPREFIX) --extract --file=-
	rm -rf $(DESTDIR)/$(datadir)/texmf $(DESTDIR)/$(datadir)/texmf-dist
	mv $(DESTDIR)/$(datadir)/$(TEXMFARPREFIX)/texmf $(DESTDIR)/$(datadir)
	mv $(DESTDIR)/$(datadir)/$(TEXMFARPREFIX)/texmf-dist $(DESTDIR)/$(datadir)
	rm -rf $(DESTDIR)/$(datadir)/$(TEXMFARPREFIX)
	: create additional hierarchy to reflect texmf.cnf
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(datadir)/texmf-local
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(localstatedir)/lib/texmf-var
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(localstatedir)/cache/texmf-fonts
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(sysconfdir)/texmf
	: create all the available formats:
	PATH=$(DESTDIR)/$(bindir):${PATH} LD_LIBRARY_PATH=$(DESTDIR)/$(libdir) fmtutil-sys --all
	: create symbolic links for available formats:
	cd $(DESTDIR)/$(bindir) && ln -s -f aleph lamed
	cd $(DESTDIR)/$(bindir) && ln -s -f pdftex amstex
	cd $(DESTDIR)/$(bindir) && ln -s -f pdftex cslatex
	cd $(DESTDIR)/$(bindir) && ln -s -f pdftex pdfcslatex
	cd $(DESTDIR)/$(bindir) && ln -s -f pdftex csplain
	cd $(DESTDIR)/$(bindir) && ln -s -f pdftex pdfcsplain
	cd $(DESTDIR)/$(bindir) && ln -s -f pdftex eplain
	cd $(DESTDIR)/$(bindir) && ln -s -f pdftex jadetex
	cd $(DESTDIR)/$(bindir) && ln -s -f pdftex pdfjadetex
	cd $(DESTDIR)/$(bindir) && ln -s -f pdftex latex
	cd $(DESTDIR)/$(bindir) && ln -s -f pdftex pdflatex
	cd $(DESTDIR)/$(bindir) && ln -s -f luatex dvilualatex
	cd $(DESTDIR)/$(bindir) && ln -s -f luatex lualatex
	cd $(DESTDIR)/$(bindir) && ln -s -f luatex dviluatex
	cd $(DESTDIR)/$(bindir) && ln -s -f pdftex mex
	cd $(DESTDIR)/$(bindir) && ln -s -f pdftex pdfmex
	cd $(DESTDIR)/$(bindir) && ln -s -f pdftex utf8mex
	cd $(DESTDIR)/$(bindir) && ln -s -f pdftex mllatex
	cd $(DESTDIR)/$(bindir) && ln -s -f pdftex mltex
	cd $(DESTDIR)/$(bindir) && ln -s -f pdftex etex
	cd $(DESTDIR)/$(bindir) && ln -s -f pdftex pdfetex
	cd $(DESTDIR)/$(bindir) && ln -s -f pdftex cyramstex
	cd $(DESTDIR)/$(bindir) && ln -s -f pdftex cyrtex
	cd $(DESTDIR)/$(bindir) && ln -s -f pdftex cyrtexinfo
	cd $(DESTDIR)/$(bindir) && ln -s -f pdftex texsis
	cd $(DESTDIR)/$(bindir) && ln -s -f euptex uplatex
	cd $(DESTDIR)/$(bindir) && ln -s -f xetex xelatex
	cd $(DESTDIR)/$(bindir) && ln -s -f pdftex xmltex
	cd $(DESTDIR)/$(bindir) && ln -s -f pdftex pdfxmltex
	$(MAKECOOKIE)

# this is private and not available publicly
mydependencies:
	for package in $(PACKAGES); do echo '___' $${package}; $(HOME)/bin/ocswdeplist --depth 1 --dependencies --packaging --csw --prototype $(HOME)/opencsw/$(NAME)/trunk/work/build-global/$${package}.prototype --target $(HOME)/opencsw/$(NAME)/trunk/work/pkgroot; done
