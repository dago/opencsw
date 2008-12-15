GARNAME = sudo
GARVERSION = 1.6.9p8
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

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-((\d+(?:\.\d+)*)(p\d+)?).tar.gz

DISTFILES += CSWsudo.gspec CSWsudo.postinstall 
DISTFILES += CSWsudo.prototype CSWsudo.depend
DISTFILES += CSWsudo.space CSWsudo.postremove

DISTFILES += CSWsudo-common.gspec CSWsudo-common.postinstall 
DISTFILES += CSWsudo-common.prototype CSWsudo-common.depend
DISTFILES += CSWsudo-common.space

# Original maintainer's patch to disable strip on install
PATCHFILES = install.diff

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-pam

TEST_TARGET = check
FIXCONFIG_DIRS = $(DESTDIR)$(libexecdir)

include gar/category.mk

post-install:
	@( cd $(DESTDIR)$(sysconfdir) ; mv sudoers sudoers.CSW )
	@$(MAKECOOKIE)
	$(DONADA)
