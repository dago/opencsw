# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = ant
VERSION = 1.8.4
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = Apache Ant is Java Build Tool 
define BLURB
  Long description
endef

MASTER_SITES = http://ftp.halifax.rwth-aachen.de/apache//ant/source/
MASTER_SITES += http://www.junit.org
MASTER_SITES += http://search.maven.org/remotecontent?filepath=org/mod4j/org/junit/3.8.2/
DISTNAME = apache-$(NAME)-$(VERSION)
DISTFILES  = $(DISTNAME)-src.tar.gz
DISTFILES  += junit-3.8.2.jar

NOGITPATCH = 1

REINPLACE_USRLOCAL = manual/*.*

PACKAGING_PLATFORMS += solaris10x
RUNTIME_DEPENDENCY_CSWant += CSWjunit

ARCHALL_CSWant = 1
ARCHALL_CSWantdoc = 1

PACKAGES += CSWant
SPKG_DESC_CSWant = $(DESCRIPTION), base
# not really 
RUNTIME_DEP_PKGS_CSWant += CSWpython
RUNTIME_DEP_PKGS_CSWant += CSWperl
# usr share is ok
CHECKPKG_OVERRIDES_CSWant += file-with-bad-content|/usr/share|root/opt/csw/share/java/ant/bin/ant
# no, the license is there
CHECKPKG_OVERRIDES_CSWant += license-missing|/opt/csw/share/doc/ant/license

PACKAGES += CSWantdoc
SPKG_DESC_CSWantdoc = $(DESCRIPTION), docs
PKGFILES_CSWantdoc += $(PKGFILES_DOC)

CONFIGURE_SCRIPTS = 
TEST_SCRIPTS = 
BUILD_SCRIPTS = ant
INSTALL_SCRIPTS = ant
EXTRA_BUILD_ENV += JAVA_HOME=/usr/jdk/instances/jdk1.6.0 
EXTRA_BUILD_ENV += ANT_OPTS="-Dhttp.proxyHost=proxy -Dhttp.proxyPort=3128"

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

pre-build-modulated:
	(cd $(WORKSRC)/lib/optional && jar -xf ../../../junit-3.8.2.jar)
	@$(MAKECOOKIE)

build-ant: 
	(cd $(WORKSRC) && $(BUILD_ENV) sh build.sh dist	)
	@$(MAKECOOKIE)

ant_home = $(datadir)/java/$(NAME)
install-ant:
	ginstall -d -m755 $(DESTDIR)/$(bindir)
	ginstall -d -m755 $(DESTDIR)/$(datadir)/java
	ginstall -d -m755 $(DESTDIR)/$(ant_home)/bin
	ginstall -d -m755 $(DESTDIR)/$(docdir)/$(NAME)
	gcp -Rp $(WORKSRC)/$(DISTNAME)/etc $(DESTDIR)/$(ant_home)
	find $(WORKSRC)/$(DISTNAME)/bin -type f -a ! -name \*.bat -a ! -name \*.cmd -exec ginstall -m755 {} $(DESTDIR)/$(ant_home)/bin \;
	ln -s $(DESTDIR)/$(ant_home)/bin/ant $(DESTDIR)/$(bindir)
	gsed -i -e '/^ANT_LIB/s/lib/share\/java/' $(DESTDIR)/$(ant_home)/bin/ant
	ginstall -m644 $(WORKSRC)/$(DISTNAME)/lib/*.jar $(DESTDIR)/$(datadir)/java
	gcp -Rp $(WORKSRC)/$(DISTNAME)/manual $(DESTDIR)/$(docdir)/$(NAME)
	ginstall -m644 $(WORKSRC)/$(DISTNAME)/LICENSE $(DESTDIR)/$(docdir)/$(NAME)
	ginstall -m644 $(WORKSRC)/$(DISTNAME)/NOTICE $(DESTDIR)/$(docdir)/$(NAME)
	$(MAKECOOKIE)

