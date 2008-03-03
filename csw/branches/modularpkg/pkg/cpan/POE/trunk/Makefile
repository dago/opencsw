GARNAME = POE
GARVERSION = 0.3601
CATEGORIES = cpan
AUTHOR = RCAPUTO

DESCRIPTION = portable multitasking and networking framework for Perl
define BLURB
  POE is a framework for cooperative, event driven multitasking in Perl. Other
  languages have similar frameworks. Python has Twisted. TCL has "the event
  loop".

  POE originally was developed as the core of a persistent object server and
  runtime environment. It has evolved into a general purpose multitasking and
  networking framework, encompassing and providing a consistent interface to
  other event loops such as Event and the Tk and Gtk toolkits.
endef

DISTFILES += CSWpmpoe.gspec CSWpmpoe.depend

# Disable Tk/Gtk optional module checks
PATCHFILES = optional.diff

DEPENDS += cpan/Curses cpan/IO-Tty cpan/Term-Cap cpan/Event

include gar/category.mk
