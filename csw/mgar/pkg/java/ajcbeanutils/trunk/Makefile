SHORTNAME = beanutils
GARVERSION = 1.8.0

GARNAME = commons-$(SHORTNAME)
CATEGORIES = java

DESCRIPTION = Apache Jakarta Commons BeanUtils
define BLURB
Apache Jakarta Commons BeanUtils provides wrappers around the Java reflection and introspection
endef

# Use jakarta sources
MASTER_SITES = http://apache.cict.fr/commons/$(SHORTNAME)/binaries/

# Set archive filename
DISTFILES = $(GARNAME)-$(GARVERSION)-bin.tar.gz

# Defines two packages, lib and doc
DISTFILES += $(call admfiles,CSWajcbeanutils,)
DISTFILES += $(call admfiles,CSWajcbeanutilsdoc,)

# Defines package description
SPKG_DESC_CSWajcbeanutils    = $(DESCRIPTION)
SPKG_DESC_CSWajcbeanutilsdoc = $(DESCRIPTION) documentation package

# Defines dependencies
# REQUIRED_PKGS_CSWajcbeanutils  = 

# Defines package content
PKGFILES_CSWajcbeanutils   	 = $(prefix)/share/doc/$(GARNAME)/LICENSE.txt
PKGFILES_CSWajcbeanutils   	+= $(prefix)/share/java/.*

# Defines custom steps since java libs do not use autotools
WORKSRC = $(WORKDIR)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	@ginstall -d $(DESTDIR)$(datadir)/java
	@gcp -fp $(WORKSRC)/$(DISTNAME)/commons-beanutils-1.8.0.jar $(DESTDIR)$(datadir)/java
	@( cd $(DESTDIR)$(datadir)/java ; \
	   ln -s $(GARNAME)-$(GARVERSION).jar $(GARNAME)-1.8.jar ; \
	   ln -s $(GARNAME)-$(GARVERSION).jar $(GARNAME)-1.jar ; \
	   ln -s $(GARNAME)-$(GARVERSION).jar $(GARNAME).jar )
	@ginstall -d $(DESTDIR)$(datadir)/doc/$(GARNAME)
	@gcp -fp $(WORKSRC)/$(DISTNAME)/LICENSE.txt $(DESTDIR)$(datadir)/doc/$(GARNAME)
	@gcp -fp $(WORKSRC)/$(DISTNAME)/LICENSE.txt $(DESTDIR)$(datadir)/doc/$(GARNAME)/LICENSE-documentation.txt
	@gcp -frp $(WORKSRC)/$(DISTNAME)/apidocs/* $(DESTDIR)$(datadir)/doc/$(GARNAME)
	@$(MAKECOOKIE)
