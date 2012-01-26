NAME = Cache-Cache
VERSION = 1.06
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = JSWARTZ

DESCRIPTION = Cache interface
define BLURB
  The Cache modules are designed to assist a developer in persisting data for
  a specified period of time. Often these modules are used in web applications
  to store data locally to save repeated and redundant expensive calls to
  remote machines or databases. People have also been known to use
  Cache::Cache for its straightforward interface in sharing data between runs
  of an application or invocations of a CGI-style script or simply as an easy
  to use abstraction of the filesystem or shared memory.
endef

PACKAGES = CSWpmcachecache
CATALOGNAME = pm_cachecache

DEP_PKGS = CSWpmdigestsha1 CSWpmerror CSWpmipcshrlite

ARCHALL = 1

CHECKPKG_OVERRIDES_CSWpmcachecache += surplus-dependency|CSWpmipcshrlite
CHECKPKG_OVERRIDES_CSWpmcachecache += surplus-dependency|CSWpmerror
CHECKPKG_OVERRIDES_CSWpmcachecache += surplus-dependency|CSWpmdigestsha1

include gar/category.mk
