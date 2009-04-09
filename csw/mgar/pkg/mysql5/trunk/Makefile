GARNAME = mysql5
GARVERSION = 5.1.32
CATEGORIES = server

GARCOMPILER = GCC4

DESCRIPTION = Multithreaded SQL database
define BLURB
  MySQL is a very fast, multi-threaded, multi-user and robust SQL
  (Structured Query Language) database server.
endef

MASTER_SITES = ftp://mirror.switch.ch/mirror/mysql/Downloads/MySQL-5.1/
DISTFILES  = mysql-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWmysql5,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# Change prefix to /opt/csw/mysql5
prefix = /opt/csw/mysql5

WORKSRC = $(WORKDIR)/mysql-$(GARVERSION)

EXTRA_LIB = /opt/csw/lib

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

# Enable 64 bits build
# BUILD64 = 1

include gar/category.mk

