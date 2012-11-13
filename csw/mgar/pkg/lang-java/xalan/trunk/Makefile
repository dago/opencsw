# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = xalan-j
VERSION = 2.7.1
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = XSLT Processor
define BLURB
  Xalan is an XSLT processor for transforming XML documents into HTML, text, or other XML document types. It uses the Xerces (XML Parser) to convert XML documents to internal nodesets.
endef

MASTER_SITES = http://archive.apache.org/dist/xml/xalan-j/
DISTNAME = $(NAME)_$(subst .,_,$(VERSION))
DISTFILES  = $(DISTNAME)-bin-2jars.tar.gz

LICENSE = LICENSE.txt

PACKAGING_PLATFORMS = solaris10-i386

ARCHALL = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = xalan
SKIPTEST = 1

RUNTIME_DEP_PKGS += CSWxercesj
RUNTIME_DEP_PKGS += CSWxmlcommonsext
# there are overlapping contents or common files
CHECKPKG_OVERRIDES_CSWxalan-j += surplus-dependency|CSWxercesj
CHECKPKG_OVERRIDES_CSWxalan-j += surplus-dependency|CSWxmlcommonsext

include gar/category.mk

JAR_FILES += xalan.jar
JAR_FILES += xsltc.jar

install-xalan:
	ginstall -d -m755 $(DESTDIR)/$(datadir)/java
	ginstall -m644 $(foreach jar,$(JAR_FILES),$(WORKSRC)/$(jar)) $(DESTDIR)$(datadir)/java
	@$(MAKECOOKIES)
