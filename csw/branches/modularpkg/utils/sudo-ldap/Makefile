GARNAME = sudo
GARVERSION = 1.6.9p8
CATEGORIES = utils

DESCRIPTION = Provides limited super user privileges to specific users
define BLURB
  Sudo (superuser do) allows a system administrator to give certain users (or
  groups of users) the ability to run some (or all) commands as root while
  logging all commands and arguments. Sudo operates on a per-command basis, it
  is not a replacement for the shell.
endef

MASTER_SITES = ftp://ftp.sudo.ws/pub/sudo/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz 

DISTFILES += CSWsudo-ldap.gspec CSWsudo-ldap.postinstall
DISTFILES += CSWsudo-ldap.prototype CSWsudo-ldap.depend
DISTFILES += CSWsudo-ldap.space CSWsudo-ldap.postremove

# Original maintainer's patch to disable strip on install
PATCHFILES = install.diff

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-pam
CONFIGURE_ARGS += --with-ldap=$(prefix)
CONFIGURE_ARGS += --with-ldap-conf-file=$(sysconfdir)/ldap.conf

TEST_TARGET = check

include ../category.mk

