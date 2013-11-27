NAME = MARC-Charset
VERSION = 1.35
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = GMCHARLT

DESCRIPTION = Convert MARC-8 encoded strings to UTF-8
define BLURB
endef

# Our version of makemake only allows one author
PATCHFILES += 0001-Only-one-author-allowed.patch

CATALOG_RELEASE = unstable

LICENSE_TEXT = This module is licensed under the perl license

PACKAGES += CSWpm-marc-charset
CATALOGNAME_CSWpm-marc-charset = pm_marc_charset
SPKG_DESC_CSWpm-marc-charset = Convert MARC-8 encoded strings to UTF-8
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-marc-charset = 1
RUNTIME_DEP_PKGS_CSWpm-marc-charset += CSWpm-xml-sax
RUNTIME_DEP_PKGS_CSWpm-marc-charset += CSWpm-class-accessor

include gar/category.mk
