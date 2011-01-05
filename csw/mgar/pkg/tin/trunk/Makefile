NAME = tin
VERSION = 1.9.6
CATEGORIES = net

DESCRIPTION = Terminal-based news reader
define BLURB
  tin is an easy-to-use USENET news reader for the console using NNTP.
  It supports threading, scoring, different charsets, and many other
  useful things. It has also support for different languages.
endef

MASTER_SITES = ftp://ftp.tin.org/pub/news/clients/tin/unstable/
DISTFILES = $(NAME)-$(VERSION).tar.gz
DISTFILES += COPYING
PATCHFILES = configure.patch

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS_CSWtin += CSWpcrert
RUNTIME_DEP_PKGS_CSWtin += CSWggettextrt
RUNTIME_DEP_PKGS_CSWtin += CSWperl
RUNTIME_DEP_PKGS_CSWtin += CSWlibidn
RUNTIME_DEP_PKGS_CSWtin += CSWlibicu46
RUNTIME_DEP_PKGS_CSWtin += CSWiconv
RUNTIME_DEP_PKGS_CSWtin += CSWncurses
RUNTIME_DEP_PKGS_CSWtin += CSWlibgsasl7

BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS) CSWpcre

VENDOR_URL = http://www.tin.org/

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-coffee
CONFIGURE_ARGS += --enable-ipv6
CONFIGURE_ARGS += --with-screen=ncursesw --with-curses-dir=$(prefix)
CONFIGURE_ARGS += --with-pcre=$(prefix)
CONFIGURE_ARGS += --x-includes=/usr/openwin/include
CONFIGURE_ARGS += --x-libraries=/usr/openwin/lib 
CONFIGURE_ARGS += --with-x --with-Xaw3d
CONFIGURE_ARGS += --with-libdir=$(libdir)/news
CONFIGURE_ARGS += --with-spooldir=/var/opt/csw/spool/news

# tin requires to run 'make build'
BUILD_ARGS = build

# tin doesn't have a test target
TEST_TARGET =

# These are provided by CSWmutt-base
EXTRA_MERGE_EXCLUDE_FILES += $(mandir)/man5/mmdf\.5
EXTRA_MERGE_EXCLUDE_FILES += $(mandir)/man5/mbox\.5

# These will be necessary until CSWlibicu46 has been officially released
CHECKPKG_OVERRIDES_CSWtin += unidentified-dependency|CSWlibicu46
CHECKPKG_OVERRIDES_CSWtin += soname-not-found|libicuuc.so.46|is|needed|by|opt/csw/bin/tin
CHECKPKG_OVERRIDES_CSWtin += surplus-dependency|CSWlibicu46

include gar/category.mk

post-install-modulated:
	/usr/ccs/bin/strip $(DESTDIR)$(prefix)/bin/tin
	/usr/ccs/bin/mcs -d $(DESTDIR)$(prefix)/bin/tin

