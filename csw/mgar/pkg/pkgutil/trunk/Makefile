GARNAME = pkgutil
GARVERSION = 1.2
CATEGORIES = utils

DESCRIPTION = install Solaris packages the easy way
define BLURB
	Pkgutil, written in Perl and licensed under GPL, is a tool to make 
	installation of packages in Solaris easier. It handles package 
	dependencies so all required packages are installed before the desired 
	package automatically.
endef

MASTER_SITES = http://mirror.csw.baltic-online.de/testing/pkgutil/
DISTFILES  = $(GARNAME)
DISTFILES += $(GARNAME).conf
DISTFILES += admin
DISTFILES += bldcat
DISTFILES += chkcat
DISTFILES += readme
DISTFILES += wget-i386
DISTFILES += wget-sparc
DISTFILES += $(call admfiles,CSWpkgutil,preremove postinstall prototype)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

WORKSRC = $(WORKDIR)
SPKG_SOURCEURL = http://wiki.opencsw.org/pkgutil/

install-custom:
	@echo " ==> Installing $(GARNAME) (custom)"
	@rm -rf $(DESTDIR)
	@ginstall -d $(DESTDIR)/etc/opt/csw
	@ginstall -d $(DESTDIR)/opt/csw
	@ginstall -d $(DESTDIR)/opt/csw/bin
	@ginstall -d $(DESTDIR)/opt/csw/libexec/pkgutil
	@ginstall -d $(DESTDIR)/opt/csw/share
	@ginstall -d $(DESTDIR)/opt/csw/share/doc
	@ginstall -d $(DESTDIR)/opt/csw/share/doc/pkgutil
	@ginstall -d $(DESTDIR)$(mandir)
	@ginstall -d $(DESTDIR)$(mandir)/man1
	@ginstall -d $(DESTDIR)/var/opt/csw/pkgutil
	@ginstall -d $(DESTDIR)/var/opt/csw/pkgutil/packages
	@pod2man --section=1 $(WORKSRC)/$(GARNAME) > $(DESTDIR)$(mandir)/man1/pkgutil.1
	@cp -r $(WORKSRC)/$(GARNAME).conf $(DESTDIR)/etc/opt/csw/$(GARNAME).conf.CSW
	@cp -r $(WORKSRC)/$(GARNAME) $(DESTDIR)/opt/csw/bin/
	@cp -r $(WORKSRC)/bldcat $(DESTDIR)/opt/csw/bin/
	@cp -r $(WORKSRC)/chkcat $(DESTDIR)/opt/csw/bin/
	@cp -r $(WORKSRC)/readme $(DESTDIR)/opt/csw/share/doc/pkgutil/
	@cp -r $(FILEDIR)/CSWpkgutil.copyright $(DESTDIR)/opt/csw/share/doc/pkgutil/copyright
	@cp -r $(WORKSRC)/admin $(DESTDIR)/var/opt/csw/pkgutil/admin.CSW
	@cp -r $(WORKSRC)/wget-`uname -p` $(DESTDIR)/opt/csw/libexec/pkgutil/wget
	@$(MAKECOOKIE)
