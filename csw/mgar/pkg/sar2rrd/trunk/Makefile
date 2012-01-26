NAME = sar2rrd
VERSION = 2.5
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Generate RRDTool graphs from sar output
define BLURB
  It creates a PNG Graph for each statistics group collected by sar.
  Version 2.0 handles both Linux and Solaris sar output.
  Each statistics of the group is represented as a single line in the graph.
endef

MASTER_SITES = http://www.trickytools.com/downloads/
DISTFILES  = $(NAME)-$(VERSION).pl
DISTFILES += $(NAME)-graph-$(VERSION).pl

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://www.trickytools.com/php/sar2rrd.php

RUNTIME_DEP_PKGS = CSWrrd CSWperl CSWpmdatecalc CSWpmxmlsimple

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

ARCHALL = 1

CHECKPKG_OVERRIDES_CSWsar2rrd += license-missing|/opt/csw/share/doc/sar2rrd/license
CHECKPKG_OVERRIDES_CSWsar2rrd += surplus-dependency|CSWperl
CHECKPKG_OVERRIDES_CSWsar2rrd += surplus-dependency|CSWpmdatecalc
CHECKPKG_OVERRIDES_CSWsar2rrd += surplus-dependency|CSWpmxmlsimple
CHECKPKG_OVERRIDES_CSWsar2rrd += surplus-dependency|CSWrrd

include gar/category.mk

post-extract-modulated:
	$(foreach F,$(DISTFILES),perl -pi \
		-e 's,/usr/bin/perl,/opt/csw/bin/perl,; s,/usr/local/rrdtool/bin/rrdtool,/opt/csw/bin/rrdtool,' \
		$(WORKDIR)/$F;)
	@$(MAKECOOKIE)

install-custom:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall $(WORKDIR)/$(NAME)-$(VERSION).pl $(DESTDIR)$(bindir)/$(NAME)
	ginstall $(WORKDIR)/$(NAME)-graph-$(VERSION).pl $(DESTDIR)$(bindir)/$(NAME)-graph
	@$(MAKECOOKIE)
