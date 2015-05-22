# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = clojure
VERSION = 1.6.0
GARTYPE = v2

DESCRIPTION = A dynamic programming language that targets the Java Virtual Machine

MASTER_SITES = http://repo1.maven.org/maven2/org/clojure/clojure/1.6.0/
DISTFILES += $(DISTNAME).zip
DISTFILES += clojure
EXPANDVARS += clojure

VENDOR_URL = http://clojure.org
LICENSE = readme.txt

PACKAGES += CSWclojure
SPKG_DESC_CSWclojure = A dynamic programming language that targets the Java Virtual Machine
# PKGFILES is catchall
ARCHALL_CSWclojure = 1
RUNTIME_DEP_PKGS_CSWclojure += CSWjre8
# checkpkg cannot trace this dependency
CHECKPKG_OVERRIDES_CSWclojure += surplus-dependency|CSWjre8

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	ginstall -D -m 0644 $(WORKSRC)/clojure-$(VERSION).jar $(DESTDIR)$(sharedstatedir)/java/clojure-$(VERSION).jar
	ln -s clojure-$(VERSION).jar $(DESTDIR)$(sharedstatedir)/java/clojure.jar
	ginstall -D -m 0755 $(WORKDIR)/clojure $(DESTDIR)$(bindir)/clojure
	@$(MAKECOOKIE)
