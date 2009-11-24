GARNAME = sar2rrd
GARVERSION = 2.4
CATEGORIES = utils

DESCRIPTION = Generate RRDTool graphs from sar output
define BLURB
  It creates a PNG Graph for each statistics group collected by sar.
  Version 2.0 handles both Linux and Solaris sar output.
  Each statistics of the group is represented as a single line in the graph.
endef

MASTER_SITES = http://www.trickytools.com/downloads/
DISTFILES  = $(GARNAME)-$(GARVERSION).pl
DISTFILES += $(GARNAME)-graph-$(GARVERSION).pl

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://www.trickytools.com/php/sar2rrd.php

REQUIRED_PKGS = CSWrrd CSWperl CSWpmdatecalc

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

post-extract-modulated:
	$(foreach F,$(DISTFILES),perl -pi \
		-e 's,/usr/bin/perl,/opt/csw/bin/perl,; s,/usr/local/rrdtool/bin/rrdtool,/opt/csw/bin/rrdtool,' \
		$(WORKDIR)/$F;)
	@$(MAKECOOKIE)

install-custom:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall $(WORKDIR)/$(GARNAME)-$(GARVERSION).pl $(DESTDIR)$(bindir)/$(GARNAME)
	ginstall $(WORKDIR)/$(GARNAME)-graph-$(GARVERSION).pl $(DESTDIR)$(bindir)/$(GARNAME)-graph
	@$(MAKECOOKIE)
