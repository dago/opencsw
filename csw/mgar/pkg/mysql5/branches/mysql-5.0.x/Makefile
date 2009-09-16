GARNAME = mysql5
GARVERSION = 5.0.84
CATEGORIES = server

DISTNAME = mysql-$(GARVERSION)

DESCRIPTION = Multithreaded SQL database
define BLURB
  MySQL is a very fast, multi-threaded, multi-user and robust SQL
  (Structured Query Language) database server.
endef

# Change prefix to /opt/csw/mysql5
prefix = /opt/csw/mysql5
sysconfdir = /etc/opt/csw/mysql5
localstatedir = /var/opt/csw/mysql5

INITSMF = $(sysconfdir)/init\.d/cswmysql5

PATCHFILES  = 0001-Use-libc-not-libcrypt.patch
PATCHFILES += 0002-cast-user_info-pw_gid-to-gid_t.patch
PATCHFILES += 0003-OpenCSW-perl-for-tests.patch
PATCHFILES += 0004-basedir-and-datadir-in-the-cnf-files.patch

PACKAGES  = CSWmysql5 CSWmysql5bench CSWmysql5client CSWmysql5devel
PACKAGES += CSWmysql5rt CSWmysql5test

CATALOGNAME_CSWmysql5       = $(GARNAME)
CATALOGNAME_CSWmysql5bench  = $(GARNAME)bench
CATALOGNAME_CSWmysql5client = $(GARNAME)client
CATALOGNAME_CSWmysql5devel  = $(GARNAME)devel
CATALOGNAME_CSWmysql5rt     = $(GARNAME)rt
CATALOGNAME_CSWmysql5test   = $(GARNAME)test

SPKG_DESC_CSWmysql5       = Multithreaded SQL database
SPKG_DESC_CSWmysql5bench  = MySQL 5 benchmarking
SPKG_DESC_CSWmysql5client = MySQL 5 client binaries
SPKG_DESC_CSWmysql5devel  = MySQL 5 header files
SPKG_DESC_CSWmysql5rt     = MySQL 5 runtime files
SPKG_DESC_CSWmysql5test   = MySQL 5 testing files

support64 = (/(amd64|i386))?
PKGFILES_CSWmysql5client  = $(bindir)
PKGFILES_CSWmysql5client += $(bindir)$(support64)/myisam(log|pack)
PKGFILES_CSWmysql5client += $(bindir)$(support64)/mysql
PKGFILES_CSWmysql5client += $(bindir)$(support64)/mysql_client_test
PKGFILES_CSWmysql5client += $(bindir)$(support64)/mysql(_zap|access|admin|binlog|check)
PKGFILES_CSWmysql5client += $(bindir)$(support64)/mysql(dump|hotcopy|import|show)
PKGFILES_CSWmysql5client += $(bindir)$(support64)/(perror|replace)
PKGFILES_CSWmysql5client += $(mandir)/man1/mysql(|\_zap|access|admin|dump|show)\.1
PKGFILES_CSWmysql5client += $(mandir)/man1/(perror|replace)\.1
PKGFILES_CSWmysql5devel   = $(prefix)/include.*
PKGFILES_CSWmysql5devel  += $(bindir)$(support64)/mysql_config
PKGFILES_CSWmysql5devel  += $(mandir)/man1/mysql_config\.1
PKGFILES_CSWmysql5rt      = $(prefix)/lib/.*\.so.*
PKGFILES_CSWmysql5bench   = $(prefix)/sql-bench.*
PKGFILES_CSWmysql5test    = $(prefix)/mysql-test.*

REQUIRED_PKGS_CSWmysql5client = CSWmysql5rt

MASTER_SITES = ftp://mirror.switch.ch/mirror/mysql/Downloads/MySQL-5.0/
DISTFILES  = mysql-$(GARVERSION).tar.gz
DISTFILES += cswmysql5 quick_start-csw README.CSW


# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS = CSWncurses CSWzlib
PREREQUISITE_PKGS = $(REQUIRED_PKGS)

# because we alter the prefix.  this gets us proper linking as well as
# LD_OPTIONS (RPATH)
EXTRA_LIB = /opt/csw/lib
EXTRA_INC = /opt/csw/include
EXTRA_CFLAGS = -mt -D_POSIX_C_SOURCE=199506L -D__EXTENSIONS__
EXTRA_CXXFLAGS = -mt -D_POSIX_C_SOURCE=199506L -D__EXTENSIONS__

# Set ./configure options
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-assembler
CONFIGURE_ARGS += --without-docs
CONFIGURE_ARGS += --enable-local-infile
CONFIGURE_ARGS += --with-extra-charsets=all
CONFIGURE_ARGS += --with-low-memory
CONFIGURE_ARGS += --with-pthread
CONFIGURE_ARGS += --with-readline
CONFIGURE_ARGS += --with-zlib-dir=/opt/csw
CONFIGURE_ARGS += --with-ssl=/opt/csw
CONFIGURE_ARGS += --with-plugins=max-no-ndb

TEST_SCRIPTS =

# Enable 64 bits build
BUILD64 = 1

include gar/category.mk

post-install-modulated:
	ginstall -m 755 -d $(DESTDIR)$(localstatedir)
	ginstall -m 755 -d $(DESTDIR)$(datadir)/mysql5/doc
	ginstall -m 644 $(FILEDIR)/README.CSW $(DESTDIR)$(datadir)/mysql5/doc
	ginstall -m 755 -d $(DESTDIR)/opt/csw/share/mysql5/doc
	ln -s ../../../mysql5/share/mysql5/doc/README.CSW \
		$(DESTDIR)/opt/csw/share/mysql5/doc/README.CSW
	ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/init.d
	ginstall -m 755 $(FILEDIR)/cswmysql5 $(DESTDIR)/etc/opt/csw/init.d
	ginstall -m 755 $(FILEDIR)/quick_start-csw $(DESTDIR)$(datadir)/mysql5
	@$(MAKECOOKIE)
