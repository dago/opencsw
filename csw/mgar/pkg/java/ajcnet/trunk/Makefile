SHORTNAME = net
VERSION = 3.0.1

NAME = commons-$(SHORTNAME)
CATEGORIES = java
GARTYPE = v2

DESCRIPTION = Apache Jakarta Commons Net
define BLURB
Apache Jakarta Commons Net : collection of network utilities, including FTP clients etc.
endef

# Use jakarta sources
MASTER_SITES = http://apache.cict.fr/commons/$(SHORTNAME)/binaries/

# Set archive filename
DISTFILES = $(NAME)-$(VERSION)-bin.tar.gz

# Defines two packages, lib and doc
PACKAGES = CSWajcnet CSWajcnetdoc

# Package architecture is ALL (pure java)
ARCHALL = 1

CATALOGNAME_CSWajcnet = commons_net
CATALOGNAME_CSWajcnetdoc = commons_net_doc

LICENSE = LICENSE.txt

CHECKPKG_OVERRIDES_CSWajcnetdoc += catalogname-does-not-match-pkgname|pkgname=CSWajcnetdoc|catalogname=commons_net_doc|expected-catalogname=ajcnetdoc
CHECKPKG_OVERRIDES_CSWajcnet += catalogname-does-not-match-pkgname|pkgname=CSWajcnet|catalogname=commons_net|expected-catalogname=ajcnet

# Defines package description
SPKG_DESC_CSWajcnet    = $(DESCRIPTION)
SPKG_DESC_CSWajcnetdoc = $(DESCRIPTION) documentation package

# Defines dependencies
RUNTIME_DEP_PKGS_CSWajcnet = CSWajclogging CSWajccollect CSWajcbeanutils

# Defines package content
PKGFILES_CSWajcnet += $(prefix)/share/java/.*

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
	   ln -s $(NAME)-$(VERSION).jar $(NAME)-3.0.jar ; \
	   ln -s $(NAME)-$(VERSION).jar $(NAME)-3.jar ; \
	   ln -s $(NAME)-$(VERSION).jar $(NAME).jar )
	@ginstall -d $(DESTDIR)$(datadir)/doc/$(NAME)
	@gcp -frp $(WORKSRC)/$(DISTNAME)/apidocs/* $(DESTDIR)$(datadir)/doc/$(NAME)
	@$(MAKECOOKIE)
