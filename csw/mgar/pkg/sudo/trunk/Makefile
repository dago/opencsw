# $Id$

NAME = sudo
VERSION = 1.8.3p2
CATEGORIES = utils

DESCRIPTION = Provides limited super user privileges
define BLURB
  Sudo (superuser do) allows a system administrator to give certain users (or
  groups of users) the ability to run some (or all) commands as root while
  logging all commands and arguments. Sudo operates on a per-command basis, it
  is not a replacement for the shell.
endef

MASTER_SITES = ftp://ftp.sudo.ws/pub/sudo/
DISTFILES  = $(NAME)-$(VERSION).tar.gz 
PATCHFILES = install.diff

# We define upstream file regex so we can be notifed of new 
# upstream software release
UFILES_REGEX = $(NAME)-((\d+(?:\.\d+)*)(p\d+)?).tar.gz

PACKAGES += CSWsudo
PACKAGES += CSWsudo-common

CATALOGNAME_CSWsudo = sudo
SPKG_DESC_CSWsudo = $(DESCRIPTION)
SPKG_SOURCEURL_CSWsudo = http://www.sudo.ws/sudo/
RUNTIME_DEP_PKGS_CSWsudo += CSWsudo-common
RUNTIME_DEP_PKGS_CSWsudo += CSWggettextrt
RUNTIME_DEP_PKGS_CSWsudo += CSWlibintl8

CATALOGNAME_CSWsudo-common = sudo_common
SPKG_DESC_CSWsudo-common = Common files for sudo
SPKG_SOURCEURL_CSWsudo-common = http://www.sudo.ws
RUNTIME_DEP_PKGS_CSWsudo-common = CSWggettextrt
RUNTIME_DEP_PKGS_CSWsudo-common += CSWlibintl8
RUNTIME_DEP_PKGS_CSWsudo-common += CSWlibz1

DISTFILES += CSWsudo-common.postinstall 


# sysconfdir to be enabled later
sysconfdir = /etc/opt/csw
localstatedir = /var/opt/csw

LOGPATH    = $(localstatedir)/log/sudo
TIMEPATH   = $(localstatedir)/sudo
IOLOGPATH  = $(LOGPATH)/io

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-pam
CONFIGURE_ARGS += --with-logging=both
CONFIGURE_ARGS += --with-ignore-dot
CONFIGURE_ARGS += --with-env-editor
CONFIGURE_ARGS += --enable-zlib=/opt/csw/lib
CONFIGURE_ARGS += --disable-path-info
CONFIGURE_ARGS += --with-logpath=$(LOGPATH)/sudolog
CONFIGURE_ARGS += --with-iologdir=$(IOLOGPATH)
CONFIGURE_ARGS += --with-timedir=$(TIMEPATH)
CONFIGURE_ARGS += --disable-root-sudo

ifneq ($(shell uname -r),5.8)
    CONFIGURE_ARGS += --with-project
endif


TEST_TARGET = check
FIXCONFIG_DIRS = $(DESTDIR)$(libexecdir)

PKGFILES_CSWsudo  = $(bindir)/sudo\.minimal
PKGFILES_CSWsudo += $(bindir)/sudoedit\.minimal

PROTOTYPE_MODIFIERS = sudo
PROTOTYPE_FILES_sudo = $(bindir)/sudo(edit)?.minimal
PROTOTYPE_PERMS_sudo = 4755


PROTOTYPE_FILES_timedir =  $(TIMEPATH)  # a normal Perl regexp. Watch out for links!
PROTOTYPE_PERMS_timedir = 0700
PROTOTYPE_USER_timedir = root
PROTOTYPE_GROUP_timedir = bin

PROTOTYPE_FILES_iodir =  $(IOLOGPATH)  # a normal Perl regexp. Watch out for links!
PROTOTYPE_PERMS_iodir = 0700
PROTOTYPE_USER_iodir = root
PROTOTYPE_GROUP_iodir = bin

LICENSE = doc/LICENSE
ALTERNATIVES_CSWsudo = minimal
ALTERNATIVE_minimal  = $(bindir)/sudo     sudo     $(bindir)/sudo.minimal     50
ALTERNATIVE_minimal += $(bindir)/sudoedit sudoedit $(bindir)/sudoedit.minimal

CHECKPKG_OVERRIDES_CSWsudo += surplus-dependency|CSWalternatives
CHECKPKG_OVERRIDES_CSWsudo += surplus-dependency|CSWsudo-common


CHECKPKG_OVERRIDES_CSWsudo-common += file-with-bad-content|/usr/local|root/opt/csw/share/doc/sudo/ChangeLog
CHECKPKG_OVERRIDES_CSWsudo-common += file-with-bad-content|/usr/local|root/opt/csw/share/doc/sudo/sample.sudoers
CHECKPKG_OVERRIDES_CSWsudo-common += file-with-bad-content|/usr/local|root/opt/csw/share/doc/sudo/UPGRADE
CHECKPKG_OVERRIDES_CSWsudo-common += file-with-bad-content|/usr/local|root/opt/csw/share/doc/sudo/TROUBLESHOOTING
CHECKPKG_OVERRIDES_CSWsudo-common += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1m/sudo.1m
CHECKPKG_OVERRIDES_CSWsudo-common += file-with-bad-content|/usr/local|root/opt/csw/share/man/man4/sudoers.4
CHECKPKG_OVERRIDES_CSWsudo-common += file-with-bad-content|/usr/local|root/etc/opt/csw/sudoers.CSW
CHECKPKG_OVERRIDES_CSWsudo-common += file-with-bad-content|/usr/share|root/opt/csw/share/doc/sudo/ChangeLog

CHECKPKG_OVERRIDES_CSWsudo-common += soname-not-part-of-filename|soname=libsudo_noexec.so|filename=sudo_noexec.so

include gar/category.mk


post-install-modulated:
	@( cd $(DESTDIR)$(bindir) ; gmv sudo sudo.minimal )
	@( cd $(DESTDIR)$(bindir) ; gmv sudoedit sudoedit.minimal )
	@( cd $(DESTDIR)$(sysconfdir) ; gmv sudoers sudoers.CSW )
	@ginstall -d $(DESTDIR)$(IOLOGPATH)
	@ginstall -d $(DESTDIR)$(TIMEPATH)
	@$(MAKECOOKIE)
