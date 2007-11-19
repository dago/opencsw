MASTER_SITES = ftp://ftp.vim.org/pub/vim/unix/
DISTFILES += $(GARNAME)-$(DISTVERSION).tar.bz2
DISTFILES += $(GARNAME)-$(DISTVERSION)-lang.tar.gz
DISTFILES += $(GARNAME)-$(DISTVERSION)-extra.tar.gz

WORKSRC = $(WORKDIR)/$(GARNAME)$(subst .,,$(DISTVERSION))

# common options
CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --with-global-runtime=$(sharedstatedir)/$(GARNAME)
CONFIGURE_ARGS += --with-features=huge
CONFIGURE_ARGS += --with-tlib=ncurses
#CONFIGURE_ARGS += --enable-perlinterp
#CONFIGURE_ARGS += --enable-pythoninterp
#CONFIGURE_ARGS += --with-python-config-dir=$(libdir)/python/config/
#CONFIGURE_ARGS += --enable-tclinterp
#CONFIGURE_ARGS += --enable-rubyinterp
CONFIGURE_ARGS += --enable-multibyte
CONFIGURE_ARGS += --enable-cscope
CONFIGURE_ARGS += --disable-static
CONFIGURE_ARGS += --enable-shared

