GARNAME = vim
DISTVERSION = 7.2
PATCHREV = 088
GARVERSION = $(DISTVERSION).$(PATCHREV)
CATEGORIES = utils
SPKG_SOURCEURL = http://www.vim.org/download.php
DESCRIPTION = Vi IMproved
define BLURB
  Vim is an almost fully-compatible version of the Unix editor Vi. Many new
  features have been added including multi-level undo, syntax highlighting,
  commandline history, online help, filename completion, and block operations.
  It is descended from the vi clone "stevie" and runs on many systems, including
  Unix, MS Windows, OS/2, Macintosh, VMS, and Amiga.
endef

MASTER_SITES += ftp://ftp.vim.org/pub/vim/patches/$(DISTVERSION)/
MASTER_SITES += ftp://ftp.vim.org/pub/vim/extra/
MASTER_SITES += ftp://ftp.vim.org/pub/vim/unix/

DISTFILES += $(call admfiles,CSWvim,)
DISTFILES += $(call admfiles,CSWvimrt,)
DISTFILES += $(GARNAME)-$(DISTVERSION).tar.bz2
DISTFILES += $(GARNAME)-$(DISTVERSION)-lang.tar.gz
DISTFILES += $(GARNAME)-$(DISTVERSION)-extra.tar.gz

PATCHFILES  = $(foreach T,$(shell gseq -f "%03g" 001 $(PATCHREV)),$(DISTVERSION).$(T))
PATCHFILES += vimtutor.patch

WORKSRC = $(WORKDIR)/$(GARNAME)$(subst .,,$(DISTVERSION))

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-xim
CONFIGURE_ARGS += --without-x
CONFIGURE_ARGS += --enable-gui=no
CONFIGURE_ARGS += --disable-gpm
CONFIGURE_ARGS += --with-global-runtime=$(sharedstatedir)/$(GARNAME)
CONFIGURE_ARGS += --with-features=huge
CONFIGURE_ARGS += --with-tlib=ncurses
CONFIGURE_ARGS += --enable-multibyte
CONFIGURE_ARGS += --enable-cscope

BUILD_ARGS  = "VIMRCLOC=/opt/csw/etc/vim"
BUILD_ARGS += "VIMRUNTIMEDIR=/opt/csw/share/vim/vim72"
BUILD64 = 1

PATCHDIRLEVEL = 0

REQUIRED_PKGS_CSWvim = CSWggettext CSWiconv CSWncurses CSWvimrt
INCOMPATIBLE_PKGS_CSWvim = CSWvim-minimal

PKGFILES_CSWvimrt = /opt/csw/share/.*

ISAEXEC_EXCLUDE_FILES  = /opt/csw/bin/view
ISAEXEC_EXCLUDE_FILES += /opt/csw/bin/rvim
ISAEXEC_EXCLUDE_FILES += /opt/csw/bin/rview
ISAEXEC_EXCLUDE_FILES += /opt/csw/bin/vimdiff
ISAEXEC_EXCLUDE_FILES += /opt/csw/bin/ex
ISAEXEC_EXCLUDE_FILES += /opt/csw/bin/vimtutor

MERGE_EXCLUDE_FILES_isa-sparcv9  = /opt/csw/bin/sparcv9/view
MERGE_EXCLUDE_FILES_isa-sparcv9 += /opt/csw/bin/sparcv9/rvim
MERGE_EXCLUDE_FILES_isa-sparcv9 += /opt/csw/bin/sparcv9/rview
MERGE_EXCLUDE_FILES_isa-sparcv9 += /opt/csw/bin/sparcv9/vimdiff
MERGE_EXCLUDE_FILES_isa-sparcv9 += /opt/csw/bin/sparcv9/ex
MERGE_EXCLUDE_FILES_isa-sparcv9 += /opt/csw/bin/sparcv9/vimtutor

MERGE_EXCLUDE_FILES_isa-amd64  = /opt/csw/bin/amd64/view
MERGE_EXCLUDE_FILES_isa-amd64 += /opt/csw/bin/amd64/rvim
MERGE_EXCLUDE_FILES_isa-amd64 += /opt/csw/bin/amd64/rview
MERGE_EXCLUDE_FILES_isa-amd64 += /opt/csw/bin/amd64/vimdiff
MERGE_EXCLUDE_FILES_isa-amd64 += /opt/csw/bin/amd64/ex
MERGE_EXCLUDE_FILES_isa-amd64 += /opt/csw/bin/amd64/vimtutor

# Test requires controlling terminal
TEST_SCRIPTS =

include gar/category.mk

post-configure: make-interps-lazy

make-interps-lazy:
	@perl -i.bak -plne \
	    's/(-l(?:perl|python|ruby|tcl)\S*)/-zlazyload $$1 -znolazyload/' \
	    $(WORKSRC)/src/auto/config.mk
