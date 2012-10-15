NAME      = tomcat5
VERSION   = 5.5.36
CATEGORIES   = server
GARTYPE = v2

DESCRIPTION  =  Apache Jakarta Tomcat 5.5 Servlet/JSP Container
define BLURB
Apache Tomcat is the servlet container that is used in the official Reference Implementation for the Java Servlet and JavaServer Pages technologies. The Java Servlet and JavaServer Pages specifications are developed by Sun under the Java Community Process.
endef

VENDOR_URL = http://tomcat.apache.org/
MASTER_SITES  =  http://mir2.ovh.net/ftp.apache.org/dist/jakarta/tomcat-5/v$(VERSION)/bin/
UPSTREAM_MASTER_SITES  =  http://mir2.ovh.net/ftp.apache.org/dist/jakarta/tomcat-5/v$(VERSION)/bin/
DISTFILES     = apache-tomcat-$(VERSION).tar.gz
PKGDIST       = apache-tomcat-$(VERSION).tar.gz
DISTFILES    += cswusergroup
DISTFILES    += cswtomcat5
DISTFILES    += LICENSE

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = v(\d+(?:\.\d+)*)

PACKAGES = CSWtomcat5
CATALOGNAME = tomcat5
LICENSE = LICENSE
ARCHALL = 1

CONFIGURE_SCRIPTS = none
BUILD_SCRIPTS     = none
TEST_SCRIPTS	  = none
INSTALL_SCRIPTS   = tomcat
prefix            = /

INITSMF = /etc/opt/csw/init.d/csw$(NAME)
USERGROUP = /etc/opt/csw/pkg/$(NAME)/cswusergroup

#PRESERVECONF = /etc/opt/csw/$(NAME)/conf/.*
PRESERVECONF = /etc/opt/csw/$(NAME)/conf/catalina.policy
PRESERVECONF += /etc/opt/csw/$(NAME)/conf/catalina.properties
PRESERVECONF += /etc/opt/csw/$(NAME)/conf/Catalina/localhost/host-manager.xml
PRESERVECONF += /etc/opt/csw/$(NAME)/conf/Catalina/localhost/manager.xml
PRESERVECONF += /etc/opt/csw/$(NAME)/conf/context.xml
PRESERVECONF += /etc/opt/csw/$(NAME)/conf/logging.properties
PRESERVECONF += /etc/opt/csw/$(NAME)/conf/server-minimal.xml
PRESERVECONF += /etc/opt/csw/$(NAME)/conf/server.xml
PRESERVECONF += /etc/opt/csw/$(NAME)/conf/tomcat-users.xml
PRESERVECONF += /etc/opt/csw/$(NAME)/conf/web.xml


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
MIGRATE_FILES  = catalina.policy
MIGRATE_FILES += catalina.properties
MIGRATE_FILES += context.xml
MIGRATE_FILES += logging.properties
MIGRATE_FILES += server.xml
MIGRATE_FILES += server-minimal.xml
MIGRATE_FILES += tomcat-users.xml
MIGRATE_FILES += web.xml
MIGRATE_FILES += Catalina/localhost/host-manager.xml
MIGRATE_FILES += Catalina/localhost/manager.xml

# Reviewed and fine to override
CHECKPKG_OVERRIDES_CSWtomcat5 += file-with-bad-content|/usr/local|root/opt/csw/share/tomcat5/RUNNING.txt
CHECKPKG_OVERRIDES_CSWtomcat5 += file-with-bad-content|/usr/local|root/opt/csw/share/tomcat5/server/webapps/manager/manager-howto.html
CHECKPKG_OVERRIDES_CSWtomcat5 += file-with-bad-content|/usr/local|root/opt/csw/share/tomcat5/webapps/tomcat-docs/virtual-hosting-howto.html
CHECKPKG_OVERRIDES_CSWtomcat5 += file-with-bad-content|/usr/local|root/opt/csw/share/tomcat5/webapps/tomcat-docs/manager-howto.html
CHECKPKG_OVERRIDES_CSWtomcat5 += file-with-bad-content|/usr/local|root/opt/csw/share/tomcat5/webapps/tomcat-docs/ssl-howto.html
CHECKPKG_OVERRIDES_CSWtomcat5 += file-with-bad-content|/usr/local|root/opt/csw/share/tomcat5/webapps/tomcat-docs/printer/ssl-howto.html
CHECKPKG_OVERRIDES_CSWtomcat5 += file-with-bad-content|/usr/local|root/opt/csw/share/tomcat5/webapps/tomcat-docs/printer/manager-howto.html
CHECKPKG_OVERRIDES_CSWtomcat5 += file-with-bad-content|/usr/local|root/opt/csw/share/tomcat5/webapps/tomcat-docs/printer/virtual-hosting-howto.html
CHECKPKG_OVERRIDES_CSWtomcat5 += file-with-bad-content|/usr/local|root/opt/csw/share/tomcat5/webapps/tomcat-docs/appdev/processes.html
CHECKPKG_OVERRIDES_CSWtomcat5 += file-with-bad-content|/usr/local|root/opt/csw/share/tomcat5/webapps/tomcat-docs/appdev/printer/processes.html
CHECKPKG_OVERRIDES_CSWtomcat5 += file-with-bad-content|/usr/share|root/opt/csw/share/tomcat5/webapps/tomcat-docs/building.html
CHECKPKG_OVERRIDES_CSWtomcat5 += file-with-bad-content|/usr/share|root/opt/csw/share/tomcat5/webapps/tomcat-docs/printer/building.html


include gar/category.mk

configure-none:
	@$(MAKECOOKIE)

test-none:
	@$(MAKECOOKIE)

build-none:
	@$(MAKECOOKIE)

post-extract:
	( mv $(WORKDIR)/apache-tomcat-$(VERSION) $(WORKDIR)/$(DISTNAME) )
	( for i in temp work logs conf ; do  find $(WORKDIR)/$(DISTNAME)/$$i -type d -exec chmod 0750 {} \;  ; find $(WORKDIR)/$(DISTNAME)/$$i -type f -exec chmod 0640 {} \; ; done )
	@$(MAKECOOKIE)

install-tomcat:
	( mkdir -p $(DESTDIR)/etc/opt/csw/init.d )
	( mkdir -p $(DESTDIR)/etc/opt/csw/pkg/$(NAME) )
	( mkdir -p $(DESTDIR)/etc/opt/csw/$(NAME) )
	( mkdir -p $(DESTDIR)/opt/csw/etc/$(NAME) )
	( mkdir -p $(DESTDIR)/var/opt/csw/$(NAME) )
	( mkdir -p $(DESTDIR)/opt/csw/share )
	( cp -fr $(WORKDIR)/apache-tomcat-$(VERSION) $(DESTDIR)/opt/csw/share/$(NAME) )
	( cp -fr $(FILEDIR)/csw$(NAME) $(DESTDIR)/etc/opt/csw/init.d )
	( mv     $(DESTDIR)/opt/csw/share/$(NAME)/conf $(DESTDIR)/etc/opt/csw/$(NAME)/conf )
	( mv     $(DESTDIR)/opt/csw/share/$(NAME)/logs $(DESTDIR)/var/opt/csw/$(NAME) )
	( mv     $(DESTDIR)/opt/csw/share/$(NAME)/work $(DESTDIR)/var/opt/csw/$(NAME) )
	( mv     $(DESTDIR)/opt/csw/share/$(NAME)/temp $(DESTDIR)/var/opt/csw/$(NAME) )
	( rm $(DESTDIR)/var/opt/csw/tomcat5/temp/bugzilla37035-safeToDelete.tmp )
	( ln -s ../../../../etc/opt/csw/$(NAME)/conf $(DESTDIR)/opt/csw/share/$(NAME)/conf )
	( ln -s ../../../../var/opt/csw/$(NAME)/logs $(DESTDIR)/opt/csw/share/$(NAME)/logs )
	( ln -s ../../../../var/opt/csw/$(NAME)/work $(DESTDIR)/opt/csw/share/$(NAME)/work )
	( ln -s ../../../../var/opt/csw/$(NAME)/temp $(DESTDIR)/opt/csw/share/$(NAME)/temp )
	( ginstall -m 644 $(FILEDIR)/cswusergroup $(DESTDIR)/etc/opt/csw/pkg/$(NAME) )
	@$(MAKECOOKIE)

