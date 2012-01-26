NAME = vim
DISTVERSION = 7.3
PATCHREV = 254
VERSION = $(DISTVERSION).$(PATCHREV)
CATEGORIES = utils
GARTYPE = v2
SPKG_SOURCEURL = http://www.vim.org/download.php
DESCRIPTION = Vi IMproved
define BLURB
  Vim is an almost fully-compatible version of the Unix editor Vi. Many new
  features have been added including multi-level undo, syntax highlighting,
  commandline history, online help, filename completion, and block operations.
  It is descended from the vi clone "stevie" and runs on many systems, including
  Unix, MS Windows, OS/2, Macintosh, VMS, and Amiga.
endef

PACKAGES = CSWvim
CATALOGNAME_CSWvim = vim
SPKG_DESC_CSWvim = Vi IMproved without GUI
RUNTIME_DEP_PKGS_CSWvim += CSWlibintl8
RUNTIME_DEP_PKGS_CSWvim += CSWlibncurses5
RUNTIME_DEP_PKGS_CSWvim += CSWiconv
# This contains base configuration stuff checkpkg cannot track
RUNTIME_DEP_PKGS_CSWvim += CSWvimrt
CHECKPKG_OVERRIDES_CSWvim += surplus-dependency|CSWvimrt
INCOMPATIBLE_PKGS_CSWvim = CSWvim-minimal

PACKAGES += CSWvimrt
CATALOGNAME_CSWvimrt = vimrt
SPKG_DESC_CSWvimrt = Vi IMproved runtime and documentation
PKGFILES_CSWvimrt = $(sharedstatedir)/.*
ARCHALL_CSWvimrt = 1

# We have .el files, but that is purely optional
CHECKPKG_OVERRIDES_CSWvimrt += missing-dependency|CSWemacscommon

# Some tools need Perl and one is hardcoded to CSW Perl:
#   /opt/csw/share/vim/vim73/tools/efm_perl.pl
# Maybe the tools should be separated package depending on CSWperl.
# Overwrite for the moment.
CHECKPKG_OVERRIDES_CSWvimrt += missing-dependency|CSWperl

# These are all in the docs
CHECKPKG_OVERRIDES_CSWvimrt += file-with-bad-content

MASTER_SITES  = ftp://ftp.vim.org/pub/vim/patches/$(DISTVERSION)/
MASTER_SITES += ftp://ftp.vim.org/pub/vim/extra/
MASTER_SITES += ftp://ftp.vim.org/pub/vim/unix/

DISTFILES  = $(NAME)-$(DISTVERSION).tar.bz2
DISTFILES += vimrc
DISTFILES += vimrc.tiny
DISTFILES += gvimrc
DISTFILES += COPYING

PATCHFILES  = $(foreach T,$(shell gseq -f "%03g" 001 $(PATCHREV)),$(DISTVERSION).$(T))

PATCHFILES += 0001-Expect-tab-instead-of-whitespace.patch

DISTNAME = $(NAME)$(subst .,,$(DISTVERSION))

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-xim
CONFIGURE_ARGS += --without-x
CONFIGURE_ARGS += --enable-gui=no
CONFIGURE_ARGS += --disable-gpm
CONFIGURE_ARGS += --with-global-runtime=$(sharedstatedir)/$(NAME)
CONFIGURE_ARGS += --with-features=huge
CONFIGURE_ARGS += --with-tlib=ncurses
CONFIGURE_ARGS += --enable-multibyte
CONFIGURE_ARGS += --enable-cscope

CONFIGURE_ARGS += --enable-pythoninterp=dynamic
CONFIGURE_ARGS += --with-python-config-dir=$(libdir)/python

BUILD_ARGS  = "VIMRCLOC=/opt/csw/share/vim"
BUILD_ARGS += "VIMRUNTIMEDIR=/opt/csw/share/vim/vim$(subst .,,$(DISTVERSION))"

PATCHDIRLEVEL = 0

# Note: Tests require controlling terminal
TEST_TARGET = test


include gar/category.mk

post-configure: make-interps-lazy

make-interps-lazy:
	@perl -i.bak -plne \
	    's/(-l(?:perl|python|ruby|tcl)\S*)/-zlazyload $$1 -znolazyload/' \
	    $(WORKSRC)/src/auto/config.mk

post-install-isa-sparcv8 post-install-isa-i386:
	@cp $(DOWNLOADDIR)/vimrc $(DOWNLOADDIR)/gvimrc $(DOWNLOADDIR)/vimrc.tiny $(DESTDIR)/opt/csw/share/vim
	@(cd $(DESTDIR)/opt/csw/share/vim;ln -s vim$(subst .,,$(DISTVERSION)) vimcurrent)
	@$(MAKECOOKIE)
	$(DONADA)
