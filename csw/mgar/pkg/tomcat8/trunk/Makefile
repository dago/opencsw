NAME = apache-tomcat
VERSION = 8.0.23

DESCRIPTION = Apache Jakarta Tomcat 8 Servlet/JSP Container

MASTER_SITES = http://ftp.fau.de/apache/tomcat/tomcat-8/v$(VERSION)/bin/
DISTFILES += $(DISTNAME).tar.gz
DISTFILES += cswusergroup
DISTFILES += cswtomcat8
#DISTFILES    += LICENSE
NOGITPATCH    = 1

VENDOR_URL = http://tomcat.apache.org/

PACKAGES += CSWtomcat8
SPKG_DESC_CSWtomcat8 = Apache Jakarta Tomcat 8 Servlet/JSP Container
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWtomcat += CSWjre8
ARCHALL_CSWtomcat8 = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = tomcat

INITSMF = /etc/opt/csw/init.d/cswtomcat8
USERGROUP = /etc/opt/csw/pkg/CSWtomcat8/cswusergroup
PRESERVECONF = /etc/opt/csw/tomcat8/conf/.*

PROTOTYPE_MODIFIERS += varuser
PROTOTYPE_FILES_varuser = /var/opt/csw/tomcat8/.*
PROTOTYPE_USER_varuser  = tomcat
PROTOTYPE_GROUP_varuser = tomcat
PROTOTYPE_CLASS_varuser = ugfiles

PROTOTYPE_MODIFIERS += etcperm
PROTOTYPE_FILES_etcperm = /etc/opt/csw/tomcat8/conf/.*\.CSW
PROTOTYPE_PERMS_etcperm = 0640
PROTOTYPE_USER_etcperm  = tomcat
PROTOTYPE_GROUP_etcperm = tomcat

include gar/category.mk

xpost-extract:
	( for i in temp work logs conf ; do  find $(WORKSRC)/$$i -type d -exec chmod 0750 {} \;  ; find $(WORKSRC)/$$i -type f -exec chmod 0640 {} \; ; done )
	@$(MAKECOOKIE)

install-tomcat:
	mkdir -p $(DESTDIR)/etc/opt/csw/init.d
	mkdir -p $(DESTDIR)/etc/opt/csw/pkg/tomcat8
	mkdir -p $(DESTDIR)/etc/opt/csw/tomcat8
	mkdir -p $(DESTDIR)/opt/csw/etc/tomcat8
	mkdir -p $(DESTDIR)/var/opt/csw/tomcat8
	mkdir -p $(DESTDIR)/opt/csw/share
	cp -fr $(WORKDIR)/$(DISTNAME) $(DESTDIR)/opt/csw/share/tomcat8
	mv $(DESTDIR)/opt/csw/share/tomcat8/conf $(DESTDIR)/etc/opt/csw/tomcat8
	mv $(DESTDIR)/opt/csw/share/tomcat8/logs $(DESTDIR)/var/opt/csw/tomcat8
	mv $(DESTDIR)/opt/csw/share/tomcat8/work $(DESTDIR)/var/opt/csw/tomcat8
	mv $(DESTDIR)/opt/csw/share/tomcat8/temp $(DESTDIR)/var/opt/csw/tomcat8
	ln -s ../../../../etc/opt/csw/tomcat8/conf $(DESTDIR)/opt/csw/share/tomcat8/conf
	ln -s ../../../../var/opt/csw/tomcat8/logs $(DESTDIR)/opt/csw/share/tomcat8/logs
	ln -s ../../../../var/opt/csw/tomcat8/work $(DESTDIR)/opt/csw/share/tomcat8/work
	ln -s ../../../../var/opt/csw/tomcat8/temp $(DESTDIR)/opt/csw/share/tomcat8/temp
	rm $(DESTDIR)/var/opt/csw/tomcat8/temp/safeToDelete.tmp
	#cp -fr $(WORKDIR)/cswtomcat8 $(DESTDIR)/etc/opt/csw/init.d
	ginstall -m 644 $(WORKDIR)/cswusergroup $(DESTDIR)/etc/opt/csw/pkg/$(NAME)
	@$(MAKECOOKIE)

