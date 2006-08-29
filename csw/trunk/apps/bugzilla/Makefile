GARNAME = bugzilla
GARVERSION = 2.22
CATEGORIES = apps

DESCRIPTION = Integrated SCM and Project Management
define BLURB
	Trac is an enhanced wiki and issue tracking system for software development
	projects. Trac uses a minimalistic approach to web-based software project
	management. Our mission; to help developers write great software while
	staying out of the way. Trac should impose as little as possible on a team's
	established development process and policies.
endef

MASTER_SITES = ftp://ftp.mozilla.org/pub/mozilla.org/webtools/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWbugzilla,prototype depend)

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

include ../category.mk

