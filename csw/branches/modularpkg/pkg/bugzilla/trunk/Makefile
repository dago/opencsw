GARNAME = bugzilla
GARVERSION = 2.22
CATEGORIES = apps

DESCRIPTION = Bugzilla defect tracking system.
define BLURB
  Bugzilla defect tracking system.
endef

MASTER_SITES = ftp://ftp.mozilla.org/pub/mozilla.org/webtools/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWbugzilla,prototype depend)

# Adjust the shebang path for all scripts
PATCHFILES += perlpath.diff

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS =
TEST_SCRIPTS =

# Required
DEPENDS += cpan/AppConfig
DEPENDS += cpan/TimeDate
DEPENDS += cpan/DBI
DEPENDS += cpan/Data-ShowTable
DEPENDS += cpan/DBD-mysql
DEPENDS += cpan/DBD-Pg
DEPENDS += cpan/Template-Toolkit
DEPENDS += cpan/Text-Tabs+Wrap
DEPENDS += cpan/MailTools
DEPENDS += cpan/MIME-tools

# Optional
DEPENDS += cpan/GD
DEPENDS += cpan/Chart
DEPENDS += cpan/GDGraph
DEPENDS += cpan/GDTextUtil
DEPENDS += cpan/XML-Twig
DEPENDS += cpan/PatchReader
DEPENDS += lib/ImageMagick
# Currently calls out 'graphvis' in depend, but should move to graphviz2
#DEPENDS += utils/graphviz2

include gar/category.mk

