NAME = sudo
VERSION = 1.8.2
CATEGORIES = utils

DESCRIPTION = Provides limited super user privileges (LDAP Enabled)
define BLURB
  Sudo (superuser do) allows a system administrator to give certain users (or
  groups of users) the ability to run some (or all) commands as root while
  logging all commands and arguments. Sudo operates on a per-command basis, it
  is not a replacement for the shell.
endef

MASTER_SITES = ftp://ftp.sudo.ws/pub/sudo/
DISTFILES  = $(NAME)-$(VERSION).tar.gz 
PATCHFILES = install.diff

PACKAGES = CSWsudoldap 

CATALOGNAME_CSWsudoldap = sudo_ldap
SPKG_DESC_CSWsudoldap = $(DESCRIPTION)
SPKG_SOURCEURL_CSWsudoldap = http://www.sudo.ws
RUNTIME_DEP_PKGS_CSWsudoldap += CSWlibintl8
RUNTIME_DEP_PKGS_CSWsudoldap += CSWoldaprt
RUNTIME_DEP_PKGS_CSWsudoldap += CSWsudo-common
RUNTIME_DEP_PKGS_CSWsudoldap += CSWzlib
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS_CSWsudoldap) CSWggettext

CHECKPKG_OVERRIDES_CSWsudoldap += surplus-dependency|CSWalternatives
CHECKPKG_OVERRIDES_CSWsudoldap += surplus-dependency|CSWsudo-common

LOGPATH = /var$(prefix)/log/sudo

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-pam
CONFIGURE_ARGS += --with-logging=both
CONFIGURE_ARGS += --with-ignore-dot
CONFIGURE_ARGS += --with-env-editor
CONFIGURE_ARGS += --with-ldap=$(prefix)
CONFIGURE_ARGS += --with-ldap-conf-file=$(sysconfdir)/ldap.conf
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

PKGFILES_CSWsudoldap  = $(bindir)/sudo\.ldap
PKGFILES_CSWsudoldap += $(bindir)/sudoedit\.ldap
PKGFILES_CSWsudoldap += $(mandir)/man4/sudoers\.ldap\.4

PROTOTYPE_MODIFIERS = sudo
PROTOTYPE_FILES_sudo = $(bindir)/sudo(|edit).ldap
PROTOTYPE_PERMS_sudo = 4755

LICENSE = README
ALTERNATIVES_CSWsudoldap = sudoldap
ALTERNATIVE_sudoldap  = $(bindir)/sudo     sudo     $(bindir)/sudo.ldap     60
ALTERNATIVE_sudoldap += $(bindir)/sudoedit sudoedit $(bindir)/sudoedit.ldap

# Legacy naming.
CHECKPKG_OVERRIDES_CSWsudoldap += catalogname-does-not-match-pkgname|pkgname=CSWsudoldap|catalogname=sudo_ldap|expected-catalogname=sudoldap

include gar/category.mk

PKGFILES_CSWsudoldap = $(bindir)/sudo.*

post-install-modulated:
	( cd $(DESTDIR)$(bindir) ; gmv sudo sudo.ldap )
	( cd $(DESTDIR)$(bindir) ; gmv sudoedit sudoedit.ldap )
	install -m 755 -d $(DESTDIR)$(LOGPATH)/logs
	@$(MAKECOOKIE)
