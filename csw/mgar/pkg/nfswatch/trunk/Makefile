GARNAME = nfswatch
GARVERSION = 4.99.10
CATEGORIES = utils

DESCRIPTION = Monitors NFS client traffic and response time
define BLURB
  NFSwatch lets you monitor NFS requests to any givenmachine, or the entire
  local network. It mostly monitors NFS client traffic (NFS requests); it also
  monitors the NFS reply traffic from a server inorder to measure the response
  time for each RPC.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
PATCHFILES = 0001-Add-missing-ifdefs-to-shield-Linux.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://nfswatch.sourceforge.net/

LICENSE = LICENSE

CONFIGURE_SCRIPTS =

BUILD_ARGS = CFLAGS="-DSUNOS58 -DSUNOS5 $(CFLAGS)"
BUILD_ARGS += LIBS="-lcurses -lnsl -lsocket -lm"
BUILD_ARGS += nfswatch nfslogsum

TEST_SCRIPTS =

INSTALL_OVERRIDE_VARS = INSTALL BINDIR MANDIR MANSUF
INSTALL_OVERRIDE_VAR_INSTALL = /usr/ucb/install
INSTALL_OVERRIDE_VAR_BINDIR = $(sbindir)
INSTALL_OVERRIDE_VAR_MANDIR = $(mandir)/man8
INSTALL_OVERRIDE_VAR_MANSUF = 8

include gar/category.mk
