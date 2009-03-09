GARNAME = log4j
GARVERSION = 1.2.15
CATEGORIES = java

DESCRIPTION = Apache log4j Logging Services
define BLURB
A fast and flexible framework for logging application debugging messages
endef

# Use jakarta sources
MASTER_SITES = http://apache.cict.fr/logging/$(GARNAME)/$(GARVERSION)/
UPSTREAM_MASTER_SITES = http://www.apache.org/dyn/closer.cgi/logging
UFILES_REGEX = (\d+(?:\.\d+)*)

# Set archive filename
DISTFILES = apache-$(GARNAME)-$(GARVERSION).tar.gz

# Defines two packages, lib and doc
DISTFILES += $(call admfiles,CSWlog4j,)
DISTFILES += $(call admfiles,CSWlog4jdoc,)

# Defines package description
SPKG_DESC_CSWlog4j    = $(DESCRIPTION)
SPKG_DESC_CSWlog4jdoc = $(DESCRIPTION) documentation package

# Defines dependencies
# REQUIRED_PKGS_CSWlog4j = No dependency

# Defines package content
PKGFILES_CSWlog4j  = $(prefix)/share/doc/$(GARNAME)/License.txt
PKGFILES_CSWlog4j += $(prefix)/share/java/.*

# Defines custom steps since java libs do not use autotools
WORKSRC = $(WORKDIR)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = 
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

post-extract:
	@mv $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/apache-$(GARNAME)-$(GARVERSION) $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/$(GARNAME)-$(GARVERSION)
	@$(MAKECOOKIE)

install-custom:
	@ginstall -d $(DESTDIR)$(datadir)/java
	@gcp -fp $(WORKSRC)/$(DISTNAME)/$(GARNAME)-$(GARVERSION).jar $(DESTDIR)$(datadir)/java
	@( cd $(DESTDIR)$(datadir)/java ; \
	   ln -s $(GARNAME)-$(GARVERSION).jar $(GARNAME)-1.2.jar ; \
	   ln -s $(GARNAME)-$(GARVERSION).jar $(GARNAME)-1.jar ; \
	   ln -s $(GARNAME)-$(GARVERSION).jar $(GARNAME).jar )
	@ginstall -d $(DESTDIR)$(datadir)/doc/$(GARNAME)
	@gcp -fp $(WORKSRC)/$(DISTNAME)/LICENSE $(DESTDIR)$(datadir)/doc/$(GARNAME)/License.txt
	@gcp -fp $(WORKSRC)/$(DISTNAME)/LICENSE $(DESTDIR)$(datadir)/doc/$(GARNAME)/License-documentation.txt
	@gcp -frp $(WORKSRC)/$(DISTNAME)/contribs $(DESTDIR)$(datadir)/doc/$(GARNAME)
	@gcp -frp $(WORKSRC)/$(DISTNAME)/examples $(DESTDIR)$(datadir)/doc/$(GARNAME)
	@gcp -frp $(WORKSRC)/$(DISTNAME)/site/* $(DESTDIR)$(datadir)/doc/$(GARNAME)
	@$(MAKECOOKIE)
