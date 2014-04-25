# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! So far, it looks like it's a lot more work. This particular version of
# Xorg requires lots of headers, and even though we only need to build xvfb,
# we might need to bring in more packages first before ./configure can
# complete.
#
# Or maybe we don't need the ./configure to complete to build just xvfb?

NAME = xvfb
VERSION = 1.12.2
GARTYPE = v2

DESCRIPTION = Brief description

MASTER_SITES = ftp://ftp.fu-berlin.de/unix/X11/FTP.X.ORG/pub/X11R7.7/src/everything/
DISTFILES  = xorg-server-$(VERSION).tar.bz2

PACKAGING_PLATFORMS = solaris9-i386 solaris9-sparc

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-xorg
CONFIGURE_ARGS += --disable-xnest
CONFIGURE_ARGS += --disable-xwin
CONFIGURE_ARGS += --disable-standalone-xpbproxy
CONFIGURE_ARGS += --disable-dmx
CONFIGURE_ARGS += --disable-xres
CONFIGURE_ARGS += --disable-glx
CONFIGURE_ARGS += --disable-pciaccess
CONFIGURE_ARGS += --disable-dri
CONFIGURE_ARGS += --disable-dri2

WORKSRC = $(WORKDIR)/xorg-server-$(VERSION)

include gar/category.mk
