NAME      = tomcat4
VERSION   = 4.1.37
GARTYPE = v1
CATEGORIES   = server

DESCRIPTION  =  Apache Jakarta Tomcat 4 Servlet/JSP Container
define BLURB
Apache Tomcat is the servlet container that is used in the official Reference Implementation for the Java Servlet and JavaServer Pages technologies. The Java Servlet and JavaServer Pages specifications are developed by Sun under the Java Community Process.
endef

UPSTREAM_MASTER_SITES  =  http://mir2.ovh.net/ftp.apache.org/dist/jakarta/tomcat-4/
MASTER_SITES  =  http://mir2.ovh.net/ftp.apache.org/dist/jakarta/tomcat-4/v$(VERSION)/bin/
DISTFILES     = apache-tomcat-$(VERSION).tar.gz
PKGDIST       = apache-tomcat-$(VERSION).tar.gz
DISTFILES    += CSWtomcat4.gspec CSWtomcat4.prototype CSWtomcat4.depend preremove postinstall preinstall checkinstall space i.smfno i.smfyes svc-tomcat4 tomcat4.xml tomcat4 cswtomcat4
# DISTFILES    += $(call admfiles, CSWtomcat4, depend )

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = v(\d+(?:\.\d+)*)

CONFIGURE_SCRIPTS = none
BUILD_SCRIPTS     = none
TEST_SCRIPTS	  = none
INSTALL_SCRIPTS   = tomcat
prefix            = /

include gar/category.mk

configure-none:
	@$(MAKECOOKIE)

test-none:
	@$(MAKECOOKIE)

build-none:
	@$(MAKECOOKIE)

post-extract:
	( mv $(WORKDIR)/apache-tomcat-$(VERSION) $(WORKDIR)/$(DISTNAME) )
	( OLDDIR=`pwd` && cd $(WORKDIR)/$(DISTNAME)/conf && for i in `find . -type f` ; do mv $$i $$i.CSW ; done && cd $$OLDDIR )
	( for i in temp work logs conf ; do  find $(WORKDIR)/$(DISTNAME)/$$i -type d -exec chmod 0750 {} \;  ; find $(WORKDIR)/$(DISTNAME)/$$i -type f -exec chmod 0640 {} \; ; done )
	@$(MAKECOOKIE)

install-tomcat:
	( mkdir -p $(DESTDIR)/etc/init.d )
	( mkdir -p $(DESTDIR)/etc/opt/csw )
	( mkdir -p $(DESTDIR)/etc/rc0.d )
	( mkdir -p $(DESTDIR)/etc/rc1.d )
	( mkdir -p $(DESTDIR)/etc/rc2.d )
	( mkdir -p $(DESTDIR)/etc/rc3.d )
	( mkdir -p $(DESTDIR)/etc/rcS.d )
	( mkdir -p $(DESTDIR)/opt/csw/etc/$(NAME) )
	( mkdir -p $(DESTDIR)/var/opt/csw/$(NAME) )
	( mkdir -p $(DESTDIR)/opt/csw/share )
	( mkdir -p $(DESTDIR)/etc/opt/csw )
	( cp -fr $(WORKDIR)/$(DISTNAME) $(DESTDIR)/opt/csw/share/$(NAME) )
	( cp -fr $(FILEDIR)/$(NAME) $(DESTDIR)/etc/opt/csw/$(NAME) )
	( cp -fr $(FILEDIR)/csw$(NAME) $(DESTDIR)/etc/init.d )
	( mv     $(DESTDIR)/opt/csw/share/$(NAME)/conf $(DESTDIR)/opt/csw/etc/$(NAME)/conf )
	( mv     $(DESTDIR)/opt/csw/share/$(NAME)/logs $(DESTDIR)/var/opt/csw/$(NAME) )
	( mv     $(DESTDIR)/opt/csw/share/$(NAME)/work $(DESTDIR)/var/opt/csw/$(NAME) )
	( mv     $(DESTDIR)/opt/csw/share/$(NAME)/temp $(DESTDIR)/var/opt/csw/$(NAME) )
	( ln -s /opt/csw/etc/$(NAME)/conf $(DESTDIR)/opt/csw/share/$(NAME)/conf )
	( ln -s /var/opt/csw/$(NAME)/logs $(DESTDIR)/opt/csw/share/$(NAME)/logs )
	( ln -s /var/opt/csw/$(NAME)/work $(DESTDIR)/opt/csw/share/$(NAME)/work )
	( ln -s /var/opt/csw/$(NAME)/temp $(DESTDIR)/opt/csw/share/$(NAME)/temp )
	( ln -s /etc/init.d/cswtomcat4 $(DESTDIR)/etc/rc0.d/K17$(NAME) )
	( ln -s /etc/init.d/cswtomcat4 $(DESTDIR)/etc/rc1.d/K17$(NAME) )
	( ln -s /etc/init.d/cswtomcat4 $(DESTDIR)/etc/rc2.d/K17$(NAME) )
	( ln -s /etc/init.d/cswtomcat4 $(DESTDIR)/etc/rc3.d/S51$(NAME) )
	( ln -s /etc/init.d/cswtomcat4 $(DESTDIR)/etc/rcS.d/K17$(NAME) )
	@$(MAKECOOKIE)



