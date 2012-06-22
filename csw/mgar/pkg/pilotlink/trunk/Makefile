# $Id$

NAME = pilot-link
VERSION = 0.12.5
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Free package to manage palmos based PDAs with Unix
define BLURB
  pilot-link is a suite of tools used to connect your Palm or PalmOS
  compatible handheld with Unix, Linux, and any other POSIX-compatible
  machine. pilot-link works with all PalmOS handhelds, including those
  made by Handspring, Sony, and Palm, as well as others.

  pilot-link includes userspace "conduits" that allow you to syncronize
  information to and from your Palm device, as well as libraries of
  Palm-compatible functions that allow other applications to take advantage
  of the code included in pilot-link.

  There are also several language "bindings" that allow you to use your
  favorite development language with pilot-link, such as Java, Tcl, Perl,
  and Python.
endef

MASTER_SITES		=	http://downloads.pilot-link.org/
DISTFILES			=	$(DISTNAME).tar.bz2

PACKAGING_PLATFORMS	=	solaris10-sparc
PACKAGING_PLATFORMS	+=	solaris10-i386

BUILD_DEP_PKGS		+=	CSWperl
BUILD_DEP_PKGS		+=	CSWtcl
BUILD_DEP_PKGS		+=	CSWpython-dev
BUILD_DEP_PKGS		+=	SUNWlibusb
BUILD_DEP_PKGS		+=	SUNWj6dev
BUILD_DEP_PKGS		+=	CSWdoxygen

RUNTIME_DEP_PKGS	=	CSWperl
RUNTIME_DEP_PKGS	+=	CSWtcl
RUNTIME_DEP_PKGS	+=	CSWpython
RUNTIME_DEP_PKGS	+=	SUNWlibusb
RUNTIME_DEP_PKGS	+=	SUNWj6rt

# This cannot be tracked with checkpkg
# CHECKPKG_OVERRIDES_CSWpilot-link += surplus-dependency|CSWperl
# CHECKPKG_OVERRIDES_CSWpilot-link += surplus-dependency|CSWtcl
# CHECKPKG_OVERRIDES_CSWpilot-link += surplus-dependency|CSWpython

PATCHFILES			=	0001-Fix-python-binding-configuration.patch
PATCHFILES			+=	0002-Fix-ctime_r-prototype.patch
PATCHFILES			+=	0003-Avoid-including-redundant-SFW.patch
PATCHFILES			+=	0004-Include-Solaris-specifics-Java-binding.patch

GARCOMPILER			=	SOS12U3
EXTRA_INC			=	/usr/sfw/include
EXTRA_LDFLAGS		=	-L/usr/sfw/lib -R/usr/sfw/lib -lusb

CONFIGURE_ARGS		=	$(DIRPATHS)
CONFIGURE_ARGS		+=	--enable-threads
CONFIGURE_ARGS		+=	--enable-conduits
CONFIGURE_ARGS		+=	--enable-libusb
CONFIGURE_ARGS		+=	--with-perl=$(bindir)/perl
CONFIGURE_ARGS		+=	--with-java=/usr/java
CONFIGURE_ARGS		+=	--with-tcl=$(libdir)
CONFIGURE_ARGS		+=	--with-tclinclude=$(includedir)
CONFIGURE_ARGS		+=	--with-python

#LICENCE_CSWpilot-link		=	COPYING
#LICENCE_CSWpilot-link-lib	=	COPYING.LIB

include gar/category.mk

# kludge to ensure that /opt/csw/include come before /usr/sfw/include
# (needed to have USB capacity):
CPPFLAGS	:=	$(sort $(CPPFLAGS))

pre-configure-modulated:
	@echo "executing $@"
	cd $(WORKSRC) && libtoolize
	cd $(WORKSRC) && aclocal -I m4
	cd $(WORKSRC) && automake -a
	cd $(WORKSRC) && autoconf
	$(MAKECOOKIE)

documents	=	\
				doc/README \
				doc/README.libusb \
				doc/README.usb

post-install-modulated: pkgdocdir = $(docdir)/$(NAME)
post-install-modulated:
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)$(pkgdocdir)
	cd $(WORKSRC) && ginstall --preserve-timestamps --mode=u=rw,go=r $(documents) $(DESTDIR)$(pkgdocdir)
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)$(mandir)/man1 $(DESTDIR)$(mandir)/man7
	cd $(WORKSRC) && ginstall --preserve-timestamps --mode=u=rw,go=r doc/man/*.1 $(DESTDIR)$(mandir)/man1
	cd $(WORKSRC) && ginstall --preserve-timestamps --mode=u=rw,go=r doc/man/*.7 $(DESTDIR)$(mandir)/man7

# this is private and not available publicly
mydependencies:
	$(HOME)/bin/ocswdeplist --package $(NAME)
