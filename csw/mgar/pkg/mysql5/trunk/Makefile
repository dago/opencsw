GARNAME = mysql5
GARVERSION = 5.1.32
CATEGORIES = server

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

# Set ./configure options
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-assembler
CONFIGURE_ARGS += --without-docs 
CONFIGURE_ARGS += --enable-thread-safe-client 
CONFIGURE_ARGS += --with-named-z-libs=yes 
CONFIGURE_ARGS += --with-berkeley-db 
CONFIGURE_ARGS += --with-innodb 
CONFIGURE_ARGS += --enable-local-infile 
CONFIGURE_ARGS += --with-extra-charsets=all 
CONFIGURE_ARGS += --with-low-memory

# Enable 64 bits build
# BUILD64 = 1

include gar/category.mk

post-extract:
	@for i in $(WORKROOTDIR)/build-isa* ; do mv $$i/mysql-$(GARVERSION) $$i/$(GARNAME)-$(GARVERSION) ; done 
	@$(MAKECOOKIE)
