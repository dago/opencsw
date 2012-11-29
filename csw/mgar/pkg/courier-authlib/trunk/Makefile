# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = courier-authlib
VERSION = 0.65.0
GARTYPE = v2

DESCRIPTION = Courier authentication library
define BLURB
   Courier authentication library for use with rest of Courier suite.
endef

MASTER_SITES = $(SF_MIRRORS)
SF_PROJECT = courier/authlib
DISTFILES  = $(DISTNAME).tar.bz2
DISTFILES += cswusergroup
DISTFILES += cswcourier-authlib
DISTFILES += cswcourier-authlib.xml

PACKAGING_PLATFORMS = solaris10-i386 solaris10-sparc

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-mysql-libs=/opt/csw/lib
CONFIGURE_ARGS += --with-mysql-includes=/opt/csw/include
CONFIGURE_ARGS += --with-pgsql-lib=/opt/csw/lib
CONFIGURE_ARGS += --with-pgsql-includes=/opt/csw/include/postgresql

PACKAGES = CSWcourier-authlib
SPKG_DESC_CSWcourier-authlib = Courier auth library
BUILD_DEP_PKGS_CSWcourier-authlib += CSWmysql-dev
BUILD_DEP_PKGS_CSWcourier-authlib += CSWpostgresql-dev
BUILD_DEP_PKGS_CSWcourier-authlib += CSWopenldap-dev
RUNTIME_DEP_PKGS_CSWcourier-authlib += CSWlibmysqlclient18
RUNTIME_DEP_PKGS_CSWcourier-authlib += CSWlibpq5
RUNTIME_DEP_PKGS_CSWcourier-authlib += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWcourier-authlib += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWcourier-authlib += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWcourier-authlib += CSWlibgdbm4
RUNTIME_DEP_PKGS_CSWcourier-authlib += CSWlibldap2-4-2
OBSOLETED_BY_CSWcourier-authlib += CSWcourierauth

MIGRATE_SOURCE_DIR_CSWcourier-authlib = $(prefix)/etc/authlib
MIGRATE_DEST_DIR_CSWcourier-authlib = $(sysconfdir)/authlib
MIGRATE_FILES_CSWcourier-authlib += authdaemonrc
MIGRATE_FILES_CSWcourier-authlib += authldaprc
MIGRATE_FILES_CSWcourier-authlib += authmysqlrc
MIGRATE_FILES_CSWcourier-authlib += authpgsqlrc
MIGRATE_FILES_CSWcourier-authlib += userdb

PRESERVECONF += authdaemonrc
PRESERVECONF += authldaprc
PRESERVECONF += authmysqlrc
PRESERVECONF += authpgsqlrc
PRESERVECONF += userdb

INITSMF = /etc/opt/csw/init.d/cswcourier-authlib

USERGROUP = /etc/opt/csw/pkg/CSW$(NAME)/cswusergroup
PROTOTYPE_MODIFIERS = 1
PROTOTYPE_CLASS_1   = ugfiles
PROTOTYPE_FILES_1   = \/var\/opt\/csw\/spool\/authdaemon
PROTOTYPE_USER_1    = authlib
PROTOTYPE_GROUP_1   = authlib
PROTOTYPE_PERMS_1   = 755

# Just a harmless override, there is /usr/local in the script somewhere
CHECKPKG_OVERRIDES_CSWcourier-authlib += file-with-bad-content|/usr/local|root/opt/csw/sbin/makeuserdb
CHECKPKG_OVERRIDES_CSWcourier-authlib += file-with-bad-content|/usr/share|root/var/opt/csw/svc/manifest/application/cswcourier-authlib.xml

PACKAGES += CSWcourier-authlib-dev
SPKG_DESC_CSWcourier-authlib-dev = Courier auth library development files
PKGFILES_CSWcourier-authlib-dev = $(PKGFILES_DEVEL)

include gar/category.mk

post-install-modulated:
	@/opt/csw/bin/ginstall -d -m 755 $(DESTDIR)/etc/opt/csw/init.d
	@/opt/csw/bin/ginstall -d -m 755 $(DESTDIR)/var/opt/csw/svc/manifest/application
	@/opt/csw/bin/ginstall -d -m 755 $(DESTDIR)/etc/opt/csw/pkg/CSW$(NAME)
	@/opt/csw/bin/ginstall -m 755 $(FILEDIR)/cswcourier-authlib $(DESTDIR)/$(INITSMF)
	@/opt/csw/bin/ginstall -m 644 $(FILEDIR)/cswcourier-authlib.xml $(DESTDIR)/var/opt/csw/svc/manifest/application/cswcourier-authlib.xml
	@/opt/csw/bin/ginstall -m 644 $(FILEDIR)/cswusergroup $(DESTDIR)/etc/opt/csw/pkg/CSW$(NAME)
	@$(MAKECOOKIE)

