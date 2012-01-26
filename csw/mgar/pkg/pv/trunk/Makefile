NAME = pv
VERSION = 1.2.0
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION =  Monitor the progress of data through a pipe
define BLURB
  Pipe Viewer is a terminal-based tool for monitoring the progress
  of data through a pipeline. It can be inserted into any normal
  pipeline between two processes to give a visual indication of how
  quickly data is passing through, how long it has taken, how near
  to completion it is, and an estimate of how long it will be until
  completion.
endef

VENDOR_URL   = http://www.ivarch.com/programs/pv.shtml
MASTER_SITES = http://pipeviewer.googlecode.com/files/
DISTFILES    = $(NAME)-$(VERSION).tar.gz
LICENSE      = doc/COPYING

UPSTREAM_MASTER_SITES = $(VENDOR_URL)

RUNTIME_DEP_PKGS = CSWlibintl8

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

# test-012 uses tr complements (-c) which don't work with /usr/bin/tr
PATH := /opt/csw/gnu:$(PATH)

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(NAME)
post-install-modulated:
	gunzip $(DESTDIR)$(mandir)/man1/pv.1.gz
	ginstall -d -m 755 $(DOCDEST)
	cp $(WORKSRC)/doc/NEWS $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
