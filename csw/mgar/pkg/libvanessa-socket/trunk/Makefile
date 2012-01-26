NAME = libvanessa-socket
VERSION = 0.0.9
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Library to simplify common socket operations.
define BLURB
  Simplifies TCP/IP socket operations. It includes code to open a socket
  to a server as a client, to listen on socket for clients as a server and
  to pipe information between sockets.
endef

VENDOR_URL   = http://www.vergenet.net/linux/vanessa/
MASTER_SITES = $(VENDOR_URL)/download/vanessa_socket/$(VERSION)/
DISTFILES    = vanessa_socket-$(VERSION).tar.gz
DISTNAME     = vanessa_socket-$(VERSION)
UFILES_REGEX = (\d+(?:\.\d+)*)
UPSTREAM_MASTER_SITES = $(VENDOR_URL)/download/vanessa_socket/

PACKAGES = CSWlibvanessa-socket
CATALOGNAME = libvanessa_socket
RUNTIME_DEP_PKGS = CSWlibvanessa-logger

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

post-merge: $(foreach P,$(_PKG_SPECS),install-changelog-$P)

install-changelog-%:
	ginstall -D $(FILEDIR)/changelog.CSW \
		$(PKGROOT)$(docdir)/$(call catalogname,$*)/changelog.CSW
	@$(MAKECOOKIE)
