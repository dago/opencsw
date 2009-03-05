GARNAME = mairix
GARVERSION = 0.21
CATEGORIES = utils

DESCRIPTION = An index and search tool for Maildir, MH, or mbox
define BLURB
  mairix is a program for indexing and searching email messages stored in
  Maildir, MH or mbox folders.

  * Indexing is fast. It runs incrementally on new messages - any particular
    message only gets scanned once in the lifetime of the index file.

  * The search mode populates a "virtual" maildir (or MH) folder with symlinks
    which point to the real messages. This folder can be opened as usual in your
    mail program. (Note, if messages are in mbox folders, copies are made. 
    Similarly if the virtual folder has mbox format, it is filled with copies 
    of the matched messages.)
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
SPKG_SOURCEURL = http://www.rpcurnow.force9.co.uk/mairix/

REQUIRED_PKGS = CSWbzip2 CSWzlib

TEST_SCRIPTS =

# Mention option -x in the help message (-h)
PATCHFILES  = patch-excerpt.diff

# configure doesn't understand most of the $(DIRPATHS) arguments
CONFIGURE_ARGS = --prefix=/opt/csw
CONFIGURE_ARGS += --bindir=/opt/csw/bin
CONFIGURE_ARGS += --infodir=/opt/csw/share/info
CONFIGURE_ARGS += --mandir=/opt/csw/share/man

#GARFLAVOR = DBG

include gar/category.mk

# configure uses bashisms but doesn't declare bash as its interpreter
pre-configure-modulated:
	@perl -pi -e 's|#!/bin/sh|#!/bin/bash|' $(WORKSRC)/configure
	$(MAKECOOKIE)

pre-build-modulated:
	@perl -pi -e 's/__inline__/inline/' $(WORKSRC)/memmac.h
	$(MAKECOOKIE)

post-install-modulated: DOCS = ACKNOWLEDGEMENTS NEWS README dotmairixrc.eg
post-install-modulated: DOCDEST = $(DESTDIR)$(docdir)/$(GARNAME)
post-install-modulated:
	@ginstall -d $(DOCDEST)
	@$(foreach DOC,$(DOCS),ginstall -m 644 $(WORKSRC)/$(DOC) $(DOCDEST);)
	$(MAKECOOKIE)
