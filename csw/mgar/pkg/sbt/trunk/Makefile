NAME = sbt
VERSION = 0.7.3
CATEGORIES = devel
GARTYPE = v2
ARCHALL = 1

DESCRIPTION = A build tool for Scala

VENDOR_URL   = http://code.google.com/p/simple-build-tool/
MASTER_SITES = http://simple-build-tool.googlecode.com/files/
DISTFILES  = sbt-launch-$(VERSION).jar
DISTFILES += sbt

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = sbt-launch-(\d+(?:\.\d+)*).jar

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_SCRIPTS = 
BUILD_SCRIPTS =
TEST_SCRIPTS = 
INSTALL_SCRIPTS =

include gar/category.mk

post-merge:
	mkdir -p $(PKGROOT)/opt/csw/share/doc/sbt/
	(cd $(PKGROOT)/opt/csw/share/doc/sbt; jar xfv $(abspath $(WORKDIR_FIRSTMOD))/sbt-launch-$(VERSION).jar LICENSE)
	mv $(PKGROOT)/opt/csw/share/doc/sbt/LICENSE $(PKGROOT)/opt/csw/share/doc/sbt/license
	ginstall -D $(WORKDIR_FIRSTMOD)/sbt $(PKGROOT)/opt/csw/bin/sbt
	ginstall -D $(WORKDIR_FIRSTMOD)/sbt-launch-$(VERSION).jar $(PKGROOT)/opt/csw/share/sbt/sbt-launch-$(VERSION).jar 
	ln -s sbt-launch-$(VERSION).jar $(PKGROOT)/opt/csw/share/sbt/sbt-launch.jar
	@$(MAKECOOKIE)
