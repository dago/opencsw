GARNAME = joe
GARVERSION = 3.3
CATEGORIES = utils
SPKG_PACKAGER   = Markus Mayer
SPKG_EMAIL      = mmayer@blastwave.org


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
  UNIX-integration features of VI.
endef

MASTER_SITES = http://superb-west.dl.sourceforge.net/sourceforge/joe-editor/ http://mesh.dl.sourceforge.net/sourceforge/joe-editor/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWjoe,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

# joe doesn't have a test target
TEST_TARGET =

include gar/category.mk
