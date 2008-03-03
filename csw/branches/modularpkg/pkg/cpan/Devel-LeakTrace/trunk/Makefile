GARNAME = Devel-LeakTrace
GARVERSION = 0.05
CATEGORIES = cpan
AUTHOR = RCLAMP

DESCRIPTION = indicate where leaked variables are coming from
define BLURB
  Based heavily on Devel::Leak, Devel::LeakTrace uses the pluggable runops
  feature found in perl 5.6 and later in order to trace SV allocations of a
  running program.
endef

DISTFILES += $(call admfiles,CSWpmdevleaktrace,depend)

DEPENDS += lib/glib2
DEPENDS += cpan/Module-Build

include gar/category.mk
