GARNAME = imapfilter
GARVERSION = 1.2.2
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
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += CSWimapfilter.gspec CSWimapfilter.depend CSWimapfilter.prototype

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

# Remove anti-social makeflags
PATCHFILES += make.diff

#LIBDEPS += lib/openssl

CONFIGURE_ARGS = -d $(prefix) -m $(mandir)

# No test suite
TEST_SCRIPTS =

include gar/category.mk
