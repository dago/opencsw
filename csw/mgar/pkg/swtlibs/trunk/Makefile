GARNAME      = swtlibs
GARVERSION   = 3.2.2
CATEGORIES   = lib

DESCRIPTION  = Standard Widget Toolkit (SWT) libraries
define BLURB
SWT, the Standard Widget Toolkit, is an open source widget toolkit for Java designed to provide efficient, portable access to the user-interface facilities of the operating systems on which it is implemented.

SWT can be used independently of the rest of the Eclipse Platform. 
endef

MASTER_SITES  = ftp://sunsite.informatik.rwth-aachen.de/pub/mirror/eclipse/R-3.2.2-200702121330/
DISTFILES     = swt-$(GARVERSION)-gtk-solaris-sparc.zip
PKGDIST       = swt-$(GARVERSION)-gtk-solaris-sparc.zip
# DISTFILES    += CSWswtlibs.gspec CSWswtlibs.prototype CSWswtlibs.depend
DISTFILES += $(call admfiles, CSWswtlibs, depend )

CFLAGS       += -xlibmil -errtags=yes -erroff=E_EMPTY_DECLARATION
CFLAGS       += -I/usr/dt/share/include/Dt
CXXFLAGS     += -xlibmil -xlibmopt -features=tmplife -norunpath
LDFLAGS      += -L/opt/csw/lib -R/opt/csw/lib

export CFLAGS CXXFLAGS LDFLAGS 

CONFIGURE_SCRIPTS = none
BUILD_SCRIPTS     = build.sh
INSTALL_SCRIPTS   = none

PATCHFILES = make_solaris.mak.diff

include gar/category.mk

CONFIGURE_ARGS = --prefix=/opt/csw --mandir=/opt/csw/share/man --disable-tests --with-xml=libxml

configure-none:
	@$(MAKECOOKIE)

build-build.sh:
	( CURRENT_DIRECTORY=`pwd` && cd $(WORKDIR)/$(DISTNAME) && CDE_HOME=/usr/dt ./build.sh && cd $(CURRENT_DIRECTORY) )

post-extract:
	( mkdir -p $(WORKDIR)/$(DISTNAME) )
	( mv $(WORKDIR)/swt*sparc/src.zip $(WORKDIR)/$(DISTNAME) )
	( mv $(WORKDIR)/swt*sparc/swt.jar $(WORKDIR)/$(DISTNAME) )
	( cp $(FILEDIR)/COPYING $(WORKDIR)/$(DISTNAME) )
	( CURRENT_DIRECTORY=`pwd` && cd $(WORKDIR)/$(DISTNAME) && unzip src.zip && chmod +x build.sh && cd $(CURRENT_DIRECTORY) )
	@$(MAKECOOKIE)

install-none:
	( mkdir -p $(DESTDIR)/opt/csw/lib )
	( mkdir -p $(DESTDIR)/opt/csw/share/swt )
	( cp $(WORKDIR)/$(DISTNAME)/swt.jar $(DESTDIR)/opt/csw/share/swt )
	( cp $(WORKDIR)/$(DISTNAME)/*.so $(DESTDIR)/opt/csw/lib )
	( rm $(DESTDIR)/opt/csw/lib/libswt-mozilla-gtk-*.so )
	@$(MAKECOOKIE)

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | grep ELF | grep -e 'executable' -e 'dynamic lib' | grep 'not stripped' && strip {}"  \; )

