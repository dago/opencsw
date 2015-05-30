NAME = joe
VERSION = 4.0
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Joe's Own Editor
define BLURB
  JOE is the professional freeware ASCII text screen editor for UNIX.
  It makes full use of the power and versatility of UNIX, but lacks the steep
  learning curve and basic nonsense you have to deal with in every other UNIX
  editor. JOE has the feel of most IBM PC text editors: The key-sequences are
  reminiscent of WordStar and Turbo-C.  JOE is much more powerful than those
  editors, however.  JOE has all of the features a UNIX user should expect:
  full use of termcap/terminfo, excellent screen update optimizations (JOE is
  fully usable at 2400 baud), simple installation, and all of the
  UNIX-integration features ofECT VI.
endef

SF_PROJ = joe-editor
MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=23475
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*)

sysconfdir = /etc/opt/csw
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-curses

PRESERVECONF = /etc/opt/csw/joe/.*
MIGRATE_FILES = jmacsrc joerc jpico# If configure detects Solaris it adds unconditionally /usr/local - why??
REINPLACEMENTS += foo
REINPLACE_MATCH_foo = solaris
REINPLACE_WITH_foo = goaway
REINPLACE_FILES_foo += configure

include gar/category.mk
