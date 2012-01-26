NAME = mairix
VERSION = 0.22
CATEGORIES = utils
GARTYPE = v2

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

VENDOR_URL   = http://www.rpcurnow.force9.co.uk/mairix/
MASTER_SITES = $(SF_MIRROR)
DISTFILES    = $(NAME)-$(VERSION).tar.gz

RUNTIME_DEP_PKGS = CSWbzip2 CSWzlib

# Let make invocations refer to $(MAKE) not "make". Otherwise gmake flags
# might be passed to invocations of make (via $MAKEFLAGS) which make
# doesn't understand. This particulary pertains to ~skayser/bin/mgar.
PATCHFILES += 0001-Use-MAKE-instead-of-a-hardcoded-make.patch

TEST_SCRIPTS =

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
post-install-modulated: DOCDEST = $(DESTDIR)$(docdir)/$(NAME)
post-install-modulated:
	@ginstall -d $(DOCDEST)
	@$(foreach DOC,$(DOCS),ginstall -m 644 $(WORKSRC)/$(DOC) $(DOCDEST);)
	$(MAKECOOKIE)

# Install changelog.CSW
post-merge: $(foreach P,$(_PKG_SPECS),install-changelog-$P)
install-changelog-%:
	ginstall -D $(FILEDIR)/changelog.CSW \
		$(PKGROOT)$(docdir)/$(call catalogname,$*)/changelog.CSW
	@$(MAKECOOKIE)
