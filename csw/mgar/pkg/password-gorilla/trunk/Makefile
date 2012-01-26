# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! Requires http://incrtcl.sourceforge.net/itcl/ (running password-gorilla
#   currently fails with "The Password Gorilla requires the [incr Tcl] add-on
#   to Tcl. Please install the [incr Tcl] package."
#
NAME = password-gorilla
VERSION = 1.4
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = A cross-platform, Tcl/Tk-based Password Manager
define BLURB
  The Password Gorilla helps you manage your logins. It stores all your user
  names and passwords, along with login information and other notes, in a
  securely encrypted file. A single "master password" is used to protect the
  file. This way, you only need to remember the single master password, instead
  of the many logins that you use. 
endef

VENDOR_URL   = http://www.fpx.de/fp/Software/Gorilla/
MASTER_SITES = http://www.fpx.de/fp/Software/Gorilla/download/
DISTNAME     = gorilla-$(VERSION)
DISTFILES    = gorilla-$(VERSION).tar.gz
UFILES_REGEX = gorilla-(\d+(?:\.\d+)*).tar.gz
CATALOGNAME  = password_gorilla
ARCHALL      = 1
LICENSE      = LICENSE.txt

RUNTIME_DEP_PKGS = CSWtk

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += -with-wish=$(bindir)/tclsh

BUILD_SCRIPTS   =
INSTALL_SCRIPTS = custom
TEST_SCRIPTS    =

CHECKPKG_OVERRIDES_CSWpassword-gorilla += surplus-dependency|CSWtk

include gar/category.mk

install-custom: TCLPKGS = twofish blowfish sha1 pwsafe
install-custom: TCLDEST = $(DESTDIR)$(datadir)/password-gorilla
install-custom:
	$(foreach P,$(TCLPKGS),\
		mkdir -p $(TCLDEST)/$(P); \
		cp $(WORKSRC)/$(P)/* $(TCLDEST)/$(P); \
		chmod 644 $(TCLDEST)/$(P)/*; \
	)
	ginstall -m755 \
		$(WORKSRC)/gorilla \
		$(WORKSRC)/gorilla.tcl \
		$(WORKSRC)/isaac.tcl \
		$(TCLDEST)
	mkdir -p $(DESTDIR)$(bindir)
	echo '#!/bin/sh\nexec $(datadir)/password-gorilla/gorilla' > \
		$(DESTDIR)$(bindir)/password-gorilla
	chmod 755 $(DESTDIR)$(bindir)/password-gorilla
	chmod 644 $(WORKSRC)/$(LICENSE)
	$(MAKECOOKIE)
