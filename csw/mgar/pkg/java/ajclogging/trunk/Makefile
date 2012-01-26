SHORTNAME = logging
VERSION = 1.1.1

NAME = commons-$(SHORTNAME)
CATEGORIES = java
GARTYPE = v2

DESCRIPTION = Apache Jakarta Commons Logging
define BLURB
Apache Jakarta Commons Logging : bridge between different logging libraries
endef

# Use jakarta sources
MASTER_SITES = http://apache.cict.fr/commons/$(SHORTNAME)/binaries/

# Set archive filename
DISTFILES = $(NAME)-$(VERSION)-bin.tar.gz

# Defines two packages, lib and doc
PACKAGES = CSWajclogging CSWajcloggingdoc

# Package architecture is ALL (pure java)
ARCHALL = 1

CATALOGNAME_CSWajclogging = commons_logging
CATALOGNAME_CSWajcloggingdoc = commons_logging_doc

LICENSE = LICENSE.txt

CHECKPKG_OVERRIDES_CSWajclogging += catalogname-does-not-match-pkgname|pkgname=CSWajclogging|catalogname=commons_logging|expected-catalogname=ajclogging
CHECKPKG_OVERRIDES_CSWajcloggingdoc += catalogname-does-not-match-pkgname|pkgname=CSWajcloggingdoc|catalogname=commons_logging_doc|expected-catalogname=ajcloggingdoc

# Defines package description
SPKG_DESC_CSWajclogging    = $(DESCRIPTION)
SPKG_DESC_CSWajcloggingdoc = $(DESCRIPTION) documentation package

# Defines dependencies
RUNTIME_DEP_PKGS_CSWajclogging = CSWlog4j

# Defines package content
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
	@gcp -frp $(WORKSRC)/$(DISTNAME)/site/* $(DESTDIR)$(datadir)/doc/$(NAME)
	@$(MAKECOOKIE)
