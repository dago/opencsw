GARNAME = sudo
GARVERSION = 1.7.1
CATEGORIES = utils

DESCRIPTION = Provides limited super user privileges
define BLURB
  Sudo (superuser do) allows a system administrator to give certain users (or
  groups of users) the ability to run some (or all) commands as root while
  logging all commands and arguments. Sudo operates on a per-command basis, it
  is not a replacement for the shell.
endef

MASTER_SITES = ftp://ftp.sudo.ws/pub/sudo/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz 
PATCHFILES = install.diff

# We define upstream file regex so we can be notifed of new 
# upstream software release
UFILES_REGEX = $(GARNAME)-((\d+(?:\.\d+)*)(p\d+)?).tar.gz

PACKAGES = CSWsudo CSWsudo-common

BUILD64 = 1
CATALOGNAME_CSWsudo = sudo
SPKG_DESC_CSWsudo = $(DESCRIPTION)
SPKG_SOURCEURL_CSWsudo = http://www.sudo.ws
REQUIRED_PKGS_CSWsudo = CSWsudo-common CSWggettextrt

CATALOGNAME_CSWsudo-common = sudo_common
SPKG_DESC_CSWsudo-common = Common files for sudo
SPKG_SOURCEURL_CSWsudo-common = http://www.sudo.ws
REQUIRED_PKGS_CSWsudo-common = CSWggettextrt

DISTFILES += CSWsudo-common.postinstall 

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-pam
CONFIGURE_ARGS += --with-logging=both
CONFIGURE_ARGS += --with-ignore-dot
CONFIGURE_ARGS += --with-env-editor

TEST_TARGET = check
FIXCONFIG_DIRS = $(DESTDIR)$(libexecdir)

include gar/category.mk

PKGFILES_CSWsudo  = .*$(bindir).*/sudo
PKGFILES_CSWsudo  = .*$(bindir).*/sudo.minimal

post-install-modulated:
	@( cd $(DESTDIR)$(bindir) ; gcp sudo sudo.minimal )
	@( cd $(DESTDIR)$(bindir) ; grm -f sudoedit )
	@( cd $(DESTDIR)$(bindir) ; gcp sudo sudoedit )
	@( cd $(DESTDIR)$(sysconfdir) ; gmv sudoers sudoers.CSW )
	@( cd $(DESTDIR)$(bindir) ; gchmod 4755 sudo* )
	@$(MAKECOOKIE)
