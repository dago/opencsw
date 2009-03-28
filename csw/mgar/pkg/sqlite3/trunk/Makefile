GARNAME      = sqlite3
GARVERSION   = 3.6.10
CATEGORIES   = lib

DESCRIPTION  = An embeddable SQL engine in a C library
define BLURB
SQLite is a in-process library that implements a self-contained, serverless, zero-configuration, transactional SQL database engine.
endef

# Download informations
MASTER_SITES  = http://sqlite.org/
DISTFILES     = sqlite-$(GARVERSION).tar.gz 
DISTFILES    += $(call admfiles, CSWsqlite3, ) 
DISTFILES    += $(call admfiles, CSWsqlite3devel, ) 
DISTFILES    += $(call admfiles, CSWsqlite3rt, ) 
DISTFILES    += copyright.html

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = sqlite-(\d+(?:\.\d+)*).tar.gz

# Package description
SPKG_DESC_CSWsqlite3 	  = $(DESCRIPTION)
SPKG_DESC_CSWsqlite3devel = $(SPKG_DESC_CSWsqlite3) development package
SPKG_DESC_CSWsqlite3rt    = $(SPKG_DESC_CSWsqlite3) runtime

# Dynamic prototype
PKGFILES_CSWsqlite3devel   = $(PKGFILES_DEVEL)
PKGFILES_CSWsqlite3devel  += /opt/csw/share/doc/sqlite3devel/copyright.html
PKGFILES_CSWsqlite3rt      = $(PKGFILES_RT)
PKGFILES_CSWsqlite3rt     += /opt/csw/share/doc/sqlite3rt/copyright.html
PKGFILES_CSWsqlite3rt     += /opt/csw/lib/.*

# Dependencies
REQUIRED_PKGS_CSWsqlite3      = CSWsqlite3rt
REQUIRED_PKGS_CSWsqlite3devel = CSWsqlite3

# Build the 64 bits binaries
NO_ISAEXEC             = 1
EXTRA_BUILD_ISAS_sparc = sparcv9

# Add some patches to the sources
PATCHFILES     = gar-base.diff

# Do not execute make test step
TEST_SCRIPTS   = none

# Make configure options
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-threadsafe --disable-debug 

test-none:
	@$(MAKECOOKIE)

post-extract:
	( cd $(WORKROOTDIR) ; for i in build-isa-* ; do mv $$i/sqlite-$(GARVERSION) $$i/$(GARNAME)-$(GARVERSION) ; done )
	@$(MAKECOOKIE)

pre-install:
	@ginstall -d $(WORKROOTDIR)/install-$(firstword $(MODULATIONS))$(datadir)/doc/$(GARNAME) 
	@ginstall -d $(WORKROOTDIR)/install-$(firstword $(MODULATIONS))$(datadir)/doc/$(GARNAME)devel 
	@ginstall -d $(WORKROOTDIR)/install-$(firstword $(MODULATIONS))$(datadir)/doc/$(GARNAME)rt 
	@gcp -fp $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/copyright.html $(WORKROOTDIR)/install-$(firstword $(MODULATIONS))$(datadir)/doc/$(GARNAME) 
	@gcp -fp $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/copyright.html $(WORKROOTDIR)/install-$(firstword $(MODULATIONS))$(datadir)/doc/$(GARNAME)devel 
	@gcp -fp $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/copyright.html $(WORKROOTDIR)/install-$(firstword $(MODULATIONS))$(datadir)/doc/$(GARNAME)rt 

include gar/category.mk

