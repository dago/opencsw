GARNAME = pv
GARVERSION = 1.1.4
CATEGORIES = utils

DESCRIPTION =  Monitor the progress of data through a pipe
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
MASTER_SITES = http://pipeviewer.googlecode.com/files/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
LICENSE = doc/COPYING

REQUIRED_PKGS = CSWiconv CSWggettextrt

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# Test with dd (010-dd) is unrealiable because of partial reads on SPARC.
# Upstream patch for a rewritten test is pending.
# Substituted with 010-opencsw-cksum in the meantime.
# See also: http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=324308
PATCHFILES = fix-test-010.diff

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

post-install-modulated:
	@gunzip $(DESTDIR)$(mandir)/man1/pv.1.gz
	@ginstall -d -m 755 $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 644 \
		$(WORKSRC)/doc/NEWS \
		$(DESTDIR)$(docdir)/$(GARNAME)
