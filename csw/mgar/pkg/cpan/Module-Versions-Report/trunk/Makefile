GARNAME = Module-Versions-Report
GARVERSION = 1.02
CATEGORIES = cpan
AUTHOR = SBURKE

DESCRIPTION = report versions of all modules in memory
define BLURB
  I often get email from someone reporting a bug in a module I've written. I
  email back, asking what version of the module it is, what version of Perl on
  what OS, and sometimes what version of some relevent third library (like
  XML::Parser). They reply, saying "Perl 5". I say "I need the exact version, as
  reported by perl -v". They tell me. And I say "I, uh, also asked about the
  version of my module and XML::Parser [or whatever]". They say "Oh yeah. It's
  2.27". "Is that my module or XML::Parser?" "XML::Parser." "OK, and what about
  my module's version?" "Ohyeah. That's 3.11." By this time, days have passed,
  and what should have been a simple operation -- reporting the version of Perl
  and relevent modules, has been needlessly complicated.

  This module is for simplifying that task. If you add "use
  Module::Versions::Report;" to a program (especially handy if your program is
  one that demonstrates a bug in some module), then when the program has
  finished running, you well get a report detailing the all modules in memory,
  and noting the version of each (for modules that defined a $VERSION, at
  least).
endef

DISTFILES += CSWpmmodversrpt.gspec

include gar/category.mk
