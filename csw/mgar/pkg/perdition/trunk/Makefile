# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! build state unknown, work in progress, please verify
#
GARNAME = perdition
GARVERSION = 1.18
CATEGORIES = server

DESCRIPTION = POP3 and IMAP4 proxy server with high capacity in mind.
define BLURB
  Perdition is a fully featured POP3 and IMAP4 proxy server. It is able to
  handle both SSL and non-SSL connections and redirect users to a
  real-server based on a database lookup. Perdition supports modular based
  database access. ODBC, MySQL, PostgreSQL, GDBM, POSIX Regular Expression
  and NIS modules ship with the distribution. The API for modules is open
  allowing arbitrary modules to be written to allow access to any data
  store. 
endef

VENDOR_URL   = http://horms.net/projects/perdition/
MASTER_SITES = http://horms.net/projects/perdition/download/$(GARVERSION)/
DISTFILES    = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = (\d+(?:\.\d+)*)
UPSTREAM_MASTER_SITES = http://horms.net/projects/perdition/download/

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
