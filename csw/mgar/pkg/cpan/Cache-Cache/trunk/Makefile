GARNAME = Cache-Cache
GARVERSION = 1.05
CATEGORIES = cpan
AUTHOR = DCLINTON

DESCRIPTION = cache interface
define BLURB
  The Cache modules are designed to assist a developer in persisting data for
  a specified period of time. Often these modules are used in web applications
  to store data locally to save repeated and redundant expensive calls to
  remote machines or databases. People have also been known to use
  Cache::Cache for its straightforward interface in sharing data between runs
  of an application or invocations of a CGI-style script or simply as an easy
  to use abstraction of the filesystem or shared memory.
endef

DISTFILES += CSWpmcachecache.gspec CSWpmcachecache.depend

DEPENDS += cpan/Digest-SHA1 cpan/IPC-ShareLite cpan/Error

include gar/category.mk
