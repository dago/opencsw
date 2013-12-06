# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = transfig
VERSION = 3.2.5e
GARTYPE = v2

DESCRIPTION = Brief description
define BLURB
  Long description
endef

MASTER_SITES =  $(SF_MIRROR)
# MASTER_SITES = http://sourceforge.net/projects/mcj/files/mcj-source/transfig.3.2.5e.tar.gz/download
DISTNAME = $(NAME).$(VERSION)
DISTFILES  = $(DISTNAME).tar.gz

GARCOMPILER = GCC4
REINPLACE_USRLOCAL += fig2dev/Imakefile
REINPLACE_USRLOCAL += transfig/Imakefile

BUILD_DEP_PKGS += CSWlibjpeg-dev
BUILD_DEP_PKGS += CSWlibpng-dev
BUILD_DEP_PKGS += CSWlibz-dev

RUNTIME_DEP_PKGS_CSWtransfig += CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWtransfig += CSWlibxpm4

EXTRA_CONFIGURE_ENV += PATH=$(PATH):/usr/openwin/bin
CONFIGURE_ARS = $(DIRPATHS)
CONFIGURE_SCRIPTS = xmkmf
configure-xmkmf:
	(cd $(WORKSRC) && OPENWINHOME=/usr/openwin export OPENWINHOME && env && \
	[ -f Makefile ] && mv -f Makefile Makefile.bak; \
	gsed -i -e '/XCOMM BINDIR/s/.*/BINDIR = \/opt\/csw\/bin/' -e'/XCOMM MKDIRHIER/s/.*/MKDIRHIER = \/usr\/bin\/mkdir/' transfig/Imakefile ; \
	imake -DUseInstalled -I/usr/openwin/lib/X11/config -DHasGcc2=YES -ftransfig/Imakefile -s transfig/Makefile ; \
	gsed -i -e '/XCOMM BINDIR/s/.*/BINDIR = \/opt\/csw\/bin/' -e'/XCOMM MKDIRHIER/s/.*/MKDIRHIER = \/usr\/bin\/mkdir -p/' fig2dev/Imakefile ; \
	imake -DUseInstalled -I/usr/openwin/lib/X11/config -DHasGcc2=YES -ffig2dev/Imakefile -s fig2dev/Makefile ; \
	gsed -i -e '21 i BINDIR = $(prefix)\nMKDIRHIER = /usr/bin/mkdir -p\n' fig2dev/dev/Imakefile ; \
	imake -DUseInstalled -I/usr/openwin/lib/X11/config -DHasGcc2=YES -ffig2dev/dev/Imakefile -s fig2dev/dev/Makefile ; \
	gsed -i -e '/ MAKE = /s/usr\/ccs\/bin\/make/opt\/csw\/bin\/gmake/' transfig/Makefile ; \
	gsed -i -e '/ MAKE = /s/usr\/ccs\/bin\/make/opt\/csw\/bin\/gmake/' fig2dev/Makefile ; \
	imake -DUseInstalled -I/usr/openwin/lib/X11/config -DHasGcc2=YES ; \
	gsed -i -e '/ MAKE = /s/usr\/ccs\/bin\/make/opt\/csw\/bin\/gmake/' Makefile ; \
	)
	$(MAKECOOKIE)

TEST_SCRIPTS = 

include gar/category.mk

