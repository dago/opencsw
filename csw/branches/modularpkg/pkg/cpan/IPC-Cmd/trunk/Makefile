GARNAME = IPC-Cmd
GARVERSION = 0.36
CATEGORIES = cpan
AUTHOR = KANE

DESCRIPTION = Finding and running system commands made easy
define BLURB
  IPC::Cmd allows you to run commands, interactively if desired, platform
  independent but have them still work.
endef

DISTFILES += $(call admfiles,CSWpmipccmd,depend prototype)

DEPENDS += cpan/Params-Check
DEPENDS += cpan/Module-Load-Conditional
DEPENDS += cpan/Locale-Maketext-Simple
DEPENDS += cpan/IPC-Run

include gar/category.mk
