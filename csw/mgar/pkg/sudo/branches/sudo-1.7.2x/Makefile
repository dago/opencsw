# $Id$

GARNAME = sudo
GARVERSION = 1.7.3
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

PACKAGES += CSWsudo
PACKAGES += CSWsudo-common

CATALOGNAME_CSWsudo = sudo
SPKG_DESC_CSWsudo = $(DESCRIPTION)
SPKG_SOURCEURL_CSWsudo = http://www.sudo.ws/sudo/
RUNTIME_DEP_PKGS_CSWsudo += CSWsudo-common
RUNTIME_DEP_PKGS_CSWsudo += CSWggettextrt

CATALOGNAME_CSWsudo-common = sudo_common
SPKG_DESC_CSWsudo-common = Common files for sudo
SPKG_SOURCEURL_CSWsudo-common = http://www.sudo.ws
RUNTIME_DEP_PKGS_CSWsudo-common = CSWggettextrt
RUNTIME_DEP_PKGS_CSWsudo += CSWzlib
RUNTIME_DEP_PKGS_CSWsudo-common += CSWzlib

DISTFILES += CSWsudo-common.postinstall 

LOGPATH = /var/opt/csw/log/sudo

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-pam
CONFIGURE_ARGS += --with-logging=both
CONFIGURE_ARGS += --with-ignore-dot
CONFIGURE_ARGS += --with-env-editor
CONFIGURE_ARGS += --disable-path-info
CONFIGURE_ARGS += --with-logpath=$(LOGPATH)/sudolog
ifneq ($(shell uname -r),5.8)
    CONFIGURE_ARGS += --with-project
endif

# sysconfdir to be enabled later
# sysconfdir = /etc/opt/csw
localstatedir = /var/opt/csw

TEST_TARGET = check
FIXCONFIG_DIRS = $(DESTDIR)$(libexecdir)

PKGFILES_CSWsudo  = $(bindir)/sudo\.minimal
PKGFILES_CSWsudo += $(bindir)/sudoedit\.minimal

PROTOTYPE_MODIFIERS = sudo
PROTOTYPE_FILES_sudo = $(bindir)/sudo(edit)?.minimal
PROTOTYPE_PERMS_sudo = 4755

LICENSE = LICENSE
ALTERNATIVES_CSWsudo = minimal
ALTERNATIVE_minimal  = $(bindir)/sudo     sudo     $(bindir)/sudo.minimal     50
ALTERNATIVE_minimal += $(bindir)/sudoedit sudoedit $(bindir)/sudoedit.minimal

CHECKPKG_OVERRIDES_CSWsudo += surplus-dependency|CSWalternatives
CHECKPKG_OVERRIDES_CSWsudo += surplus-dependency|CSWsudo-common

include gar/category.mk

post-install-modulated:
	@( cd $(DESTDIR)$(bindir) ; gmv sudo sudo.minimal )
	@( cd $(DESTDIR)$(bindir) ; gmv sudoedit sudoedit.minimal )
	@( cd $(DESTDIR)$(sysconfdir) ; gmv sudoers sudoers.CSW )
	install -m 755 -d $(DESTDIR)$(LOGPATH)/logs
	@$(MAKECOOKIE)
