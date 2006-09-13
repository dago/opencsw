GARNAME = glib2
GARVERSION = 2.4.0
CATEGORIES = lib

DESCRIPTION = The GLib library of C routines.
define BLURB
  GLib is a library containing many useful C routines for things such as trees,
  hashes, and lists. GLib was previously distributed with the GTK toolkit, but
  has been split off as of the developers' version 1.1.0.
endef

MASTER_SITES = ftp://ftp.gtk.org/pub/gtk/v2.4/

DISTFILES = glib-$(GARVERSION).tar.bz2
WORKSRC = $(WORKDIR)/glib-$(GARVERSION)

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-debug=yes

TEST_TARGET = check

# Bug #136867 (child-watch)
TEST_SCRIPTS =

include ../category.mk

# For some reason, autoconf drops the ball on this one...
post-install:
	@( cd $(DESTDIR)$(bindir) ; \
	$(PERL) -i -plne '$$. == 1 && s{#!\s+}{#!$(PERL) }' glib-mkenums )
