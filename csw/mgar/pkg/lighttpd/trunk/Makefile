# $Id$
NAME = lighttpd
VERSION = 1.4.31
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
DISTFILES   += cswlighttpd

PATCHFILES += 0001-Work-around-linking-problem-buffer.c.patch

# When mkdir is issued on an automounted directory like /home/<someuser> errno is
# set to ENOSYS halting recursive directory generation. This patches handles
# ENOSYS similar to EEXIST and just continues with the creation which then may
# or may not work later on.
#
# There's a thread started on lighttpd forums about the issue:
#   http://redmine.lighttpd.net/boards/2/topics/4163
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
RUNTIME_DEP_PKGS_CSWlighttpd += CSWlibz1

PACKAGES += CSWlighttpd-mod-auth
SPKG_DESC_CSWlighttpd-mod-auth = Lighttpd module for authentication
PKGFILES_CSWlighttpd-mod-auth += $(call baseisadirs,$(libdir_install),mod_auth.so)
RUNTIME_DEP_PKGS_CSWlighttpd-mod-auth += CSWlighttpd
RUNTIME_DEP_PKGS_CSWlighttpd-mod-auth += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWlighttpd-mod-auth += CSWlibldap2-4-2

PACKAGES += CSWlighttpd-mod-webdav
SPKG_DESC_CSWlighttpd-mod-webdav = Lighttpd module for WebDAV access
PKGFILES_CSWlighttpd-mod-webdav += $(call baseisadirs,$(libdir_install),mod_webdav.so)
RUNTIME_DEP_PKGS_CSWlighttpd-mod-webdav += CSWlighttpd
RUNTIME_DEP_PKGS_CSWlighttpd-mod-webdav += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWlighttpd-mod-webdav += CSWlibxml2-2

PACKAGES += CSWlighttpd-mod-mysql-vhost
SPKG_DESC_CSWlighttpd-mod-mysql-vhost = Lighttpd module for MySQL-driven VHOSTs
PKGFILES_CSWlighttpd-mod-mysql-vhost += $(call baseisadirs,$(libdir_install),mod_mysql_vhost.so)
RUNTIME_DEP_PKGS_CSWlighttpd-mod-mysql-vhost += CSWlighttpd
RUNTIME_DEP_PKGS_CSWlighttpd-mod-mysql-vhost += CSWlibmysqlclient18
RUNTIME_DEP_PKGS_CSWlighttpd-mod-mysql-vhost += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWlighttpd-mod-mysql-vhost += CSWlibz1

# Add library needed for sendfilev64 referenced from .libs/liblightcomp_la-network_solaris_sendfilev.o
EXTRA_LINKER_FLAGS += -lsendfile

# To fix undefined symbol 'dlopen' on Solaris 9
EXTRA_LINKER_FLAGS_5.9 += -ldl
EXTRA_LINKER_FLAGS += $(EXTRA_LINKER_FLAGS_$(GAROSREL))

# lighttpd puts its modules under libdir, so we pass libdir as a subdirectory,
# because modules are not supposed to be in /opt/csw/lib.
libdir_install = $(prefix)/lib/lighttpd

CONFIGURE_ARGS  = $(DIRPATHS)

CONFIGURE_ARGS += --with-openssl=yes
CONFIGURE_ARGS += --with-openssl-includes=$(includedir)
CONFIGURE_ARGS += --with-openssl-libs=$(libpath)
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
CONFIGURE_ARGS += --with-mysql

# -- LUA support
# Disable LUA for now until this is fixed:
#   http://redmine.lighttpd.net/issues/2421
# CONFIGURE_ARGS += --with-lua
#EXTRA_CONFIGURE_EXPORTS += LUA_CFLAGS LUA_LIBS
CONFIGURE_ENV_LUA_CFLAGS = $(CPPFLAGS)
CONFIGURE_ENV_LUA_LIBS = -L$(libdir) -llua

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

post-merge:
	ginstall -d -m 755 $(PKGROOT)$(sysconfdir)/init.d
	ginstall -m 755 $(DOWNLOADDIR)/cswlighttpd $(PKGROOT)$(sysconfdir)/init.d
	# ginstall -m 644 $(WORKSRC)/doc/config/lighttpd.conf $(PKGROOT)$(sysconfdir)
	# gsed -i -e 's+/usr/local+/opt/csw+g' $(PKGROOT)$(sysconfdir)/lighttpd.conf
	ginstall -m 644 $(FILEDIR)/lighttpd.conf $(PKGROOT)$(sysconfdir)
	gsed -i -e 's+/usr/local+/opt/csw+g' $(PKGROOT)$(sysconfdir)/lighttpd.conf
	ginstall -d -m 755 $(PKGROOT)$(localstatedir)/run
	ginstall -d -m 755 $(PKGROOT)$(datadir)/lighttpd-root
	echo 'lighttpd is working!' > $(PKGROOT)$(datadir)/lighttpd-root/index.html
	ginstall -d -m 755 $(PKGROOT)$(localstatedir)/log/lighttpd
	ginstall -d -m 755 $(PKGROOT)$(sysconfdir)/pkg/$(NAME)
	echo "lighttpd:lighttpd:lighttpd web server::::" \
		> $(PKGROOT)$(sysconfdir)/pkg/$(NAME)/cswusergroup
	(cd $(PKGROOT)$(libdir_install); ln -s . 32)
	(cd $(PKGROOT)$(libdir_install); ln -s $(ISA_DEFAULT64) 64)
	@$(MAKECOOKIE)
