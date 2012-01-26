SHORTNAME = codec
VERSION = 1.5

NAME = commons-$(SHORTNAME)
CATEGORIES = java
GARTYPE = v2

DESCRIPTION = Apache Jakarta Commons Codec
define BLURB
Apache Jakarta Commons Codec : implementations of common encoders and decoders such as Base64
endef

# Use jakarta sources
MASTER_SITES = http://apache.cict.fr/commons/$(SHORTNAME)/binaries/

# Set archive filename
DISTFILES = $(NAME)-$(VERSION)-bin.tar.gz

PACKAGES = CSWajccodec CSWajccodecdoc
ARCHALL  = 1
CATALOGNAME_CSWajccodec = commons_codec
CATALOGNAME_CSWajccodecdoc = commons_codec_doc

LICENSE = LICENSE.txt

# Defines package description
SPKG_DESC_CSWajccodec    = $(DESCRIPTION)
SPKG_DESC_CSWajccodecdoc = $(DESCRIPTION) documentation package

CHECKPKG_OVERRIDES_CSWajccodec += catalogname-does-not-match-pkgname|pkgname=CSWajccodec|catalogname=commons_codec|expected-catalogname=ajccodec
CHECKPKG_OVERRIDES_CSWajccodecdoc += catalogname-does-not-match-pkgname|pkgname=CSWajccodecdoc|catalogname=commons_codec_doc|expected-catalogname=ajccodecdoc

# Defines package content
PKGFILES_CSWajccodec   	+= $(prefix)/share/java/.*

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
