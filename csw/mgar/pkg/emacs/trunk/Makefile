# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME		=	emacs
VERSION		=	23.4
GARTYPE		=	v2
CATEGORIES	=	apps

DESCRIPTION = The GNU Emacs editor
define BLURB
  Emacs is the extensible, customizable, self-documenting real-time
  display editor.
endef

DISTFILES		=	$(DISTNAME).tar.bz2
MASTER_SITES	=	$(GNU_MIRROR)

# this is necessary because GNU id options dialect is is used; BTW, I
# think that adding this systematically at the beginning of the PATH
# helps in packaging projects issued from the Linux steam.
INSTALL_ARGS		+=	PATH="/opt/csw/gnu:$$PATH"

GARCOMPILER			=	GNU

BUILD_DEP_PKGS		=	CSWcoreutils
BUILD_DEP_PKGS		+=	CSWglib2devel
BUILD_DEP_PKGS		+=	CSWlibatk-dev
BUILD_DEP_PKGS		+=	CSWlibbz2-dev
BUILD_DEP_PKGS		+=	CSWlibcairo-dev
BUILD_DEP_PKGS		+=	CSWlibdatrie-dev
BUILD_DEP_PKGS		+=	CSWlibdbus-dev
BUILD_DEP_PKGS		+=	CSWlibdbus-glib-dev
BUILD_DEP_PKGS		+=	CSWlibexpat-dev
BUILD_DEP_PKGS		+=	CSWlibfreetype-dev
BUILD_DEP_PKGS		+=	CSWlibgconf-dev
BUILD_DEP_PKGS		+=	CSWlibgdk-pixbuf-dev
BUILD_DEP_PKGS		+=	CSWlibgif-dev
BUILD_DEP_PKGS		+=	CSWlibglib2-dev
BUILD_DEP_PKGS		+=	CSWlibgtk2-dev
BUILD_DEP_PKGS		+=	CSWlibiconv-dev
BUILD_DEP_PKGS		+=	CSWlibjbig-dev
BUILD_DEP_PKGS		+=	CSWlibjpeg-dev
BUILD_DEP_PKGS		+=	CSWlibm17n-dev
BUILD_DEP_PKGS		+=	CSWlibotf-dev
BUILD_DEP_PKGS		+=	CSWlibpixman-dev
BUILD_DEP_PKGS		+=	CSWlibpng-dev
BUILD_DEP_PKGS		+=	CSWlibpthreadstubs
BUILD_DEP_PKGS		+=	CSWlibrsvg-dev
BUILD_DEP_PKGS		+=	CSWlibthai-dev
BUILD_DEP_PKGS		+=	CSWlibtiff-dev
BUILD_DEP_PKGS		+=	CSWlibx11devel
BUILD_DEP_PKGS		+=	CSWlibxaudevel
BUILD_DEP_PKGS		+=	CSWlibxcbdevel
BUILD_DEP_PKGS		+=	CSWlibxdmcpdevel
BUILD_DEP_PKGS		+=	CSWlibxft2devel
BUILD_DEP_PKGS		+=	CSWlibxml2-dev
BUILD_DEP_PKGS		+=	CSWlibxpmdevel
BUILD_DEP_PKGS		+=	CSWlibz-dev
BUILD_DEP_PKGS		+=	CSWpangodevel
BUILD_DEP_PKGS		+=	CSWpkgconfig
BUILD_DEP_PKGS		+=	CSWsunx11devel

PACKAGING_PLATFORMS	=	solaris10-sparc
PACKAGING_PLATFORMS	+=	solaris10-i386

PATCHFILES			+=	0001-activate-Xft-for-configure.patch

EXTRA_MODULATORS			=	FEATURES
MODULATIONS_FEATURES		=	athena
MODULATIONS_FEATURES		+=	gtk
MODULATIONS_FEATURES		+=	nox

EXTRA_CONFIGURE_ARGS_athena	=	--with-x-toolkit=athena
EXTRA_CONFIGURE_ARGS_athena	+=	--without-dbus
EXTRA_CONFIGURE_ARGS_athena	+=	--without-gconf

EXTRA_CONFIGURE_ARGS_gtk	=	--with-x-toolkit=gtk

EXTRA_CONFIGURE_ARGS_nox	=	--with-x-toolkit=no
EXTRA_CONFIGURE_ARGS_nox	+=	--without-sound
EXTRA_CONFIGURE_ARGS_nox	+=	--without-xpm
EXTRA_CONFIGURE_ARGS_nox	+=	--without-jpeg
EXTRA_CONFIGURE_ARGS_nox	+=	--without-tiff
EXTRA_CONFIGURE_ARGS_nox	+=	--without-gif
EXTRA_CONFIGURE_ARGS_nox	+=	--without-png
EXTRA_CONFIGURE_ARGS_nox	+=	--without-rsvg
EXTRA_CONFIGURE_ARGS_nox	+=	--without-xft
EXTRA_CONFIGURE_ARGS_nox	+=	--without-libotf
EXTRA_CONFIGURE_ARGS_nox	+=	--without-m17n-flt
EXTRA_CONFIGURE_ARGS_nox	+=	--without-toolkit-scroll-bars
EXTRA_CONFIGURE_ARGS_nox	+=	--without-xim
EXTRA_CONFIGURE_ARGS_nox	+=	--without-dbus
EXTRA_CONFIGURE_ARGS_nox	+=	--without-x

CONFIGURE_ARGS	= $(DIRPATHS)
CONFIGURE_ARGS	+= $(EXTRA_CONFIGURE_ARGS_$(FEATURES))

MERGE_SCRIPTS_isa-default-features-athena	=	copy-all

MERGE_DIRS_isa-default-features-gtk			=	$(bindir)
MERGE_SCRIPTS_isa-default-features-gtk		=	copy-only

MERGE_DIRS_isa-default-features-nox			=	$(bindir)
MERGE_SCRIPTS_isa-default-features-nox		=	copy-only

ALTERNATIVES_CSWemacs		=	athena
ALTERNATIVES_CSWemacs-gtk	=	gtk
ALTERNATIVES_CSWemacs-nox	=	nox

ALTERNATIVE_athena			=	$(bindir)/emacs emacs $(bindir)/emacs-athena 200
ALTERNATIVE_gtk				=	$(bindir)/emacs emacs $(bindir)/emacs-gtk 100
ALTERNATIVE_nox				=	$(bindir)/emacs emacs $(bindir)/emacs-nox 300

PACKAGES					=	CSWemacs-common
SPKG_DESC_CSWemacs-common	=	$(DESCRIPTION) - architecture neutral common components
CATALOGNAME_CSWemacs-common		=	emacs_common
# as we use alternatives, we need to obsolete emacs_chooser;
# emacs_common, being the root dependence of all emacs related
# packages, seems the best place to do it.
OBSOLETED_BY_CSWemacs-common	=	CSWemacschooser
OBSOLETED_BY_CSWemacs-common	+=	CSWemacscommon
CATALOGNAME_CSWemacscommon		=	emacscommon_stub
ARCHALL_CSWemacs-common			=	1

PACKAGES					+=	CSWemacs-el
SPKG_DESC_CSWemacs-el		=	$(DESCRIPTION) - elisp sources
CATALOGNAME_CSWemacs-el		=	emacs_el
OBSOLETED_BY_CSWemacs-el	=	CSWemacsel
CATALOGNAME_CSWemacsel		=	emacsel_stub
RUNTIME_DEP_PKGS_CSWemacs-el=	CSWemacs-common
PKGFILES_CSWemacs-el		=	/opt/csw/share/emacs/$(VERSION)/.*[.]el[.]gz
ARCHALL_CSWemacs-el			=	1

PACKAGES								+=	CSWemacs-bin-common
SPKG_DESC_CSWemacs-bin-common			=	$(DESCRIPTION) - common binaries
CATALOGNAME_CSWemacs-bin-common			=	emacs_bin_common
OBSOLETED_BY_CSWemacs-bin-common		=	CSWemacsbincommon
CATALOGNAME_CSWemacsbincommon			=	emacsbincommon_stub
RUNTIME_DEP_PKGS_CSWemacs-bin-common	=	CSWemacs-common
PKGFILES_CSWemacs-bin-common			=	/opt/csw/bin/b2m
PKGFILES_CSWemacs-bin-common			+=	/opt/csw/bin/ctags
PKGFILES_CSWemacs-bin-common			+=	/opt/csw/bin/ebrowse
PKGFILES_CSWemacs-bin-common			+=	/opt/csw/bin/emacsclient
PKGFILES_CSWemacs-bin-common			+=	/opt/csw/bin/etags
PKGFILES_CSWemacs-bin-common			+=	/opt/csw/libexec/emacs/$(VERSION)/[^/]*solaris[^/]*/digest-doc
PKGFILES_CSWemacs-bin-common			+=	/opt/csw/libexec/emacs/$(VERSION)/[^/]*solaris[^/]*/fakemail
PKGFILES_CSWemacs-bin-common			+=	/opt/csw/libexec/emacs/$(VERSION)/[^/]*solaris[^/]*/hexl
PKGFILES_CSWemacs-bin-common			+=	/opt/csw/libexec/emacs/$(VERSION)/[^/]*solaris[^/]*/movemail
PKGFILES_CSWemacs-bin-common			+=	/opt/csw/libexec/emacs/$(VERSION)/[^/]*solaris[^/]*/profile
PKGFILES_CSWemacs-bin-common			+=	/opt/csw/libexec/emacs/$(VERSION)/[^/]*solaris[^/]*/sorted-doc
PKGFILES_CSWemacs-bin-common			+=	/opt/csw/libexec/emacs/$(VERSION)/[^/]*solaris[^/]*/update-game-score

PACKAGES					+=	CSWemacs
SPKG_DESC_CSWemacs			=	$(DESCRIPTION) - based on the Athena toolkit
CATALOGNAME_CSWemacs		=	emacs
RUNTIME_DEP_PKGS_CSWemacs	=	CSWemacs-common
RUNTIME_DEP_PKGS_CSWemacs	+=	CSWemacs-bin-common
RUNTIME_DEP_PKGS_CSWemacs	+=	CSWfconfig
RUNTIME_DEP_PKGS_CSWemacs	+=	CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWemacs	+=	CSWlibcairo2
RUNTIME_DEP_PKGS_CSWemacs	+=	CSWlibcroco
RUNTIME_DEP_PKGS_CSWemacs	+=	CSWlibdatrie1
RUNTIME_DEP_PKGS_CSWemacs	+=	CSWlibexpat1
RUNTIME_DEP_PKGS_CSWemacs	+=	CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWemacs	+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWemacs	+=	CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWemacs	+=	CSWlibgif4
RUNTIME_DEP_PKGS_CSWemacs	+=	CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWemacs	+=	CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWemacs	+=	CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWemacs	+=	CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWemacs	+=	CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWemacs	+=	CSWlibiconv2
RUNTIME_DEP_PKGS_CSWemacs	+=	CSWlibintl8
RUNTIME_DEP_PKGS_CSWemacs	+=	CSWlibjbig2
RUNTIME_DEP_PKGS_CSWemacs	+=	CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWemacs	+=	CSWlibm17n0
RUNTIME_DEP_PKGS_CSWemacs	+=	CSWlibotf0
RUNTIME_DEP_PKGS_CSWemacs	+=	CSWlibpixman1-0
RUNTIME_DEP_PKGS_CSWemacs	+=	CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWemacs	+=	CSWlibrsvg2-2
RUNTIME_DEP_PKGS_CSWemacs	+=	CSWlibthai0
RUNTIME_DEP_PKGS_CSWemacs	+=	CSWlibtiff3
RUNTIME_DEP_PKGS_CSWemacs	+=	CSWlibxft2
RUNTIME_DEP_PKGS_CSWemacs	+=	CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWemacs	+=	CSWlibxrender
RUNTIME_DEP_PKGS_CSWemacs	+=	CSWlibz1
RUNTIME_DEP_PKGS_CSWemacs	+=	CSWpango
RUNTIME_DEP_PKGS_CSWemacs	+=	CSWxpm
PKGFILES_CSWemacs			=	/opt/csw/bin/emacs-athena
PKGFILES_CSWemacs			+=	/opt/csw/bin/emacs-$(VERSION)-athena

PACKAGES						+=	CSWemacs-gtk
SPKG_DESC_CSWemacs-gtk			=	$(DESCRIPTION) - based on the GTK toolkit
CATALOGNAME_CSWemacs-gtk		=	emacs_gtk
OBSOLETED_BY_CSWemacs-gtk		=	CSWemacsgtk
CATALOGNAME_CSWemacsgtk			=	emacs_gtk_stub
RUNTIME_DEP_PKGS_CSWemacs-gtk	=	CSWemacs-common
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWemacs-bin-common
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWfconfig
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibcairo2
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibcroco
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibdatrie1
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibdbus1-3
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibexpat1
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibgconf2-4
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibgif4
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibiconv2
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibintl8
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibjbig2
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibm17n0
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibotf0
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibpixman1-0
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibrsvg2-2
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibthai0
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibtiff3
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibxft2
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibxrender
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibz1
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWorbit2
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWpango
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWxpm
PKGFILES_CSWemacs-gtk			=	/opt/csw/bin/emacs-gtk
PKGFILES_CSWemacs-gtk			+=	/opt/csw/bin/emacs-$(VERSION)-gtk

PACKAGES						+=	CSWemacs-nox
SPKG_DESC_CSWemacs-nox			=	$(DESCRIPTION) - without any XWindows dependencies
CATALOGNAME_CSWemacsnox			=	emacs_nox
OBSOLETED_BY_CSWemacs-nox		=	CSWemacsnox
CATALOGNAME_CSWemacsnox			=	emacs_nox_stub
RUNTIME_DEP_PKGS_CSWemacs-nox	=	CSWemacs-common
RUNTIME_DEP_PKGS_CSWemacs-nox	+=	CSWemacs-bin-common
PKGFILES_CSWemacs-nox			=	/opt/csw/bin/emacs-nox
PKGFILES_CSWemacs-nox			+=	/opt/csw/bin/emacs-$(VERSION)-nox

include gar/category.mk

post-install-modulated:
	@echo "executing $@"
	mv -f $(DESTDIR)$(bindir)/emacs $(DESTDIR)$(bindir)/emacs-$(FEATURES)
	mv -f $(DESTDIR)$(bindir)/emacs-$(VERSION) $(DESTDIR)$(bindir)/emacs-$(VERSION)-$(FEATURES)
	$(MAKECOOKIE)

# this is private and not available publicly
mydependencies:
	$(HOME)/bin/ocswdeplist --package $(NAME)
