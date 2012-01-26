NAME = tcsh
VERSION = 6.17.00
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Enhanced version of the Berkeley C shell (csh)
define BLURB
  Tcsh is an enhanced, but completely compatible version of the Berkeley UNIX C shell (csh).
  It is a command language interpreter usable both as an interactive login shell and a shell
  script command processor. It includes a command-line editor, programmable word completion,
  spelling correction, a history mechanism, job control and a C-like syntax.
endef

MASTER_SITES = ftp://ftp.astron.com/pub/tcsh/
DISTFILES  = $(DISTNAME).tar.gz

LICENSE = Copyright

RUNTIME_DEP_PKGS = CSWiconv

VENDOR_URL = http://www.tcsh.org/

EXTRA_CPPFLAGS += -D_FILE_OFFSET_BITS=64
# As documented in README, this overrides the setting in pathnames.h
EXTRA_CPPFLAGS += -D_PATH_LOCAL=\'\"$(bindir)\"\'
# EXTRA_CPPFLAGS += -D_PATH_TCSHELL=\"$(bindir)/tcsh\"

# Skip tests until this one is fixed:
#   http://bugs.gw.com/view.php?id=87
SKIPTEST = 1

INSTALL_ARGS = install.man

ETCSHELLS = /opt/csw/bin/tcsh

# These are examples only
CHECKPKG_OVERRIDES_CSWtcsh += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/tcsh.1

# This is from tw.h, possibly harmless.
#   #define DEFAULTLIST ":/usr/man/cat1:/usr/man/cat8:/usr/man/cat6:/usr/local/man/cat1:/usr/local/man/cat8:/usr/local/man/cat6"    /* if no HPATH */
CHECKPKG_OVERRIDES_CSWtcsh += file-with-bad-content|/usr/local|root/opt/csw/bin/tcsh

include gar/category.mk
