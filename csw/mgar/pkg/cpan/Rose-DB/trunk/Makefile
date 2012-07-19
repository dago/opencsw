NAME = Rose-DB
VERSION = 0.769
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = JSIRACUSA

DESCRIPTION = A DBI wrapper and abstraction layer
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE_TEXT = This module is licensed under the perl license, please see for details http://dev.perl.org/licenses/

PACKAGES += CSWpm-rose-db
CATALOGNAME_CSWpm-rose-db = pm_rose_db
SPKG_DESC_CSWpm-rose-db = A DBI wrapper and abstraction layer
ARCHALL_CSWpm-rose-db = 1
RUNTIME_DEP_PKGS_CSWpm-rose-db += CSWpm-datetime-format-mysql
RUNTIME_DEP_PKGS_CSWpm-rose-db += CSWpm-dbi
RUNTIME_DEP_PKGS_CSWpm-rose-db += CSWpm-datetime-format-pg
RUNTIME_DEP_PKGS_CSWpm-rose-db += CSWpm-bit-vector
RUNTIME_DEP_PKGS_CSWpm-rose-db += CSWpm-datetime-format-oracle
RUNTIME_DEP_PKGS_CSWpm-rose-db += CSWpm-rose-datetime
RUNTIME_DEP_PKGS_CSWpm-rose-db += CSWpm-time-clock
RUNTIME_DEP_PKGS_CSWpm-rose-db += CSWpm-datetime
RUNTIME_DEP_PKGS_CSWpm-rose-db += CSWpm-clone-pp
RUNTIME_DEP_PKGS_CSWpm-rose-db += CSWpm-sql-reservedwords
RUNTIME_DEP_PKGS_CSWpm-rose-db += CSWpm-rose-object

# These are only comments
CHECKPKG_OVERRIDES_CSWpm-rose-db += file-with-bad-content|/usr/local|root/opt/csw/share/man/man3/Rose::DB.3perl
CHECKPKG_OVERRIDES_CSWpm-rose-db += file-with-bad-content|/usr/local|root/opt/csw/share/perl/csw/Rose/DB.pm

include gar/category.mk
