SHORTNAME = validator
VERSION = 1.3.1

NAME = commons-$(SHORTNAME)
CATEGORIES = java
GARTYPE = v2

DESCRIPTION = Apache Jakarta Commons Validator
define BLURB
Apache Jakarta Commons Validator : This package addresses some of these issues of validation rules
endef

# Use jakarta sources
MASTER_SITES = http://apache.cict.fr/commons/$(SHORTNAME)/binaries/

# Set archive filename
DISTFILES = $(NAME)-$(VERSION).tar.gz

# Defines two packages, lib and doc
PACKAGES = CSWajcvalidator CSWajcvalidatordoc

# Package architecture is ALL (pure java)
ARCHALL = 1

CATALOGNAME_CSWajcvalidator = commons_validator
CATALOGNAME_CSWajcvalidatordoc = commons_validat_doc

LICENSE = LICENSE.txt

CHECKPKG_OVERRIDES_CSWajcvalidatordoc += catalogname-does-not-match-pkgname|pkgname=CSWajcvalidatordoc|catalogname=commons_validat_doc|expected-catalogname=ajcvalidatordoc
CHECKPKG_OVERRIDES_CSWajcvalidator += catalogname-does-not-match-pkgname|pkgname=CSWajcvalidator|catalogname=commons_validator|expected-catalogname=ajcvalidator

# Defines package description
SPKG_DESC_CSWajcvalidator    = $(DESCRIPTION)
SPKG_DESC_CSWajcvalidatordoc = $(DESCRIPTION) documentation package

# Defines dependencies
# RUNTIME_DEP_PKGS_CSWajcvalidator = No dependency

# Defines package content
PKGFILES_CSWajcvalidator += $(prefix)/share/java/.*

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
	   ln -s $(NAME)-$(VERSION).jar $(NAME)-1.3.jar ; \
	   ln -s $(NAME)-$(VERSION).jar $(NAME)-1.jar ; \
	   ln -s $(NAME)-$(VERSION).jar $(NAME).jar )
	@ginstall -d $(DESTDIR)$(datadir)/doc/$(NAME)
	@gcp -frp $(WORKSRC)/$(DISTNAME)/docs/* $(DESTDIR)$(datadir)/doc/$(NAME)
	@$(MAKECOOKIE)
