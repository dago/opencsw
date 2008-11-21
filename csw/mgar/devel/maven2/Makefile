GARNAME = maven2
GARVERSION = 2.0.8
CATEGORIES = devel
GARCH = all

DESCRIPTION = Java software project management and comprehension tool
define BLURB
Maven is a software project management and comprehension tool. Based on the concept of a project object model (POM), Maven can manage a project's build, reporting and documentation from a central piece of information. 

Maven's primary goal is to allow a developer to comprehend the complete state of a development effort in the shortest period of time. In order to attain this goal there are several areas of concern that Maven attempts to deal with: 

   * Making the build process easy
   * Providing a uniform build system
   * Providing quality project information
   * Providing guidelines for best practices development
   * Allowing transparent migration to new features
endef

MASTER_SITES = http://www.powertech.no/apache/dist/maven/binaries
DISTFILES  = apache-maven-$(GARVERSION)-bin.tar.gz
DISTFILES += $(call admfiles,CSWmaven2,)
DISTFILES += bin-mvn

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = common

include ../category.mk

install-common:
	mkdir -p $(DESTDIR)/opt/csw/bin
	mkdir -p $(DESTDIR)/opt/csw/share
	rm -rf $(DESTDIR)/opt/csw/share/apache-maven-$(GARVERSION)
	cp -r $(WORKDIR)/apache-maven-$(GARVERSION)/ $(DESTDIR)/opt/csw/share/maven2
	cp $(WORKDIR)/bin-mvn $(DESTDIR)/opt/csw/bin/mvn
	chmod +x $(DESTDIR)/opt/csw/bin/mvn
	$(MAKECOOKIE)
