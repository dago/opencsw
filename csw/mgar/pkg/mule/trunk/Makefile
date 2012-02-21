NAME = mule
VERSION = 3.2.1
GARTYPE = v2
CATEGORIES = server

DESCRIPTION = Java based lightweight enterprise service bus
define BLURB
  Lightweight enterprise service bus (ESB) and integration framework
endef

MASTER_SITES = http://www.mulesoft.org/
DISTNAME = $(NAME)-standalone-$(VERSION)
DISTFILES  = $(DISTNAME).tar.gz
DISTFILES += cswusergroup
DISTFILES += cswmule.xml
DISTFILES += cswmule
DISTFILES += CSWmule.postinstall

PATCHFILES += 0001-javapath.patch
PATCHFILES += 0001-runasusermule.patch
PATCHFILES += 0001-piddir.patch

PACKAGING_PLATFORMS +=  solaris10-sparc solaris10-i386

ARCHALL = 1

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

SPKG_CLASSES  = none cswinitsmf cswsampleconf cswusergroup ugfiles
INITSMF       = /etc/opt/csw/init.d/cswmule
PRESERVECONF  = /etc/opt/csw/mule/.*
USERGROUP     = /etc/opt/csw/pkg/CSWmule/cswusergroup

PROTOTYPE_MODIFIERS          = mule_ugfiles
MULE_UGFILES                 = /var/opt/csw/mule/logs /var/opt/csw/mule/pid
PROTOTYPE_FILES_mule_ugfiles = $(MULE_UGFILES)
PROTOTYPE_USER_mule_ugfiles  = mule
PROTOTYPE_GROUP_mule_ugfiles = mule
PROTOTYPE_CLASS_mule_ugfiles = ugfiles

install-custom:
	@ginstall -d $(DESTDIR)/opt/csw/$(NAME)
	@cp -rp $(WORKDIR)/$(DISTNAME)/* $(DESTDIR)/opt/csw/$(NAME)
	@ginstall -d $(DESTDIR)/var/opt/csw/mule
	@mv $(DESTDIR)/opt/csw/mule/logs $(DESTDIR)/var/opt/csw/mule
	@ln -s /var/opt/csw/mule/logs $(DESTDIR)/opt/csw/mule/logs
	@ginstall -d $(DESTDIR)/etc/opt/csw
	@mv $(DESTDIR)/opt/csw/mule/conf $(DESTDIR)/etc/opt/csw/mule
	@ln -s /etc/opt/csw/mule $(DESTDIR)/opt/csw/mule/conf
	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	@ginstall -m 755 $(FILEDIR)/cswmule $(DESTDIR)/etc/opt/csw/init.d/cswmule
	@ginstall -d $(DESTDIR)/var/opt/csw/svc/manifest/application
	@ginstall -m 644 $(FILEDIR)/cswmule.xml $(DESTDIR)/var/opt/csw/svc/manifest/application/cswmule.xml
	@ginstall -d $(DESTDIR)/etc/opt/csw/pkg/CSWmule
	@ginstall -m 644 $(FILEDIR)/cswusergroup $(DESTDIR)/etc/opt/csw/pkg/CSWmule/cswusergroup
	@ginstall -d $(DESTDIR)/var/opt/csw/mule/pid
	@$(MAKECOOKIE)

include gar/category.mk

