SHORTNAME = fileupload
VERSION = 1.2.1

NAME = commons-$(SHORTNAME)
CATEGORIES = java

DESCRIPTION = Apache Jakarta Commons FileUpload
define BLURB
Apache Jakarta Commons FileUpload : robust, high-performance, file upload capability
endef

# Use jakarta sources
MASTER_SITES = http://apache.cict.fr/commons/$(SHORTNAME)/binaries/
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*)(-bin*).tar.gz

# Set archive filename
DISTFILES = $(NAME)-$(VERSION)-bin.tar.gz

# Defines two packages, lib and doc
DISTFILES += $(call admfiles,CSWajcupload,)
DISTFILES += $(call admfiles,CSWajcuploaddoc,)

# Defines package description
SPKG_DESC_CSWajcupload    = $(DESCRIPTION)
SPKG_DESC_CSWajcuploaddoc = $(DESCRIPTION) documentation package

# Defines dependencies
RUNTIME_DEP_PKGS_CSWajcupload = CSWajclogging CSWajcdigester

# Defines package content
PKGFILES_CSWajcupload  = $(prefix)/share/doc/$(NAME)/License.txt
PKGFILES_CSWajcupload += $(prefix)/share/java/.*

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
	@gcp -fp $(WORKSRC)/$(DISTNAME)/LICENSE.txt $(DESTDIR)$(datadir)/doc/$(NAME)/License.txt
	@gcp -fp $(WORKSRC)/$(DISTNAME)/LICENSE.txt $(DESTDIR)$(datadir)/doc/$(NAME)/License-documentation.txt
	@gcp -frp $(WORKSRC)/$(DISTNAME)/site/* $(DESTDIR)$(datadir)/doc/$(NAME)
	@$(MAKECOOKIE)
