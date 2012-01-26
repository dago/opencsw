# $Id$
NAME = rssh
VERSION = 2.3.3
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = A restricted shell for use with OpenSSH
define BLURB
  rssh is a restricted shell for use with OpenSSH, allowing only scp and/or sftp.
  It now also includes support for rdist, rsync, and cvs. For example, if you have
  a server which you only want to allow users to copy files off of via scp, without
  providing shell access, you can use rssh to do that. For a list of platforms on
  which rssh is known to work, see the Platform Support Page.
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PATCHFILES = 0001-Use-DESTDIR-on-install-libexec-hook.patch 

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://www.pizzashack.org/rssh/

BUILD_DEP_PKGS = CSWossh CSWcvs CSWrdist CSWrsync

# We need at least OpenSSH, the other programs are optional
# Looks like I was wrong: even that one is optional. See
#   https://www.opencsw.org/mantis/view.php?id=4549
# RUNTIME_DEP_PKGS = CSWossh

sysconfdir = /etc/opt/csw
MIGRATE_FILES = rssh.conf
PRESERVECONF = $(sysconfdir)/rssh.conf

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-scp=$(bindir)/scp
CONFIGURE_ARGS += --with-sftp-server=$(libexecdir)/sftp-server
CONFIGURE_ARGS += --with-cvs=$(bindir)/cvs
CONFIGURE_ARGS += --with-rdist=$(bindir)/rdist
CONFIGURE_ARGS += --with-rsync=$(bindir)/rsync

PROTOTYPE_MODIFIERS = makesuid
PROTOTYPE_FILES_makesuid = $(libexecdir)/rssh_chroot_helper
PROTOTYPE_PERMS_makesuid = 4755

# CHECKPKG_OVERRIDES_CSWrssh += surplus-dependency|CSWossh

include gar/category.mk

post-install-modulated:
	ginstall -d $(DESTDIR)$(docdir)/$(NAME)
	cd $(WORKSRC) && ginstall -m 0644 CHROOT INSTALL README SECURITY $(DESTDIR)$(docdir)/$(NAME)
	@$(MAKECOOKIE)
