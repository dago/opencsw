NAME = imapfilter
VERSION = 2.2.2
GARTYPE = v2
CATEGORIES = net

DESCRIPTION = IMAP mail filtering utility
define BLURB
  IMAPFilter is a mail filtering utility. It connects to remote mail servers
  using the Internet Message Access Protocol (IMAP), sends searching queries
  to the server and processes mailboxes based on the results. It can be used
  to delete, copy, move, flag, etc. messages residing in mailboxes at the same
  or different mail servers. The 4rev1 and 4 versions of the IMAP protocol are
  supported.
endef

MASTER_SITES = http://imapfilter.hellug.gr/source/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

BUILD_DEP_PKGS += CSWlibssl-dev
BUILD_DEP_PKGS += CSWlua
BUILD_DEP_PKGS += CSWlibpcre-dev

RUNTIME_DEP_PKGS_CSWimapfilter += CSWlua
RUNTIME_DEP_PKGS_CSWimapfilter += CSWlibpcre1
RUNTIME_DEP_PKGS_CSWimapfilter += CSWlibssl1-0-0

PATCHFILES += 0001-Bludgeon-the-build-system-to-do-what-we-need.patch

GARCOMPILER = GNU

CONFIGURE_ARGS = -d $(prefix) -m $(mandir)

# No test suite
TEST_SCRIPTS =

include gar/category.mk

PATH := /opt/csw/gnu:/opt/csw/bin:$(PATH)
