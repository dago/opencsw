GARNAME = ncurses
GARVERSION = 5.7
CATEGORIES = lib

DESCRIPTION = ncurses library and utilities
define BLURB
        The ncurses (new curses) library is a free software emulation of curses in System V Release 4.0 and more. It uses terminfo forma
t, supports pads and color and multiple highlights and forms charcters and function-key mapping, and has all the other SYSV-curses enhan
cements over BSD curses. It should port easily to any ANSI/POSIX-conforming UNIX-like system. On systems supporting libiconv, the librar
y can be built to support wide- and multibyte-character applications, e.g., UTF-8. 
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWncurses)

PATCHFILES = patch-xcode.diff

SPKG_SOURCEURL = http://www.gnu.org/software/ncurses/ncurses.html

BUILD64 = 1
NO_ISAEXEC = 1
RUNPATHQUOTE = 1

CONFIGURE_ARGS = --prefix=$(prefix)
CONFIGURE_ARGS += --bindir=$(bindir)
CONFIGURE_ARGS += --libdir=$(libdir)
CONFIGURE_ARGS += --mandir=$(mandir)
CONFIGURE_ARGS += --without-libtool
CONFIGURE_ARGS += --with-shared 
CONFIGURE_ARGS += --disable-overwrite
CONFIGURE_ARGS += --without-ada

# Don't use capabilities HPA and VPA as Solaris xterm doesn't understand it.
# See for details
#   <http://opencsw.org/bugtrack/view.php?id=2961>
#   <http://opencsw.org/bugtrack/view.php?id=2942>
#   <http://bugs.opensolaris.org/bugdatabase/view_bug.do?bug_id=6569261>
CONFIGURE_ARGS += --without-xterm-new

include gar/category.mk

LDFLAGS := $(filter-out -L%,$(LDFLAGS))
