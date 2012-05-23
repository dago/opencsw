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

CONFIGURE_ARGS	= $(DIRPATHS)

# this is necessary because GNU id options dialect is is used; BTW, I
# think that adding this systematically at the beginning of the PATH
# helps in packaging projects issued from the Linux steam.
INSTALL_ARGS		+=	\
						PATH="/opt/csw/gnu:$$PATH"

GARCOMPILER			=	GNU

BUILD_DEP_PKGS		=	\
						CSWcoreutils \
						CSWglib2devel \
						CSWlibatk-dev \
						CSWlibbz2-dev \
						CSWlibcairo-dev \
						CSWlibdatrie-dev \
						CSWlibdbus-dev \
						CSWlibdbus-glib-dev \
						CSWlibexpat-dev \
						CSWlibfreetype-dev \
						CSWlibgconf-dev \
						CSWlibgdk-pixbuf-dev \
						CSWlibgif-dev \
						CSWlibglib2-dev \
						CSWlibgtk2-dev \
						CSWlibiconv-dev \
						CSWlibjbig-dev \
						CSWlibjpeg-dev \
						CSWlibm17n-dev \
						CSWlibotf-dev \
						CSWlibpixman-dev \
						CSWlibpng-dev \
						CSWlibpthreadstubs \
						CSWlibrsvg-dev \
						CSWlibthai-dev \
						CSWlibtiff-dev \
						CSWlibx11devel \
						CSWlibxaudevel \
						CSWlibxcbdevel \
						CSWlibxdmcpdevel \
						CSWlibxft2devel \
						CSWlibxml2-dev \
						CSWlibxpmdevel \
						CSWlibz-dev \
						CSWpangodevel \
						CSWpkgconfig \
						CSWsunx11devel

PACKAGING_PLATFORMS	=	\
						solaris10-sparc \
						solaris10-i386

PATCHFILES			+=	0001-activate-Xft-for-configure.patch

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
RUNTIME_DEP_PKGS_CSWemacsel	=	\
								CSWemacscommon
PKGFILES_CSWemacsel			=	\
								/opt/csw/share/emacs/$(VERSION)/.*[.]el[.]gz
ARCHALL_CSWemacsel			=	1

PACKAGES							+=	CSWemacsbincommon
SPKG_DESC_CSWemacsbincommon			=	$(DESCRIPTION) - based on the Athena toolkit
CATALOGNAME_CSWemacsbincommon		=	emacs_bin_common
RUNTIME_DEP_PKGS_CSWemacsbincommon	=	\
										CSWemacscommon
PKGFILES_CSWemacsbincommon			=	\
										/opt/csw/bin/b2m \
										/opt/csw/bin/ctags \
										/opt/csw/bin/ebrowse \
										/opt/csw/bin/emacsclient \
										/opt/csw/bin/etags \
										/opt/csw/libexec/emacs/$(VERSION)/[^/]*solaris[^/]*/digest-doc \
										/opt/csw/libexec/emacs/$(VERSION)/[^/]*solaris[^/]*/fakemail \
										/opt/csw/libexec/emacs/$(VERSION)/[^/]*solaris[^/]*/hexl \
										/opt/csw/libexec/emacs/$(VERSION)/[^/]*solaris[^/]*/movemail \
										/opt/csw/libexec/emacs/$(VERSION)/[^/]*solaris[^/]*/profile \
										/opt/csw/libexec/emacs/$(VERSION)/[^/]*solaris[^/]*/sorted-doc \
										/opt/csw/libexec/emacs/$(VERSION)/[^/]*solaris[^/]*/update-game-score

PACKAGES					+=	CSWemacsgtk
SPKG_DESC_CSWemacsgtk		=	$(DESCRIPTION) - based on the GTK toolkit
CATALOGNAME_CSWemacsgtk		=	emacs_gtk
RUNTIME_DEP_PKGS_CSWemacsgtk=	\
								CSWemacscommon \
								CSWemacsbincommon
PKGFILES_CSWemacsgtk		=	\
								/opt/csw/bin/emacs \
								/opt/csw/bin/emacs-$(VERSION)

# PACKAGES					+=	CSWemacs
# SPKG_DESC_CSWemacs			=	$(DESCRIPTION) - based on the Athena toolkit
# CATALOGNAME_CSWemacs		=	emacs
# RUNTIME_DEP_PKGS_CSWemacs	=	\
# 								CSWemacscommon

# PACKAGES					+=	CSWemacsnox
# SPKG_DESC_CSWemacsnox		=	$(DESCRIPTION) - without any XWindows dependencies
# CATALOGNAME_CSWemacsnox		=	emacs_nox
# RUNTIME_DEP_PKGS_CSWemacsnox=	\
# 								CSWemacscommon

include gar/category.mk

# this is private and not available publicly
mydependencies:
	$(HOME)/bin/ocswdeplist --package $(NAME)
