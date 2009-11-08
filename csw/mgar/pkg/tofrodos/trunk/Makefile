GARNAME = tofrodos
GARVERSION = 1.7.8
CATEGORIES = utils

DESCRIPTION = Text file conversion utility that converts ASCII files between the MSDOS (or Windows) to Unix format.
define BLURB
It is a useful utility to have around when you have to convert files between 
MSDOS (or Windows) and Unix/Linux/BSD (and her clones and variants). It comes 
standard with a number of systems and is often found on the system as "todos", 
"fromdos", "dos2unix" and "unix2dos".
endef

WORKSRC ?= $(WORKDIR)/$(GARNAME)/src
MASTER_SITES = http://tofrodos.sourceforge.net/download/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_SCRIPTS =

#BUILD_ARGS = CC=$(CC) LD=$(CC) MAKE=$(MAKE) CDEBUG= CFLAGS="$(CFLAGS) -c"
BUILD_ARGS = CC=$(CC) LD=$(CC) MAKE=$(MAKE) CDEBUG= CFLAGS="$(CFLAGS) -c -Dstricmp=strcasecmp"

TEST_SCRIPTS =

INSTALL_ARGS = BINDIR=$(DESTDIR)$(bindir) MANDIR=$(DESTDIR)$(mandir)/man1 INSTALL=$(bindir)/ginstall

pre-install-modulated:
	@echo "Creating directories"
	mkdir -p $(DESTDIR)$(bindir)
	mkdir -p $(DESTDIR)$(mandir)/man1

post-install-modulated:
	@echo "Creating links"
	ln -s ./fromdos $(DESTDIR)$(bindir)/dos2unix
	ln -s ./fromdos $(DESTDIR)$(bindir)/unix2dos
	ln -s ./fromdos.1 $(DESTDIR)$(mandir)/man1/dos2unix
	ln -s ./fromdos.1 $(DESTDIR)$(mandir)/man1/unix2dos

include gar/category.mk
