GARNAME = pkgutil
GARVERSION = 1.3.1
CATEGORIES = utils

DESCRIPTION = Installs Solaris packages easily
define BLURB
	Pkgutil, written in Perl and licensed under GPL, is a tool to make 
	installation of packages in Solaris easier. It handles package 
	dependencies so all required packages are installed before the desired 
	package automatically.
endef

MASTER_SITES = http://www.bonivart.com/pkgutil/
DISTFILES  = $(GARNAME)-$(GARVERSION).zip
DISTFILES += $(call admfiles,CSWpkgutil,prototype postinstall preremove)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).zip

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

WORKSRC = $(WORKDIR)
SPKG_SOURCEURL = http://pkgutil.wikidot.com/
#SPKG_CLASSES = none cswpkgutil

install-custom:
	@echo " ==> Installing $(GARNAME) (custom)"
	@rm -rf $(DESTDIR)
	@ginstall -d $(DESTDIR)$(bindir)
	@ginstall -d $(DESTDIR)$(sysconfdir)
	@ginstall -d $(DESTDIR)/opt/csw/libexec/pkgutil
	@ginstall -d $(DESTDIR)$(docdir)/pkgutil
	@ginstall -d $(DESTDIR)$(mandir)/man1
#	@ginstall -d $(DESTDIR)/usr/sadm/install/scripts
	@ginstall -d $(DESTDIR)/var/opt/csw/pkgutil/packages
#	@cp -r $(WORKSRC)/$(GARNAME).conf $(DESTDIR)/etc/opt/csw/$(GARNAME).conf.CSW
	@cp -r $(WORKSRC)/$(GARNAME).conf $(DESTDIR)$(sysconfdir)/$(GARNAME).conf.CSW
	@cp -r $(WORKSRC)/$(GARNAME) $(DESTDIR)$(bindir)
	@cp -r $(WORKSRC)/bldcat $(DESTDIR)$(bindir)
	@cp -r $(WORKSRC)/chkcat $(DESTDIR)$(bindir)
	@cp -r $(WORKSRC)/readme $(DESTDIR)$(docdir)/pkgutil/
#	@cp -r $(FILEDIR)/CSWpkgutil.copyright $(DESTDIR)$(docdir)/pkgutil/LICENSE
	@cp -r $(WORKSRC)/copyright $(DESTDIR)$(docdir)/pkgutil/LICENSE
#	@cp -r $(FILEDIR)/CSWpkgutil.i.cswpkgutil $(DESTDIR)/usr/sadm/install/scripts/i.cswpkgutil
#	@cp -r $(FILEDIR)/CSWpkgutil.r.cswpkgutil $(DESTDIR)/usr/sadm/install/scripts/r.cswpkgutil
	@cp -r $(WORKSRC)/admin $(DESTDIR)/var/opt/csw/pkgutil/admin.CSW
	@cp -r $(WORKSRC)/wget-`uname -p` $(DESTDIR)/opt/csw/libexec/pkgutil/wget
	@pod2man --section=1 $(WORKSRC)/$(GARNAME) > $(DESTDIR)$(mandir)/man1/pkgutil.1
	@$(MAKECOOKIE)
