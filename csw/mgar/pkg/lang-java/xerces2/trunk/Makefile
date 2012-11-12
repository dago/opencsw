# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = xercesj
VERSION = 2.11.0
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Java XML parser
define BLURB
  The Apache Xerces2 parser is the reference implementation of XNI but other parser components, configurations, and parsers can be written using the Xerces Native Interface. For complete design and implementation documents, refer to the XNI Manual.


endef

NOGITPATCH = 1

# MASTER_SITES = http://apache.lauf-forum.at//xerces/j/source/
MASTER_SITES = http://mirror.lwnetwork.org.uk/APACHE//xerces/j/binaries/
DISTFILES  = Xerces-J-bin.$(VERSION).tar.gz
LICENSE = LICENSE
EXTRA_LICENSE += LICENSE-SAX.html
EXTRA_LICENSE += LICENSE.DOM-documentation.html
EXTRA_LICENSE += LICENSE.DOM-software.html
EXTRA_LICENSE += LICENSE.resolver.txt
EXTRA_LICENSE += LICENSE.serializer.txt
EXTRA_LICENSE += NOTICE
EXTRA_LICENSE += NOTICE.resolver.txt
EXTRA_LICENSE += NOTICE.serializer.txt

DISTNAME = xerces-$(subst .,_,$(VERSION))

ARCHALL = 1
PACKAGES += CSWxercesj
SPKG_DESC_CSWxercesj = $(DESCRIPTION)

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

JAR_FILES += resolver.jar 
JAR_FILES += serializer.jar
JAR_FILES += xercesImpl.jar
JAR_FILES += xercesSamples.jar

install-xerces:
	ginstall -d -m 755 $(DESTDIR)$(datadir)/java
	ginstall -d -m 755 $(DESTDIR)$(docdir)/$(NAME)
	ginstall -m644 $(foreach jar,$(JAR_FILES),$(WORKSRC)/$(jar)) $(DESTDIR)$(datadir)/java
	ginstall -m644 $(foreach lic,$(EXTRA_LICENSE),$(WORKSRC)/$(lic)) $(DESTDIR)$(docdir)/$(NAME)
	@$(MAKECOOKIES)
