# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = gnome-ssh-askpass
VERSION = 5.9p1
GARTYPE = v2
CATEGORIES = gnome

DESCRIPTION = A GNOME and Gtk2 passphrase requester
define BLURB
  A GNOME and Gtk2 passphrase requester
endef

DISTNAME = openssh-$(VERSION)
MASTER_SITES = ftp://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/
DISTFILES  = $(DISTNAME).tar.gz
DISTFILES += LICENSE
DISTFILES += README.CSW

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

PACKAGES = CSW$(NAME)
RUNTIME_DEP_PKGS  = CSWgtk2
RUNTIME_DEP_PKGS += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS += CSWlibatk1-0-0
RUNTIME_DEP_PKGS += CSWlibgio2-0-0
RUNTIME_DEP_PKGS += CSWlibglib2-0-0
RUNTIME_DEP_PKGS += CSWpango
RUNTIME_DEP_PKGS += CSWlibatk
RUNTIME_DEP_PKGS += CSWlibintl8
RUNTIME_DEP_PKGS += CSWftype2
RUNTIME_DEP_PKGS += CSWfconfig
RUNTIME_DEP_PKGS += CSWlibcairo2

BUILD_DEP_PKGS  =  CSWgtk2devel
BUILD_DEP_PKGS += CSWlibglib2-dev
BUILD_DEP_PKGS += CSWpangodevel
BUILD_DEP_PKGS += CSWlibpixman-dev
BUILD_DEP_PKGS += CSWlibatk-dev
BUILD_DEP_PKGS += CSWlibpng-dev
BUILD_DEP_PKGS += CSWsunx11devel

LICENSE = LICENSE

# Does not use GNU configure
CONFIGURE_SCRIPTS =
# No test script
TEST_SCRIPTS = 

BUILD_SCRIPTS = custom

INSTALL_SCRIPTS = custom

include gar/category.mk

build-custom:
	cd $(WORKSRC)/contrib ; \
	$(BUILD_ENV) gmake gnome-ssh-askpass2
	@$(MAKECOOKIE)

install-custom:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall $(WORKSRC)/contrib/gnome-ssh-askpass2 $(DESTDIR)$(bindir)/gnome-ssh-askpass
