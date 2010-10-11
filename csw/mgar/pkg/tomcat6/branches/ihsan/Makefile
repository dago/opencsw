GARNAME      = tomcat6
GARVERSION   = 6.0.29
CATEGORIES   = server

DESCRIPTION  =  Apache Jakarta Tomcat 6 Servlet/JSP Container
define BLURB
Apache Tomcat is the servlet container that is used in the official Reference Implementation for the Java Servlet and JavaServer Pages technologies. The Java Servlet and JavaServer Pages specifications are developed by Sun under the Java Community Process.
endef

MASTER_SITES  = http://tomcat.apache.org/
UPSTREAM_MASTER_SITES  =  http://mir2.ovh.net/ftp.apache.org/dist/jakarta/tomcat-6/v$(GARVERSION)/bin/
DISTFILES     = apache-tomcat-$(GARVERSION).tar.gz
PKGDIST       = apache-tomcat-$(GARVERSION).tar.gz
DISTFILES    += cswusergroup
DISTFILES    += cswtomcat6
DISTFILES    += LICENSE

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = v(\d+(?:\.\d+)*)

PACKAGES = CSWtomcat6
CATALOGNAME = tomcat6
LICENSE = LICENSE
ARCHALL = 1

CONFIGURE_SCRIPTS = none
BUILD_SCRIPTS     = none
TEST_SCRIPTS	  = none
INSTALL_SCRIPTS   = tomcat
prefix            = /

INITSMF = /etc/opt/csw/init.d/csw$(GARNAME)
USERGROUP = /etc/opt/csw/pkg/$(GARNAME)/cswusergroup
PRESERVECONF = /etc/opt/csw/$(GARNAME)/conf/.*

PROTOTYPE_MODIFIERS     = varuser etcperm
PROTOTYPE_FILES_varuser = /var/opt/csw/$(GARNAME)/.*
PROTOTYPE_USER_varuser  = tomcat
PROTOTYPE_GROUP_varuser = tomcat
PROTOTYPE_FILES_etcperm = /etc/opt/csw/$(GARNAME)/conf/.*\.CSW
PROTOTYPE_PERMS_etcperm = 0640
PROTOTYPE_USER_etcperm  = tomcat
PROTOTYPE_GROUP_etcperm = tomcat

MIGRATE_SOURCE_DIR = /opt/csw/etc/$(GARNAME)/conf
MIGRATE_DEST_DIR = /etc/opt/csw/$(GARNAME)/conf
MIGRATE_FILES  = catalina.policy
MIGRATE_FILES += catalina.properties
MIGRATE_FILES += context.xml
MIGRATE_FILES += logging.properties
MIGRATE_FILES += server.xml
MIGRATE_FILES += tomcat-users.xml
MIGRATE_FILES += web.xml

include gar/category.mk

configure-none:
	@$(MAKECOOKIE)

test-none:
	@$(MAKECOOKIE)

build-none:
	@$(MAKECOOKIE)

post-extract:
	( mv $(WORKDIR)/apache-tomcat-$(GARVERSION) $(WORKDIR)/$(DISTNAME) )
	( for i in temp work logs conf ; do  find $(WORKDIR)/$(DISTNAME)/$$i -type d -exec chmod 0750 {} \;  ; find $(WORKDIR)/$(DISTNAME)/$$i -type f -exec chmod 0640 {} \; ; done )
	@$(MAKECOOKIE)

install-tomcat:
	( mkdir -p $(DESTDIR)/etc/opt/csw/init.d )
	( mkdir -p $(DESTDIR)/etc/opt/csw/pkg/$(GARNAME) )
	( mkdir -p $(DESTDIR)/etc/opt/csw/$(GARNAME) )
	( mkdir -p $(DESTDIR)/opt/csw/etc/$(GARNAME) )
	( mkdir -p $(DESTDIR)/var/opt/csw/$(GARNAME) )
	( mkdir -p $(DESTDIR)/opt/csw/share )
	( cp -fr $(WORKDIR)/apache-tomcat-$(GARVERSION) $(DESTDIR)/opt/csw/share/$(GARNAME) )
	( cp -fr $(FILEDIR)/csw$(GARNAME) $(DESTDIR)/etc/opt/csw/init.d )
	( mv     $(DESTDIR)/opt/csw/share/$(GARNAME)/conf $(DESTDIR)/etc/opt/csw/$(GARNAME)/conf )
	( mv     $(DESTDIR)/opt/csw/share/$(GARNAME)/logs $(DESTDIR)/var/opt/csw/$(GARNAME) )
	( mv     $(DESTDIR)/opt/csw/share/$(GARNAME)/work $(DESTDIR)/var/opt/csw/$(GARNAME) )
	( mv     $(DESTDIR)/opt/csw/share/$(GARNAME)/temp $(DESTDIR)/var/opt/csw/$(GARNAME) )
	( ln -s /etc/opt/csw/$(GARNAME)/conf $(DESTDIR)/opt/csw/share/$(GARNAME)/conf )
	( ln -s /var/opt/csw/$(GARNAME)/logs $(DESTDIR)/opt/csw/share/$(GARNAME)/logs )
	( ln -s /var/opt/csw/$(GARNAME)/work $(DESTDIR)/opt/csw/share/$(GARNAME)/work )
	( ln -s /var/opt/csw/$(GARNAME)/temp $(DESTDIR)/opt/csw/share/$(GARNAME)/temp )
	( ginstall -m 644 $(FILEDIR)/cswusergroup $(DESTDIR)/etc/opt/csw/pkg/$(GARNAME) )
	@$(MAKECOOKIE)

