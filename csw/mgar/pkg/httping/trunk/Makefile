# Known issue:
# - Options -C, -6, and -y not documented in man page. Reported upstream,
#   feedback pending.
#
NAME = httping
VERSION = 1.5.3
CATEGORIES = net
GARTYPE = v2

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

DESCRIPTION = Httping is like 'ping' but for http-requests.
define BLURB
  Httping is like 'ping' but for http-requests.  Give it an url, and it'll
  show you how long it takes to connect, send a request and retrieve the
  reply (only the headers). Be aware that the transmission across the
  network also takes time! 
endef

MASTER_SITES = http://www.vanheusden.com/httping/
DISTFILES    = $(NAME)-$(VERSION).tgz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tgz

BUILD_DEP_PKGS += CSWlibssl-dev
RUNTIME_DEP_PKGS += CSWlibssl1-0-0

# Makefile comes pre-set with gcc defaults and hardcoded tools
# Already submitted upstream, feedback pending.
PATCHFILES = 0001-Makefile-make-options-and-tools-con# strndup is not defined anymore in httping source (file str.c)
# starting from at least 1.5.3 but it still doesn't exist under
# Solaris 9 so we have to define the function
PATCHFILES += 0002-Define-strndup-functionools-configurable.patch

CONFIGURE_SCRIPTS =
TEST_SCRIPTS =

# Build options (see $(WORKSRC)/Makefile)
EXTRA_LD_FLAGS = -lsocket -lnsl
EXTRA_BUILD_EXPORTS = WFLAGS OFLAGS
WFLAGS =
OFLAGS =

# Install options (see $(WOEXTRA_RKSRC)/Makefile)
INSTALL_EXPORTS = PREFIX INSTALL STRIP
PREFIX  = $(prefix)
INSTALL = ginstall
STRIP   = /usr/ccs/bin/strip

LICENSE = license.txt

include gar/category.mk

post-install-modulated:
	ginstall -d $(DESTDIR)$(docdir)/$(NAME)
	cp $(FILEDIR)/changelog.CSW $(DESTDIR)$(docdir)/$(NAME)