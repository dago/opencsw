GARNAME = mysql5
GARVERSION = 5.1.32
CATEGORIES = server

DESCRIPTION = Multithreaded SQL database
define BLURB
  MySQL is a very fast, multi-threaded, multi-user and robust SQL
  (Structured Query Language) database server.
endef

MASTER_SITES = ftp://mirror.switch.ch/mirror/mysql/Downloads/MySQL-5.1
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWmysql5,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
