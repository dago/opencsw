GARNAME = kawa
GARVERSION = 1.9.1
CATEGORIES = utils
GARCH = all

DESCRIPTION = Java implementation of Scheme and a framework for implementing high-level and dynamic languages

MASTER_SITES = ftp://ftp.gnu.org/pub/gnu/kawa
DISTFILES  = apache-maven-$(GARVERSION)-bin.tar.gz
DISTFILES += $(call admfiles,CSWkawa,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = kawa-(\d+(?:\.\d+)*).tar.gz

#CONFIGURE_SCRIPTS =
#BUILD_SCRIPTS =
#TEST_SCRIPTS =
#INSTALL_SCRIPTS = common

include gar/category.mk

#install-common:
#	mkdir -p $(DESTDIR)/opt/csw/bin
#	rm -rf $(DESTDIR)/opt/csw/share/maven2
#	mkdir -p $(DESTDIR)/opt/csw/share/maven2
#	cp -r $(WORKDIR)/apache-maven-$(GARVERSION)/ $(DESTDIR)/opt/csw/share/maven2/home
#	cp $(WORKDIR)/bin-mvn $(DESTDIR)/opt/csw/bin/mvn
#	chmod +x $(DESTDIR)/opt/csw/bin/mvn
#	$(MAKECOOKIE)
