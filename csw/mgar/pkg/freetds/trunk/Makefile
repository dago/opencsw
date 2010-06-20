# $Id$
GARNAME = freetds
GARVERSION = 0.82
CATEGORIES = lib

DESCRIPTION = Implementation of the TDS protocol used by MS SQL Server and Sybase
define BLURB
  FreeTDS is a set of libraries for Unix and Linux that allows your programs
  to natively talk to Microsoft SQL Server and Sybase databases.
endef

MASTER_SITES = http://ftp.ibiblio.org/pub/Linux/ALPHA/freetds/stable/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

DEP_PKGS = CSWunixodbc CSWiconv CSWreadline CSWncurses

sysconfdir = /etc/opt/csw

BUILD64 = 1
NOISAEXEC = 1
CONFIGURE_ARGS = $(DIRPATHS)

MERGE_DIRS_isa-extra = $(libdir)

EXTRA_PAX_ARGS = '-s,/doc/$(GARNAME)-$(GARVERSION),/doc/$(GARNAME),p'

PRESERVECONF = $(addprefix $(sysconfdir)/,freetds.conf locales.conf pool.conf)
MIGRATE_FILES = freetds.conf locales.conf pool.conf

include gar/category.mk

post-configure-modulated:
	@# Use latest libtool, the one shipped is too old
	cp $(bindir_install)/libtool $(WORKSRC)/libtool
	@$(MAKECOOKIE)
