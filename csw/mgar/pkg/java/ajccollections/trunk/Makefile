SHORTNAME = collections
GARVERSION = 3.2.1

GARNAME = commons-$(SHORTNAME)
CATEGORIES = java

DESCRIPTION = Apache Jakarta Commons Collections
define BLURB
Apache Jakarta Commons Collections : suite of classes that extend the Java Collections Framework
endef

# Use jakarta sources
MASTER_SITES = http://apache.cict.fr/commons/$(SHORTNAME)/binaries/

# Set archive filename
DISTFILES = $(GARNAME)-$(GARVERSION)-bin.tar.gz

# Defines two packages, lib and doc
DISTFILES += $(call admfiles,CSWajccollect,)
DISTFILES += $(call admfiles,CSWajccollectdoc,)

# Defines package description
SPKG_DESC_CSWajccollect    = $(DESCRIPTION) 
SPKG_DESC_CSWajccollectdoc = $(DESCRIPTION) documentation package

# Defines dependencies
REQUIRED_PKGS_CSWajccollect  = CSWjunit

# Defines package content
PKGFILES_CSWajccollectdoc   = $(prefix)/share/doc/$(GARNAME)-doc.*

# Defines custom steps since java libs do not use autotools
WORKSRC = $(WORKDIR)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	@ginstall -d $(DESTDIR)$(datadir)/java
	@gcp -fp $(WORKSRC)/$(DISTNAME)/commons-collections-3.2.1.jar $(DESTDIR)$(datadir)/java
	@( cd $(DESTDIR)$(datadir)/java ; \
	   ln -s $(GARNAME)-$(GARVERSION).jar $(GARNAME)-3.2.jar ; \
	   ln -s $(GARNAME)-$(GARVERSION).jar $(GARNAME)-3.jar ; \
	   ln -s $(GARNAME)-$(GARVERSION).jar $(GARNAME).jar )
	@ginstall -d $(DESTDIR)$(datadir)/doc/$(GARNAME)
	@ginstall -d $(DESTDIR)$(datadir)/doc/$(GARNAME)-doc
	@gcp -fp $(WORKSRC)/$(DISTNAME)/LICENSE.txt $(DESTDIR)$(datadir)/doc/$(GARNAME)
	@gcp -fp $(WORKSRC)/$(DISTNAME)/LICENSE.txt $(DESTDIR)$(datadir)/doc/$(GARNAME)-doc
	@gcp -frp $(WORKSRC)/$(DISTNAME)/apidocs/* $(DESTDIR)$(datadir)/doc/$(GARNAME)-doc
	@$(MAKECOOKIE)
