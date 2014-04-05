# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = torsocks
VERSION = 1.2
GARTYPE = v2

DESCRIPTION = Use SOCKS-friendly applications with Tor
define BLURB
  Torsocks allows you to use most SOCKS-friendly applications in a safe way with Tor. It ensures that DNS requests are handled safely and explicitly rejects UDP traffic from the application you're using.
endef

MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PATCHFILES = torsocks-HEAD-2034625.nww.solaris.patch

# replace shell in wrapper executable scripts
REINPLACEMENTS += shell 
REINPLACE_MATCH_shell = /bin/sh
REINPLACE_WITH_shell = /opt/csw/bin/bash
REINPLACE_FILES_shell += src/torsocks.in
REINPLACE_FILES_shell += src/usewithtor.in

CONFIGURE_ARGS = $(DIRPATHS)

RUNTIME_DEP_PKGS_CSWtorsocks += CSWbash
CHECKPKG_OVERRIDES_CSWtorsocks += surplus-dependency|CSWbash

include gar/category.mk

pre-configure:
	cd $(WORKSRC) && autoreconf -i
	@$(MAKECOOKIE)
