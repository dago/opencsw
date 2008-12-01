GARNAME = ddd
GARVERSION = 3.3.8
CATEGORIES = utils

DESCRIPTION = Common graphical user interface for GDB, DBX and XDB
define BLURB
    GNU DDD, the Data Display Debugger, is a GUI to command-line debuggers like
    GDB, DBX, JDB, XDB, Ladebug, WDB, the Perl debugger, or the Python debugger. It
    provides a graphical data display where complex data structures can be explored
    incrementally and interactively.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz 

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

ifneq ($(BUILD_XDEPS),0)
LIBDEPS = lib/ncurses lib/readline
endif

CONFIGURE_ARGS  = --prefix=$(DESTDIR)$(prefix)
CONFIGURE_ARGS += --with-ncurses-libraries=$(tool_prefix)
CONFIGURE_ARGS += --with-readline-libraries=$(tool_prefix)

include gar/category.mk
