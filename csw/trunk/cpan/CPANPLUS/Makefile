GARNAME = CPANPLUS
GARVERSION = 0.076
CATEGORIES = cpan
AUTHOR = KANE

DESCRIPTION = API and CLI access to the CPAN mirrors
define BLURB
  The CPANPLUS library is an API to the CPAN mirrors and a collection of
  interactive shells, commandline programs, etc, that use this API.
endef

DISTFILES += $(call admfiles,CSWpmcpanplus,depend prototype)

DEPENDS += cpan/Archive-Extract
DEPENDS += cpan/File-Fetch
DEPENDS += cpan/IPC-Cmd
DEPENDS += cpan/Locale-Maketext-Simple
DEPENDS += cpan/Log-Message
DEPENDS += cpan/Module-CoreList
DEPENDS += cpan/Module-Load
DEPENDS += cpan/Module-Load-Conditional
DEPENDS += cpan/Module-Loaded
DEPENDS += cpan/Module-Pluggable
DEPENDS += cpan/Object-Accessor
DEPENDS += cpan/Package-Constants
DEPENDS += cpan/Params-Check
DEPENDS += cpan/Term-UI

include ../category.mk
