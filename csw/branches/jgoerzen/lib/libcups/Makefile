GARNAME = libcups
GARVERSION = 1.2.2
CATEGORIES = lib

DESCRIPTION = Library and Header Files for the Common UNIX Printing System
define BLURB
  CUPS provides a portable printing layer for UNIX(R)-based operating
  systems.  It is developed and maintained by Easy Software Products to
  promote a standard printing solution and is the standard printing system
  in MacOS(R) X and most Linux(R) distributions.
endef

MASTER_SITES = http://ftp.easysw.com/pub/cups/1.2.2/
DISTFILES  = cups-$(GARVERSION)-source.tar.bz2
DISTFILES += $(call admfiles,CSWlibcups,depend prototype)

LD_OPTIONS = -R/opt/csw/lib/\$$ISALIST -R/opt/csw/lib

CONFIGURE_ARGS = $(DIRPATHS)

# This is a hack that's needed, because configure (Makedefs) will otherwise
# plase -ltiff, etc. first and -L/opt/csw/lib afterwards, thus being unable
# to find any of the image libraries.
# Fortunately, configure honors values already in $DSOFLAGS, so we can use
# that to make sure -L/opt/csw/lib is the first argument passed to ld.
DSOFLAGS = -L/opt/csw/lib
export DSOFLAGS

# For some reason, the CUPS guys have decided to use DSTROOT for what
# everybody else calls DESTDIR.
DSTROOT = $(DESTDIR)
export DSTROOT

WORKSRC ?= $(WORKDIR)/cups-$(GARVERSION)

include ../category.mk

## This little hack makes sure that libcups-<version> is a symlink to the
## directory cups-<version>, so the makefile system can proceed to use the
## package name as directory name where the sources reside.
#post-extract:
#	(cd $(WORKDIR); \
#	test -d libcups-$(GARVERSION) && rmdir libcups-$(GARVERSION); \
#	test -h libcups-$(GARVERSION) || ln -s cups-$(GARVERSION) libcups-$(GARVERSION))
