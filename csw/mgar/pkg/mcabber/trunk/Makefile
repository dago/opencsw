GARNAME = mcabber
GARVERSION = 0.9.9
CATEGORIES = utils

DESCRIPTION = A small Jabber console client
define BLURB
mcabber is a small Jabber console client.  mcabber includes features such as
SSL support, MUC (Multi-User Chat) support, history logging, command
completion, OpenPGP encryption, OTR (Off-the-Record Messaging) support and
external action triggers.
endef

MASTER_SITES = http://www.lilotux.net/~mikael/mcabber/files/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
SPKG_SOURCEURL = http://www.lilotux.net/~mikael/mcabber/

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS = CSWncurses CSWosslrt CSWotr
REQUIRED_PKGS = CSWaspell CSWggettextrt CSWglib2 
REQUIRED_PKGS = CSWgpgerr CSWgpgme CSWiconv

TEST_SCRIPTS = 

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-openssl=/opt/csw/lib
CONFIGURE_ARGS += --enable-otr
CONFIGURE_ARGS += --enable-aspell

# mcabber is geared towards gcc and heavily uses inline functions without
# static/extern storage qualifiers. Sun Studio needs to emulate gcc 
# behaviour with regards to these inline functions.
#  
# For details see http://blogs.sun.com/dew/entry/c99_inline_function
#
EXTRA_CFLAGS = -features=no%extinl

EXTRA_LDFLAGS = -lsocket
EXTRA_INC = /opt/csw/lib/ncurses

# Get rid of inline functions which are referenced externally (no%extinl
# makes inline functions static and would break linking otherwise)
PATCHFILES = patch-inline.diff

# Solaris 8 doesn't have iswlbank(), provide replacement macro
PATCHFILES = patch-iswblank.diff

include gar/category.mk

pre-build-modulated:
	@perl -pi -e 's|#! /bin/sh|#!/bin/bash|' $(WORKSRC)/hgcset.sh
	@perl -pi -e 's|-O2||' \
		$(WORKSRC)/Makefile \
		$(WORKSRC)/src/Makefile \
		$(WORKSRC)/libjabber/Makefile
