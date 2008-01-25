GARNAME = Log-Dispatch
GARVERSION = 2.16
CATEGORIES = cpan
AUTHOR = DROLSKY

DESCRIPTION = dispatches messages to one or more outputs
define BLURB
  This module manages a set of Log::Dispatch::* objects, allowing you to add
  and remove output objects as desired.
endef

DISTFILES += $(call admfiles,CSWpmlogdispatch,depend prototype)

DEPENDS += cpan/Module-Build
DEPENDS += cpan/Params-Validate

CONFIGURE_ARGS = destdir=$(DESTDIR)

include ../category.mk
