GARNAME = glib2
GARVERSION = 2.4.0
CATEGORIES = lib

SPKG_PKGNAME = CSWglib2
SPKG_BITNAME = glib2

DESCRIPTION = The GLib library of C routines.
define BLURB
  GLib is a library containing many useful C routines for things such as trees,
  hashes, and lists. GLib was previously distributed with the GTK toolkit, but
  has been split off as of the developers' version 1.1.0.
endef

MASTER_SITES = http://ftp.gnome.org/pub/gnome/sources/glib/2.4/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS) --enable-debug=yes

TEST_TARGET = check

# Bug #136867 (child-watch)
ENABLE_TEST = 0

include ../category.mk

# For some reason, autoconf drops the ball on this one...
post-install:
	@( cd $(DESTDIR)$(bindir) ; \
	$(PERL) -i -plne '$$. == 1 && s{#!\s+}{#!$(PERL) }' glib-mkenums )
