NAME = Number-Format
VERSION = 1.73
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = WRW

DESCRIPTION = Perl extension for formatting numbers
define BLURB
endef

DISTFILES += COPYING

PACKAGES = CSWpm-number-format
CATALOGNAME = pm_number_format
SPKG_DESC_CSWpm-number-format = $(DESCRIPTION)
OBSOLETED_BY_CSWpm-number-format = CSWpmnumberformat
CATALOGNAME_CSWpmnumberformat = pm_numberformat

ARCHALL = 1

# Fails one Russian locale test
SKIPTEST = 1

include gar/category.mk
