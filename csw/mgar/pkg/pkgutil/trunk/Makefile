GARNAME = pkgutil
GARVERSION = 1.7
CATEGORIES = utils

DESCRIPTION = Installs Solaris packages easily
define BLURB
	Pkgutil, written in Perl and licensed under GPL, is a tool to make 
	installation of packages in Solaris easier. It handles package 
	dependencies so all required packages are installed before the desired 
	package automatically.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).zip
#DISTFILES += $(call admfiles,CSWpkgutil,prototype postinstall preremove)
DISTFILES += $(call admfiles,CSWpkgutil,postinstall preremove)

PACKAGES = CSWpkgutil CSWpkgutilplus

SPKG_DESC_CSWpkgutil = $(DESCRIPTION)
SPKG_DESC_CSWpkgutilplus = Extends pkgutil functionality

REQUIRED_PKGS_CSWpkgutilplus = CSWperl CSWgnupg

PKGFILES_CSWpkgutilplus  = .*bldcat.*
PKGFILES_CSWpkgutilplus += .*chkcat.*

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
	@ginstall -d $(DESTDIR)/opt/csw/libexec/$(GARNAME)
	@ginstall -d $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -d $(DESTDIR)$(mandir)/man1
#	@ginstall -d $(DESTDIR)/usr/sadm/install/scripts
	@ginstall -d $(DESTDIR)/var/opt/csw/$(GARNAME)/packages
	@ginstall -d $(DESTDIR)/etc/opt/csw
	@cp $(WORKSRC)/$(GARNAME).conf $(DESTDIR)$(sysconfdir)/$(GARNAME).conf.CSW
	@cp $(WORKSRC)/$(GARNAME).conf $(DESTDIR)/etc/opt/csw/$(GARNAME).conf.CSW
	@cp $(WORKSRC)/$(GARNAME) $(DESTDIR)$(bindir)
	@cp $(WORKSRC)/bldcat $(DESTDIR)$(bindir)
	@cp $(WORKSRC)/chkcat $(DESTDIR)$(bindir)
	@cp $(WORKSRC)/readme $(DESTDIR)$(docdir)/$(GARNAME)/
	@cp $(WORKSRC)/license $(DESTDIR)$(docdir)/$(GARNAME)/
#	@cp $(FILEDIR)/CSWpkgutil.i.cswpkgutil $(DESTDIR)/usr/sadm/install/scripts/i.cswpkgutil
#	@cp $(FILEDIR)/CSWpkgutil.r.cswpkgutil $(DESTDIR)/usr/sadm/install/scripts/r.cswpkgutil
	@cp $(WORKSRC)/admin $(DESTDIR)/var/opt/csw/$(GARNAME)/admin.CSW
	@cp $(WORKSRC)/wget-`uname -p` $(DESTDIR)/opt/csw/libexec/$(GARNAME)/wget
	@pod2man --section=1 $(WORKSRC)/$(GARNAME) > $(DESTDIR)$(mandir)/man1/pkgutil.1
	@pod2man --section=1 $(WORKSRC)/bldcat > $(DESTDIR)$(mandir)/man1/bldcat.1
	@pod2man --section=1 $(WORKSRC)/chkcat > $(DESTDIR)$(mandir)/man1/chkcat.1
	@$(MAKECOOKIE)
