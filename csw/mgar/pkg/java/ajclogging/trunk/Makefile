SHORTNAME = logging
VERSION = 1.1.1

NAME = commons-$(SHORTNAME)
CATEGORIES = java

DESCRIPTION = Apache Jakarta Commons Logging
define BLURB
Apache Jakarta Commons Logging : bridge between different logging libraries
endef

# Use jakarta sources
MASTER_SITES = http://apache.cict.fr/commons/$(SHORTNAME)/binaries/
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*)(-bin*).tar.gz

# Set archive filename
DISTFILES = $(NAME)-$(VERSION)-bin.tar.gz

# Defines two packages, lib and doc
DISTFILES += $(call admfiles,CSWajclogging,)
DISTFILES += $(call admfiles,CSWajcloggingdoc,)

# Defines package description
SPKG_DESC_CSWajclogging    = $(DESCRIPTION)
SPKG_DESC_CSWajcloggingdoc = $(DESCRIPTION) documentation package

# Defines dependencies
RUNTIME_DEP_PKGS_CSWajclogging = CSWlog4j

# Defines package content
PKGFILES_CSWajclogging  = $(prefix)/share/doc/$(NAME)/License.txt
PKGFILES_CSWajclogging += $(prefix)/share/java/.*

# Defines custom steps since java libs do not use autotools
WORKSRC = $(WORKDIR)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = 
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	@ginstall -d $(DESTDIR)$(datadir)/java
	@gcp -fp $(WORKSRC)/$(DISTNAME)/$(NAME)-$(VERSION).jar $(DESTDIR)$(datadir)/java
	@( cd $(DESTDIR)$(datadir)/java ; \
	   ln -s $(NAME)-$(VERSION).jar $(NAME)-1.1.jar ; \
	   ln -s $(NAME)-$(VERSION).jar $(NAME)-1.jar ; \
	   ln -s $(NAME)-$(VERSION).jar $(NAME).jar )
	@ginstall -d $(DESTDIR)$(datadir)/doc/$(NAME)
	@gcp -fp $(WORKSRC)/$(DISTNAME)/LICENSE.txt $(DESTDIR)$(datadir)/doc/$(NAME)/License.txt
	@gcp -fp $(WORKSRC)/$(DISTNAME)/LICENSE.txt $(DESTDIR)$(datadir)/doc/$(NAME)/License-documentation.txt
	@gcp -frp $(WORKSRC)/$(DISTNAME)/site/* $(DESTDIR)$(datadir)/doc/$(NAME)
	@$(MAKECOOKIE)
