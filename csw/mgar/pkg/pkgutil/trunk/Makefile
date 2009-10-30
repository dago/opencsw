GARNAME = pkgutil
GARVERSION = 1.8
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
DISTFILES += $(call admfiles,CSWpkgutil,prototype postinstall preremove)
#DISTFILES += $(call admfiles,CSWpkgutil,postinstall preremove)

PACKAGES = CSWpkgutil CSWpkgutilplus

SPKG_DESC_CSWpkgutil = $(DESCRIPTION)
SPKG_DESC_CSWpkgutilplus = Extends pkgutil functionality

REQUIRED_PKGS_CSWpkgutilplus = CSWperl CSWgnupg CSWpkgutil

PKGFILES_CSWpkgutilplus  = .*bldcat.*
PKGFILES_CSWpkgutilplus += .*chkcat.*
PKGFILES_CSWpkgutilplus += .*pkgutilplus.*

ARCHALL_CSWpkgutilplus = 1

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
	@ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/pkg-hooks/preargproc.d
	@cp $(WORKSRC)/$(GARNAME).conf $(DESTDIR)/etc/opt/csw/$(GARNAME).conf.CSW
	@cp $(WORKSRC)/pkgutillog $(DESTDIR)/etc/opt/csw/pkg-hooks/preargproc.d/01-CSW$(GARNAME)plus-log
	@ginstall -m 755 -d $(DESTDIR)$(bindir)
	@cp $(WORKSRC)/$(GARNAME) $(DESTDIR)$(bindir)
	@cp $(WORKSRC)/bldcat $(DESTDIR)$(bindir)
	@cp $(WORKSRC)/chkcat $(DESTDIR)$(bindir)
	@ginstall -m 755 -d $(DESTDIR)$(sysconfdir)
	@cp $(WORKSRC)/$(GARNAME).conf $(DESTDIR)$(sysconfdir)/$(GARNAME).conf.CSW
	@ginstall -m 755 -d $(DESTDIR)/opt/csw/libexec/$(GARNAME)
	@cp $(WORKSRC)/wget-`uname -p` $(DESTDIR)/opt/csw/libexec/$(GARNAME)/wget
	@ginstall -m 755 -d $(DESTDIR)$(docdir)/$(GARNAME)
	@cp $(WORKSRC)/readme $(DESTDIR)$(docdir)/$(GARNAME)/
	@cp $(WORKSRC)/license $(DESTDIR)$(docdir)/$(GARNAME)/
	@ginstall -m 755 -d $(DESTDIR)$(docdir)/$(GARNAME)plus
	@cp $(WORKSRC)/license $(DESTDIR)$(docdir)/$(GARNAME)plus/
	@cp $(WORKSRC)/readme.pkgutilplus $(DESTDIR)$(docdir)/$(GARNAME)plus/readme
	@ginstall -m 755 -d $(DESTDIR)$(mandir)/man1
	@pod2man --section=1 $(WORKSRC)/$(GARNAME) > $(DESTDIR)$(mandir)/man1/pkgutil.1
	@pod2man --section=1 $(WORKSRC)/bldcat > $(DESTDIR)$(mandir)/man1/bldcat.1
	@pod2man --section=1 $(WORKSRC)/chkcat > $(DESTDIR)$(mandir)/man1/chkcat.1
	@ginstall -m 755 -d $(DESTDIR)/var/opt/csw/$(GARNAME)/packages
	@cp $(WORKSRC)/admin $(DESTDIR)/var/opt/csw/$(GARNAME)/admin.CSW
#	@ginstall -m 755 -d $(DESTDIR)/usr/sadm/install/scripts
#	@cp $(FILEDIR)/CSWpkgutil.i.cswpkgutil $(DESTDIR)/usr/sadm/install/scripts/i.cswpkgutil
#	@cp $(FILEDIR)/CSWpkgutil.r.cswpkgutil $(DESTDIR)/usr/sadm/install/scripts/r.cswpkgutil
	@$(MAKECOOKIE)
