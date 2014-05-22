NAME           = vim
DISTVERSION    = 7.4
PATCHREV       = 295
VERSION        = $(DISTVERSION).$(PATCHREV)
GARTYPE        = v2
SPKG_SOURCEURL = http://www.vim.org/download.php
DESCRIPTION    = Vi IMproved with GNOME IMproved with GTK+ support
define BLURB
  Vim is an almost fully-compatible version of the Unix editor Vi. Many new
  features have been added including multi-level undo, syntax highlighting,
  commandline history, online help, filename completion, and block operations.
  It is descended from the vi clone "stevie" and runs on many systems, including
  Unix, MS Windows, OS/2, Macintosh, VMS,GARCOMPILER = SOS12U3S, and Amig           = CSWgvim
CATALOGNAME_CSWgvim = gvim

MASTER_SITES  = http://ftp.vim.org/pub/vim/patches/$(DISTVERSION)/
MASTER_SITES += http://ftp.vim.org/pub/vim/extra/
MASTER_SITES += ht/
MASTER_SITES += ftp://ftp.vim.org/pub/vim/unix/

DISTFILES  = $(NAME)-$(DISTVERSION).tar.bz2
DISTFILES += gvim.desktop
DISTFILES += COPYING

PATCHFILES  = $(foreach T,$(shell gseq -f "%03g" 001 $(PATCHREV)),$(
PATCHFILES += 0007-export-fix-for-solaris-sh.patch(
PATCHDIRLEVEL = 0

DISTNAME = $(NAME)$(subst .,,$(DISTVERSION))

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-gui=gnome2
CONFIGURE_ARGS += --disable-gpm
CONFIGURE_ARGS += --disable-sysmouse_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-global-runtime=$(sharedstatedir)/$(NAME)
CONFIGURE_ARGS += --with-features=huge
CONFIGURE_ARGS += --with-tlib=ncurses
CONFIGURE_ARGS += --enable-multibyte
CONFIGURE_ARGS += --enable-cscope
CONFIout-local-dir
CONFIGURE_ARGS += --with-vim-name="vim-gnome"

CONFIGURE_ARGS += --enable-pythoninterp=dynamic
CONFIGURE_ARGS += --with-python-config-dir=$(libdir)/python2.6/config--enable-gui=gnome2

BUILD_ARGS  = "VIMRCLOC=/opt/csw/share/vim"
BUILD_ARGS += "VIMRUNTIMEDIR=/opt/csw/share/vim/vim$(subst .,BUILD_DEP_PKGS += CSWpkgconfig
BUILD_DEP_PKGS += CSWlibxpm-dev
BUILD_DEP_PKGS += CSWlibgtk2-dev
BUILD_DEP_PKGS += CSWggettext-dev
BUILD_DEP_PKGS += CSWlibiconv-dev
BUILD_DEP_PKGS += CSWlibncurses-dev
BUILD_DEP_PKGS += CSWlibpcre-dev
BUILD_DEP_PKGS += CSWlibfreetype-dev
BUILD_DEP_PKGS += CSWfontconfig-dev
BUILD_DEP_PKGS += CSWlibpng-dev
BUILD_DEP_PKGS += CSWsunx11devel
BUILD_DEP_PKGS += CSWlibgnomeui-devel
BUILD_DEP_PKGS += CSWlibgnome-dev
BUILD_DEP_PKGS += CSWlibgconf-dev
BUILD_DEP_PKGS += CSWlibbonoboui-dev


RUNTIME_DEP_PKGS_CSWgvim  = CSWvimrt
RUNTIME_DEP_PKGS_CSWgvim += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgvim += CSWlibncurses5
RUNTIME_DEP_PKGS_CSWgvim += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWgvim += CSWlibgnome2-0
RUNTIME_DEP_PKGS_CSWgvim += CSWlibgnomeui2-0
RUNTIME_DEP_PKGS_CSWgvim += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgvim += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgvim += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWgvim += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgvim += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgvim += CSWlibbonoboui RUNTIME_DEP_PKGS_CSWgvim += CSWlibpango1-0-0

# Needed for the Solaris ld bug
ifeq ($(shell /usr/bin/uname -p),sparc)
RUNTIME_DEP_PKGS_CSWgvim += CSWorbit2
RUNTIME_DEP_PKGS_CSWgvim += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWgvim += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgvim += CSWlibfreetype6 endif
# CSWorbit2 CSWpango

# It is ok to depend on the base files
CHECKPKG_OVERRIDES_CSWgvim += surplus-dependency|CSWvimrt

INSTALL_SCRIPTS = minimal

# Note: Tests require controlling terminal
TEST_TARGET = test

include gar/categormodulatedst-install-isa-i386:
	mkdir -p $(DESTDIR)/opt/csw/share/pixmaps
	cp $(WORKSRC)/runtime/vim48x48.png $(DESTDIR)/opt/csw/share/pixmaps/gvim.png
	mkdir -p $(DESTDIR)/opt/csw/share/applications
	cp $(DOWNLOADDIR)/gvim.desktop $(DESTDIR)/opt/csw/share/applications/gvim.desktop
	mv $(DESTDIRgnometutor $(DESTDIR)/opt/csw/bin/gvimtutor
	mv $(DESTDIR)/opt/csw/bin/gvim-gnome      $(DESTDIR)/opt/csw/bin/gvim
	mv $(DESTDIR)/opt/csw/bin/rgvim-gnome     $(DESTDIR)/opt/csw/bin/rgvim
	mv $(DESTDIR)/opt/csw/bin/evim-gnome      $(DESTDIR)/opt/csw/bin/evim
	mv $(DESTDIR)/opt/csw/bin/gvim-gnomediff sw/bin/gvim-x11diff $(DESTDIR)/opt/csw/bin/gvimdiff
	@$(MAKECOOKIE)
	$(DONADA)

# Don't install the runtime
install-minimal:
	@$(INSTALL_ENV) $(MAKE) -C $(WORKSRC)/src \
		installvimbin installglinks installgtutorbin
	@$(MAKE