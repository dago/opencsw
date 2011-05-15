# Do not update gar, new gar doesn't work on sol8! If removed, recreate with:
# svn co -r 9999 https://gar.svn.sourceforge.net/svnroot/gar/csw/mgar/gar/v2 gar

NAME = pkgutil
VERSION = 2.4
GARVERSION = $(VERSION)
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

#MASTER_SITES = $(SF_MIRRORS)
MASTER_SITES = http://sourceforge.net/projects/pkgutil/files/pkgutil/2.4/
DISTFILES  = $(NAME)-$(VERSION).zip

DISTFILES += $(call admfiles,CSWpkgutil,prototype preremove postinstall)
#DISTFILES += $(call admfiles,CSWpkgutil,preremove postinstall)
#ifeq ($(shell uname -p), sparc)
#  DISTFILES += CSWpkgutilsparc.prototype
#else
#  DISTFILES += CSWpkgutili386.prototype
#endif

DISTFILES += build_sun_catalog.py
DISTFILES += opencsw.py
DISTFILES += cswcatalog

PACKAGING_PLATFORMS = solaris8-sparc solaris8-i386

CHECKPKG_OVERRIDES_CSWpkgutilplus += unidentified-dependency|CSWpmstringapprox
CHECKPKG_OVERRIDES_CSWpkgutilplus += surplus-dependency|CSWpmstringapprox
CHECKPKG_OVERRIDES_CSWpkgutilplus += surplus-dependency|CSWperl
CHECKPKG_OVERRIDES_CSWpkgutilplus += surplus-dependency|CSWcswpkgloghooks
CHECKPKG_OVERRIDES_CSWpkgutilplus += surplus-dependency|CSWgnupg
CHECKPKG_OVERRIDES_CSWpkgutilplus += surplus-dependency|CSWpkgutil
CHECKPKG_OVERRIDES_CSWpkgutil += disallowed-path

PACKAGES = CSWpkgutil CSWpkgutilplus

SPKG_DESC_CSWpkgutil = $(DESCRIPTION)
SPKG_DESC_CSWpkgutilplus = Extends pkgutil functionality

# Explicitly depend on CSWcommon here since it's not the default
RUNTIME_DEP_PKGS_CSWpkgutilplus  = CSWcommon CSWperl CSWgnupg CSWpkgutil
RUNTIME_DEP_PKGS_CSWpkgutilplus += CSWcswpkgloghooks CSWpython CSWpmstringapprox
#RUNTIME_DEP_PKGS_CSWpkgutilplus += CSWpmwwwcurl

PKGFILES_CSWpkgutilplus  = .*bldcat.*
PKGFILES_CSWpkgutilplus += .*chkcat.*
PKGFILES_CSWpkgutilplus += .*pkgutilplus.*
PKGFILES_CSWpkgutilplus += .*build_sun_catalog.*
PKGFILES_CSWpkgutilplus += .*opencsw.py
PKGFILES_CSWpkgutilplus += .*cswcatalog

ARCHALL_CSWpkgutilplus = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

WORKSRC = $(WORKDIR)
SPKG_SOURCEURL = http://pkgutil.wikidot.com/

install-custom:
	@echo " ==> Installing $(NAME) (custom)"
	@rm -rf $(DESTDIR)
	@ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/pkg-hooks/preargproc.d
	@ginstall -m 644 $(WORKSRC)/$(NAME).conf $(DESTDIR)/etc/opt/csw/$(NAME).conf.CSW
	@ginstall -m 755 $(WORKSRC)/pkgutillog $(DESTDIR)/etc/opt/csw/pkg-hooks/preargproc.d/01-CSW$(NAME)plus-log
	@ginstall -m 755 -d $(DESTDIR)$(bindir)
	@ginstall -m 755 $(WORKSRC)/$(NAME) $(WORKSRC)/bldcat $(WORKSRC)/chkcat $(DESTDIR)$(bindir)
	@ginstall -m 755 $(FILEDIR)/cswcatalog $(DESTDIR)$(bindir)
	@ginstall -m 755 -d $(DESTDIR)/opt/csw/etc
	@ginstall -m 644 $(WORKSRC)/$(NAME).conf $(DESTDIR)/opt/csw/etc/$(NAME).conf.CSW
	@ginstall -m 755 -d $(DESTDIR)/opt/csw/libexec/$(NAME)
#	@ginstall -m 755 $(WORKSRC)/wget-`uname -p` $(DESTDIR)/opt/csw/libexec/$(NAME)/
	@ginstall -m 755 $(WORKSRC)/wget-`uname -p` $(DESTDIR)/opt/csw/libexec/$(NAME)/wget
	@ginstall -m 755 $(FILEDIR)/build_sun_catalog.py $(FILEDIR)/opencsw.py $(DESTDIR)/opt/csw/libexec/$(NAME)
	@ln -s ../libexec/pkgutil/build_sun_catalog.py $(DESTDIR)$(bindir)/build_sun_catalog
	@ginstall -m 755 -d $(DESTDIR)$(docdir)/$(NAME)
	@ginstall -m 444 $(WORKSRC)/readme $(WORKSRC)/license $(DESTDIR)$(docdir)/$(NAME)/
	@ginstall -m 755 -d $(DESTDIR)$(docdir)/$(NAME)plus
	@ginstall -m 444 $(WORKSRC)/license $(DESTDIR)$(docdir)/$(NAME)plus/
	@ginstall -m 444 $(WORKSRC)/readme.pkgutilplus $(DESTDIR)$(docdir)/$(NAME)plus/readme
	@ginstall -m 755 -d $(DESTDIR)$(mandir)/man1
	@pod2man --section=1 $(WORKSRC)/$(NAME) > $(DESTDIR)$(mandir)/man1/pkgutil.1
	@pod2man --section=1 $(WORKSRC)/bldcat > $(DESTDIR)$(mandir)/man1/bldcat.1
	@pod2man --section=1 $(WORKSRC)/chkcat > $(DESTDIR)$(mandir)/man1/chkcat.1
	@chmod 444 $(DESTDIR)$(mandir)/man1/*
	@ginstall -m 755 -d $(DESTDIR)/opt/csw/var/$(NAME)
	@ginstall -m 644 $(WORKSRC)/admin $(DESTDIR)/opt/csw/var/$(NAME)/admin.CSW
	@ginstall -m 755 -d $(DESTDIR)/var/opt/csw/$(NAME)/packages
	@ginstall -m 755 -d $(DESTDIR)/var/opt/csw/$(NAME)/pkgask
	@$(MAKECOOKIE)
