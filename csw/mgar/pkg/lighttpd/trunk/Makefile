# $Id$
NAME = lighttpd
VERSION = 1.4.34
CATEGORIES = server
GARTYPE = v2

DESCRIPTION = HTTP server built for security, speed, compliance, and flexibility
define BLURB
  Security, speed, compliance, and flexibility -- all of these describe lighttpd
  (pron. lighty) which is rapidly redefining efficiency of a webserver; as it is
  designed and optimized for high performance environments. With a small memory
  footprint compared to other web-servers, effective management of the cpu-load,
  and advanced feature set (FastCGI, SCGI, Auth, Output-Compression,
  URL-Rewriting and many more) lighttpd is the perfect solution for every server
  that is suffering load problems. And best of all it's Open Source licensed
  under the revised BSD license. 
endef

MASTER_SITES = http://download.lighttpd.net/lighttpd/releases-1.4.x/
DISTFILES   += $(NAME)-$(VERSION).tar.gz
DISTFILE#PATCHFILES += 0001-Work-around-linking-problem-buffer.c.patch
# Patch from http://buildfarm.opencsw.org/source/xref/solaris-userland/components/lighttpd/patches/05-network-nodelay.patch
PATCHFILES += 0002-fix_missing_tcp_nodelaying-problem-buffer.c.patch

# When mkdir is issued on an automounted directory like /home/<someuser> errno is
# set to ENOSYS halting recursive directory generation. This patches handles
# ENOSYS similar to EEXIST and just continues with the creation which then may
# or may notUse patch until this is fixed:
#   http://redmine.lighttpd.net/issues/2527boards/2/topics/4163
PATCHFILES += 0003-Ignore-ENOSYS-on-mkdir-which-happens-on-automounted-.patch

# PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386                                                                          
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

PACKAGES += CSWlighttpd
CATALOGNAME_CSWlighttpd = lighttpd
SPKG_DESC_CSWlighttpd = HTTP server built for security, speed, compliance, and flexibility
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlighttpd += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlighttpd += CSWlibpcre1
RUNTIME_DEP_PKGS_CSWlighttpd += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWlRUNTIME_DEP_PKGS_CSWlighttpd += CSWlibfam0lighttpd += CSWlibz1

PACKAGES += CSWlighttpd-mod-auth
SPKG_DESC_CSWlighttpd-mod-auth = Lighttpd module for authentication
PKGFILES_CSWlighttpd-mod-auth += $(call baseisadirs,$(libdir_install),mod_auth.so)
RUNTIME_DEP_PKGS_CSWlighttpd-mod-auth += CSWlighttpd
RUNTIME_DEP_PKGS_CSWlighttpd-mod-auth += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWlighttpd-mod-authRUNTIME_DEP_PKGS_CSWlighttpd-mod-auth += CSWlibssl1-0-0

# These are problems within checkpkg
CHECKPKG_OVERRIDES_CSWlighttpd-mod-auth += 64-bit-binaries-missing
CHECKPKG_OVERRIDES_CSWlighttpd-mod-auth += surplus-dependency|CSWlighttpdh# Issues with linker defect and -z ignore
CHECKPKG_OVERRIDES_CSWlighttpd-mod-auth += surplus-dependency|CSWliblber2-4-2h += CSWlibldap2-4-2

PACKAGES += CSWlighttpd-mod-webdav
SPKG_DESC_CSWlighttpd-mod-webdav = Lighttpd module for WebDAV access
PKGFILES_CSWlighttpd-mod-webdav += $(call baseisadirs,$(libdir_install),mod_webdav.so)
RUNTIME_DEP_PKGS_CSWlighttpd-mod-webdav += CSWlighttpd
RUNTIME_DEP_PKGS_CSWlighttpd-mod-webdav += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWlighttpd-mod-webRUNTIME_DEP_PKGS_CSWlighttpd-mod-webdav += CSWlibuuid1

# These are problems within checkpkg
CHECKPKG_OVERRIDES_CSWlighttpd-mod-webdav += 64-bit-binaries-missing
CHECKPKG_OVERRIDES_CSWlighttpd-mod-webdav += surplus-dependency|CSWlighttpdbdav += CSWlibxml2-2

PACKAGES += CSWlighttpd-mod-mysql-vhost
SPKG_DESC_CSWlighttpd-mod-mysql-vhost = Lighttpd module for MySQL-driven VHOSTs
PKGFILES_CSWlighttpd-mod-mysql-vhost += $(call baseisadirs,$(libdir_install),mod_mysql_vhost.so)
RUNTIME_DEP_PKGS_CSWlighttpd-mod-mysql-vhost += CSWlighttpd
RUNTIME_DEP_PKGS_CSWlighttpd-mod-mysql-vhost += CSWlibmysqlclient18
RUNTIME_DEP_PKGS_CSWlighttpd-mod-mysql-vhost += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWlighttpd-mod-mysql-vThese are problems within checkpkg
CHECKPKG_OVERRIDES_CSWlighttpd-mod-mysql-vhost += 64-bit-binaries-missing
CHECKPKG_OVERRIDES_CSWlighttpd-mod-mysql-vhost += surplus-dependency|CSWlighttpd
# Issues with linker defect and -z ignore
CHECKPKG_OVERRIDES_CSWlighttpd-mod-mysql-vhost += surplus-dependency|CSWlibz1
CHECKPKG_OVERRIDES_CSWlighttpd-mod-mysql-vhost += surplus-dependency|CSWlibssl1-0-0

PACKAGES += CSWlighttpd-mod-trigger
SPKG_DESC_CSWlighttpd-mod-trigger = Lighttpd module
PKGFILES_CSWlighttpd-mod-trigger += $(call baseisadirs,$(libdir_install),mod_trigger_b4_dl.so)
RUNTIME_DEP_PKGS_CSWlighttpd-mod-trigger += CSWlighttpd
RUNTIME_DEP_PKGS_CSWlighttpd-mod-trigger += CSWlibpcre1
RUNTIME_DEP_PKGS_CSWlighttpd-mod-trigger += CSWlibgdbm4

# These are problems within checkpkg
CHECKPKG_OVERRIDES_CSWlighttpd-mod-trigger += 64-bit-binaries-missing
CHECKPKG_OVERRIDES_CSWlighttpd-mod-trigger += surplus-dependency|CSWlighttpdql-vhost += CSWlibz1

# Add library needed for sendfilev64 referenced from .libs/liblightcomp_la-network_solaris_sendfilev.o
EXTRA_LINKER_FLAGS += -lsendfile

# To fix undefined symbol 'dlopen' on Solaris 9
EXTRA_LINKER_FLAGS_5.9 += -ldl
EXTRA_LINKER_FLAGS += $(EXTRA_LINKER_FLAGS_$(GAROSREL))

# lighttpd puts its modules under libdir, so we pass libdir as a subdirectory,
# because modules are not supposed to be in /opt/csw/lib.exec_prefix)/lib/lighttpd
#libdir = $(abspath $(libdir_install)/$(MM_LIBDIR))/lighttpd
#be in /opt/csw/lib.
libdir_install = $(prefix)/lib/lighttpd

CONFIGURE_ARGS  = $(DIRPATHS)

CONFIGURE_ARGS += --with-openssl=yes
CONFIGURE_ARGS += --with-openssl-includes=$(includedir)
CONFIGURE_ARGS += --with-open
# Hardcode until this is fixed:
#   http://redmine.lighttpd.net/issues/2528
CONFIGURE_ARGS += ac_cv_search_crypt=-lcrypto
nssl-libs=$(libpath)
# EXTRA_LINKER_FLAGS += -lcrypto

# Solaris 9 does not have IPV6_V6ONLY.
# IPv6 support only works on Solaris 10.
CONFIGURE_ARGS_5.9 = --disable-ipv6
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GAROSREL))

# Plugins:
# disabled: 
#   mod_cml
#   mod_magnet
#   mod_mysql_vhost
# 
# Features:
# disabled: 
#   auth-ldap
#   stat-cache-fam
#   storage-gdbm
#   storage-memcache
#   webdav-locks
#   webdav-properties

CONFIGURE_ARGS += --with-webdav-props
CONFIGURE_ARGS += --with-webdav-locks
CONFIGURE_ARGS += --with-memcache
CONFIGURE_ARGS += --with-ldap
CONFIGURE_ACONFIGURE_ARGS += --with-fam
CONFIGURE_ARGS += --with-gdbm
CONFIGURE_ARGS += --with-memcacheARGS += --with-mysql

# -- LUA support
# Disable LUA for now until this is fixed:
#   http://redmine.lighttpd.net/issues/2421
# CONFIGURE_ARGS += --with-lua
#EXTRA_CONFIGURE_EXPORTS += LUA_CFLAGS LUA_LIBS
CONFIGURE_ENV_LUA_CFLAGS = $(CPPFLAGS)
CONFIGURE_ENV_LUA_LIBS =# Make sure 'id -u' and 'id -g' works
CONFIGURE_ENV_PATH = /usr/xpg4/bin:$(PATH) = -L$(libdir) -llua

INITSMF = $(sysconfdir)/init\.d/cswlighttpd
PRESERVECONF = $(sysconfdir)/lighttpd\.conf
USERGROUP = $(sysconfdir)/pkg/$(NAME)/cswusergroup

# Migrating the configuration file from /opt/csw/etc to /etc/opt/csw
MIGRATE_FILES_CSWlighttpd = lighttpd.conf

# To allow lighttpd to write logs
PROTOTYPE_MODIFIERS = user
PROTOTYPE_FILES_user = $(localstatedir)/log/lighttpd
PROTOTYPE_USER_user = lighttpd
PROTOTYPE_GROUP_user = lighttpd
PROTOTYPE_CLASS_user = ugfiles

BUILD64 = 1
ISAEXEC = 1

include gar/category.mk

post-install-modulated:
	ginstall -d -m 755 $(DESTDIR)$(sysconfdir)/init.d
	ginstall -m 755 $(DOWNLOADDIR)/cswlighttpd $(DESTDIR)$(sysconfdir)/init.d
	# ginstall -m 644 $(WORKSRC)/doc/config/lighttpd.conf $(DESTDIR)$(sysconfdir)
	# gsed -i -e 's+/usr/local+/opt/csw+g' $(DESTDIR)$(sysconfdir)/lighttpd.conf
	ginstall -m 644 $(FILEDIR)/lighttpd.conf $(DESTDIR)$(sysconfdir)
	gsed -i -e 's+/usr/local+/opt/csw+g' $(DESTDIR)$(sysconfdir)/lighttpd.conf
	ginstall -d -m 755 $(DESTDIR)$(localstatedir)/run
	ginstall -d -m 755 $(DESTDIR)$(datadir)/lighttpd-root
	echo 'lighttpd is working!' > $(DESTDIR)$(datadir)/lighttpd-root/index.html
	ginstall -d -m 755 $(DESTDIR)$(localstatedir)/log/lighttpd
	@$(MAK-allECOOKIE)

post-merge:
	ginstall -d -m 755 $(PKGROOT)$(sysconfdir)/pkg/$(NAME)
	echo "lighttpd:lighttpd:lighttpd web server::::" \
		> $(PKGROOT)$(sysconfdir)/pkg/$(NAME)/cswusergroup
	(cd $(PKGROOTgln -s . 32)
	(cd $(PKGROOT)$(libdir_install); gln -s $(ISA_DEFAULT64) 64)
	@$(MAKECOOKIE)
