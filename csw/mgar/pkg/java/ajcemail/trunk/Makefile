SHORTNAME = email
VERSION = 1.2

NAME = commons-$(SHORTNAME)
CATEGORIES = java
GARTYPE = v2

DESCRIPTION = Apache Jakarta Commons Email
define BLURB
Apache Jakarta Commons Email : provide a API for sending email
endef

# Use jakarta sources
MASTER_SITES = http://apache.cict.fr/commons/$(SHORTNAME)/binaries/

# Set archive filename
DISTFILES = $(NAME)-$(VERSION)-bin.tar.gz

# Defines two packages, lib and doc
PACKAGES = CSWajcemail CSWajcemaildoc

# Package architecture is ALL (pure java)
ARCHALL = 1

CATALOGNAME_CSWajcemail = commons_email
CATALOGNAME_CSWajcemaildoc = commons_email_doc

LICENSE = LICENSE.txt

CHECKPKG_OVERRIDES_CSWajcemail += catalogname-does-not-match-pkgname|pkgname=CSWajcemail|catalogname=commons_email|expected-catalogname=ajcemail
CHECKPKG_OVERRIDES_CSWajcemaildoc += catalogname-does-not-match-pkgname|pkgname=CSWajcemaildoc|catalogname=commons_email_doc|expected-catalogname=ajcemaildoc

# Defines package description
SPKG_DESC_CSWajcemail    = $(DESCRIPTION)
SPKG_DESC_CSWajcemaildoc = $(DESCRIPTION) documentation package

# Defines dependencies
RUNTIME_DEP_PKGS_CSWajcemail = CSWajclogging CSWajccollect CSWajcbeanutils 	

# Defines package content
PKGFILES_CSWajcemail += $(prefix)/share/java/.*

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
	   ln -s $(NAME)-$(VERSION).jar $(NAME)-1.jar ; \
	   ln -s $(NAME)-$(VERSION).jar $(NAME).jar )
	@ginstall -d $(DESTDIR)$(datadir)/doc/$(NAME)
	@gcp -frp $(WORKSRC)/$(DISTNAME)/apidocs/* $(DESTDIR)$(datadir)/doc/$(NAME)
	@$(MAKECOOKIE)
