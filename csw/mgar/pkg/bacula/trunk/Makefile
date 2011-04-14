# $Id$
NAME = bacula
VERSION = 5.0.3
CATEGORIES = apps

DESCRIPTION = The Open Source Network Backup Solution
define BLURB
Bacula is a set of Open Source, enterprise ready, computer programs that permit you (or the system administrator) to manage backup, recovery, and verification of computer data across a network of computers of different kinds. Bacula is relatively easy to use and efficient, while offering many advanced storage management features that make it easy to find and recover lost or damaged files. In technical terms, it is an Open Source, enterprise ready, network based backup program. 
endef

PACKAGES  = CSWbacula-common CSWbacula-fd CSWbacula-sd
PACKAGES += CSWbacula-director CSWbacula-client

CATALOG_NAME_CSWbacula-client = bacula_client
SPKG_DESC_CSWbacula-client = $(DESCRIPTION) - Client meta-package
RUNTIME_DEP_PKGS_CSWbacula-client += CSWbacula-fd
PKGFILES_CSWbacula-client = NOFILES
OBSOLETED_BY_CSWbacula-client = CSWbaculaclient
# set this explicitly to help phil's tools for now
CATALOG_NAME_CSWbaculaclient = bacula_client_stub

CATALOG_NAME_CSWbacula-common = bacula_common
SPKG_DESC_CSWbacula-common = $(DESCRIPTION) - shared files
RUNTIME_DEP_PKGS_CSWbacula-common += CSWmysql5rt
RUNTIME_DEP_PKGS_CSWbacula-common += CSWlibintl8
RUNTIME_DEP_PKGS_CSWbacula-common += CSWtcpwrap
RUNTIME_DEP_PKGS_CSWbacula-common += CSWosslrt
RUNTIME_DEP_PKGS_CSWbacula-common += CSWzlib
PKGFILES_CSWbacula-common += .*libbac-$(VERSION).so .*libbac.so
PKGFILES_CSWbacula-common +=  .*libbaccfg-$(VERSION).so .*libbaccfg.so
PKGFILES_CSWbacula-common += .*libbacfind-$(VERSION).so .*libbacfind.so
PKGFILES_CSWbacula-common += .*libbaccpy-$(VERSION).so .*libbaccpy.so
PKGFILES_CSWbacula-common += .*libbacsql-$(VERSION).so .*libbacsql.so
PKGFILES_CSWbacula-common += .*sbin/bsmtp .*sbin/btraceback
PKGFILES_CSWbacula-common += .*man1/bsmtp.1.gz .*man1/btraceback.1.gz
PKGFILES_CSWbacula-common += .*man8/bacula.8.gz
PKGFILES_CSWbacula-common += .*libexec/btraceback.gdb
CHECKPKG_OVERRIDES_CSWbacula-common += shared-lib-package-contains-so-symlink

CATALOG_NAME_CSWbacula-fd = bacula_fd
SPKG_DESC_CSWbacula-fd = $(DESCRIPTION) - File Daemon
RUNTIME_DEP_PKGS_CSWbacula-fd = CSWbacula-common
RUNTIME_DEP_PKGS_CSWbacula-fd += CSWtcpwrap
RUNTIME_DEP_PKGS_CSWbacula-fd += CSWlibintl8
RUNTIME_DEP_PKGS_CSWbacula-fd += CSWzlib
RUNTIME_DEP_PKGS_CSWbacula-fd += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWbacula-fd += CSWosslrt
PKGFILES_CSWbacula-fd += .*/bpipe-fd.so .*sbin/bacula-fd
PKGFILES_CSWbacula-fd += .*man8/bacula-fd.8.gz

CATALOG_NAME_CSWbacula-sd = bacula_sd
SPKG_DESC_CSWbacula-sd = $(DESCRIPTION) - Storage Daemon
RUNTIME_DEP_PKGS_CSWbacula-sd = CSWbacula-common
RUNTIME_DEP_PKGS_CSWbacula-sd += CSWmysql5rt
RUNTIME_DEP_PKGS_CSWbacula-sd += CSWtcpwrap
RUNTIME_DEP_PKGS_CSWbacula-sd += CSWlibintl8
RUNTIME_DEP_PKGS_CSWbacula-sd += CSWzlib
RUNTIME_DEP_PKGS_CSWbacula-sd += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWbacula-sd += CSWosslrt
PKGFILES_CSWbacula-sd += .*libexec.*disk-changer .*libexec.*dvd-handler
PKGFILES_CSWbacula-sd += .*libexec.*mtx-changer.*
PKGFILES_CSWbacula-sd += .*sbin/bacula-sd .*sbin/bextract .*sbin/bls
PKGFILES_CSWbacula-sd += .*sbin/bcopy .*sbin/bscan .*sbin/btape
PKGFILES_CSWbacula-sd += .*man8/bacula-sd.8.gz .*man8/bextract.8.gz
PKGFILES_CSWbacula-sd += .*man8/bls.8.gz .*man8/btape.8.gz
PKGFILES_CSWbacula-sd += .*man8/bcopy.8.gz .*man8/bscan.8.gz

CATALOG_NAME_CSWbacula-director = bacula_director
SPKG_DESC_CSWbacula-director = $(DESCRIPTION) - Director
RUNTIME_DEP_PKGS_CSWbacula-director = CSWbacula-common
RUNTIME_DEP_PKGS_CSWbacula-director += CSWmysql5rt
RUNTIME_DEP_PKGS_CSWbacula-director += CSWtcpwrap
RUNTIME_DEP_PKGS_CSWbacula-director += CSWlibintl8
RUNTIME_DEP_PKGS_CSWbacula-director += CSWzlib
RUNTIME_DEP_PKGS_CSWbacula-director += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWbacula-director += CSWosslrt
PKGFILES_CSWbacula-director += .*sbin/bregex .*sbin/bwild .*sbin/bacula-dir
PKGFILES_CSWbacula-director += .*sbin/dbcheck
PKGFILES_CSWbacula-director += .*libexec.*catalog_backup.* .*libexec.*query.sql
PKGFILES_CSWbacula-director += .*libexec.*mysql_tables.*
PKGFILES_CSWbacula-director += .*man8/bacula-dir.8.gz .*man8/dbcheck.8.gz

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(DISTNAME).tar.gz
DISTFILES += CSWbacula.cswreleasenotes
PATCHFILES += 0001-Update-AC_INIT-use-to-make-configure-handle-docdir.patch

BUILD_DEP_PKGS  = CSWmysql5devel CSWiconv CSWtcpwrap CSWossldevel
BUILD_DEP_PKGS += CSWreadline CSWggettext-dev

# force libraries into a separate subdirectory
libdir = $(prefix)/lib/$(NAME)

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-working-dir=$(localstatedir)/$(NAME)/working
CONFIGURE_ARGS += --with-libiconv-prefix=$(prefix)
CONFIGURE_ARGS += --with-libintl-prefix=$(prefix)
CONFIGURE_ARGS += --disable-conio
CONFIGURE_ARGS += --enable-readline
CONFIGURE_ARGS += --with-readline=$(prefix)
CONFIGURE_ARGS += --with-python=$(prefix)
CONFIGURE_ARGS += --with-tcp-wrappers=$(prefix)
CONFIGURE_ARGS += --with-openssl=$(prefix)
CONFIGURE_ARGS += --with-mysql=$(prefix)/mysql5
CONFIGURE_ARGS += --with-scriptdir=$(libexecdir_install)/$(NAME)
CONFIGURE_ARGS += --with-logdir=$(localstatedir)/log/$(NAME)
CONFIGURE_ARGS += --with-pid-dir=$(localstatedir)/run
CONFIGURE_ARGS += --with-subsys-dir=$(localstatedir)/run/subsys
CONFIGURE_ARGS += --enable-tray-monitor

EXTRA_INC += $(includedir)/ncursesw
EXTRA_LIB += $(libdir)/ncursesw $(prefix)/mysql5/lib/mysql
EXTRA_LINKER_FLAGS = -norunpath

# no tests supplied.
TEST_SCRIPTS =

# these are both original documentation files from the tarball
CHECKPKG_OVERRIDES_CSWbacula += file-with-bad-content|/usr/share|root/opt/csw/share/doc/bacula/technotes
CHECKPKG_OVERRIDES_CSWbacula += file-with-bad-content|/usr/local|root/opt/csw/share/doc/bacula/INSTALL

include gar/category.mk

pre-configure-modulated:
	@echo Re-generating configure so docdir works properly...
	@(cd $(WORKSRC); \
		autoconf --prepend-include=$(abspath $(WORKSRC))/autoconf \
			autoconf/configure.in > configure; \
        chmod 755 configure)
	@$(MAKECOOKIE)

post-merge:
	@(cd $(PKGROOT); rmdir tmp)
	@$(MAKECOOKIE)
