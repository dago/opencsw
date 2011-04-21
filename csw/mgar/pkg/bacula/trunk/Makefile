# $Id$
NAME = bacula
VERSION = 5.0.3
CATEGORIES = apps

DESCRIPTION = The Open Source Network Backup Solution
define BLURB
Bacula is a set of Open Source, enterprise ready, computer programs that permit you (or the system administrator) to manage backup, recovery, and verification of computer data across a network of computers of different kinds. Bacula is relatively easy to use and efficient, while offering many advanced storage management features that make it easy to find and recover lost or damaged files. In technical terms, it is an Open Source, enterprise ready, network based backup program. 
endef

GARCOMPILER = GNU

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(DISTNAME).tar.gz
DISTFILES += CSWbacula-doc.cswreleasenotes
DISTFILES += README.CSW
DISTFILES += CSWbacula-director.postinstall
DISTFILES += CSWbacula-sd.postinstall
DISTFILES += CSWbacula-fd.postinstall
DISTFILES += CSWbacula-console.postinstall
DISTFILES += postmsg
PATCHFILES += 0001-Update-AC_INIT-use-to-make-configure-handle-docdir.patch
PATCHFILES += 0002-Clean-up-solaris-install-autostart-targets.patch

BUILD_DEP_PKGS  = CSWmysql5devel CSWiconv CSWtcpwrap CSWossldevel
BUILD_DEP_PKGS += CSWreadline CSWggettext-dev

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
RUNTIME_DEP_PKGS_CSWbacula-console = CSWbacula-common
RUNTIME_DEP_PKGS_CSWbacula-console += CSWtcpwrap
RUNTIME_DEP_PKGS_CSWbacula-console += CSWncurses
RUNTIME_DEP_PKGS_CSWbacula-console += CSWzlib
RUNTIME_DEP_PKGS_CSWbacula-console += CSWlibintl8
RUNTIME_DEP_PKGS_CSWbacula-console += CSWreadline
RUNTIME_DEP_PKGS_CSWbacula-console += CSWosslrt
RUNTIME_DEP_PKGS_CSWbacula-console += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWbacula-console += CSWgcc4g++rt
PKGFILES_CSWbacula-console  = .*sbin/bconsole .*man8/bconsole.* .*bconsole.conf.CSW
PKGFILES_CSWbacula-console += .*libexec.*bconsole

CATALOGNAME_CSWbacula-client = bacula_client
SPKG_DESC_CSWbacula-client = $(DESCRIPTION) - Client meta-package
ARCHALL_CSWbacula-client = 1
RUNTIME_DEP_PKGS_CSWbacula-client += CSWbacula-fd
PKGFILES_CSWbacula-client = NOFILES
OBSOLETED_BY_CSWbacula-client = CSWbaculaclient CSWbaculagnome
SPKG_DESC_CSWbaculagnome = Obsolete bacula gnome console
CATALOGNAME_CSWbaculagnome = bacula_gnome_stub
# set this explicitly to help phil's tools for now
CATALOGNAME_CSWbaculaclient = bacula_client_stub
CHECKPKG_OVERRIDES_CSWbacula-client += surplus-dependency|CSWbacula-fd

CATALOGNAME_CSWbacula-doc = bacula_doc
SPKG_DESC_CSWbacula-doc = $(DESCRIPTION) - Documentation
PKGFILES_CSWbacula-doc += .*doc/$(NAME)/.*
CHECKPKG_OVERRIDES_CSWbacula-doc += file-with-bad-content
CHECKPKG_OVERRIDES_CSWbacula-doc += missing-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWbacula-doc += missing-dependency|CSWperl

CATALOGNAME_CSWbacula-tray-monitor = bacula_tray_monitor
SPKG_DESC_CSWbacula-tray-monitor = $(DESCRIPTION) - Tray monitor
RUNTIME_DEP_PKGS_CSWbacula-tray-monitor += CSWbacula-common
RUNTIME_DEP_PKGS_CSWbacula-tray-monitor += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWbacula-tray-monitor += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWbacula-tray-monitor += CSWtcpwrap
RUNTIME_DEP_PKGS_CSWbacula-tray-monitor += CSWosslrt
RUNTIME_DEP_PKGS_CSWbacula-tray-monitor += CSWlibintl8
RUNTIME_DEP_PKGS_CSWbacula-tray-monitor += CSWftype2
RUNTIME_DEP_PKGS_CSWbacula-tray-monitor += CSWzlib
RUNTIME_DEP_PKGS_CSWbacula-tray-monitor += CSWgtk2
RUNTIME_DEP_PKGS_CSWbacula-tray-monitor += CSWlibatk
RUNTIME_DEP_PKGS_CSWbacula-tray-monitor += CSWpango
RUNTIME_DEP_PKGS_CSWbacula-tray-monitor += CSWlibcairo
RUNTIME_DEP_PKGS_CSWbacula-tray-monitor += CSWfconfig
RUNTIME_DEP_PKGS_CSWbacula-tray-monitor += CSWglib2
PKGFILES_CSWbacula-tray-monitor = .*tray-monitor.*

CATALOGNAME_CSWbacula-common = bacula_common
SPKG_DESC_CSWbacula-common = $(DESCRIPTION) - shared files
RUNTIME_DEP_PKGS_CSWbacula-common += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWbacula-common += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWbacula-common += CSWmysql5rt
RUNTIME_DEP_PKGS_CSWbacula-common += CSWlibintl8
RUNTIME_DEP_PKGS_CSWbacula-common += CSWtcpwrap
RUNTIME_DEP_PKGS_CSWbacula-common += CSWosslrt
RUNTIME_DEP_PKGS_CSWbacula-common += CSWzlib
RUNTIME_DEP_PKGS_CSWbacula-common += CSWlibpython2-6-1-0
PKGFILES_CSWbacula-common += .*libbac-$(VERSION).so .*libbac.so
PKGFILES_CSWbacula-common +=  .*libbaccfg-$(VERSION).so .*libbaccfg.so
PKGFILES_CSWbacula-common += .*libbacfind-$(VERSION).so .*libbacfind.so
PKGFILES_CSWbacula-common += .*libbacpy-$(VERSION).so .*libbacpy.so
PKGFILES_CSWbacula-common += .*libbacsql-$(VERSION).so .*libbacsql.so
PKGFILES_CSWbacula-common += .*sbin/bsmtp .*sbin/btraceback
PKGFILES_CSWbacula-common += .*man1/bsmtp.1.gz .*man1/btraceback.1.gz
PKGFILES_CSWbacula-common += .*man8/bacula.8.gz
PKGFILES_CSWbacula-common += .*libexec/btraceback.gdb

CATALOGNAME_CSWbacula-fd = bacula_fd
SPKG_DESC_CSWbacula-fd = $(DESCRIPTION) - File Daemon
RUNTIME_DEP_PKGS_CSWbacula-fd = CSWbacula-common
RUNTIME_DEP_PKGS_CSWbacula-fd += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWbacula-fd += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWbacula-fd += CSWtcpwrap
RUNTIME_DEP_PKGS_CSWbacula-fd += CSWlibintl8
RUNTIME_DEP_PKGS_CSWbacula-fd += CSWzlib
RUNTIME_DEP_PKGS_CSWbacula-fd += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWbacula-fd += CSWosslrt
PKGFILES_CSWbacula-fd += .*init.d/cswbacula-fd
PKGFILES_CSWbacula-fd += .*/bpipe-fd.so .*sbin/bacula-fd .*bacula/working
PKGFILES_CSWbacula-fd += .*man8/bacula-fd.8.gz .*bacula/bacula-fd.conf.CSW
PKGFILES_CSWbacula-fd += /var/opt/csw/run
PKGFILES_CSWbacula-fd += .*bacula_fd/.*postmsg

CATALOGNAME_CSWbacula-sd = bacula_sd
SPKG_DESC_CSWbacula-sd = $(DESCRIPTION) - Storage Daemon
RUNTIME_DEP_PKGS_CSWbacula-sd = CSWbacula-common
RUNTIME_DEP_PKGS_CSWbacula-sd += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWbacula-sd += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWbacula-sd += CSWmysql5rt
RUNTIME_DEP_PKGS_CSWbacula-sd += CSWtcpwrap
RUNTIME_DEP_PKGS_CSWbacula-sd += CSWlibintl8
RUNTIME_DEP_PKGS_CSWbacula-sd += CSWzlib
RUNTIME_DEP_PKGS_CSWbacula-sd += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWbacula-sd += CSWosslrt
PKGFILES_CSWbacula-sd += .*init.d/cswbacula-sd
PKGFILES_CSWbacula-sd += .*libexec.*disk-changer .*libexec.*dvd-handler
PKGFILES_CSWbacula-sd += .*libexec.*mtx-changer.* .*bacula/bacula-sd.conf.CSW
PKGFILES_CSWbacula-sd += /etc/opt/csw/bacula/mtx-changer.conf.CSW
PKGFILES_CSWbacula-sd += .*sbin/bacula-sd .*sbin/bextract .*sbin/bls
PKGFILES_CSWbacula-sd += .*sbin/bcopy .*sbin/bscan .*sbin/btape
PKGFILES_CSWbacula-sd += .*man8/bacula-sd.8.gz .*man8/bextract.8.gz
PKGFILES_CSWbacula-sd += .*man8/bls.8.gz .*man8/btape.8.gz .*bacula/working
PKGFILES_CSWbacula-sd += .*man8/bcopy.8.gz .*man8/bscan.8.gz
PKGFILES_CSWbacula-sd += /var/opt/csw/run
PKGFILES_CSWbacula-sd += $(localstatedir)/$(NAME)/archive
PKGFILES_CSWbacula-sd += .*bacula_sd/.*postmsg

CATALOGNAME_CSWbacula-director = bacula_director
SPKG_DESC_CSWbacula-director = $(DESCRIPTION) - Director
RUNTIME_DEP_PKGS_CSWbacula-director = CSWbacula-common
RUNTIME_DEP_PKGS_CSWbacula-director += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWbacula-director += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWbacula-director += CSWmysql5rt
RUNTIME_DEP_PKGS_CSWbacula-director += CSWtcpwrap
RUNTIME_DEP_PKGS_CSWbacula-director += CSWlibintl8
RUNTIME_DEP_PKGS_CSWbacula-director += CSWzlib
RUNTIME_DEP_PKGS_CSWbacula-director += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWbacula-director += CSWosslrt
RUNTIME_DEP_PKGS_CSWbacula-director += CSWperl
PKGFILES_CSWbacula-director += .*init.d/cswbacula-dir
PKGFILES_CSWbacula-director += .*sbin/bregex .*sbin/bwild .*sbin/bacula-dir
PKGFILES_CSWbacula-director += .*sbin/dbcheck .*bacula/working
PKGFILES_CSWbacula-director += .*libexec.*catalog_backup.* .*libexec.*query.sql
PKGFILES_CSWbacula-director += /etc/opt/csw/bacula/query.sql.CSW
PKGFILES_CSWbacula-director += .*libexec.*mysql_tables.*
PKGFILES_CSWbacula-director += .*bacula/bacula-dir.conf.CSW
PKGFILES_CSWbacula-director += .*man8/bacula-dir.8.gz .*man8/dbcheck.8.gz
PKGFILES_CSWbacula-director += /var/opt/csw/run
PKGFILES_CSWbacula-director += .*share/doc/bacula_director/README.CSW
PKGFILES_CSWbacula-director += .*bacula_director/.*postmsg

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
CONFIGURE_ARGS += --with-mysql=$(prefix)/mysql5
CONFIGURE_ARGS += --with-scriptdir=$(libexecdir_install)/$(NAME)
CONFIGURE_ARGS += --with-logdir=$(localstatedir)/log/$(NAME)
CONFIGURE_ARGS += --with-pid-dir=$(localstatedir)/run
CONFIGURE_ARGS += --with-subsys-dir=$(localstatedir)/run/subsys
CONFIGURE_ARGS += --enable-tray-monitor

EXTRA_INC += $(includedir)/ncursesw
EXTRA_LIB += $(prefix)/lib/ncursesw $(prefix)/mysql5/lib/mysql
EXTRA_LINKER_FLAGS = -norunpath

# no tests supplied.
TEST_SCRIPTS =

INITSMF = /etc/opt/csw/init.d/cswbacula-dir /etc/opt/csw/init.d/cswbacula-sd
INITSMF += /etc/opt/csw/init.d/cswbacula-fd

PRESERVECONF = $(sysconfdir)/bacula-dir.conf $(sysconfdir)/bacula-sd.conf
PRESERVECONF += $(sysconfdir)/bacula-fd.conf $(sysconfdir)/bconsole.conf
PRESERVECONF += $(sysconfdir)/mtx-changer.conf $(sysconfdir)/query.sql

POSTMSG  = /opt/csw/share/doc/bacula_director/README.postmsg
POSTMSG += /opt/csw/share/doc/bacula_console/README.postmsg
POSTMSG += /opt/csw/share/doc/bacula_sd/README.postmsg
POSTMSG += /opt/csw/share/doc/bacula_fd/README.postmsg

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
		(ggrep '^#' bacula-dir; echo '#AUTOENABLE no'; ggrep -v '^#' bacula-dir) > bacula-dir.csw; \
		ginstall -m 0755 bacula-dir.csw $(INITD)/cswbacula-dir; \
		for s in fd sd; do \
			ginstall -m 0755 bacula-$$s $(INITD)/cswbacula-$$s; \
		done; \
		cd ../..; \
		ginstall -m 0755 updatedb/update_mysql_tables_10_to_11 $(DESTDIR)$(prefix)/libexec/bacula; \
		gcp -pR examples $(DOCD); \
		ginstall -d -m 0755 $(DESTDIR)/var/opt/csw/run;)
	@(for p in console director sd fd; do \
		ginstall -d -m 0755 $(DOCD)_$$p; \
		ginstall -m 0644 $(WORKDIR)/postmsg $(DOCD)_$$p/README.postmsg; \
	done)
	@( cd $(DESTDIR)/opt/csw/libexec/bacula/; \
	   for f in mtx-changer.conf query.sql; do \
		mv $$f $(DESTDIR)/etc/opt/csw/bacula/$$f; \
		ln -s /etc/opt/csw/bacula/$$f $$f; \
	   done)
	@$(MAKECOOKIE)
