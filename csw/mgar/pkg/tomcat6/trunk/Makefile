NAME = tomcat6
VERSION = 6.0.43
GARTYPE = v2

DESCRIPTION  =  Apache Jakarta Tomcat 6 Servlet/JSP Container
define BLURB
Apache Tomcat is the servlet container that is used in the official Reference Implementation for the Java Servlet and JavaServer Pages technologies. The Java Servlet and JavaServer Pages specifications are developed by Sun under the Java Community Process.
endef

VENDOR_URL = http://tomcat.apache.org/
MASTER_SITES += http://mirror.dkd.de/apache/tomcat/tomcat-6/v$(VERSION)/bin/
DISTNAME = apache-tomcat-$(VERSION)
DISTFILES += $(DISTNAME).tar.gz
DISTFILES += cswusergroup
DISTFILES += cswtomcat6

# Otherwise we copy .git into the package
NOGITPATCH = 1

PACKAGES += CSWtomcat6
SPKG_DESC_CSWtomcat6 = Apache Jakarta Tomcat 6 Servlet/JSP Container
# PKGFILES is catchall
ARCHALL_CSWtomcat6 = 1

PACKAGES += CSWlibtcnative1-0
SPKG_DESC_CSWlibtcnative1-0 = Tomcat Native Java library
PKGFILES_CSWlibtcnative1-0 += $(call pkgfiles_lib,libtcnative-1.so)
RUNTIME_DEP_PKGS_CSWlibtcnative1-0 += CSWlibapr1-0
RUNTIME_DEP_PKGS_CSWlibtcnative1-0 += CSWlibssl1-0-0

PACKAGES += CSWlibtcnative-dev
SPKG_DESC_CSWlibtcnative-dev = Development files for Tomcat Native Java library
# The .so *must* go into the library package as this name id dlopen'ed by java
PKGFILES_DEVEL_SHAREDLIBLINK =
CHECKPKG_OVERRIDES_CSWlibtcnative1-0 += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/libtcnative-1.so
PKGFILES_CSWlibtcnative-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibtcnative-dev += CSWlibtcnative1-0

LICENSE = LICENSE

CONFIGURE_SCRIPTS = $(WORKSRC)/bin/tomcat-native-1.1.32-src/jni/native/configure
BUILD_SCRIPTS = $(WORKSRC)/bin/tomcat-native-1.1.32-src/jni/native/Makefile
TEST_SCRIPTS =
INSTALL_SCRIPTS += tomcat
INSTALL_SCRIPTS += $(WORKSRC)/bin/tomcat-native-1.1.32-src/jni/native/Makefile

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --with-apr=$(bindir)/apr-1-config
CONFIGURE_ARGS += --with-ssl=$(prefix)
CONFIGURE_ARGS += --with-java-home=/usr/jdk1.6.0_20

INITSMF = /etc/opt/csw/init.d/csw$(NAME)
USERGROUP = /etc/opt/csw/pkg/$(NAME)/cswusergroup
PRESERVECONF = /etc/opt/csw/$(NAME)/conf/.*

PROTOTYPE_MODIFIERS     = varuser etcperm
PROTOTYPE_FILES_varuser = /var/opt/csw/$(NAME)/.*
PROTOTYPE_USER_varuser  = tomcat
PROTOTYPE_GROUP_varuser = tomcat
PROTOTYPE_CLASS_varuser = ugfiles
PROTOTYPE_FILES_etcperm = /etc/opt/csw/$(NAME)/conf/.*\.CSW
PROTOTYPE_PERMS_etcperm = 0640
PROTOTYPE_USER_etcperm  = tomcat
PROTOTYPE_GROUP_etcperm = tomcat

MIGRATE_SOURCE_DIR = /opt/csw/etc/$(NAME)/conf
MIGRATE_DEST_DIR = /etc/opt/csw/$(NAME)/conf
MIGRATE_FILES_CSWtomcat6 += catalina.policy
MIGRATE_FILES_CSWtomcat6 += catalina.properties
MIGRATE_FILES_CSWtomcat6 += context.xml
MIGRATE_FILES_CSWtomcat6 += logging.properties
MIGRATE_FILES_CSWtomcat6 += server.xml
MIGRATE_FILES_CSWtomcat6 += tomcat-users.xml
MIGRATE_FILES_CSWtomcat6 += web.xml

include gar/category.mk

post-extract:
	#( for i in temp work logs conf ; do  find $(WORKDIR)/$(DISTNAME)/$$i -type d -exec chmod 0750 {} \;  ; find $(WORKDIR)/$(DISTNAME)/$$i -type f -exec chmod 0640 {} \; ; done )
	cd $(WORKSRC)/bin && gtar zxf tomcat-native.tar.gz
	@$(MAKECOOKIE)

install-tomcat:
	mkdir -p $(DESTDIR)/etc/opt/csw/init.d
	mkdir -p $(DESTDIR)/etc/opt/csw/pkg/$(NAME)
	mkdir -p $(DESTDIR)/etc/opt/csw/$(NAME)
	mkdir -p $(DESTDIR)/opt/csw/etc/$(NAME)
	mkdir -p $(DESTDIR)/var/opt/csw/$(NAME)
	mkdir -p $(DESTDIR)/opt/csw/share
	cp -fr $(WORKSRC) $(DESTDIR)/opt/csw/share/$(NAME)
	@# The native library stuff goes into another package
	rm -rf $(DESTDIR)/opt/csw/share/$(NAME)/bin/tomcat-native-1.1.32-src
	cp -fr $(FILEDIR)/csw$(NAME) $(DESTDIR)/etc/opt/csw/init.d
	mv $(DESTDIR)/opt/csw/share/$(NAME)/conf $(DESTDIR)/etc/opt/csw/$(NAME)/conf
	mv $(DESTDIR)/opt/csw/share/$(NAME)/logs $(DESTDIR)/var/opt/csw/$(NAME)
	mv $(DESTDIR)/opt/csw/share/$(NAME)/work $(DESTDIR)/var/opt/csw/$(NAME)
	mv $(DESTDIR)/opt/csw/share/$(NAME)/temp $(DESTDIR)/var/opt/csw/$(NAME)
	rm $(DESTDIR)/var/opt/csw/tomcat6/temp/safeToDelete.tmp
	ln -s ../../../../etc/opt/csw/$(NAME)/conf $(DESTDIR)/opt/csw/share/$(NAME)/conf
	ln -s ../../../../var/opt/csw/$(NAME)/logs $(DESTDIR)/opt/csw/share/$(NAME)/logs
	ln -s ../../../../var/opt/csw/$(NAME)/work $(DESTDIR)/opt/csw/share/$(NAME)/work
	ln -s ../../../../var/opt/csw/$(NAME)/temp $(DESTDIR)/opt/csw/share/$(NAME)/temp
	ginstall -m 644 $(FILEDIR)/cswusergroup $(DESTDIR)/etc/opt/csw/pkg/$(NAME)
	cd $(WORKSRC)/bin/tomcat-native-1.1.32-src/jni/native && /usr/bin/env -i $(INSTALL_ENV) gmake $(INSTALL_ARGS)
	@$(MAKECOOKIE)

