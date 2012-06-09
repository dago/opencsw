# $Id$
NAME = bacula
VERSION = 5.0.3
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = The Open Source Network Backup Solution
define BLURB
Bacula is a set of Open Source, enterprise ready, computer programs that permit you (or the system administrator) to manage backup, recovery, and verification of computer data across a network of computers of different kinds. Bacula is relatively easy to use and efficient, while offering many advanced storage management features that make it easy to find and recover lost or damaged files. In technical terms, it is an Open Source, enterprise ready, network based backup program. 
endef

GARCOMPILER = GNU

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(DISTNAME).tar.gz
DISTFILES += CSWbacula-doc.cswreleasenotes
DISTFILES += CSWbacula-common.cswreleasenotes
DISTFILES += README.CSW
DISTFILES += CSWbacula-director.postinstall
DISTFILES += CSWbacula-sd.postinstall
DISTFILES += CSWbacula-fd.postinstall
DISTFILES += CSWbacula-console.postinstall
DISTFILES += postmsg
PATCHFILES += 0001-Update-AC_INIT-use-to-make-configure-handle-docdir.patch
PATCHFILES += 0002-Clean-up-solaris-install-autostart-targets.patch
PATCHFILES += 0003-Make-the-solaris-init-scripts-user-group-aware.patch
PATCHFILES += 0004-Update-man-page-installation-so-we-don-t-get-gzipped.patch

BUILD_DEP_PKGS  = CSWmysql-dev CSWiconv CSWtcpwrap CSWlibssl-dev
BUILD_DEP_PKGS += CSWreadline CSWggettext-dev CSWlibcairo-dev

PACKAGES  = CSWbacula-common CSWbacula-fd CSWbacula-sd
PACKAGES += CSWbacula-director CSWbacula-client CSWbacula
PACKAGES += CSWbacula-tray-monitor CSWbacula-console CSWbacula-doc

CATALOGNAME_CSWbacula = bacula
SPKG_DESC_CSWbacula = $(DESCRIPTION)
ARCHALL_CSWbacula = 1
RUNTIME_DEP_PKGS_CSWbacula  = CSWbacula-fd CSWbacula-sd CSWbacula-director
RUNTIME_DEP_PKGS_CSWbacula += CSWbacula-console CSWbacula-doc
PKGFILES_CSWbacula = NOFILES
CHECKPKG_OVERRIDES_CSWbacula += surplus-dependency|CSWbacula-sd
CHECKPKG_OVERRIDES_CSWbacula += surplus-dependency|CSWbacula-fd
CHECKPKG_OVERRIDES_CSWbacula += surplus-dependency|CSWbacula-director
CHECKPKG_OVERRIDES_CSWbacula += surplus-dependency|CSWbacula-console
CHECKPKG_OVERRIDES_CSWbacula += surplus-dependency|CSWbacula-doc

CATALOGNAME_CSWbacula-console = bacula_console
SPKG_DESC_CSWbacula-console = $(DESCRIPTION) - Console
OBSOLETED_BY_CSWbacula-console = CSWbaculaclient
RUNTIME_DEP_PKGS_CSWbacula-console = CSWbacula-common
RUNTIME_DEP_PKGS_CSWbacula-console += CSWtcpwrap
RUNTIME_DEP_PKGS_CSWbacula-console += CSWncurses
RUNTIME_DEP_PKGS_CSWbacula-console += CSWzlib
RUNTIME_DEP_PKGS_CSWbacula-console += CSWlibintl8
RUNTIME_DEP_PKGS_CSWbacula-console += CSWreadline
RUNTIME_DEP_PKGS_CSWbacula-console += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWbacula-console += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWbacula-console += CSWgcc4g++rt
PKGFILES_CSWbacula-console  = .*sbin/bconsole .*man8/bconsole.* .*bconsole.conf.CSW
PKGFILES_CSWbacula-console += /etc/opt/csw/bacula/scripts/bconsole.CSW

CATALOGNAME_CSWbacula-client = bacula_client
SPKG_DESC_CSWbacula-client = $(DESCRIPTION) - Client meta-package
ARCHALL_CSWbacula-client = 1
RUNTIME_DEP_PKGS_CSWbacula-client += CSWbacula-fd
PKGFILES_CSWbacula-client = NOFILES
OBSOLETED_BY_CSWbacula-client = CSWbaculaclient CSWbaculagnome
CHECKPKG_OVERRIDES_CSWbacula-client += surplus-dependency|CSWbacula-fd

# set this explicitly to help phil's tools for now
CATALOGNAME_CSWbaculaclient = bacula_client_stub

SPKG_DESC_CSWbaculagnome = Obsolete bacula gnome console
CATALOGNAME_CSWbaculagnome = bacula_gnome_stub

CATALOGNAME_CSWbacula-doc = bacula_doc
SPKG_DESC_CSWbacula-doc = $(DESCRIPTION) - Documentation
PKGFILES_CSWbacula-doc += .*doc/$(NAME)/.*
ARCHALL_CSWbacula-doc = 1
CHECKPKG_OVERRIDES_CSWbacula-doc += file-with-bad-content
CHECKPKG_OVERRIDES_CSWbacula-doc += missing-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWbacula-doc += missing-dependency|CSWperl

CATALOGNAME_CSWbacula-tray-monitor = bacula_tray_monitor
SPKG_DESC_CSWbacula-tray-monitor = $(DESCRIPTION) - Tray monitor
OBSOLETED_BY_CSWbacula-tray-monitor = CSWbaculaclient
RUNTIME_DEP_PKGS_CSWbacula-tray-monitor += CSWbacula-common
RUNTIME_DEP_PKGS_CSWbacula-tray-monitor += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWbacula-tray-monitor += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWbacula-tray-monitor += CSWtcpwrap
RUNTIME_DEP_PKGS_CSWbacula-tray-monitor += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWbacula-tray-monitor += CSWlibintl8
RUNTIME_DEP_PKGS_CSWbacula-tray-monitor += CSWftype2
RUNTIME_DEP_PKGS_CSWbacula-tray-monitor += CSWzlib
RUNTIME_DEP_PKGS_CSWbacula-tray-monitor += CSWgtk2
RUNTIME_DEP_PKGS_CSWbacula-tray-monitor += CSWlibatk
RUNTIME_DEP_PKGS_CSWbacula-tray-monitor += CSWpango
RUNTIME_DEP_PKGS_CSWbacula-tray-monitor += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWbacula-tray-monitor += CSWfconfig
RUNTIME_DEP_PKGS_CSWbacula-tray-monitor += CSWglib2
PKGFILES_CSWbacula-tray-monitor = .*tray-monitor.*

CATALOGNAME_CSWbacula-common = bacula_common
SPKG_DESC_CSWbacula-common = $(DESCRIPTION) - shared files
RUNTIME_DEP_PKGS_CSWbacula-common += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWbacula-common += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWbacula-common += CSWlibmysqlclient18
RUNTIME_DEP_PKGS_CSWbacula-common += CSWlibintl8
RUNTIME_DEP_PKGS_CSWbacula-common += CSWtcpwrap
RUNTIME_DEP_PKGS_CSWbacula-common += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWbacula-common += CSWzlib
RUNTIME_DEP_PKGS_CSWbacula-common += CSWlibpython2-6-1-0
PKGFILES_CSWbacula-common += .*libbac-$(VERSION).so .*libbac.so
PKGFILES_CSWbacula-common +=  .*libbaccfg-$(VERSION).so .*libbaccfg.so
PKGFILES_CSWbacula-common += .*libbacfind-$(VERSION).so .*libbacfind.so
PKGFILES_CSWbacula-common += .*libbacpy-$(VERSION).so .*libbacpy.so
PKGFILES_CSWbacula-common += .*libbacsql-$(VERSION).so .*libbacsql.so
PKGFILES_CSWbacula-common += .*sbin/bsmtp .*sbin/btraceback
PKGFILES_CSWbacula-common += .*man1/bsmtp.1 .*man1/btraceback.1
PKGFILES_CSWbacula-common += .*man8/bacula.8
PKGFILES_CSWbacula-common += /etc/opt/csw//bacula/scripts/btraceback.*
CHECKPKG_OVERRIDES_CSWbacula-common += file-with-bad-content|/usr/share|root/opt/csw/share/man/man8/bacula.8

CATALOGNAME_CSWbacula-fd = bacula_fd
SPKG_DESC_CSWbacula-fd = $(DESCRIPTION) - File Daemon
RUNTIME_DEP_PKGS_CSWbacula-fd = CSWbacula-common
RUNTIME_DEP_PKGS_CSWbacula-fd += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWbacula-fd += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWbacula-fd += CSWtcpwrap
RUNTIME_DEP_PKGS_CSWbacula-fd += CSWlibintl8
RUNTIME_DEP_PKGS_CSWbacula-fd += CSWzlib
RUNTIME_DEP_PKGS_CSWbacula-fd += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWbacula-fd += CSWlibssl1-0-0
PKGFILES_CSWbacula-fd += .*init.d/cswbacula-fd
PKGFILES_CSWbacula-fd += .*/bpipe-fd.so .*sbin/bacula-fd .*bacula/working
PKGFILES_CSWbacula-fd += .*man8/bacula-fd.8 .*bacula/bacula-fd.conf.CSW
PKGFILES_CSWbacula-fd += /var/opt/csw/run
PKGFILES_CSWbacula-fd += .*bacula_fd/.*postmsg
PKGFILES_CSWbacula-fd += /etc/opt/csw/pkg/CSWbacula-fd/cswusergroup
PKGFILES_CSWbacula-fd += /etc/opt/csw/pkg/CSWbacula-fd/services

CATALOGNAME_CSWbacula-sd = bacula_sd
SPKG_DESC_CSWbacula-sd = $(DESCRIPTION) - Storage Daemon
RUNTIME_DEP_PKGS_CSWbacula-sd = CSWbacula-common
RUNTIME_DEP_PKGS_CSWbacula-sd += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWbacula-sd += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWbacula-sd += CSWlibmysqlclient18
RUNTIME_DEP_PKGS_CSWbacula-sd += CSWtcpwrap
RUNTIME_DEP_PKGS_CSWbacula-sd += CSWlibintl8
RUNTIME_DEP_PKGS_CSWbacula-sd += CSWzlib
RUNTIME_DEP_PKGS_CSWbacula-sd += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWbacula-sd += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWbacula-sd += CSWmtx
PKGFILES_CSWbacula-sd += .*init.d/cswbacula-sd
PKGFILES_CSWbacula-sd += /etc/opt/csw/bacula/.*disk-changer.CSW
PKGFILES_CSWbacula-sd += /etc/opt/csw/bacula/.*dvd-handler.CSW
PKGFILES_CSWbacula-sd += /etc/opt/csw/bacula/.*mtx-changer.*
PKGFILES_CSWbacula-sd += /etc/opt/csw/bacula/bacula-sd.conf.CSW
PKGFILES_CSWbacula-sd += /etc/opt/csw/bacula/mtx-changer.conf.CSW
PKGFILES_CSWbacula-sd += .*sbin/bacula-sd .*sbin/bextract .*sbin/bls
PKGFILES_CSWbacula-sd += .*sbin/bcopy .*sbin/bscan .*sbin/btape
PKGFILES_CSWbacula-sd += .*man8/bacula-sd.8 .*man8/bextract.8
PKGFILES_CSWbacula-sd += .*man8/bls.8 .*man8/btape.8 .*bacula/working
PKGFILES_CSWbacula-sd += .*man8/bcopy.8 .*man8/bscan.8
PKGFILES_CSWbacula-sd += /var/opt/csw/run
PKGFILES_CSWbacula-sd += $(localstatedir)/$(NAME)/archive
PKGFILES_CSWbacula-sd += .*bacula_sd/.*postmsg
PKGFILES_CSWbacula-sd += /etc/opt/csw/pkg/CSWbacula-sd/cswusergroup
PKGFILES_CSWbacula-sd += /etc/opt/csw/pkg/CSWbacula-sd/services
CHECKPKG_OVERRIDES_CSWbacula-sd += surplus-dependency|CSWmtx

CATALOGNAME_CSWbacula-director = bacula_director
SPKG_DESC_CSWbacula-director = $(DESCRIPTION) - Director
RUNTIME_DEP_PKGS_CSWbacula-director = CSWbacula-common
RUNTIME_DEP_PKGS_CSWbacula-director += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWbacula-director += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWbacula-director += CSWlibmysqlclient18
RUNTIME_DEP_PKGS_CSWbacula-director += CSWtcpwrap
RUNTIME_DEP_PKGS_CSWbacula-director += CSWlibintl8
RUNTIME_DEP_PKGS_CSWbacula-director += CSWzlib
RUNTIME_DEP_PKGS_CSWbacula-director += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWbacula-director += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWbacula-director += CSWperl
PKGFILES_CSWbacula-director += .*init.d/cswbacula-dir
PKGFILES_CSWbacula-director += .*sbin/bregex .*sbin/bwild .*sbin/bacula-dir
PKGFILES_CSWbacula-director += .*sbin/dbcheck .*bacula/working
PKGFILES_CSWbacula-director += /etc/opt/csw/bacula/scripts/catalog_backup.*
PKGFILES_CSWbacula-director += /etc/opt/csw/bacula/scripts/query.sql.CSW
PKGFILES_CSWbacula-director += /etc/opt/csw/bacula/.*_tables.CSW
PKGFILES_CSWbacula-director += /etc/opt/csw/bacula/.*_database.CSW
PKGFILES_CSWbacula-director += /etc/opt/csw/bacula/.*_privileges.CSW
PKGFILES_CSWbacula-director += /etc/opt/csw/bacula/.*_catalog.*CSW
PKGFILES_CSWbacula-director += /etc/opt/csw/bacula/scripts/update.*tables.*CSW
PKGFILES_CSWbacula-director += .*bacula/bacula-dir.conf.CSW
PKGFILES_CSWbacula-director += .*man8/bacula-dir.8 .*man8/dbcheck.8
PKGFILES_CSWbacula-director += /var/opt/csw/run
PKGFILES_CSWbacula-director += .*share/doc/bacula_director/README.CSW
PKGFILES_CSWbacula-director += .*bacula_director/.*postmsg
PKGFILES_CSWbacula-director += /etc/opt/csw/pkg/CSWbacula-director/cswusergroup
PKGFILES_CSWbacula-director += /etc/opt/csw/pkg/CSWbacula-director/services
# this is because the .pl script is .pl.CSW due to preserveconf
CHECKPKG_OVERRIDES_CSWbacula-director += surplus-dependency|CSWperl

# force libraries into a separate subdirectory
libdir = $(prefix)/lib/$(NAME)
sysconfdir = /etc$(prefix)/$(NAME)

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-working-dir=$(localstatedir)/$(NAME)/working
CONFIGURE_ARGS += --with-archivedir=$(localstatedir)/$(NAME)/archive
CONFIGURE_ARGS += --with-libiconv-prefix=$(prefix)
CONFIGURE_ARGS += --with-libintl-prefix=$(prefix)
CONFIGURE_ARGS += --disable-conio
CONFIGURE_ARGS += --enable-readline
CONFIGURE_ARGS += --with-readline=$(prefix)
CONFIGURE_ARGS += --with-python=$(prefix)
CONFIGURE_ARGS += --with-tcp-wrappers=$(prefix)
CONFIGURE_ARGS += --with-openssl=$(prefix)
CONFIGURE_ARGS += --with-mysql=$(prefix)
CONFIGURE_ARGS += --with-scriptdir=$(sysconfdir)/scripts
CONFIGURE_ARGS += --with-logdir=$(localstatedir)/log/$(NAME)
CONFIGURE_ARGS += --with-pid-dir=$(localstatedir)/run
CONFIGURE_ARGS += --with-subsys-dir=$(localstatedir)/run/subsys
CONFIGURE_ARGS += --enable-tray-monitor
# we add these so that our template configs change less over time
CONFIGURE_ARGS += --with-dir-password=S4B2ZIN1kBli3AtC0yPR7Iaw7EiIVCOsI9IOSF7HucND
CONFIGURE_ARGS += --with-fd-password=iUXtIn91oqxXhUHw9UmmdePGRaKn8aRXX8oX2e02BwCL
CONFIGURE_ARGS += --with-sd-password=h6F8l+Vkp8eiJpZclqqA/bpLD71bP8S+vMG01qxXzlrX
CONFIGURE_ARGS += --with-mon-dir-password=QhTqgNyq8s6l7RJc/+3NmVqQkyxkqlnaJLPwsZF7fXUp
CONFIGURE_ARGS += --with-mon-fd-password=IEKXaPXrRO8BzJYBJueDJgkVsXzR/1cVvPNGJhZPrsHB
CONFIGURE_ARGS += --with-mon-sd-password=e5fbjZnW+1hohTYFBfTXFe1KP7BIgCrAvY4fA4fg39TN
# don't run as root except for the file daemon which will need those privs
CONFIGURE_ARGS += --with-dir-user=bacula-dir
CONFIGURE_ARGS += --with-dir-group=bacula
CONFIGURE_ARGS += --with-sd-user=bacula-sd
CONFIGURE_ARGS += --with-sd-group=bacula

EXTRA_INC += $(includedir)/ncursesw
EXTRA_LIB += $(prefix)/lib/ncursesw
#EXTRA_LINKER_FLAGS = -norunpath

# no tests supplied.
TEST_SCRIPTS =

INITSMF = /etc/opt/csw/init.d/cswbacula-dir /etc/opt/csw/init.d/cswbacula-sd
INITSMF += /etc/opt/csw/init.d/cswbacula-fd

MIGRATE_FILES_CSWbacula-director = "query.sql bacula-dir.conf"
MIGRATE_FILES_CSWbacula-sd = "mtx-changer.conf bacula-sd.conf"
MIGRATE_FILES_CSWbacula-fd = "bacula-fd.conf"
MIGRATE_FILES_CSWbacula-console = "bconsole.conf"
MIGRATE_FILES_CSWbacula-tray-monitor = "tray-monitor.conf"

MIGRATE_SOURCE_DIR = /opt/csw/etc/bacula
MIGRATE_DEST_DIR = $(sysconfdir)
MIGRATE_DEST_DIR_mtx-changer_conf = $(sysconfdir)/scripts

PRESERVECONF = $(sysconfdir)/bacula-dir.conf $(sysconfdir)/bacula-sd.conf
PRESERVECONF += $(sysconfdir)/bacula-fd.conf $(sysconfdir)/bconsole.conf
PRESERVECONF += $(sysconfdir)/tray-monitor.conf
PRESERVECONF += $(sysconfdir)/scripts/bacula-ctl-fd
PRESERVECONF += $(sysconfdir)/scripts/btraceback.dbx
PRESERVECONF += $(sysconfdir)/scripts/grant_mysql_privileges
PRESERVECONF += $(sysconfdir)/scripts/drop_mysql_tables
PRESERVECONF += $(sysconfdir)/scripts/drop_bacula_tables
PRESERVECONF += $(sysconfdir)/scripts/stopmysql
PRESERVECONF += $(sysconfdir)/scripts/drop_bacula_database
PRESERVECONF += $(sysconfdir)/scripts/make_catalog_backup
PRESERVECONF += $(sysconfdir)/scripts/create_mysql_database
PRESERVECONF += $(sysconfdir)/scripts/startmysql
PRESERVECONF += $(sysconfdir)/scripts/delete_catalog_backup
PRESERVECONF += $(sysconfdir)/scripts/btraceback.mdb
PRESERVECONF += $(sysconfdir)/scripts/make_mysql_tables
PRESERVECONF += $(sysconfdir)/scripts/update_mysql_tables
PRESERVECONF += $(sysconfdir)/scripts/grant_bacula_privileges
PRESERVECONF += $(sysconfdir)/scripts/mtx-changer
PRESERVECONF += $(sysconfdir)/scripts/btraceback.gdb
PRESERVECONF += $(sysconfdir)/scripts/mtx-changer.conf
PRESERVECONF += $(sysconfdir)/scripts/update_mysql_tables_10_to_11
PRESERVECONF += $(sysconfdir)/scripts/disk-changer
PRESERVECONF += $(sysconfdir)/scripts/make_bacula_tables
PRESERVECONF += $(sysconfdir)/scripts/bacula-ctl-dir
PRESERVECONF += $(sysconfdir)/scripts/dvd-handler
PRESERVECONF += $(sysconfdir)/scripts/bacula-ctl-sd
PRESERVECONF += $(sysconfdir)/scripts/bacula_config
PRESERVECONF += $(sysconfdir)/scripts/bacula
PRESERVECONF += $(sysconfdir)/scripts/query.sql
PRESERVECONF += $(sysconfdir)/scripts/update_bacula_tables
PRESERVECONF += $(sysconfdir)/scripts/create_bacula_database
PRESERVECONF += $(sysconfdir)/scripts/drop_mysql_database
PRESERVECONF += $(sysconfdir)/scripts/make_catalog_backup.pl
PRESERVECONF += $(sysconfdir)/scripts/bconsole

USERGROUP += /etc/opt/csw/pkg/CSWbacula-director/cswusergroup
USERGROUP += /etc/opt/csw/pkg/CSWbacula-sd/cswusergroup
USERGROUP += /etc/opt/csw/pkg/CSWbacula-fd/cswusergroup

POSTMSG  = /opt/csw/share/doc/bacula_director/README.postmsg
POSTMSG += /opt/csw/share/doc/bacula_console/README.postmsg
POSTMSG += /opt/csw/share/doc/bacula_sd/README.postmsg
POSTMSG += /opt/csw/share/doc/bacula_fd/README.postmsg

ETCSERVICES  = /etc/opt/csw/pkg/CSWbacula-director/services
ETCSERVICES += /etc/opt/csw/pkg/CSWbacula-fd/services
ETCSERVICES += /etc/opt/csw/pkg/CSWbacula-sd/services

PROTOTYPE_MODIFIERS = usergroupfiles confgroup generalperms
PROTOTYPE_FILES_usergroupfiles = /var/opt/csw/bacula.*
PROTOTYPE_CLASS_usergroupfiles = ugfiles
PROTOTYPE_GROUP_usergroupfiles = bacula
PROTOTYPE_PERMS_usergroupfiles = 0770
PROTOTYPE_FILES_confgroup = /etc/opt/csw/bacula/.*conf
PROTOTYPE_CLASS_confgroup = cswpreserveconf
PROTOTYPE_GROUP_confgroup = bacula
PROTOTYPE_PERMS_confgroup = 0640
PROTOTYPE_FILES_generalperms = /opt/csw/sbin/.* /etc/opt/csw/bacula/scripts.*
PROTOTYPE_PERMS_generalperms = 0755

include gar/category.mk

pre-configure-modulated:
	@echo Re-generating configure so docdir works properly...
	@(cd $(WORKSRC); \
		autoconf --prepend-include=$(abspath $(WORKSRC))/autoconf \
			autoconf/configure.in > configure; \
        chmod 755 configure)
	@$(MAKECOOKIE)

post-install-modulated: DOCD=$(DESTDIR)$(docdir)/$(NAME)
post-install-modulated: INITD=$(DESTDIR)/etc/$(prefix)/init.d
post-install-modulated:
	@(cd $(WORKSRC)/platforms/solaris; \
		ginstall -d -m 0755 $(INITD); \
		for s in dir sd; do \
			(ggrep '^#' bacula-$$s; echo '#AUTOENABLE no'; ggrep -v '^#' bacula-$$s) > bacula-$$s.csw; \
			ginstall -m 0755 bacula-$$s.csw $(INITD)/cswbacula-$$s; \
		done; \
		ginstall -m 0755 bacula-fd $(INITD)/cswbacula-fd; \
		cd ../..; \
		ginstall -m 0755 updatedb/update_mysql_tables_10_to_11 $(DESTDIR)/etc/opt/csw/bacula/scripts; \
		gcp -pR examples $(DOCD); \
		ginstall -d -m 0755 $(DESTDIR)/var/opt/csw/run;)
	@(for p in console director sd fd; do \
		ginstall -d -m 0755 $(DOCD)_$$p; \
		ginstall -m 0644 $(WORKDIR)/postmsg $(DOCD)_$$p/README.postmsg; \
	done)
	@( cd $(DESTDIR)/etc/opt/csw/bacula; \
		perl -pi -e "s!<bacula-source>!$(docdir)/$(NAME)!" query.sql )
	@$(MAKECOOKIE)

post-merge:
	@echo Adding user/group creation info...
	@(cd $(PKGROOT)/etc/opt/csw; \
		mkdir -p pkg/CSWbacula-director; \
		echo "bacula-dir:bacula:Bacula Director:/var/opt/csw/bacula/:/bin/false:::NP" > pkg/CSWbacula-director/cswusergroup; \
		echo "bacula-dir 9101/tcp" > pkg/CSWbacula-director/services; \
		mkdir -p pkg/CSWbacula-sd; \
		echo "bacula-sd:bacula:Bacula Storage Daemon:/var/opt/csw/bacula/:/bin/false:::NP:sys" > pkg/CSWbacula-sd/cswusergroup; \
		echo "bacula-sd 9103/tcp" > pkg/CSWbacula-sd/services; \
		mkdir -p pkg/CSWbacula-fd; \
		echo ":bacula::::::" > pkg/CSWbacula-fd/cswusergroup; \
		echo "bacula-fd 9102/tcp" > pkg/CSWbacula-fd/services)
