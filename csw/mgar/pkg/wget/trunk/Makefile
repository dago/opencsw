GARNAME = wget
GARVERSION = 1.11.4
CATEGORIES = net

DESCRIPTION = A network utility to retrieve files from the Web.
define BLURB
  GNU Wget is a utility for noninteractive download of files from the Web. It
  supports HTTP and FTP protocols, as well as retrieval through HTTP proxies. It
  can follow HTML links, download many pages, and convert the links for local
  viewing. It can also mirror FTP hierarchies or only those files that have
  changed. Wget has been designed for robustness over slow network connections;
  if a download fails due to a network problem, it will keep retrying until the
  whole file has been retrieved.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWwget)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-ssl
CONFIGURE_ARGS += --disable-nls

REQUIRED_PKGS = CSWosslrt

TEST_TARGET = check

include gar/category.mk
