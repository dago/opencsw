GARNAME = libksba
GARVERSION = 1.0.6
CATEGORIES = lib

DESCRIPTION = Libksba is a CMS and X.509 access library
define BLURB
  Libksba is a library to make the tasks of working with X.509 certificates,
  CMS data and related objects more easy. It provides a highlevel interface
  to the implemented protocols and presents the data in a consistent way.
  There is no more need to worry about all the nasty details of the protocols. 
endef

MASTER_SITES = ftp://ftp.gnupg.org/gcrypt/libksba/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARVERSION)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL = http://www.gnupg.org/related_software/libksba/

REQUIRED_PKGS = CSWgpgerr

BUILD64 = 1
NO_ISAEXEC = 1

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
