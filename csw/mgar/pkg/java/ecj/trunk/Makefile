NAME = ecj
VERSION = 4.3M4
CATEGORIES = java
GARTYPE = v2

DESCRIPTION = JDT Core Batch Compiler

# There seems to be some issue with the download code which breaks on & in the URL, download manually for now and put into /home/src
MASTER_SITES += http://www.eclipse.org/downloads/download.php?r=1&file=/eclipse/downloads/drops4/S-4.3M4-201212140730/
DISTFILES += $(DISTNAME).jar
DISTFILES += ecj1
DISTFILES += README.CSW

LICENSE_TEXT = This package is distributed under the Eclipse license

PACKAGES += CSWecj
SPKG_DESC_CSWecj = Eclipse JDT Core Batch Compiler, contains ecj.jar
ARCHALL_CSWecj = 1

WORKSRC = $(WORKDIR)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = 
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)$(datadir)/java
	gcp -fp $(WORKDIR)/$(NAME)-$(VERSION).jar $(DESTDIR)$(datadir)/java
	( cd $(DESTDIR)$(datadir)/java ; \
	   ln -s $(NAME)-$(VERSION).jar $(NAME).jar )
	ginstall -D -m 0755 $(WORKDIR)/ecj1 $(DESTDIR)$(bindir)/ecj1
	@$(MAKECOOKIE)
