GARNAME = vim
DISTVERSION = 7.2
PATCHREV = 093
GARVERSION = $(DISTVERSION).$(PATCHREV)
CATEGORIES = utils
SPKG_SOURCEURL = http://www.vim.org/download.php
DESCRIPTION = Vi IMproved with GTK+ support
define BLURB
  Vim is an almost fully-compatible version of the Unix editor Vi. Many new
  features have been added including multi-level undo, syntax highlighting,
  commandline history, online help, filename completion, and block operations.
  It is descended from the vi clone "stevie" and runs on many systems, including
  Unix, MS Windows, OS/2, Macintosh, VMS, and Amiga.
endef

#DEPENDS = utils/mktemp lib/ncurses

MASTER_SITES += ftp://ftp.vim.org/pub/vim/patches/$(DISTVERSION)/
MASTER_SITES += ftp://ftp.vim.org/pub/vim/extra/
MASTER_SITES += ftp://ftp.vim.org/pub/vim/unix/

DISTFILES  = $(call admfiles,CSWgvim,)
DISTFILES += $(GARNAME)-$(DISTVERSION).tar.bz2
DISTFILES += $(GARNAME)-$(DISTVERSION)-lang.tar.gz
DISTFILES += $(GARNAME)-$(DISTVERSION)-extra.tar.gz
DISTFILES += gvim.desktop

PATCHFILES  = $(foreach T,$(shell gseq -f "%03g" 001 $(PATCHREV)),$(DISTVERSION).$(T))
PATCHFILES += vimtutor.patch

WORKSRC = $(WORKDIR)/$(GARNAME)$(subst .,,$(DISTVERSION))

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-global-runtime=$(sharedstatedir)/$(GARNAME)
CONFIGURE_ARGS += --with-features=huge
CONFIGURE_ARGS += --with-tlib=ncurses
CONFIGURE_ARGS += --enable-multibyte
CONFIGURE_ARGS += --enable-cscope
CONFIGURE_ARGS += --with-vim-name="vim-x11"
CONFIGURE_ARGS += --enable-gui=gnome2

BUILD_ARGS += "VIMRCLOC=/opt/csw/etc/vim"
BUILD_ARGS += "VIMRUNTIMEDIR=/opt/csw/share/vim/vim72"
#GTK2 needs 64-bit
#BUILD64 = 1

PATCHDIRLEVEL = 0

REQUIRED_PKGS_CSWgvim  = CSWvimrt CSWbonobo2 CSWfconfig CSWftype2 CSWgconf2
REQUIRED_PKGS_CSWgvim += CSWggettext CSWglib2 CSWgnomekeyring CSWgnomevfs2 CSWgtk2
REQUIRED_PKGS_CSWgvim += CSWiconv CSWlibart CSWlibatk CSWlibbonoboui CSWlibcairo
REQUIRED_PKGS_CSWgvim += CSWlibgnome CSWlibgnomecanvas CSWlibgnomeui CSWlibnet CSWlibpopt
REQUIRED_PKGS_CSWgvim += CSWlibxml2 CSWlibxrender CSWncurses CSWorbit2 CSWpango
REQUIRED_PKGS_CSWgvim += CSWperl CSWpng CSWzlib

INSTALL_SCRIPTS = minimal

# Note: Tests require controlling terminal
TEST_TARGET = test

ISAEXEC_EXCLUDE_FILES  = /opt/csw/bin/gview
ISAEXEC_EXCLUDE_FILES += /opt/csw/bin/gvim
ISAEXEC_EXCLUDE_FILES += /opt/csw/bin/rgvim
ISAEXEC_EXCLUDE_FILES += /opt/csw/bin/rgview
ISAEXEC_EXCLUDE_FILES += /opt/csw/bin/gvimdiff
ISAEXEC_EXCLUDE_FILES += /opt/csw/bin/gvimtutor
ISAEXEC_EXCLUDE_FILES += /opt/csw/bin/evim
ISAEXEC_EXCLUDE_FILES += /opt/csw/bin/eview

MERGE_EXCLUDE_FILES_isa-sparcv9  = /opt/csw/bin/sparcv9/gview
MERGE_EXCLUDE_FILES_isa-sparcv9 += /opt/csw/bin/sparcv9/rgvim-x11
MERGE_EXCLUDE_FILES_isa-sparcv9 += /opt/csw/bin/sparcv9/rgview
MERGE_EXCLUDE_FILES_isa-sparcv9 += /opt/csw/bin/sparcv9/eview
MERGE_EXCLUDE_FILES_isa-sparcv9 += /opt/csw/bin/sparcv9/evim-x11
MERGE_EXCLUDE_FILES_isa-sparcv9 += /opt/csw/bin/sparcv9/gvim-x11diff
MERGE_EXCLUDE_FILES_isa-sparcv9 += /opt/csw/bin/sparcv9/gvim-x11
MERGE_EXCLUDE_FILES_isa-sparcv9 += /opt/csw/bin/sparcv9/gvim-x11tutor

MERGE_EXCLUDE_FILES_isa-amd64  = /opt/csw/bin/amd64/gview
MERGE_EXCLUDE_FILES_isa-amd64 += /opt/csw/bin/amd64/rgvim-x11
MERGE_EXCLUDE_FILES_isa-amd64 += /opt/csw/bin/amd64/rgview
MERGE_EXCLUDE_FILES_isa-amd64 += /opt/csw/bin/amd64/eview
MERGE_EXCLUDE_FILES_isa-amd64 += /opt/csw/bin/amd64/evim-x11
MERGE_EXCLUDE_FILES_isa-amd64 += /opt/csw/bin/amd64/gvim-x11diff
MERGE_EXCLUDE_FILES_isa-amd64 += /opt/csw/bin/amd64/gvim-x11
MERGE_EXCLUDE_FILES_isa-amd64 += /opt/csw/bin/amd64/gvim-x11tutor

include gar/category.mk

post-install-isa-sparcv8 post-install-isa-i386:
	mkdir -p $(DESTDIR)/opt/csw/share/pixmaps
	cp $(WORKSRC)/runtime/vim48x48.png $(DESTDIR)/opt/csw/share/pixmaps/gvim.png
	mkdir -p $(DESTDIR)/opt/csw/share/applications
	cp $(DOWNLOADDIR)/gvim.desktop $(DESTDIR)/opt/csw/share/applications/gvim.desktop
	mv $(DESTDIR)/opt/csw/bin/gvim-x11tutor $(DESTDIR)/opt/csw/bin/gvimtutor
	mv $(DESTDIR)/opt/csw/bin/gvim-x11 $(DESTDIR)/opt/csw/bin/gvim
	mv $(DESTDIR)/opt/csw/bin/rgvim-x11 $(DESTDIR)/opt/csw/bin/rgvim
	mv $(DESTDIR)/opt/csw/bin/evim-x11 $(DESTDIR)/opt/csw/bin/evim
	mv $(DESTDIR)/opt/csw/bin/gvim-x11diff $(DESTDIR)/opt/csw/bin/gvimdiff
	@$(MAKECOOKIE)
	$(DONADA)

# Don't install the runtime
install-minimal:
	@$(INSTALL_ENV) $(MAKE) -C $(WORKSRC)/src \
		installvimbin installglinks installgtutorbin
	@$(MAKECOOKIE)
	$(DONADA)
