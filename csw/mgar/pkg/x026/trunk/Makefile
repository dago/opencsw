# $Id$
NAME = x026
VERSION = 1.2
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = IBM 026 Keypunch Emulator for X11
define BLECTURB
endef

SF_PROJ = x3270
MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tgz
DISTFILES += COPYING

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tgz

DEP_PKGS = CSWxpm

CONFIGURE_SCRIPTS = $(WORKSRC)/Imakefile

BUILD_OVERRIDE_VARS = XPMLIB
BUILD_OVERRIDE_VAR_XPMLIB = -L$(libdir) -R$(libdir) -lXpm

TEST_SCRIPTS =

INSTALL_ARGS = install install.man
INSTALL_OVERRIDE_VARS = BINDIR MANPATH
INSTALL_OVERRIDE_VAR_BINDIR = $(bindir)
INSTALL_OVERRIDE_VAR_MANPATH = $(mandir)

includ