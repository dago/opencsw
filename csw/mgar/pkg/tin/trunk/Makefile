NAME = tin
VERSION = 2.0.0
CATEGORIES = net

DESCRIPTION = Terminal-based news reader
define BLURB
  tin is an easy-to-use USENET news reader for the console using NNTP.
  It supports threading, scoring, different charsets, and many other
  useful things. It has also support for different languages.
endef

MASTER_SITES = ftp://ftp.tin.org/pub/news/clients/tin/stable/
DISTFILES = $(NAME)-$(VERSION).tar.bz2
DISTFILES += COPYING

BUILD_DEP_PKGS += CSWperl
BUILD_DEP_PKGS += CSWlibpcre-dev
BUILD_DEP_PKGS += CSWggettext-dev
BUILD_DEP_PKGS += CSWlibidn-dev
BUILD_DEP_PKGS += CSWlibicu-dev
BUILD_DEP_PKGS += CSWlibiconv-dev
BUILD_DEP_PKGS += CSWlibncurses-dev
BUILD_DEP_PKGS += CSWgsasl-dev

RUNTIME_DEP_PKGS_CSWtin += CSWperl
RUNTIME_DEP_PKGS_CSWtin += CSWlibpcre0
RUNTIME_DEP_PKGS_CSWtin += CSWlibintl8
RUNTIME_DEP_PKGS_CSWtin += CSWlibidn11
RUNTIME_DEP_PKGS_CSWtin += CSWlibicu46
RUNTIME_DEP_PKGS_CSWtin += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWtin += CSWlibncursesw5
RUNTIME_DEP_PKGS_CSWtin += CSWlibgsasl7

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

include gar/category.mk

#post-install-modulated:
#	/usr/ccs/bin/strip $(DESTDIR)$(prefix)/bin/tin
#	/usr/ccs/bin/mcs -d $(DESTDIR)$(prefix)/bin/tin

