GARNAME = pkgutil
GARVERSION = 1.9.1
CATEGORIES = utils

DESCRIPTION = Installs Solaris packages easily
define BLURB
	Pkgutil, written in Perl and licensed under GPL, is a tool to make 
	installation of packages in Solaris easier. It handles package 
	dependencies so all required packages are installed before the desired 
	package automatically.
endef

# Disable inclusion of CSWcommon by default.
COMMON_PKG_DEPENDS = 

MASTER_SITES  = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).zip
DISTFILES += $(call admfiles,CSWpkgutil,prototype)
DISTFILES += i.cswpkgutil
DISTFILES += r.cswpkgutil
DISTFILES += build_sun_catalog.py
DISTFILES += opencsw.py

PACKAGES = CSWpkgutil CSWpkgutilplus

SPKG_DESC_CSWpkgutil = $(DESCRIPTION)
SPKG_DESC_CSWpkgutilplus = Extends pkgutil functionality

# Explicitly depend on CSWcommon here since it's not the default
#REQUIRED_PKGS_CSWpkgutilplus = CSWcommon CSWperl CSWgnupg CSWpkgutil CSWpmwwwcurl
REQUIRED_PKGS_CSWpkgutilplus = CSWcommon CSWperl CSWgnupg CSWpkgutil CSWcswpkgloghooks CSWpython

PKGFILES_CSWpkgutilplus  = .*bldcat.*
PKGFILES_CSWpkgutilplus += .*chkcat.*
PKGFILES_CSWpkgutilplus += .*pkgutilplus.*
PKGFILES_CSWpkgutilplus += .*build_sun_catalog.*
PKGFILES_CSWpkgutilplus += .*opencsw.py.*

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
SPKG_CLASSES_CSWpkgutil = none cswpkgutil

install-custom:
	@echo " ==> Installing $(GARNAME) (custom)"
	@rm -rf $(DESTDIR)
	@ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/pkg-hooks/preargproc.d
	@ginstall -m 644 $(WORKSRC)/$(GARNAME).conf $(DESTDIR)/etc/opt/csw/$(GARNAME).conf.CSW
	@ginstall -m 755 $(WORKSRC)/pkgutillog $(DESTDIR)/etc/opt/csw/pkg-hooks/preargproc.d/01-CSW$(GARNAME)plus-log
	@ginstall -m 755 -d $(DESTDIR)$(bindir)
	@ginstall -m 755 $(WORKSRC)/$(GARNAME) $(WORKSRC)/bldcat $(WORKSRC)/chkcat $(DESTDIR)$(bindir)
	@ginstall -m 755 -d $(DESTDIR)/opt/csw/etc
	@ginstall -m 644 $(WORKSRC)/$(GARNAME).conf $(DESTDIR)/opt/csw/etc/$(GARNAME).conf.CSW
	@ginstall -m 755 -d $(DESTDIR)/opt/csw/libexec/$(GARNAME)
	@ginstall -m 755 $(WORKSRC)/wget-`uname -p` $(DESTDIR)/opt/csw/libexec/$(GARNAME)/wget
	@ginstall -m 755 $(FILEDIR)/build_sun_catalog.py $(FILEDIR)/opencsw.py $(DESTDIR)/opt/csw/libexec/$(GARNAME)
	@ln -s ../libexec/pkgutil/build_sun_catalog.py $(DESTDIR)$(bindir)/build_sun_catalog
	@ginstall -m 755 -d $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 444 $(WORKSRC)/readme $(WORKSRC)/license $(DESTDIR)$(docdir)/$(GARNAME)/
	@ginstall -m 755 -d $(DESTDIR)$(docdir)/$(GARNAME)plus
	@ginstall -m 444 $(WORKSRC)/license $(DESTDIR)$(docdir)/$(GARNAME)plus/
	@ginstall -m 444 $(WORKSRC)/readme.pkgutilplus $(DESTDIR)$(docdir)/$(GARNAME)plus/readme
	@ginstall -m 755 -d $(DESTDIR)$(mandir)/man1
	@pod2man --section=1 $(WORKSRC)/$(GARNAME) > $(DESTDIR)$(mandir)/man1/pkgutil.1
	@pod2man --section=1 $(WORKSRC)/bldcat > $(DESTDIR)$(mandir)/man1/bldcat.1
	@pod2man --section=1 $(WORKSRC)/chkcat > $(DESTDIR)$(mandir)/man1/chkcat.1
	@chmod 444 $(DESTDIR)$(mandir)/man1/*
	@ginstall -m 755 -d $(DESTDIR)/var/opt/csw/$(GARNAME)/packages
	@ginstall -m 755 -d $(DESTDIR)/var/opt/csw/$(GARNAME)/pkgask
	@ginstall -m 644 $(WORKSRC)/admin $(DESTDIR)/var/opt/csw/$(GARNAME)/admin.CSW
	@$(MAKECOOKIE)
