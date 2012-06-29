# $Id$

NAME = par2cmdline
VERSION = 0.4
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = Program for creating and using PAR2 files
define BLURB
  Program for creating and using PAR2 files to detect damage in data
  files and repair them if necessary
endef

MASTER_SITES	=	$(SF_MIRRORS)
SF_PROJ			=	parchive
DISTFILES		=	$(DISTNAME).tar.gz
PATCHFILES		=	0001-Debian-0.4-11-serial-000_unidentified.patch
PATCHFILES		+=	0002-Debian-0.4-11-serial-001_hardlinks.patch
PATCHFILES		+=	0003-Debian-0.4-11-serial-002_gcc_40_fixes.patch
PATCHFILES		+=	0004-Debian-0.4-11-serial-003_fix_crash_in_quiet_mode.patch
PATCHFILES		+=	0005-Fix-media-size-ioctl.patch
PATCHFILES		+=	0006-Fix-pretest-script.patch

GARCOMPILER		=	GNU
CONFIGURE_ARGS	=	$(DIRPATHS)

RUNTIME_DEP_PKGS	+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS	+=	CSWlibstdc++6

PACKAGING_PLATFORMS	=	solaris10-sparc
PACKAGING_PLATFORMS	+=	solaris10-i386

include gar/category.mk

post-install-modulated: pkgdocdir = $(docdir)/$(NAME)
post-install-modulated:
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)$(pkgdocdir)
	ginstall --preserve-timestamps --mode=u=rw,go=r $(WORKSRC)/README $(DESTDIR)$(pkgdocdir)
	$(MAKECOOKIE)

# this is private and not available publicly
mydependencies:
	$(HOME)/bin/ocswdeplist --package $(NAME)
