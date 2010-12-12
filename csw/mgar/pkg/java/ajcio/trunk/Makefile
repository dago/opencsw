SHORTNAME = io
VERSION = 1.4

NAME = commons-$(SHORTNAME)
CATEGORIES = java

DESCRIPTION = Apache Jakarta Commons IO
define BLURB
Apache Jakarta Commons IO : a collection of I/O utilities
endef

# Use jakarta sources
MASTER_SITES = http://apache.cict.fr/commons/$(SHORTNAME)/binaries/
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*)(-bin*).tar.gz

# Set archive filename
DISTFILES = $(NAME)-$(VERSION)-bin.tar.gz

# Defines two packages, lib and doc
DISTFILES += $(call admfiles,CSWajcio,)
DISTFILES += $(call admfiles,CSWajciodoc,)

# Defines package description
SPKG_DESC_CSWajcio    = $(DESCRIPTION)
SPKG_DESC_CSWajciodoc = $(DESCRIPTION) documentation package

# Defines dependencies
# RUNTIME_DEP_PKGS_CSWajcio = No dependency

# Defines package content
PKGFILES_CSWajcio  = $(prefix)/share/doc/$(NAME)/License.txt
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
	   ln -s $(NAME)-$(VERSION).jar $(NAME)-1.jar ; \
	   ln -s $(NAME)-$(VERSION).jar $(NAME).jar )
	@ginstall -d $(DESTDIR)$(datadir)/doc/$(NAME)
	@gcp -fp $(WORKSRC)/$(DISTNAME)/LICENSE.txt $(DESTDIR)$(datadir)/doc/$(NAME)/License.txt
	@gcp -fp $(WORKSRC)/$(DISTNAME)/LICENSE.txt $(DESTDIR)$(datadir)/doc/$(NAME)/License-documentation.txt
	@gcp -frp $(WORKSRC)/$(DISTNAME)/docs/* $(DESTDIR)$(datadir)/doc/$(NAME)
	@$(MAKECOOKIE)
