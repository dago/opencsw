# $Id$
GARNAME = rssh
GARVERSION = 2.3.3
CATEGORIES = utils

DESCRIPTION = A restricted shell for use with OpenSSH
define BLURB
  rssh is a restricted shell for use with OpenSSH, allowing only scp and/or sftp.
  It now also includes support for rdist, rsync, and cvs. For example, if you have
  a server which you only want to allow users to copy files off of via scp, without
  providing shell access, you can use rssh to do that. For a list of platforms on
  which rssh is known to work, see the Platform Support Page.
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PATCHFILES = 0001-Use-DESTDIR-on-install-libexec-hook.patch 

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://www.pizzashack.org/rssh/

sysconfdir = /etc/opt/csw
MIGRATE_FILES = rssh.conf

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

PROTOTYPE_MODIFIERS = makesuid
PROTOTYPE_FILES_makesuid = $(libexecdir)/rssh_chroot_helper
PROTOTYPE_PERMS_makesuid = 4755

include gar/category.mk

post-install-modulated:
	ginstall -d $(DESTDIR)$(docdir)/$(GARNAME)
	cd $(WORKSRC) && ginstall -m 0644 CHROOT INSTALL README SECURITY $(DESTDIR)$(docdir)/$(GARNAME)
	@$(MAKECOOKIE)
