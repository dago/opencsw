GARNAME = ncurses
GARVERSION = 5.7
CATEGORIES = lib

DESCRIPTION = A free software emulation of curses
define BLURB
 The ncurses (new curses) library is a free software emulation of curses
  in System V Release 4.0 and more. It uses terminfo format, supports pads
  and color and multiple highlights and forms charcters and function-key
  mapping, and has all the other SYSV-curses enhancements over BSD curses.
  It should port easily to any ANSI/POSIX-conforming UNIX-like system.
  On systems supporting libiconv, the library can be built to support
  wide- and multibyte-character applications, e.g., UTF-8. 
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PATCHFILES = patch-xcode.diff

LICENSE = README

SPKG_SOURCEURL = http://www.gnu.org/software/ncurses/ncurses.html

BUILD64 = 1
NO_ISAEXEC = 1
RUNPATHQUOTE = 1

EXTRA_MODULATORS = WIDEC
MODULATIONS_WIDEC = disable enable

EXTRA_CONFIGURE_WIDEC-disable = --disable-widec
EXTRA_CONFIGURE_WIDEC-enable = --enable-widec

CONFIGURE_ARGS = --prefix=$(prefix)
CONFIGURE_ARGS += --bindir=$(bindir)
CONFIGURE_ARGS += --libdir=$(libdir)
CONFIGURE_ARGS += --mandir=$(mandir)
CONFIGURE_ARGS += --without-libtool
CONFIGURE_ARGS += --with-shared 
CONFIGURE_ARGS += --disable-overwrite
CONFIGURE_ARGS += --without-ada
CONFIGURE_ARGS += $(EXTRA_CONFIGURE_WIDEC-$(WIDEC))

# Don't use capabilities HPA and VPA as Solaris xterm doesn't understand it.
# See for details
#   <http://opencsw.org/bugtrack/view.php?id=2961>
#   <http://opencsw.org/bugtrack/view.php?id=2942>
#   <http://bugs.opensolaris.org/bugdatabase/view_bug.do?bug_id=6569261>
CONFIGURE_ARGS += --without-xterm-new

MERGE_SCRIPTS_isa-sparcv8-widec-disable = copy-only copy-config-only
   MERGE_DIRS_isa-sparcv8-widec-disable = $(libdir)
MERGE_SCRIPTS_isa-sparcv9-widec-disable = copy-relocated-only copy-config-only
   MERGE_DIRS_isa-sparcv9-widec-disable = $(libdir)

 MERGE_SCRIPTS_isa-sparcv8-widec-enable = copy-all
 MERGE_SCRIPTS_isa-sparcv9-widec-enable = copy-relocated-only copy-config-only
    MERGE_DIRS_isa-sparcv9-widec-enable = $(libdir)

   MERGE_SCRIPTS_isa-i386-widec-disable = copy-only copy-config-only
      MERGE_DIRS_isa-i386-widec-disable = $(libdir)
  MERGE_SCRIPTS_isa-amd64-widec-disable = copy-relocated-only copy-config-only
     MERGE_DIRS_isa-amd64-widec-disable = $(libdir)

    MERGE_SCRIPTS_isa-i386-widec-enable = copy-all
   MERGE_SCRIPTS_isa-amd64-widec-enable = copy-relocated-only copy-config-only
      MERGE_DIRS_isa-amd64-widec-enable = $(libdir)

include gar/category.mk

LDFLAGS := $(filter-out -L%,$(LDFLAGS))
