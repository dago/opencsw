# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = xpra
VERSION = 0.3.4
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = screen for X
define BLURB
  Xpra is 'screen for X': it allows you to run X programs, usually on a remote host, direct their display to your local machine, and then to disconnect from these programs and reconnect from the same or another machine, without losing any state. It gives you remote access to individual applications.
Xpra is "rootless" or "seamless": programs you run under it show up on your desktop as regular programs, managed by your regular window manager.
Sessions can be accessed over SSH, or password protected over plain TCP sockets.
Xpra is usable over reasonably slow links and does its best to adapt to changing network bandwidth limits.
endef

MASTER_SITES = http://xpra.org/src/
DISTFILES  = $(DISTNAME).tar.bz2

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

ARCHALL = 1
BUILD_DEP_PKGS += CSWpy-gobject-dev CSWlibgtk2-dev CSWlibxtstdevel
BUILD_DEP_PKGS += CSWlibxfixesdevel CSWlibxcompositedev CSWlibxdamagedevel CSWlibxrandrdevel

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(WORKSRC)/setup.py
TEST_SCRIPTS =
INSTALL_SCRIPTS = $(WORKSRC)/setup.py

INSTALL_ARGS += --root=$(DESTDIR)
INSTALL_ARGS += --prefix=$(prefix)

include gar/category.mk

