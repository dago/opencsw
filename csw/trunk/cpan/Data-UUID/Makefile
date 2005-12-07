GARNAME = Data-UUID
GARVERSION = 0.11
CATEGORIES = cpan
AUTHOR = AGOLOMSH

DESCRIPTION = extension for generating unique identifiers
define BLURB
  This module provides a framework for generating UUIDs (Universally Unique
  Identifiers, also known as GUIDs (Globally Unique Identifiers). A UUID is 128
  bits long, and is guaranteed to be different from all other UUIDs/GUIDs
  generated until 3400 CE.
endef

DISTFILES = $(call admfiles,CSWpmdatauuid,)

CONFIGURE_ENV += PERL_MM_USE_DEFAULT=1

include ../category.mk
