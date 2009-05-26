GARNAME = sudo
GARVERSION = 1.7.1
CATEGORIES = utils

DESCRIPTION = Provides limited super user privileges (LDAP Enabled)
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

PACKAGES = CSWsudoldap 

CATALOGNAME_CSWsudoldap = sudo_ldap
SPKG_DESC_CSWsudoldap = $(DESCRIPTION)
SPKG_SOURCEURL_CSWsudoldap = http://www.sudo.ws
REQUIRED_PKGS_CSWsudoldap = CSWsudo-common CSWggettextrt CSWoldaprt CSWisaexec

BUILD64 = 1
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-pam
CONFIGURE_ARGS += --with-logging=both
CONFIGURE_ARGS += --with-ignore-dot
CONFIGURE_ARGS += --with-env-editor
CONFIGURE_ARGS += --with-ldap=$(prefix)
CONFIGURE_ARGS += --with-ldap-conf-file=$(sysconfdir)/ldap.conf

TEST_TARGET = check

include gar/category.mk

PKGFILES_CSWsudoldap = .*$(bindir).*/sudo.ldap

post-install-modulated:
	@( cd $(DESTDIR)$(bindir) ; gmv sudo sudo.ldap )
	@( cd $(DESTDIR)$(bindir) ; grm sudoedit )
	@( cd $(DESTDIR)$(bindir) ; gchmod 4755 sudo.ldap )
	@$(MAKECOOKIE)
