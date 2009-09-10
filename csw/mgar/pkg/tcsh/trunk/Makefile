GARNAME = tcsh
GARVERSION = 6.17.00
CATEGORIES = apps

DESCRIPTION = Enhanced version of the Berkeley C shell (csh)
define BLURB
  Tcsh is an enhanced, but completely compatible version of the Berkeley UNIX C shell (csh).
  It is a command language interpreter usable both as an interactive login shell and a shell
  script command processor. It includes a command-line editor, programmable word completion,
  spelling correction, a history mechanism, job control and a C-like syntax.
endef

MASTER_SITES = ftp://ftp.astron.com/pub/tcsh/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += CSWtcsh.postinstall
DISTFILES += CSWtcsh.postremove

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS = CSWiconv

SPKG_SOURCEURL = http://www.tcsh.org/

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

# Skip tests until this one is fixed:
#   http://bugs.gw.com/view.php?id=87
SKIPTEST = 1

INSTALL_ARGS = install.man

include gar/category.mk
