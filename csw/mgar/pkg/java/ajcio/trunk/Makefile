SHORTNAME = io
VERSION = 2.0.1

NAME = commons-$(SHORTNAME)
CATEGORIES = java
GARTYPE = v2

DESCRIPTION = Apache Jakarta Commons IO
define BLURB
Apache Jakarta Commons IO : a collection of I/O utilities
endef

# Use jakarta sources
MASTER_SITES = http://apache.cict.fr/commons/$(SHORTNAME)/binaries/

# Defines two packages, lib and doc
PACKAGES = CSWajcio CSWajciodoc

# Package architecture is ALL (pure java)
ARCHALL = 1

CATALOGNAME_CSWajcio = commons_io
CATALOGNAME_CSWajciodoc = commons_io_doc

LICENSE = LICENSE.txt

CHECKPKG_OVERRIDES_CSWajcio += catalogname-does-not-match-pkgname|pkgname=CSWajcio|catalogname=commons_io|expected-catalogname=ajcio
CHECKPKG_OVERRIDES_CSWajciodoc += catalogname-does-not-match-pkgname|pkgname=CSWajciodoc|catalogname=commons_io_doc|expected-catalogname=ajciodoc

# Set archive filename
DISTFILES = $(NAME)-$(VERSION)-bin.tar.gz

# Defines package description
SPKG_DESC_CSWajcio    = $(DESCRIPTION)
SPKG_DESC_CSWajciodoc = $(DESCRIPTION) documentation package

# Defines dependencies
# RUNTIME_DEP_PKGS_CSWajcio = No dependency

# Defines package content
PKGFILES_CSWajcio += $(prefix)/share/java/.*

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
	   ln -s $(NAME)-$(VERSION).jar $(NAME)-2.0.jar ; \
	   ln -s $(NAME)-$(VERSION).jar $(NAME)-2.jar ; \
	   ln -s $(NAME)-$(VERSION).jar $(NAME).jar )
	@ginstall -d $(DESTDIR)$(datadir)/doc/$(NAME)
	@gcp -frp $(WORKSRC)/$(DISTNAME)/docs/* $(DESTDIR)$(datadir)/doc/$(NAME)
	@$(MAKECOOKIE)
