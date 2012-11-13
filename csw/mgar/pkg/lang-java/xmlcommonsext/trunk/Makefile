# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = xmlcommonsext
VERSION = 1.4.01
GARTYPE = v2

DESCRIPTION = Brief description
define BLURB
  Long description
endef

MASTER_SITES = http://apache.mirror.clusters.cc//xerces/xml-commons/source/
MASTER_SITES = http://apache.mirror.iphh.net//xerces/xml-commons/binaries/
DISTFILES  = xml-commons-external-1.4.01-bin.tar.gz
DISTNAME = xml-commons-external-1.4.01

ARCHALL_CSWxmlcommonsext = 1

LICENSE = LICENSE
EXTRA_LICENSE += LICENSE.dom-documentation.txt
EXTRA_LICENSE += LICENSE.dom-software.txt
EXTRA_LICENSE += LICENSE.sac.html
EXTRA_LICENSE += LICENSE.sax.txt
EXTRA_LICENSE += NOTICE

CONFIGURE_SCRIPTS = 
TEST_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = $(NAME)
# src tar archive has no toplevel dir
# EXTRACTDIR = $(WORKDIR)/$(DISTNAME)

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

JAR_FILES += xml-apis.jar
JAR_FILES += xml-apis-ext.jar

install-$(NAME):
	ginstall -d -m 755 $(DESTDIR)$(datadir)/java
	ginstall -d -m 755 $(DESTDIR)$(docdir)/$(NAME)
	ginstall -m644 $(foreach jar,$(JAR_FILES),$(WORKSRC)/$(jar)) $(DESTDIR)$(datadir)/java
	ginstall -m644 $(foreach lic,$(EXTRA_LICENSE),$(WORKSRC)/$(lic)) $(DESTDIR)$(docdir)/$(NAME)
	@$(MAKECOOKIES)
