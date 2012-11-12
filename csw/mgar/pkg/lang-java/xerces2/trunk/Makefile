# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = Xerces
VERSION = 2.11.0
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Brief description
define BLURB
  Long description
endef

# MASTER_SITES = http://apache.lauf-forum.at//xerces/j/source/
MASTER_SITES = http://mirror.lwnetwork.org.uk/APACHE//xerces/j/binaries/
DISTNAME = $(NAME)-J-bin.$(VERSION)
DISTFILES  = $(DISTNAME).tar.gz
LICENSE = LICENSE
EXTRA_LICENSE += LICENSE-SAX.html
EXTRA_LICENSE += LICENSE.DOM-documentation.html
EXTRA_LICENSE += LICENSE.DOM-resolver.html
EXTRA_LICENSE += LICENSE.serializer.txt
EXTRA_LICENSE += NOTICE
EXTRA_LICENSE += NOTICE.resolver.txt
EXTRA_LICENSE += NOTICE.serializer.txt

WORKSRC = $(WORKDIR)/$(call tolower,$(NAME))-$(subst .,_,$(VERSION))
CONFIGURE_SCRIPTS =
TEST_SCRIPTS =
BUILD_SCRIPTS = xerces
EXTRA_BUILD_ENV += JAVA_HOME=/usr/jdk/instances/jdk1.6.0
INSTALL_SCRIPTS = xerces

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

build-xerces:
# 	(cd $(WORKDIR)/$(NAME)-$(subst .,_,$(VERSION)) \
# 	&& gsed -i -e 's///' -e '/LIBDIR/s/.\/tools/\/opt\/csw\/share\/java/' build.sh \
# 	&& $(BUILD_ENV) sh build.sh)
	@$(MAKECOOKIES)

# merge-license-modulated:
# 	umask 022 && mkdir -p $(PKGROOT)$$LICENSEDIR && \
# 	rm -f $(PKGROOT)$$LICENSEDIR/license && \
# 	cp $(foreach lic,$(LICENSE),$(WORKSRC)/$(lic)) $(PKGROOT)$$LICENSEDIR
# 	@$(MAKECOOKIE)

install-xerces:
	ginstall -d -m 755 $(DESTDIR)$(datadir)/java
	ginstall -m644 $(WORKSRC)/*.jar $(DESTDIR)$(datadir)/java
	@$(MAKECOOKIES)
