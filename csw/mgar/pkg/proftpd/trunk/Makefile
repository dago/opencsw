GARNAME = proftpd
GARVERSION = 1.3.3c
CATEGORIES = server

GARCOMPILER = GCC3

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
DISTFILES    = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES   += cswproftpd

LICENSE      = COPYING

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

RUNTIME_DEP_PKGS = CSWosslrt CSWggettextrt CSWiconv CSWgcc3corert CSWoldaprt CSWzlib CSWmysql5rt CSWsqlite3rt

EXTRA_BUILD_ISAS_i386  = pentium_pro
EXTRA_BUILD_ISAS_sparc = sparcv9

ISAEXEC_DIRS           = $(bindir) $(sbindir)
ISAEXEC_EXCLUDE_FILES  = $(bindir)/ftpasswd $(bindir)/ftpmail $(bindir)/ftpquota $(bindir)/prxs

PR_LIBEXEC_sparcv8    = $(prefix)/lib/proftpd
PR_LIBEXEC_i386       = $(prefix)/lib/proftpd
PR_LIBEXEC_$(ISA)    ?= $(prefix)/lib/$(ISA)/proftpd
PR_LIBEXEC            = $(PR_LIBEXEC_$(ISA))

sysconfdir      = /etc/opt/csw
localstatedir   = /var/opt/csw

MIGRATE_FILES   = proftpd.conf

CONFIGURE_ENV   = install_user=$(USER) install_group=csw
CONFIGURE_ENV  += CFLAGS="$(CFLAGS)" LDFLAGS="$(LDFLAGS)"
EXTRA_LIB       = $(prefix)/mysql5/lib/mysql

NODIRPATHS      = --localstatedir --libexecdir
CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --libexecdir=$(PR_LIBEXEC)
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
	ginstall -d $(DESTDIR)$(prefix)/share/doc/proftpd
	ginstall -d $(DESTDIR)$(localstatedir)/proftpd
	ginstall -d $(DESTDIR)$(localstatedir)/proftpd/logs
	cp $(WORKDIR)/cswproftpd $(DESTDIR)$(sysconfdir)/init.d/
	cd $(WORKSRC); cp -r $(PROFTPDDOC) $(DESTDIR)$(prefix)/share/doc/proftpd
	cd $(WORKSRC)/contrib ; cp $(CONTRIBUTILS) $(DESTDIR)$(bindir)
	rm -f $(DESTDIR)$(libexecdir_install)/*.la
	rm -f $(DESTDIR)$(libexecdir_install)/$(ISA)/*.la
	$(MAKECOOKIE)
