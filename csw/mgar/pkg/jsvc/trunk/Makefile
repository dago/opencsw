# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = commons-daemon
VERSION = 1.0.15

DESCRIPTION = Jsvc is a set of libraries and applications for making Java applications run on UNIX more easily

MASTER_SITES += http://artfiles.org/apache.org//commons/daemon/source/
DISTNAME = $(NAME)-$(VERSION)-src
DISTFILES += $(DISTNAME).tar.gz
# Generated with
#   docbook2man jsvc.1.xml
# and then manually take out three lines after ".de URL" as it confuses nroff
DISTFILES += jsvc.1

VENDOR_URL = http://commons.apache.org/proper/commons-daemon/jsvc.html
LICENSE = LICENSE.txt

PACKAGES += CSWjsvc
SPKG_DESC_CSWjsvc = A set of libraries and applications for making Java applications run on UNIX more easily
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWjsvc += CSWjre8
# checkpkg cannot detect this
CHECKPKG_OVERRIDES_CSWjsvc += surplus-dependency|CSWjre8

# This is /usr/local/java
CHECKPKG_OVERRIDES_CSWjsvc += file-with-bad-content|/usr/local|root/opt/csw/bin/jsvc

WORKSRC = $(WORKDIR)/$(DISTNAME)/src/native/unix

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --with-java=$(prefix)/java/jdk/jdk8

# There is no testsuite
TEST_SCRIPTS =

# There is no "install" target
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	ginstall -D -m 0755 $(WORKSRC)/jsvc $(DESTDIR)$(bindir)/jsvc
	ginstall -D -m 0644 $(WORKDIR)/jsvc.1 $(DESTDIR)$(mandir)/man1/jsvc.1
	@$(MAKECOOKIE)
