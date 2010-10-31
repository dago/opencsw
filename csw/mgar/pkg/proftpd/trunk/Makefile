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

RUNTIME_DEP_PKGS = CSWosslrt CSWggettextrt CSWiconv CSWgcc3corert CSWoldaprt CSWzlib CSWmysql5rt

PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386

EXTRA_BUILD_ISAS_i386  = pentium_pro
EXTRA_BUILD_ISAS_sparc = sparcv9

MYSQLISA_pentium_pro  = i386
MYSQLISA_$(ISA)      ?= $(ISA)
MYSQLISA              = $(MYSQLISA_$(ISA))

sysconfdir=/etc/opt/csw
localstatedir=/var/opt/csw

CONFIGURE_ENV   = install_user=$(USER) install_group=csw
CONFIGURE_ENV  += CFLAGS="$(CFLAGS)" LDFLAGS="$(LDFLAGS)"
LD_OPTIONS     += -R$(prefix)/mysql5/lib/mysql/\$$ISALIST

CONFIGURE_ARGS += --prefix=$(prefix)
CONFIGURE_ARGS += --sysconfdir=$(sysconfdir)
CONFIGURE_ARGS += --localstatedir=/var/run/proftpd
CONFIGURE_ARGS += --mandir=$(prefix)/share/man
CONFIGURE_ARGS += --libexecdir=$(prefix)/lib/proftpd
CONFIGURE_ARGS += --enable-dso --disable-static
CONFIGURE_ARGS += --enable-facl
CONFIGURE_ARGS += --enable-openssl
CONFIGURE_ARGS += --enable-sendfile
CONFIGURE_ARGS += --enable-nls
CONFIGURE_ARGS += --enable-ctrls
CONFIGURE_ARGS += --enable-buffer-size=8192
CONFIGURE_ARGS += --with-includes=$(prefix)/include:$(prefix)/include/openssl:$(prefix)/include/mysql
CONFIGURE_ARGS += --with-libraries=$(prefix)/lib/mysql/$(MYSQLISA)
CONFIGURE_ARGS += --with-modules=mod_auth_pam:mod_tls:mod_tls_shmcache:mod_wrap2
CONFIGURE_ARGS += --with-shared=mod_ban:mod_ctrls_admin:mod_ifsession:mod_ldap:mod_radius:mod_ratio:mod_readme:mod_rewrite:mod_shaper:mod_sql:mod_sql_mysql:mod_wrap2_file

TEST_SCRIPTS =

INITSMF      = $(sysconfdir)/init.d/cswproftpd
PRESERVECONF = $(sysconfdir)/proftpd.conf

PROFTPDDOC   = doc sample-configurations COPYING NEWS README RELEASE_NOTES


include gar/category.mk

post-install-modulated:
	ginstall -d $(DESTDIR)$(sysconfdir)/init.d
	ginstall -d $(DESTDIR)$(prefix)/share/doc/proftpd
	ginstall -d $(DESTDIR)$(localstatedir)/proftpd
	ginstall -d $(DESTDIR)$(localstatedir)/proftpd/logs
	cp $(WORKDIR)/cswproftpd $(DESTDIR)$(sysconfdir)/init.d/
	cd $(WORKSRC); cp -r $(PROFTPDDOC) $(DESTDIR)$(prefix)/share/doc/proftpd
	$(MAKECOOKIE)
