SHORTNAME = fileupload
VERSION = 1.2.2

NAME = commons-$(SHORTNAME)
CATEGORIES = java
GARTYPE = v2

DESCRIPTION = Apache Jakarta Commons FileUpload
define BLURB
Apache Jakarta Commons FileUpload : robust, high-performance, file upload capability
endef

# Use jakarta sources
MASTER_SITES = http://apache.cict.fr/commons/$(SHORTNAME)/binaries/

# Set archive filename
DISTFILES = $(NAME)-$(VERSION)-bin.tar.gz

# Defines two packages, lib and doc
PACKAGES = CSWajcpeupload CSWajcuploaddoc

# Package architecture is ALL (pure java)
ARCHALL = 1

CATALOGNAME_CSWajcpeupload = commons_upload
CATALOGNAME_CSWajcuploaddoc = commons_upload_doc

LICENSE = LICENSE.txt

CHECKPKG_OVERRIDES_CSWajcpeupload += catalogname-does-not-match-pkgname|pkgname=CSWajcpeupload|catalogname=commons_upload|expected-catalogname=ajcpeupload
CHECKPKG_OVERRIDES_CSWajcuploaddoc += catalogname-does-not-match-pkgname|pkgname=CSWajcuploaddoc|catalogname=commons_upload_doc|expected-catalogname=ajcuploaddoc

# Defines package description
SPKG_DESC_CSWajcpeupload    = $(DESCRIPTION)
SPKG_DESC_CSWajcuploaddoc = $(DESCRIPTION) documentation package

# Defines dependencies
RUNTIME_DEP_PKGS_CSWajcpeupload = CSWajclogging CSWajcdigester

# Defines package content
PKGFILES_CSWajcpeupload += $(prefix)/share/java/.*

# Defines custom steps since java libs do not use autotools
WORKSRC = $(WORKDIR)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = 
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	@ginstall -d $(DESTDIR)$(datadir)/java
	@gcp -fp $(WORKSRC)/$(DISTNAME)/lib/$(NAME)-$(VERSION).jar $(DESTDIR)$(datadir)/java
	@( cd $(DESTDIR)$(datadir)/java ; \
	   ln -s $(NAME)-$(VERSION).jar $(NAME)-1.2.jar ; \
	   ln -s $(NAME)-$(VERSION).jar $(NAME)-1.jar ; \
	   ln -s $(NAME)-$(VERSION).jar $(NAME).jar )
	@ginstall -d $(DESTDIR)$(datadir)/doc/$(NAME)
	@gcp -frp $(WORKSRC)/$(DISTNAME)/site/* $(DESTDIR)$(datadir)/doc/$(NAME)
	@$(MAKECOOKIE)
