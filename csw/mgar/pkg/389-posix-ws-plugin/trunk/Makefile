# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = 389-posix-ws-plugin
VERSION = 8b7d38c957
GARTYPE = v2

DESCRIPTION = Posix WinsSync Plugin for 389 Directory Server
define BLURB
  This plugin adds posix attributes to the winsync aggreement, so that posix attributes between MS-AD and DS will synced. The MS-AD MMC can get a IMU snap-in so that Posiy Attributes of Users and Groups can also maintian in the MS-AD. Normaly these attributs will not synced with the winsync agreement of a 389 Directory Server.
endef

MASTER_SITES = https://github.com/cgrzemba/Posix-Winsync-Plugin-for-389-directory-server/tarball/master
# DISTFILES = cgrzemba-Posix-Winsync-Plugin-for-389-directory-server-7a12af0.zip 
GIT_REPOS = git://github.com/cgrzemba/Posix-Winsync-Plugin-for-389-directory-server.git
# GIT_USE_PROXY = 1
# GIT_TREEISH_Posix-Winsync-Plugin-for-389-directory-server.git = $(VERSION)
GIT_TREEISH_389-posix-ws-plugin.git = $(VERSION)

BUILDDEPS += CSW389-ds-base-dev
BUILDDEPS += CSWnspr-dev

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-ds-inc=/opt/csw/include/dirsrv
CONFIGURE_ARGS += --with-nspr-inc=/opt/csw/include/nspr

include gar/category.mk

pre-configure-modulated:
	cd $(WORKSRC) && aclocal
	cd $(WORKSRC) && autoconf --force
	cd $(WORKSRC) && automake -a -c -f
	@$(MAKECOOKIE)
