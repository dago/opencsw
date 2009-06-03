GARNAME = zsh
GARVERSION = 4.3.10
CATEGORIES = devel

DESCRIPTION = Powerful UNIX shell
define BLURB
  Zsh is a shell designed for interactive use, although it is also a
  powerful scripting language. Many of the useful features of bash,
  ksh, and tcsh were incorporated into zsh; many original features were added.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWzsh,postinstall postremove)

REQUIRED_PKGS = CSWiconv CSWncurses CSWpcrert CSWgdbm

SPKG_SOURCEURL = http://www.zsh.org

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=4068
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-maildir-support
CONFIGURE_ARGS += --enable-fndir=$(sharedstatedir)/$(GARNAME)/functions
CONFIGURE_ARGS += --enable-pcre

include gar/category.mk

# Use term.h from ncurses or we get compile errors
#   http://www.zsh.org/mla/workers/2007/msg01236.html
CPPFLAGS := -I$(includedir)/ncursesw $(CPPFLAGS)
