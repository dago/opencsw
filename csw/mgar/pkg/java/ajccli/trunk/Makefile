SHORTNAME = cli
VERSION = 1.2

NAME = commons-$(SHORTNAME)
CATEGORIES = java
GARTYPE = v2

DESCRIPTION = Apache Jakarta Commons CLI
define BLURB
Apache Jakarta Commons CLI : API for working with the command line arguments and options
endef

# Use jakarta sources
MASTER_SITES = http://apache.cict.fr/commons/$(SHORTNAME)/binaries/

# Set archive filename
DISTFILES = $(NAME)-$(VERSION)-bin.tar.gz

# Defines two packages, lib and doc
PACKAGES = CSWajccli CSWajcclidoc

SPKG_DESC_CSWajccli    = $(DESCRIPTION)
SPKG_DESC_CSWajcclidoc = $(DESCRIPTION) documentation package

ARCHALL = 1

LICENSE = LICENSE.txt

CATALOGNAME_CSWajccli = commons_cli
CATALOGNAME_CSWajcclidoc = commons_cli_doc

# Defines package content
PKGFILES_CSWajccli   	+= $(prefix)/share/java/.*

# Defines custom steps since java libs do not use autotools
WORKSRC = $(WORKDIR)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

CHECKPKG_OVERRIDES_CSWajcclidoc += catalogname-does-not-match-pkgname|pkgname=CSWajcclidoc|catalogname=commons_cli_doc|expected-catalogname=ajcclidoc
CHECKPKG_OVERRIDES_CSWajccli += catalogname-does-not-match-pkgname|pkgname=CSWajccli|catalogname=commons_cli|expected-catalogname=ajccli

include gar/category.mk

install-custom:
	@ginstall -d $(DESTDIR)$(datadir)/java
	@gcp -fp $(WORKSRC)/$(DISTNAME)/commons-cli-$(VERSION).jar $(DESTDIR)$(datadir)/java
	@( cd $(DESTDIR)$(datadir)/java ; \
	   ln -s $(NAME)-$(VERSION).jar $(NAME)-1.jar ; \
	   ln -s $(NAME)-$(VERSION).jar $(NAME).jar )
	@ginstall -d $(DESTDIR)$(datadir)/doc/$(NAME)
	@gcp -frp $(WORKSRC)/$(DISTNAME)/apidocs/* $(DESTDIR)$(datadir)/doc/$(NAME)
	@$(MAKECOOKIE)
