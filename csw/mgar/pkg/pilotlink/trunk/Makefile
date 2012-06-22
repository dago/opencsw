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
BUILD_DEP_PKGS		+=	CSWlibreadline-dev
BUILD_DEP_PKGS		+=	CSWlibncurses-dev
BUILD_DEP_PKGS		+=	CSWlibpng-dev
BUILD_DEP_PKGS		+=	SUNWlibusb
#BUILD_DEP_PKGS		+=	SUNWj6dev

#RUNTIME_DEP_PKGS	+=	SUNWj6rt

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

PACKAGES							=	CSWpilot-link-doc
CATALOGNAME_CSWpilot-link-doc		=	pilot_link_doc
SPKG_DESC_CSWpilot-link-doc			=	$(DESCRIPTION), documentation
OBSOLETED_BY_CSWpilot-link-doc		=	CSWpilotlink
CATALOGNAME_CSWpilotlink			=	pilotlink_stub
LICENCE_CSWpilot-link-doc			=	COPYING
ARCHALL_CSWpilot-link-doc			=	1
CHECKPKG_OVERRIDES_CSWpilot-link-doc += file-with-bad-content|/usr/local|root/opt/csw/share/doc/pilot-link/README.usb

PACKAGES						+=	CSWpilot-link
CATALOGNAME_CSWpilot-link		=	pilot_link
SPKG_DESC_CSWpilot-link			=	$(DESCRIPTION)
OBSOLETED_BY_CSWpilot-link		=	CSWpilotlink
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pilot-addresses
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pilot-clip
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pilot-csd
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pilot-debugsh
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pilot-dedupe
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pilot-dlpsh
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pilot-file
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pilot-foto
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pilot-foto-treo600
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pilot-foto-treo650
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pilot-getram
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pilot-getrom
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pilot-getromtoken
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pilot-hinotes
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pilot-ietf2datebook
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pilot-install-datebook
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pilot-install-expenses
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pilot-install-hinote
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pilot-install-memo
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pilot-install-netsync
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pilot-install-todo
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pilot-install-todos
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pilot-install-user
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pilot-memos
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pilot-nredir
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pilot-read-expenses
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pilot-read-ical
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pilot-read-notepad
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pilot-read-palmpix
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pilot-read-screenshot
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pilot-read-todos
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pilot-read-veo
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pilot-reminders
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pilot-schlep
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pilot-sync-plan
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pilot-undelete
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pilot-wav
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pilot-xfer
PKGFILES_CSWpilot-link			+=	/opt/csw/bin/pitclsh
PKGFILES_CSWpilot-link			+=	/opt/csw/share/pilot-link/pix/b1.gif
PKGFILES_CSWpilot-link			+=	/opt/csw/share/pilot-link/pix/b2.gif
PKGFILES_CSWpilot-link			+=	/opt/csw/share/pilot-link/pix/b3.gif
PKGFILES_CSWpilot-link			+=	/opt/csw/share/pilot-link/pix/b4.gif
PKGFILES_CSWpilot-link			+=	/opt/csw/share/pilot-link/pix/b5.gif
PKGFILES_CSWpilot-link			+=	/opt/csw/share/pilot-link/pix/b6.gif
PKGFILES_CSWpilot-link			+=	/opt/csw/share/pilot-link/pix/b7.gif
PKGFILES_CSWpilot-link			+=	/opt/csw/share/pilot-link/pix/case.gif
PKGFILES_CSWpilot-link			+=	/opt/csw/share/pilot-link/pix/case.xbm
PKGFILES_CSWpilot-link			+=	/opt/csw/share/pilot-link/pix/casemask.xbm
PKGFILES_CSWpilot-link			+=	/opt/csw/share/pilot-link/prc/getrom.prc
PKGFILES_CSWpilot-link			+=	/opt/csw/share/pilot-link/prc/getrom2.prc
PKGFILES_CSWpilot-link			+=	/opt/csw/share/pilot-link/udev/60-libpisock.rules
RUNTIME_DEP_PKGS_CSWpilot-link	+=	CSWlibpisock9
RUNTIME_DEP_PKGS_CSWpilot-link	+=	CSWlibpisync1
RUNTIME_DEP_PKGS_CSWpilot-link	+=	CSWlibpitcl0
RUNTIME_DEP_PKGS_CSWpilot-link	+=	CSWlibintl8
RUNTIME_DEP_PKGS_CSWpilot-link	+=	CSWlibncurses5
RUNTIME_DEP_PKGS_CSWpilot-link	+=	CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWpilot-link	+=	CSWlibreadline6
LICENCE_CSWpilot-link			=	COPYING

PACKAGES						+=	CSWlibpisock9
CATALOGNAME_CSWlibpisock9		=	libpisock9
PKGFILES_CSWlibpisock9			+=	$(call baseisadirs,$(libdir),libpisock\.so\.9\.0\.2)
PKGFILES_CSWlibpisock9			+=	$(call baseisadirs,$(libdir),libpisock\.so\.9(\.\d+)*)
SPKG_DESC_CSWlibpisock9			+=	$(DESCRIPTION), libpisock.so.9
OBSOLETED_BY_CSWlibpisock9		=	CSWpilotlink
RUNTIME_DEP_PKGS_CSWlibpisock9	+=	SUNWlibusb
LICENCE_CSWlibpisock9			=	COPYING.LIB

PACKAGES						+=	CSWlibpisync1
CATALOGNAME_CSWlibpisync1		=	libpisync1
PKGFILES_CSWlibpisync1			+=	$(call baseisadirs,$(libdir),libpisync\.so\.1\.0\.3)
PKGFILES_CSWlibpisync1			+=	$(call baseisadirs,$(libdir),libpisync\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibpisync1			+=	$(DESCRIPTION), libpisync.so.1
OBSOLETED_BY_CSWlibpisync1		=	CSWpilotlink
RUNTIME_DEP_PKGS_CSWlibpisync1	+=	CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibpisync1	+=	CSWlibz1
RUNTIME_DEP_PKGS_CSWlibpisync1	+=	CSWlibpisock9
LICENCE_CSWlibpisync1			=	COPYING.LIB

PACKAGES						+=	CSWlibpitcl0
CATALOGNAME_CSWlibpitcl0		=	libpitcl0
PKGFILES_CSWlibpitcl0			+=	$(call baseisadirs,$(libdir),libpitcl\.so\.0\.0\.0)
PKGFILES_CSWlibpitcl0			+=	$(call baseisadirs,$(libdir),libpitcl\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibpitcl0			+=	$(DESCRIPTION), TCL binding, libpitcl.so.0
OBSOLETED_BY_CSWlibpitcl0		=	CSWpilotlink
RUNTIME_DEP_PKGS_CSWlibpitcl0	+=	CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibpitcl0	+=	CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibpitcl0	+=	CSWlibpopt0
RUNTIME_DEP_PKGS_CSWlibpitcl0	+=	CSWlibz1
RUNTIME_DEP_PKGS_CSWlibpitcl0	+=	CSWlibpisock9
RUNTIME_DEP_PKGS_CSWlibpitcl0	+=	CSWtcl
LICENCE_CSWlibpitcl0			=	COPYING.LIB

PACKAGES							+=	CSWpilot-link-perl
CATALOGNAME_CSWpilot-link-perl		=	pilot_link_perl
SPKG_DESC_CSWpilot-link-perl		=	$(DESCRIPTION), Perl binding
OBSOLETED_BY_CSWpilot-link-perl		=	CSWpilotlink
PKGFILES_CSWpilot-link-perl			+=	/opt/csw/lib/perl/5.10.1/perllocal.pod
PKGFILES_CSWpilot-link-perl			+=	/opt/csw/lib/perl/csw/PDA/Pilot.pm
PKGFILES_CSWpilot-link-perl			+=	/opt/csw/lib/perl/csw/PDA/dump.pl
PKGFILES_CSWpilot-link-perl			+=	/opt/csw/lib/perl/csw/auto/PDA/Pilot/.packlist
PKGFILES_CSWpilot-link-perl			+=	/opt/csw/lib/perl/csw/auto/PDA/Pilot/Pilot.bs
PKGFILES_CSWpilot-link-perl			+=	/opt/csw/lib/perl/csw/auto/PDA/Pilot/Pilot.so
PKGFILES_CSWpilot-link-perl			+=	/opt/csw/lib/perl/csw/auto/PDA/Pilot/autosplit.ix
RUNTIME_DEP_PKGS_CSWpilot-link-perl	+=	CSWlibpisock9
RUNTIME_DEP_PKGS_CSWpilot-link-perl	+=	CSWperl
RUNTIME_DEP_PKGS_CSWpilot-link-perl	+=	CSWlibz1
ARCHALL_CSWpilot-link-perl			=	1

PACKAGES								+=	CSWpilot-link-python
CATALOGNAME_CSWpilot-link-python		=	pilot_link_python
SPKG_DESC_CSWpilot-link-python			=	$(DESCRIPTION), Python binding
OBSOLETED_BY_CSWpilot-link-python		=	CSWpilotlink
PKGFILES_CSWpilot-link-python			+=	/opt/csw/lib/python/site-packages/_pisock.so
PKGFILES_CSWpilot-link-python			+=	/opt/csw/lib/python/site-packages/pisock.py
PKGFILES_CSWpilot-link-python			+=	/opt/csw/lib/python/site-packages/pisock.pyc
PKGFILES_CSWpilot-link-python			+=	/opt/csw/lib/python/site-packages/pisockextras.py
PKGFILES_CSWpilot-link-python			+=	/opt/csw/lib/python/site-packages/pisockextras.pyc
PKGFILES_CSWpilot-link-python			+=	/opt/csw/lib/python/site-packages/python_libpisock-0.12.5-py2.6.egg-info
RUNTIME_DEP_PKGS_CSWpilot-link-python	+=	CSWlibpisock9
RUNTIME_DEP_PKGS_CSWpilot-link-python	+=	CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpilot-link-python	+=	CSWlibz1
ARCHALL_CSWpilot-link-python			=	1
CHECKPKG_OVERRIDES_CSWpilot-link-python	+=	discouraged-path-in-pkgmap|/opt/csw/lib/python/site-packages/pisock.pyc
CHECKPKG_OVERRIDES_CSWpilot-link-python	+=	discouraged-path-in-pkgmap|/opt/csw/lib/python/site-packages/pisockextras.pyc
CHECKPKG_OVERRIDES_CSWpilot-link-python	+=	pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWpilot-link-python	+=	catalogname-does-not-start-with-py_

PACKAGES								+=	CSWpilot-link-dev
CATALOGNAME_CSWpilot-link-dev			=	pilot_link_dev
SPKG_DESC_CSWpilot-link-dev				+=	$(DESCRIPTION), development files
PKGFILES_CSWpilot-link-dev				+=	/opt/csw/lib/libpisock.so
PKGFILES_CSWpilot-link-dev				+=	/opt/csw/lib/libpisync.so
PKGFILES_CSWpilot-link-dev				+=	/opt/csw/lib/libpitcl.so
PKGFILES_CSWpilot-link-dev				+=	$(PKGFILES_DEVEL)
OBSOLETED_BY_CSWpilot-link-dev			=	CSWpilotlink
RUNTIME_DEP_PKGS_CSWpilot-link-dev		+=	CSWlibpisock9
RUNTIME_DEP_PKGS_CSWpilot-link-dev		+=	CSWlibpisync1
RUNTIME_DEP_PKGS_CSWpilot-link-dev		+=	CSWlibpitcl0
RUNTIME_DEP_PKGS_CSWpilot-link-dev		+=	CSWpilot-link-perl
RUNTIME_DEP_PKGS_CSWpilot-link-dev		+=	CSWpilot-link-python
LICENCE_CSWpilot-link-dev				=	COPYING
ARCHALL_CSWpilot-link-dev				=	1
CHECKPKG_OVERRIDES_CSWpilot-link-dev	+=	archall-devel-package

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
