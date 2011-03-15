NAME = proftpd
VERSION = 1.3.3d
CATEGORIES = server

DESCRIPTION = Advanced, incredibly configurable and secure FTP daemon
define BLURB
  ProFTPD is a proven, high-performance, scalable FTP server written from
  scratch, with a focus toward simplicity, security, and ease of configuration.
  Naturally, ProFTPD powers some of the largest sites on the Internet. It
  features a very Apache-like configuration syntax, modules, and a highly
  customizable server infrastructure, including support for multiple 'virtual'
  FTP servers, anonymous FTP, and permission-based directory visibility.
endef

MASTER_SITES = ftp://ftp.proftpd.org/distrib/source/
DISTFILES    = $(NAME)-$(VERSION).tar.bz2
DISTFILES   += cswproftpd

LICENSE      = COPYING

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

RUNTIME_DEP_PKGS = CSWosslrt CSWggettextrt CSWiconv CSWoldaprt CSWzlib CSWmysql5rt CSWsqlite3rt

EXTRA_BUILD_ISAS_i386  = amd64
EXTRA_BUILD_ISAS_sparc = sparcv9

ISAEXEC_DIRS                 = $(bindir) $(sbindir)
EXTRA_ISAEXEC_EXCLUDE_FILES  = $(bindir)/ftpasswd $(bindir)/ftpmail $(bindir)/ftpquota $(bindir)/prxs

EXTRA_MERGE_EXCLUDE_FILES_isa-amd64   = $(prefix)/bin/amd64/ftpasswd $(prefix)/bin/amd64/ftpmail $(prefix)/bin/amd64/ftpquota $(prefix)/bin/amd64/prxs
EXTRA_MERGE_EXCLUDE_FILES_isa-sparcv9 = $(prefix)/bin/sparcv9/ftpasswd $(prefix)/bin/sparcv9/ftpmail $(prefix)/bin/sparcv9/ftpquota $(prefix)/bin/sparcv9/prxs

sysconfdir      = /etc/opt/csw
localstatedir   = /var/opt/csw

MIGRATE_FILES   = proftpd.conf

CONFIGURE_ENV   = install_user=$(USER) install_group=csw
CONFIGURE_ENV  += CFLAGS="$(CFLAGS)" LDFLAGS="$(LDFLAGS)"
CONFIGURE_ENV  += LD_LIBRARY_PATH="$(libdir)"
EXTRA_LIB       = $(prefix)/mysql5/lib/mysql

NODIRPATHS      = --localstatedir --libexecdir
CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --libexecdir=$(libdir)/proftpd
CONFIGURE_ARGS += --localstatedir=/var/run/proftpd
CONFIGURE_ARGS += --enable-dso --disable-static
CONFIGURE_ARGS += --enable-facl
CONFIGURE_ARGS += --enable-openssl
CONFIGURE_ARGS += --enable-sendfile
CONFIGURE_ARGS += --enable-nls
CONFIGURE_ARGS += --enable-ctrls
CONFIGURE_ARGS += --enable-buffer-size=8192
CONFIGURE_ARGS += --with-includes=$(prefix)/include:$(prefix)/include/openssl:$(prefix)/include/mysql
CONFIGURE_ARGS += --with-modules=mod_facl
CONFIGURE_ARGS += --with-shared=mod_auth_pam:mod_ban:mod_ctrls_admin:mod_dynmasq:mod_exec:mod_ident:mod_ifsession:mod_ldap:mod_load:mod_quotatab:mod_quotatab_file:mod_quotatab_ldap:mod_quotatab_radius:mod_quotatab_sql:mod_radius:mod_ratio:mod_readme:mod_rewrite:mod_sftp:mod_sftp_pam:mod_sftp_sql:mod_shaper:mod_site_misc:mod_sql:mod_sql_mysql:mod_sql_passwd:mod_sql_sqlite:mod_tls:mod_tls_shmcache:mod_unique_id:mod_wrap2:mod_wrap2_file:mod_wrap2_sql

TEST_SCRIPTS =

INITSMF      = $(sysconfdir)/init.d/cswproftpd
PRESERVECONF = $(sysconfdir)/proftpd.conf

PROFTPDDOC   = doc sample-configurations COPYING NEWS README RELEASE_NOTES
CONTRIBUTILS = ftpasswd ftpmail ftpquota

include gar/category.mk

post-configure-modulated:
	gsed -i s/\^LDFLAGS=/#LDFLAGS=/ $(WORKSRC)/contrib/mod_load/Makefile
	gsed -i s/\^LDFLAGS=/#LDFLAGS=/ $(WORKSRC)/contrib/mod_sftp/Makefile
	gsed -i s/\^LDFLAGS=/#LDFLAGS=/ $(WORKSRC)/contrib/mod_wrap2/Makefile
	$(MAKECOOKIE)

post-install-modulated:
	ginstall -d $(DESTDIR)$(sysconfdir)/init.d
	ginstall -d $(DESTDIR)$(docdir)/proftpd
	ginstall -d $(DESTDIR)$(localstatedir)/proftpd
	ginstall -d $(DESTDIR)$(localstatedir)/proftpd/logs
	cp $(WORKDIR)/cswproftpd $(DESTDIR)$(sysconfdir)/init.d/
	cd $(WORKSRC); cp -r $(PROFTPDDOC) $(DESTDIR)$(docdir)/proftpd
	cd $(WORKSRC)/contrib ; cp $(CONTRIBUTILS) $(DESTDIR)$(bindir)
	rm -f $(DESTDIR)$(libdir)/proftpd/*.la
	$(MAKECOOKIE)
