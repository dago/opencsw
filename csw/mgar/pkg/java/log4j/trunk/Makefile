NAME = log4j
VERSION = 1.2.15
CATEGORIES = java
GARTYPE = v2

DESCRIPTION = Apache log4j Logging Services
define BLURB
A fast and flexible framework for logging application debugging messages
endef

# Use jakarta sources
MASTER_SITES = http://apache.cict.fr/logging/$(NAME)/$(VERSION)/
UPSTREAM_MASTER_SITES = http://www.apache.org/dyn/closer.cgi/logging
UFILES_REGEX = (\d+(?:\.\d+)*)

# Set archive filename
DISTFILES = apache-$(NAME)-$(VERSION).tar.gz

# Defines two packages, lib and doc
DISTFILES += $(call admfiles,CSWlog4j,)
DISTFILES += $(call admfiles,CSWlog4jdoc,)

# Defines package description
SPKG_DESC_CSWlog4j    = $(DESCRIPTION)
SPKG_DESC_CSWlog4jdoc = $(DESCRIPTION) documentation package

# Defines dependencies
# RUNTIME_DEP_PKGS_CSWlog4j = No dependency

# Defines package content
PKGFILES_CSWlog4j  = $(prefix)/share/doc/$(NAME)/License.txt
PKGFILES_CSWlog4j += $(prefix)/share/java/.*

# Defines custom steps since java libs do not use autotools
WORKSRC = $(WORKDIR)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = 
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

post-extract:
	@mv $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/apache-$(NAME)-$(VERSION) $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/$(NAME)-$(VERSION)
	@$(MAKECOOKIE)

install-custom:
	@ginstall -d $(DESTDIR)$(datadir)/java
	@gcp -fp $(WORKSRC)/$(DISTNAME)/$(NAME)-$(VERSION).jar $(DESTDIR)$(datadir)/java
	@( cd $(DESTDIR)$(datadir)/java ; \
	   ln -s $(NAME)-$(VERSION).jar $(NAME)-1.2.jar ; \
	   ln -s $(NAME)-$(VERSION).jar $(NAME)-1.jar ; \
	   ln -s $(NAME)-$(VERSION).jar $(NAME).jar )
	@ginstall -d $(DESTDIR)$(datadir)/doc/$(NAME)
	@gcp -fp $(WORKSRC)/$(DISTNAME)/LICENSE $(DESTDIR)$(datadir)/doc/$(NAME)/License.txt
	@gcp -fp $(WORKSRC)/$(DISTNAME)/LICENSE $(DESTDIR)$(datadir)/doc/$(NAME)/License-documentation.txt
	@gcp -frp $(WORKSRC)/$(DISTNAME)/contribs $(DESTDIR)$(datadir)/doc/$(NAME)
	@gcp -frp $(WORKSRC)/$(DISTNAME)/examples $(DESTDIR)$(datadir)/doc/$(NAME)
	@gcp -frp $(WORKSRC)/$(DISTNAME)/site/* $(DESTDIR)$(datadir)/doc/$(NAME)
	@$(MAKECOOKIE)
