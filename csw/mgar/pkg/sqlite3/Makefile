GARNAME      = sqlite3
GARVERSION   = 3.6.4
CATEGORIES   = libs

DESCRIPTION  = An embeddable SQL engine in a C library
define BLURB
SQLite is a in-process library that implements a self-contained, serverless, zero-configuration, transactional SQL database engine.
endef

MASTER_SITES  = http://sqlite.org/
DISTFILES     = sqlite-$(GARVERSION).tar.gz 
PKGDIST       = sqlite-$(GARVERSION).tar.gz 
DISTFILES    += CSWsqlite3.gspec CSWsqlite3.prototype CSWsqlite3.depend 
DISTFILES    += CSWsqlite3dev.gspec CSWsqlite3dev.prototype CSWsqlite3dev.depend 
DISTFILES    += COPYING
# DISTFILES    += $(call admfiles,CSWsqlite3, depend) 

CFLAGS       += -xlibmil -errtags=yes -erroff=E_EMPTY_DECLARATION
CXXFLAGS     += -xlibmil -xlibmopt -features=tmplife -norunpath
LDFLAGS      += -L/opt/csw/lib -R/opt/csw/lib

export CFLAGS CXXFLAGS LDFLAGS

PATCHFILES = gar-base.diff
TEST_SCRIPTS	  = none

GREP = ggrep

include ../category.mk

CONFIGURE_ARGS = --prefix=/opt/csw --mandir=/opt/csw/share/man --infodir=/opt/csw/share/info  --enable-threadsafe --disable-debug 

test-none:
	@$(MAKECOOKIE)

post-extract:
	( mv $(WORKDIR)/sqlite-$(GARVERSION) $(WORKDIR)/$(GARNAME)-$(GARVERSION) )
	@$(MAKECOOKIE)

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )

