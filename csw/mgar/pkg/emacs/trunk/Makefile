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
BUILD_DEP_PKGS		+=	CSWglib2devel \
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
ALTERNATIVES_CSWemacsgtk	=	gtk
ALTERNATIVES_CSWemacsnox	=	nox

ALTERNATIVE_athena			=	$(bindir)/emacs emacs $(bindir)/emacs-athena 200
ALTERNATIVE_gtk				=	$(bindir)/emacs emacs $(bindir)/emacs-gtk 100
ALTERNATIVE_nox				=	$(bindir)/emacs emacs $(bindir)/emacs-nox 300

PACKAGES					=	CSWemacscommon
SPKG_DESC_CSWemacscommon	=	$(DESCRIPTION) - architecture neutral common components
CATALOGNAME_CSWemacscommon	=	emacs_common
# as we use alternatives, we need to obsolete emacs_chooser;
# emacs_common, being the root dependence of all emacs related
# packages, seems the best place to do it.
OBSOLETED_BY_CSWemacscommon	=	CSWemacschooser
ARCHALL_CSWemacscommon		=	1

PACKAGES					+=	CSWemacsel
SPKG_DESC_CSWemacsel		=	$(DESCRIPTION) - elisp sources
CATALOGNAME_CSWemacsel		=	emacs_el
RUNTIME_DEP_PKGS_CSWemacsel	=	CSWemacscommon
PKGFILES_CSWemacsel			=	/opt/csw/share/emacs/$(VERSION)/.*[.]el[.]gz
ARCHALL_CSWemacsel			=	1

PACKAGES							+=	CSWemacsbincommon
SPKG_DESC_CSWemacsbincommon			=	$(DESCRIPTION) - common binaries
CATALOGNAME_CSWemacsbincommon		=	emacs_bin_common
RUNTIME_DEP_PKGS_CSWemacsbincommon	=	CSWemacscommon
PKGFILES_CSWemacsbincommon			=	/opt/csw/bin/b2m
PKGFILES_CSWemacsbincommon			+=	/opt/csw/bin/ctags
PKGFILES_CSWemacsbincommon			+=	/opt/csw/bin/ebrowse
PKGFILES_CSWemacsbincommon			+=	/opt/csw/bin/emacsclient
PKGFILES_CSWemacsbincommon			+=	/opt/csw/bin/etags
PKGFILES_CSWemacsbincommon			+=	/opt/csw/libexec/emacs/$(VERSION)/[^/]*solaris[^/]*/digest-doc
PKGFILES_CSWemacsbincommon			+=	/opt/csw/libexec/emacs/$(VERSION)/[^/]*solaris[^/]*/fakemail
PKGFILES_CSWemacsbincommon			+=	/opt/csw/libexec/emacs/$(VERSION)/[^/]*solaris[^/]*/hexl
PKGFILES_CSWemacsbincommon			+=	/opt/csw/libexec/emacs/$(VERSION)/[^/]*solaris[^/]*/movemail
PKGFILES_CSWemacsbincommon			+=	/opt/csw/libexec/emacs/$(VERSION)/[^/]*solaris[^/]*/profile
PKGFILES_CSWemacsbincommon			+=	/opt/csw/libexec/emacs/$(VERSION)/[^/]*solaris[^/]*/sorted-doc
PKGFILES_CSWemacsbincommon			+=	/opt/csw/libexec/emacs/$(VERSION)/[^/]*solaris[^/]*/update-game-score

PACKAGES					+=	CSWemacs
SPKG_DESC_CSWemacs			=	$(DESCRIPTION) - based on the Athena toolkit
CATALOGNAME_CSWemacs		=	emacs
RUNTIME_DEP_PKGS_CSWemacs	=	CSWemacscommon
RUNTIME_DEP_PKGS_CSWemacs	+=	CSWemacsbincommon

PKGFILES_CSWemacs			=	/opt/csw/bin/emacs-athena
PKGFILES_CSWemacs			+=	/opt/csw/bin/emacs-$(VERSION)-athena

PACKAGES					+=	CSWemacsgtk
SPKG_DESC_CSWemacsgtk		=	$(DESCRIPTION) - based on the GTK toolkit
CATALOGNAME_CSWemacsgtk		=	emacs_gtk
RUNTIME_DEP_PKGS_CSWemacsgtk=	CSWemacscommon
RUNTIME_DEP_PKGS_CSWemacsgtk+=	CSWemacsbincommon
PKGFILES_CSWemacsgtk		=	/opt/csw/bin/emacs-gtk
PKGFILES_CSWemacsgtk		+=	/opt/csw/bin/emacs-$(VERSION)-gtk

PACKAGES					+=	CSWemacsnox
SPKG_DESC_CSWemacsnox		=	$(DESCRIPTION) - without any XWindows dependencies
CATALOGNAME_CSWemacsnox		=	emacs_nox
RUNTIME_DEP_PKGS_CSWemacsnox=	CSWemacscommon
RUNTIME_DEP_PKGS_CSWemacsnox+=	CSWemacsbincommon
PKGFILES_CSWemacsnox		=	/opt/csw/bin/emacs-nox
PKGFILES_CSWemacsnox		+=	/opt/csw/bin/emacs-$(VERSION)-nox

include gar/category.mk

post-install-modulated:
	@echo "executing $@"
	mv -f $(DESTDIR)$(bindir)/emacs $(DESTDIR)$(bindir)/emacs-$(FEATURES)
	mv -f $(DESTDIR)$(bindir)/emacs-$(VERSION) $(DESTDIR)$(bindir)/emacs-$(VERSION)-$(FEATURES)
	$(MAKECOOKIE)

# this is private and not available publicly
mydependencies:
	$(HOME)/bin/ocswdeplist --package $(NAME)
