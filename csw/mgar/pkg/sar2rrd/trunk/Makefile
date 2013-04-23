NAME = sar2rrd
VERSION = 2.6.2
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
DISTFILES += $(NAME)-grVENDOR_URL = http://www.trickytools.com/php/sar2rrd.php

PACKAGES += CSWsar2rrd
SPKG_DESC_CSWsar2rrd = Generate RRDTool graphs from sar output
ARCHALL_CSWsar2rrd = 1
RUNTIME_DEP_PKGS += CSWperl
RUNTIME_DEP_PKGS += CSWpm-rrdtool
RUNTIME_DEP_PKGS += CSWpm-date-calc
RUNTIME_DEP_PKGS += CSWpm-xml-simple

# Perl modules can't be tracked with checkpkg
CHECKPKG_OVERRIDES_CSWsar2rrd += surplus-dependency|CSWpm-date-calc
CHECKPKG_OVERRIDES_CSWsar2rrd += surplus-dependency|CSWpm-xml-simpl/doc/sar2rrd/license
CHECKPKG_OVERRIDES_CSWsar2rrd += surplus-dependency|CSWperl
CHECKPKG_OVERRIDES_CSWsar2rrd += surpl-rrdtool

REINPLACEMENTS += perl
REINPLACE_MATCH_perl = /usr/bin/perl
REINPLACE_WITH_perl = /opt/csw/bin/perl
REINPLACE_FILES_perl += $(addprefix $(WORKDIR)/,$(DISTFILES))

REINPLACEMENTS += rrdtool
REINPLACE_MATCH_rrdtool = /usr/local/rrdtool/bin/rrdtool
REINPLACE_WITH_rrdtool = $(bindir)/rrdtool
REINPLACE_FILES_rrdtool += $(addprefix $(WORKDIR)/,$(DISTFILES))

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

#post-extract-modulated:
#	$(foreach F,$(DISTFILES),perl -pi \
#		-e 's,/usr/bin/perl,/opt/csw/bin/perl,; s,/usr/local/rrdtool/bin/rrdtool,/opt/csw/bin/rrdtool,' \
#		$(WORKDIR)/$F;)
#
		$(WORKDIR)/$F;)
	@$(MAKECOOKIE)

install-custom:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall $(WORKDIR)/$(NAME)-$(VERSION).pl $(DESTDIR)$(bindir)/$(NAME)
	ginstall $(WORKDIR)/$(NAME)-graph-$(VERSION).pl $(DESTDIR)$(bindir)/$(NAME)-gra