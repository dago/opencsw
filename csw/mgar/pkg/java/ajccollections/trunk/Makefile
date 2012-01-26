SHORTNAME = collections
VERSION = 3.2.1

NAME = commons-$(SHORTNAME)
CATEGORIES = java
GARTYPE = v2

DESCRIPTION = Apache Jakarta Commons Collections
define BLURB
Apache Jakarta Commons Collections : suite of classes that extend the Java Collections Framework
endef

# Use jakarta sources
MASTER_SITES = http://apache.cict.fr/commons/$(SHORTNAME)/binaries/

# Set archive filename
DISTFILES = $(NAME)-$(VERSION)-bin.tar.gz

# Defines two packages, lib and doc
PACKAGES = CSWajccollect CSWajccollectdoc

# Package architecture is ALL (pure java)
ARCHALL = 1

CATALOGNAME_CSWajccollect = commons_collect
CATALOGNAME_CSWajccollectdoc = commons_collect_doc

LICENSE = LICENSE.txt

CHECKPKG_OVERRIDES_CSWajccollect += catalogname-does-not-match-pkgname|pkgname=CSWajccollect|catalogname=commons_collect|expected-catalogname=ajccollect
CHECKPKG_OVERRIDES_CSWajccollectdoc += catalogname-does-not-match-pkgname|pkgname=CSWajccollectdoc|catalogname=commons_collect_doc|expected-catalogname=ajccollectdoc

# Defines package description
SPKG_DESC_CSWajccollect    = $(DESCRIPTION) 
SPKG_DESC_CSWajccollectdoc = $(DESCRIPTION) documentation package

# Defines dependencies
RUNTIME_DEP_PKGS_CSWajccollect  = CSWajcdigester

# Defines package content
PKGFILES_CSWajccollect   	+= $(prefix)/share/java/.*

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
	   ln -s $(NAME)-$(VERSION).jar $(NAME)-3.2.jar ; \
	   ln -s $(NAME)-$(VERSION).jar $(NAME)-3.jar ; \
	   ln -s $(NAME)-$(VERSION).jar $(NAME).jar )
	@ginstall -d $(DESTDIR)$(datadir)/doc/$(NAME)
	@gcp -frp $(WORKSRC)/$(DISTNAME)/apidocs/* $(DESTDIR)$(datadir)/doc/$(NAME)
	@$(MAKECOOKIE)
