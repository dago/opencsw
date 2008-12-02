GARNAME = pv
GARVERSION = 0.9.2
CATEGORIES = utils

DESCRIPTION = pipeviewer, like cat with progress indications
define BLURB
  Pipe Viewer is a terminal-based tool for monitoring the progress
  of data through a pipeline. It can be inserted into any normal
  pipeline between two processes to give a visual indication of how
  quickly data is passing through, how long it has taken, how near
  to completion it is, and an estimate of how long it will be until
  completion.
endef

# Project URL
SPKG_SOURCEURL = http://www.ivarch.com/programs/pv.shtml

# Source files
MASTER_SITES = http://unc.dl.sourceforge.net/sourceforge/pipeviewer/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += CSWpv.gspec CSWpv.depend CSWpv.prototype

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

post-install:
	@gunzip $(DESTDIR)$(infodir)/pv.info.gz $(DESTDIR)$(mandir)/man1/pv.1.gz

