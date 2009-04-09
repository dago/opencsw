GARNAME = maven2
GARVERSION = 2.0.10
CATEGORIES = devel
GARCH = all

DESCRIPTION = Java software project management and comprehension tool
define BLURB
Maven is a software project management and comprehension tool. Based on
the concept of a project object model (POM), Maven can manage a
project's build, reporting and documentation from a central
piece of information.

Maven's primary goal is to allow a developer to comprehend the complete
state of a development effort in the shortest period of time. In order
to attain this goal there are several areas of conce rn that Maven
attempts to deal with:

   * Making the build process easy
   * Providing a uniform build system
   * Providing quality project information
   * Providing guidelines for best practices development
   * Allowing transparent migration to new features
endef

MASTER_SITES = http://www.powertech.no/apache/dist/maven/binaries/
DISTFILES  = apache-maven-$(GARVERSION)-bin.tar.gz
DISTFILES += $(call admfiles,CSWmaven2,)
DISTFILES += bin-mvn

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = apache-maven-(\d+(?:\.\d+)*)-bin.tar.gz

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = common

include gar/category.mk

install-common:
	mkdir -p $(DESTDIR)/opt/csw/bin
	rm -rf $(DESTDIR)/opt/csw/share/maven2
	mkdir -p $(DESTDIR)/opt/csw/share/maven2
	cp -r $(WORKDIR)/apache-maven-$(GARVERSION)/ $(DESTDIR)/opt/csw/share/maven2/home
	cp $(WORKDIR)/bin-mvn $(DESTDIR)/opt/csw/bin/mvn
	chmod +x $(DESTDIR)/opt/csw/bin/mvn
	$(MAKECOOKIE)
