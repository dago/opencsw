# $Id$

NAME		=	emacs
VERSION		=	24.3
GARTYPE		=	v2

DESCRIPTION = The GNU Emacs editor
define BLURB
  Emacs is the extensible, customizable, self-documenting real-time
  display editor.
endef

MASTER_SITES	=	$(GNU_MIRROR)
DISTFILES		=	$(DISTNAME).tar.xz
DISTFILES		+=	CSWemacs-common.preinstall

# this is necessary because GNU id options dialect is is used; BTW, I
# think that adding this systematically at the beginning of the PATH
# helps in packaging projects issued from the Linux steam.
INSTALL_ARGS		+=	PATH="/opt/csw/gnu:$$PATH"

GARCOMPILER			=	GNU
#GCC4_VERSION		=	4.7

BUILD_DEP_PKGS		=	CSWcoreutils
BUILD_DEP_PKGS		+=	CSWfconfig-dev
BUILD_DEP_PKGS		+=	CSWglib2devel
BUILD_DEP_PKGS		+=	CSWimagemagick-dev
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
BUILD_DEP_PKGS		+=	CSWlibgnutls-dev
BUILD_DEP_PKGS		+=	CSWlibgtk2-dev
BUILD_DEP_PKGS		+=	CSWlibiconv-dev
BUILD_DEP_PKGS		+=	CSWlibjbig-dev
BUILD_DEP_PKGS		+=	CSWlibjpeg-dev
BUILD_DEP_PKGS		+=	CSWlibm17n-dev
BUILD_DEP_PKGS		+=	CSWlibncurses-dev
BUILD_DEP_PKGS		+=	CSWlibotf-dev
BUILD_DEP_PKGS		+=	CSWlibpixman-dev
BUILD_DEP_PKGS		+=	CSWlibpcre-dev
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
BUILD_DEP_PKGS		+=	CSWlibxpm-dev
BUILD_DEP_PKGS		+=	CSWlibxpmdevel
BUILD_DEP_PKGS		+=	CSWlibz-dev
BUILD_DEP_PKGS		+=	CSWpangodevel
BUILD_DEP_PKGS		+=	CSWpkgconfig
BUILD_DEP_PKGS		+=	CSWsunx11devel

LINKER_MAPS			=
LINKER_DIRECT		=
LINKER_IGNORE		=

PACKAGING_PLATFORMS	=	solaris10-sparc
PACKAGING_PLATFORMS	+=	solaris10-i386

PATCHFILES			+=	0001-activate-Xft-for-configure.patch
PATCHFILES			+=	0002-Filter-ImageMagik-OpenMP-compiler-flag.patch

EXTRA_MODULATORS			=	FEATURES
MODULATIONS_FEATURES		=	athena
MODULATIONS_FEATURES		+=	gtk
MODULATIONS_FEATURES		+=	nox

EXTRA_CONFIGURE_ARGS_athena	=	--with-x-toolkit=athena
EXTRA_CONFIGURE_ARGS_athena	+=	--without-dbus
EXTRA_CONFIGURE_ARGS_athena	+=	--without-gconf

EXTRA_CONFIGURE_ARGS_gtk	=	--with-x-toolkit=gtk2

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
CONFIGURE_ARGS	+= --without-compress-info
CONFIGURE_ARGS	+= $(EXTRA_CONFIGURE_ARGS_$(FEATURES))

# this is part of texinfo package:
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/share/info/info.info

MERGE_SCRIPTS_isa-default-features-athena	=	copy-all

MERGE_DIRS_isa-default-features-gtk			=	$(bindir)
MERGE_SCRIPTS_isa-default-features-gtk		=	copy-only

MERGE_DIRS_isa-default-features-nox			=	$(bindir)
MERGE_SCRIPTS_isa-default-features-nox		=	copy-only

ALTERNATIVES_CSWemacs-athena		=	athena
ALTERNATIVES_CSWemacs-gtk			=	gtk
ALTERNATIVES_CSWemacs-nox			=	nox
ALTERNATIVES_CSWemacs-bin-common	=	ctags

ALTERNATIVE_athena			=	$(bindir)/emacs emacs $(bindir)/emacs-athena 200
ALTERNATIVE_gtk				=	$(bindir)/emacs emacs $(bindir)/emacs-gtk 100
ALTERNATIVE_nox				=	$(bindir)/emacs emacs $(bindir)/emacs-nox 300
ALTERNATIVE_ctags			=	$(bindir)/ctags ctags $(bindir)/ctags.emacs 100

POSTMSG_EMACS			=	emacsalt.postmsg
POSTMSG_EMACS_ATHENA	=	$(docdir)/$(CATALOGNAME_CSWemacs-athena)/CSWemacs-athena.postmsg
DISTFILES				+=	$(notdir $(POSTMSG_EMACS_ATHENA))
POSTMSG_EMACS_GTK		=	$(docdir)/$(CATALOGNAME_CSWemacs-gtk)/CSWemacs-gtk.postmsg
DISTFILES				+=	$(notdir $(POSTMSG_EMACS_GTK))
POSTMSG_EMACS_NOX		=	$(docdir)/$(CATALOGNAME_CSWemacs-nox)/CSWemacs-nox.postmsg
DISTFILES				+=	$(notdir $(POSTMSG_EMACS_NOX))
POSTMSG_CTAGS			=	$(docdir)/$(CATALOGNAME_CSWemacs-bin-common)/CSWemacs-bin-common.postmsg
DISTFILES				+=	$(notdir $(POSTMSG_CTAGS))

PACKAGES							=	CSWemacs-common
SPKG_DESC_CSWemacs-common			=	$(DESCRIPTION) - architecture neutral common components
CATALOGNAME_CSWemacs-common			=	emacs_common
CHECKPKG_OVERRIDES_CSWemacs-common	+=	missing-dependency|CSWemacscommon
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/share|root/opt/csw/share/info/dbus
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/share|root/opt/csw/share/info/elisp-3
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/info/emacs-3
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/share|root/opt/csw/share/info/emacs-6
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/share|root/opt/csw/share/info/eintr-2
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/share|root/opt/csw/share/info/efaq
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/share|root/opt/csw/share/emacs/$(VERSION)/etc/compilation.txt
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/share|root/opt/csw/share/emacs/$(VERSION)/etc/PROBLEMS
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/share|root/opt/csw/share/emacs/$(VERSION)/etc/DOC-$(VERSION).1
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/share|root/opt/csw/share/emacs/$(VERSION)/lisp/hfy-cmap.elc
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/share|root/opt/csw/share/emacs/$(VERSION)/lisp/printing.elc
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/share|root/opt/csw/share/emacs/$(VERSION)/lisp/woman.elc
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/share|root/opt/csw/share/emacs/$(VERSION)/lisp/cedet/semantic/bovine/scm.elc
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/share|root/opt/csw/share/emacs/$(VERSION)/lisp/international/mule-cmds.elc
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/share|root/opt/csw/share/emacs/$(VERSION)/lisp/international/eucjp-ms.el
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/share|root/opt/csw/share/emacs/$(VERSION)/lisp/term/x-win.elc
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/share|root/opt/csw/share/emacs/$(VERSION)/lisp/textmodes/ispell.elc
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/share|root/opt/csw/share/emacs/$(VERSION)/lisp/mh-e/mh-xface.elc
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/share|root/opt/csw/share/emacs/$(VERSION)/lisp/mh-e/mh-alias.elc
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/share|root/opt/csw/share/emacs/$(VERSION)/lisp/gnus/gnus-art.elc
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/info/elisp-3
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/info/elisp-9
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/info/elisp-10
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/info/emacs-4
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/info/eintr-3
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/info/emacs-5
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/info/eintr-1
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/info/emacs-2
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/info/woman
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/info/elisp-5
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/info/eshell
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/info/emacs-6
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/info/mh-e-1
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/info/eintr-2
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/info/reftex
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/info/tramp
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/info/gnus-3
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/info/gnus-4
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/info/idlwave
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/info/efaq
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/emacs/$(VERSION)/etc/MH-E-NEWS
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/emacs/$(VERSION)/etc/NEWS.20
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/emacs/$(VERSION)/etc/emacs.bash
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/emacs/$(VERSION)/etc/MACHINES
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/emacs/$(VERSION)/etc/PROBLEMS
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/emacs/$(VERSION)/etc/NEWS.19
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/emacs/$(VERSION)/etc/DOC-$(VERSION).1
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/emacs/$(VERSION)/lisp/man.elc
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/emacs/$(VERSION)/lisp/paths.el
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/emacs/$(VERSION)/lisp/ffap.elc
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/emacs/$(VERSION)/lisp/ps-bdf.elc
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/emacs/$(VERSION)/lisp/find-file.elc
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/emacs/$(VERSION)/lisp/loaddefs.el
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/emacs/$(VERSION)/lisp/ldefs-boot.el
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/emacs/$(VERSION)/lisp/woman.elc
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/emacs/$(VERSION)/lisp/obsolete/complete.elc
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/emacs/$(VERSION)/lisp/progmodes/idlwave.elc
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/emacs/$(VERSION)/lisp/progmodes/idlw-help.elc
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/emacs/$(VERSION)/lisp/progmodes/m4-mode.elc
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/emacs/$(VERSION)/lisp/progmodes/ada-mode.elc
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/emacs/$(VERSION)/lisp/play/dunnet.elc
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/emacs/$(VERSION)/lisp/textmodes/ispell.elc
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/emacs/$(VERSION)/lisp/mh-e/mh-e.elc
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/emacs/$(VERSION)/lisp/gnus/gnus-setup.elc
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/emacs/$(VERSION)/lisp/gnus/gnus-art.elc
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/emacs/$(VERSION)/lisp/gnus/mailcap.elc
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/emacs/$(VERSION)/lisp/net/tramp.elc
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/emacs/$(VERSION)/lisp/net/tramp-loaddefs.el
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/emacs/$(VERSION)/lisp/net/tramp-sh.elc
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/emacs.1
# as we use alternatives, we need to obsolete emacs_chooser;
# emacs_common, being the root dependence of all emacs related
# packages, seems the best place to do it.
OBSOLETED_BY_CSWemacs-common		=	CSWemacschooser
OBSOLETED_BY_CSWemacs-common		+=	CSWemacscommon
CATALOGNAME_CSWemacscommon			=	emacscommon_stub
# this is to be done only for this sub-package but I don't know how to
# specialize the variable:
EXTRA_TEXINFO						=	$(infodir)/.*
ARCHALL_CSWemacs-common				=	1
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/info/gnus.info
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/info/tramp.info
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/info/eintr.info
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/info/reftex.info
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/info/emacs.info
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/info/efaq.info
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/info/eshell.info
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/info/elisp.info
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/info/woman.info
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/info/mh-e.info
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/info/idlwave.info
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/emacs/24.3/lisp/info.elc
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/emacs/24.3/lisp/gnus/nnspool.elc
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/emacs/24.3/etc/NEWS
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/share|root/opt/csw/share/info/eintr.info
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/share|root/opt/csw/share/info/dbus.info
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/share|root/opt/csw/share/info/emacs.info
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/share|root/opt/csw/share/info/efaq.info
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/share|root/opt/csw/share/info/elisp.info
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/share|root/opt/csw/share/emacs/24.3/lisp/ldefs-boot.el
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/share|root/opt/csw/share/emacs/24.3/lisp/loaddefs.el
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/share|root/opt/csw/share/emacs/24.3/lisp/org/org-version.el
CHECKPKG_OVERRIDES_CSWemacs-common	+=	file-with-bad-content|/usr/share|root/opt/csw/share/emacs/24.3/lisp/org/org-odt.elc

PACKAGES						+=	CSWemacs-el
SPKG_DESC_CSWemacs-el			=	$(DESCRIPTION) - elisp sources
CATALOGNAME_CSWemacs-el			=	emacs_el
OBSOLETED_BY_CSWemacs-el		=	CSWemacsel
CATALOGNAME_CSWemacsel			=	emacsel_stub
RUNTIME_DEP_PKGS_CSWemacs-el	=	CSWemacs-common
CHECKPKG_OVERRIDES_CSWemacs-el	+=	surplus-dependency|CSWemacs-common
PKGFILES_CSWemacs-el			=	/opt/csw/share/emacs/$(VERSION)/.*[.]el[.]gz
ARCHALL_CSWemacs-el				=	1

PACKAGES								+=	CSWemacs-bin-common
SPKG_DESC_CSWemacs-bin-common			=	$(DESCRIPTION) - common binaries
CATALOGNAME_CSWemacs-bin-common			=	emacs_bin_common
OBSOLETED_BY_CSWemacs-bin-common		=	CSWemacsbincommon
CATALOGNAME_CSWemacsbincommon			=	emacsbincommon_stub
RUNTIME_DEP_PKGS_CSWemacs-bin-common	=	CSWemacs-common
RUNTIME_DEP_PKGS_CSWemacs-common		+=	CSWperl
CHECKPKG_OVERRIDES_CSWemacs-bin-common	+=	surplus-dependency|CSWemacs-common
CHECKPKG_OVERRIDES_CSWemacs-bin-common	+=	no-direct-binding|/opt/csw/libexec/emacs/24.3/sparc-sun-solaris2.10/movemail|is|not|directly|bound|to|soname|libmail.so.1
PKGFILES_CSWemacs-bin-common			=	/opt/csw/bin/b2m
PKGFILES_CSWemacs-bin-common			+=	/opt/csw/bin/ctags.emacs
PKGFILES_CSWemacs-bin-common			+=	/opt/csw/bin/ebrowse
PKGFILES_CSWemacs-bin-common			+=	/opt/csw/bin/emacsclient
PKGFILES_CSWemacs-bin-common			+=	/opt/csw/bin/etags
PKGFILES_CSWemacs-bin-common			+=	/opt/csw/libexec/emacs/$(VERSION)/.*

PACKAGES					+=	CSWemacs
SPKG_DESC_CSWemacs			=	$(DESCRIPTION) - metapackage for generic dependencies
CATALOGNAME_CSWemacs		=	emacs
PKGFILES_CSWemacs			=	NOFILES
RUNTIME_DEP_PKGS_CSWemacs	=	CSWemacs-athena
CHECKPKG_OVERRIDES_CSWemacs	+=	surplus-dependency|CSWemacs-athena
ARCHALL_CSWemacs			=	1

PACKAGES							+=	CSWemacs-athena
SPKG_DESC_CSWemacs-athena			=	$(DESCRIPTION) - based on the Athena toolkit
CATALOGNAME_CSWemacs-athena			=	emacs_athena
RUNTIME_DEP_PKGS_CSWemacs-athena	=	CSWemacs-bin-common
RUNTIME_DEP_PKGS_CSWemacs-athena	+=	CSWemacs-common
RUNTIME_DEP_PKGS_CSWemacs-athena	+=	CSWfconfig
RUNTIME_DEP_PKGS_CSWemacs-athena	+=	CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWemacs-athena	+=	CSWlibcairo2
RUNTIME_DEP_PKGS_CSWemacs-athena	+=	CSWlibcroco
RUNTIME_DEP_PKGS_CSWemacs-athena	+=	CSWlibdatrie1
RUNTIME_DEP_PKGS_CSWemacs-athena	+=	CSWlibexpat1
RUNTIME_DEP_PKGS_CSWemacs-athena	+=	CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWemacs-athena	+=	CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWemacs-athena	+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWemacs-athena	+=	CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWemacs-athena	+=	CSWlibgif4
RUNTIME_DEP_PKGS_CSWemacs-athena	+=	CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWemacs-athena	+=	CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWemacs-athena	+=	CSWlibgnutls26
RUNTIME_DEP_PKGS_CSWemacs-athena	+=	CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWemacs-athena	+=	CSWlibiconv2
RUNTIME_DEP_PKGS_CSWemacs-athena	+=	CSWlibintl8
RUNTIME_DEP_PKGS_CSWemacs-athena	+=	CSWlibjbig2
RUNTIME_DEP_PKGS_CSWemacs-athena	+=	CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWemacs-athena	+=	CSWlibm17n-utils
RUNTIME_DEP_PKGS_CSWemacs-athena	+=	CSWlibm17n0
RUNTIME_DEP_PKGS_CSWemacs-athena	+=	CSWlibmagickcore5
RUNTIME_DEP_PKGS_CSWemacs-athena	+=	CSWlibmagickwand5
RUNTIME_DEP_PKGS_CSWemacs-athena	+=	CSWlibncurses5
RUNTIME_DEP_PKGS_CSWemacs-athena	+=	CSWlibotf-utils
RUNTIME_DEP_PKGS_CSWemacs-athena	+=	CSWlibotf0
RUNTIME_DEP_PKGS_CSWemacs-athena	+=	CSWlibpixman1-0
RUNTIME_DEP_PKGS_CSWemacs-athena	+=	CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWemacs-athena	+=	CSWlibrsvg2-2
RUNTIME_DEP_PKGS_CSWemacs-athena	+=	CSWlibthai0
RUNTIME_DEP_PKGS_CSWemacs-athena	+=	CSWlibtiff3
RUNTIME_DEP_PKGS_CSWemacs-athena	+=	CSWlibxft2
RUNTIME_DEP_PKGS_CSWemacs-athena	+=	CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWemacs-athena	+=	CSWlibxpm4
RUNTIME_DEP_PKGS_CSWemacs-athena	+=	CSWlibxrender
RUNTIME_DEP_PKGS_CSWemacs-athena	+=	CSWlibz1
RUNTIME_DEP_PKGS_CSWemacs-athena	+=	CSWpango
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	file-with-bad-content|/usr/local|root/opt/csw/bin/emacs-athena
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	file-with-bad-content|/usr/share|root/opt/csw/bin/emacs-athena
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	file-with-bad-content|/usr/local|root/opt/csw/bin/emacs-$(VERSION)-athena
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	file-with-bad-content|/usr/share|root/opt/csw/bin/emacs-$(VERSION)-athena
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	missing-dependency|CSWlibm17n-utils
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	missing-dependency|CSWlibotf-utils
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	missing-dependency|CSWlibfontconfig1
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	surplus-dependency|CSWlibcroco
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	surplus-dependency|CSWemacs-common
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	surplus-dependency|CSWlibiconv2
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	surplus-dependency|CSWlibotf0
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	surplus-dependency|CSWlibdatrie1
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	surplus-dependency|CSWlibthai0
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	surplus-dependency|CSWlibgcc-s1
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	surplus-dependency|CSWlibm17n0
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	surplus-dependency|CSWlibjbig2
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	surplus-dependency|CSWpango
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	surplus-dependency|CSWemacs-bin-common
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	surplus-dependency|CSWlibxml2-2
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	surplus-dependency|CSWlibexpat1
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	surplus-dependency|CSWlibpixman1-0
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	surplus-dependency|CSWfconfig
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	soname-unused|libz.so.1|is|needed|by|/opt/csw/bin/emacs-24.3-athena|but|never|used
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	soname-unused|libXext.so.0|is|needed|by|/opt/csw/bin/emacs-24.3-athena|but|never|used
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	soname-unused|libcairo.so.2|is|needed|by|/opt/csw/bin/emacs-24.3-athena|but|never|used
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	soname-unused|libintl.so.8|is|needed|by|/opt/csw/bin/emacs-24.3-athena|but|never|used
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	soname-unused|libbz2.so.1.0|is|needed|by|/opt/csw/bin/emacs-24.3-athena|but|never|used
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-athena|is|not|directly|bound|to|soname|libXft.so.2
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-athena|is|not|directly|bound|to|soname|libXt.so.4
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-athena|is|not|directly|bound|to|soname|libm17n-flt.so.0
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-athena|is|not|directly|bound|to|soname|libgnutls.so.26
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-athena|is|not|directly|bound|to|soname|libglib-2.0.so.0
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-athena|is|not|directly|bound|to|soname|libjpeg.so.7
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-athena|is|not|directly|bound|to|soname|libotf.so.0
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-athena|is|not|directly|bound|to|soname|libXpm.so.4
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-athena|is|not|directly|bound|to|soname|libMagickCore.so.5
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-athena|is|not|directly|bound|to|soname|librsvg-2.so.2
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-athena|is|not|directly|bound|to|soname|libgio-2.0.so.0
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-athena|is|not|directly|bound|to|soname|libxml2.so.2
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-athena|is|not|directly|bound|to|soname|libXaw.so.5
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-athena|is|not|directly|bound|to|soname|libX11.so.4
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-athena|is|not|directly|bound|to|soname|libSM.so.6
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-athena|is|not|directly|bound|to|soname|libfontconfig.so.1
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-athena|is|not|directly|bound|to|soname|libgobject-2.0.so.0
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-athena|is|not|directly|bound|to|soname|libXmu.so.4
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-athena|is|not|directly|bound|to|soname|libgdk_pixbuf-2.0.so.0
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-athena|is|not|directly|bound|to|soname|libncurses.so.5
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-athena|is|not|directly|bound|to|soname|libXrender.so.1
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-athena|is|not|directly|bound|to|soname|libpng15.so.15
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-athena|is|not|directly|bound|to|soname|libICE.so.6
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-athena|is|not|directly|bound|to|soname|libMagickWand.so.5
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-athena|is|not|directly|bound|to|soname|libm17n-core.so.0
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-athena|is|not|directly|bound|to|soname|libMagickWand
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-athena|is|not|directly|bound|to|soname|libMagickWand.so.5
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-athena|is|not|directly|bound|to|soname|libm17n-core.so.0
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-athena|is|not|directly|bound|to|soname|libgif.so.4
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-athena|is|not|directly|bound|to|soname|libfreetype.so.6
CHECKPKG_OVERRIDES_CSWemacs-athena	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-athena|is|not|directly|bound|to|soname|libtiff.so.3
PKGFILES_CSWemacs-athena			=	/opt/csw/bin/emacs-athena
PKGFILES_CSWemacs-athena			+=	/opt/csw/bin/emacs-$(VERSION)-athena

PACKAGES						+=	CSWemacs-gtk
SPKG_DESC_CSWemacs-gtk			=	$(DESCRIPTION) - based on the GTK toolkit
CATALOGNAME_CSWemacs-gtk		=	emacs_gtk
OBSOLETED_BY_CSWemacs-gtk		=	CSWemacsgtk
CATALOGNAME_CSWemacsgtk			=	emacs_gtk_stub
RUNTIME_DEP_PKGS_CSWemacs-gtk	=	CSWemacs-bin-common
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWemacs-common
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWfconfig
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibcairo2
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibcroco
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibdatrie1
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibdbus1-3
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibexpat1
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibgconf2-4
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibgif4
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibgnutls26
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibiconv2
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibintl8
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibjbig2
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibm17n-utils
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibm17n0
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibmagickcore5
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibmagickwand5
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibncurses5
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibotf-utils
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibotf0
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibpixman1-0
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibrsvg2-2
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibthai0
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibtiff3
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibxft2
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibxpm4
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibxrender
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWlibz1
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWorbit2
RUNTIME_DEP_PKGS_CSWemacs-gtk	+=	CSWpango
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	file-with-bad-content|/usr/local|root/opt/csw/bin/emacs-gtk
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	file-with-bad-content|/usr/share|root/opt/csw/bin/emacs-gtk
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	file-with-bad-content|/usr/local|root/opt/csw/bin/emacs-$(VERSION)-gtk
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	file-with-bad-content|/usr/share|root/opt/csw/bin/emacs-$(VERSION)-gtk
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	surplus-dependency|CSWlibcroco
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	surplus-dependency|CSWemacs-common
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	surplus-dependency|CSWlibiconv2
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	surplus-dependency|CSWlibthai0
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	surplus-dependency|CSWlibdatrie1
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	surplus-dependency|CSWlibotf0
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	surplus-dependency|CSWlibgcc-s1
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	surplus-dependency|CSWlibm17n0
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	surplus-dependency|CSWlibjbig2
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	surplus-dependency|CSWlibxml2-2
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	surplus-dependency|CSWemacs-bin-common
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	surplus-dependency|CSWlibexpat1
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	surplus-dependency|CSWlibpixman1-0
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	surplus-dependency|CSWfconfig
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	surplus-dependency|CSWorbit2
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	soname-unused|libz.so.1|is|needed|by|/opt/csw/bin/emacs-24.3-gtk|but|never|used
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	soname-unused|libatk-1.0.so.0|is|needed|by|/opt/csw/bin/emacs-24.3-gtk|but|never|used
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	soname-unused|libpangoft2-1.0.so.0|is|needed|by|/opt/csw/bin/emacs-24.3-gtk|but|never|used
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	soname-unused|libpangocairo-1.0.so.0|is|needed|by|/opt/csw/bin/emacs-24.3-gtk|but|never|used
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	soname-unused|libcairo.so.2|is|needed|by|/opt/csw/bin/emacs-24.3-gtk|but|never|used
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	soname-unused|libpango-1.0.so.0|is|needed|by|/opt/csw/bin/emacs-24.3-gtk|but|never|used
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	soname-unused|libgmodule-2.0.so.0|is|needed|by|/opt/csw/bin/emacs-24.3-gtk|but|never|used
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	soname-unused|libintl.so.8|is|needed|by|/opt/csw/bin/emacs-24.3-gtk|but|never|used
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	soname-unused|libbz2.so.1.0|is|needed|by|/opt/csw/bin/emacs-24.3-gtk|but|never|used
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-gtk|is|not|directly|bound|to|soname|libgio-2.0.so.0
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-gtk|is|not|directly|bound|to|soname|libm17n-flt.so.0
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-gtk|is|not|directly|bound|to|soname|libgnutls.so.26
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-gtk|is|not|directly|bound|to|soname|libglib-2.0.so.0
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-gtk|is|not|directly|bound|to|soname|libjpeg.so.7
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-gtk|is|not|directly|bound|to|soname|libgtk-x11-2.0.so.0
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-gtk|is|not|directly|bound|to|soname|libXpm.so.4
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-gtk|is|not|directly|bound|to|soname|libMagickCore.so.5
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-gtk|is|not|directly|bound|to|soname|librsvg-2.so.2
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-gtk|is|not|directly|bound|to|soname|libXft.so.2
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-gtk|is|not|directly|bound|to|soname|libgdk-x11-2.0.so.0
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-gtk|is|not|directly|bound|to|soname|libxml2.so.2
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-gtk|is|not|directly|bound|to|soname|libgconf-2.so.4
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-gtk|is|not|directly|bound|to|soname|libotf.so.0
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-gtk|is|not|directly|bound|to|soname|libX11.so.4
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-gtk|is|not|directly|bound|to|soname|libSM.so.6
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-gtk|is|not|directly|bound|to|soname|libfontconfig.so.1
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-gtk|is|not|directly|bound|to|soname|libthread.so.1
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-gtk|is|not|directly|bound|to|soname|libgobject-2.0.so.0
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-gtk|is|not|directly|bound|to|soname|libdbus-1.so.3
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-gtk|is|not|directly|bound|to|soname|libgdk_pixbuf-2.0.so.0
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-gtk|is|not|directly|bound|to|soname|libncurses.so.5
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-gtk|is|not|directly|bound|to|soname|libXrender.so.1
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-gtk|is|not|directly|bound|to|soname|libpng15.so.15
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-gtk|is|not|directly|bound|to|soname|libICE.so.6
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-gtk|is|not|directly|bound|to|soname|libMagickWand.so.5
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-gtk|is|not|directly|bound|to|soname|libm17n-core.so.0
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-gtk|is|not|directly|bound|to|soname|libgif.so.4
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-gtk|is|not|directly|bound|to|soname|libfreetype.so.6
CHECKPKG_OVERRIDES_CSWemacs-gtk	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-gtk|is|not|directly|bound|to|soname|libtiff.so.3
PKGFILES_CSWemacs-gtk			=	/opt/csw/bin/emacs-gtk
PKGFILES_CSWemacs-gtk			+=	/opt/csw/bin/emacs-$(VERSION)-gtk

PACKAGES						+=	CSWemacs-nox
SPKG_DESC_CSWemacs-nox			=	$(DESCRIPTION) - without any XWindows dependencies
CATALOGNAME_CSWemacsnox			=	emacs_nox
OBSOLETED_BY_CSWemacs-nox		=	CSWemacsnox
CATALOGNAME_CSWemacsnox			=	emacs_nox_stub
RUNTIME_DEP_PKGS_CSWemacs-nox	=	CSWemacs-bin-common
RUNTIME_DEP_PKGS_CSWemacs-nox	+=	CSWemacs-common
RUNTIME_DEP_PKGS_CSWemacs-nox	+=	CSWlibgnutls26
RUNTIME_DEP_PKGS_CSWemacs-nox	+=	CSWlibncurses5
RUNTIME_DEP_PKGS_CSWemacs-nox	+=	CSWlibxml2-2
CHECKPKG_OVERRIDES_CSWemacs-nox	+=	file-with-bad-content|/usr/local|root/opt/csw/bin/emacs-$(VERSION)-nox
CHECKPKG_OVERRIDES_CSWemacs-nox	+=	file-with-bad-content|/usr/share|root/opt/csw/bin/emacs-$(VERSION)-nox
CHECKPKG_OVERRIDES_CSWemacs-nox	+=	file-with-bad-content|/usr/local|root/opt/csw/bin/emacs-nox
CHECKPKG_OVERRIDES_CSWemacs-nox	+=	file-with-bad-content|/usr/share|root/opt/csw/bin/emacs-nox
CHECKPKG_OVERRIDES_CSWemacs-nox	+=	surplus-dependency|CSWemacs-bin-common
CHECKPKG_OVERRIDES_CSWemacs-nox	+=	surplus-dependency|CSWemacs-common
CHECKPKG_OVERRIDES_CSWemacs-nox	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-nox|is|not|directly|bound|to|soname|libncurses.so.5
CHECKPKG_OVERRIDES_CSWemacs-nox	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-nox|is|not|directly|bound|to|soname|libxml2.so.2
CHECKPKG_OVERRIDES_CSWemacs-nox	+=	no-direct-binding|/opt/csw/bin/emacs-24.3-nox|is|not|directly|bound|to|soname|libgnutls.so.26
PKGFILES_CSWemacs-nox			=	/opt/csw/bin/emacs-nox
PKGFILES_CSWemacs-nox			+=	/opt/csw/bin/emacs-$(VERSION)-nox

include gar/category.mk

pre-fetch:
	@echo "executing $@"
	cp $(FILEDIR)/$(POSTMSG_EMACS) $(FILEDIR)/$(notdir $(POSTMSG_EMACS_ATHENA))
	cp $(FILEDIR)/$(POSTMSG_EMACS) $(FILEDIR)/$(notdir $(POSTMSG_EMACS_GTK))
	cp $(FILEDIR)/$(POSTMSG_EMACS) $(FILEDIR)/$(notdir $(POSTMSG_EMACS_NOX))
	$(MAKECOOKIE)

post-merge:
	@echo "executing $@"
	ginstall -d $(PKGROOT)$(dir $(POSTMSG_EMACS_ATHENA))
	ginstall $(WORKDIR)/$(notdir $(POSTMSG_EMACS_ATHENA)) $(PKGROOT)$(POSTMSG_EMACS_ATHENA)
	ginstall -d $(PKGROOT)$(dir $(POSTMSG_EMACS_GTK))
	ginstall $(WORKDIR)/$(notdir $(POSTMSG_EMACS_GTK)) $(PKGROOT)$(POSTMSG_EMACS_GTK)
	ginstall -d $(PKGROOT)$(dir $(POSTMSG_EMACS_NOX))
	ginstall $(WORKDIR)/$(notdir $(POSTMSG_EMACS_NOX)) $(PKGROOT)$(POSTMSG_EMACS_NOX)
	ginstall -d $(PKGROOT)$(dir $(POSTMSG_CTAGS))
	ginstall $(WORKDIR)/$(notdir $(POSTMSG_CTAGS)) $(PKGROOT)$(POSTMSG_CTAGS)
	$(MAKECOOKIE)

post-install-modulated:
	@echo "executing $@"
	rm -f $(DESTDIR)$(bindir)/emacs
	mv -f $(DESTDIR)$(bindir)/emacs-$(VERSION) $(DESTDIR)$(bindir)/emacs-$(VERSION)-$(FEATURES)
	cd $(DESTDIR)$(bindir) && ln -s emacs-$(VERSION)-$(FEATURES) emacs-$(FEATURES)
	mv -f $(DESTDIR)$(bindir)/ctags $(DESTDIR)$(bindir)/ctags.emacs
	$(MAKECOOKIE)

# this is private and not available publicly
mydependencies:
	$(HOME)/bin/ocswdeplist --package $(NAME)
