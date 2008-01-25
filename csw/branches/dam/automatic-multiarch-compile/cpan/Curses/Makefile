GARNAME = Curses
GARVERSION = 1.06
CATEGORIES = cpan
AUTHOR = WPS

DESCRIPTION = terminal screen handling and optimization
define BLURB
  Curses is the interface between Perl and your system's curses(3) library.
  For descriptions on the usage of a given function, variable, or constant,
  consult your system's documentation, as such information invariably varies
  (:-) between different curses(3) libraries and operating systems. This
  document describes the interface itself, and assumes that you already know
  how your system's curses(3) library works.
endef

DISTFILES += CSWpmcurses.gspec CSWpmcurses.depend

DEPENDS += lib/ncurses

# Expose lib and inc settings as arguments
PATCHFILES = makefile.diff

# Call to Perl_sv_isa() should be sv_isa()
PATCHFILES += sv_isa.diff

CONFIGURE_ARGS  = PANELS MENUS FORMS
CONFIGURE_ARGS += INC="-I$(includedir)"
CONFIGURE_ARGS += LIBS="-L$(libdir) -R$(libdir) -lncurses"
CONFIGURE_ARGS += P_LIBS="-L$(libdir) -R$(libdir) -lpanel"
CONFIGURE_ARGS += M_LIBS="-L$(libdir) -R$(libdir) -lmenu"
CONFIGURE_ARGS += F_LIBS="-L$(libdir) -R$(libdir) -lform"

include ../category.mk
