GARNAME = xchat
GARVERSION = 2.8.6
CATEGORIES = gnome

DESCRIPTION = GTK+ based IRC client, similar to AmIRC (Amiga).
define BLURB
  X-Chat is a fully-featured graphical IRC client using the GTK toolkit.
  Optionally it can be compiled to use GNOME and Perl scripting.
endef

MASTER_SITES  = http://xchat.org/files/source/2.8/
MASTER_SITES += http://xchat.org/files/source/2.8/patches/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

PACKAGES = CSWxchat CSWxchat-pl CSWxchat-py CSWxchat-tcl
CATALOGNAME_CSWxchat     = xchat
CATALOGNAME_CSWxchat-pl  = xchat_pl
CATALOGNAME_CSWxchat-py  = xchat_py
CATALOGNAME_CSWxchat-tcl = xchat_tcl
SPKG_DESC_CSWxchat     = GTK+ based IRC client, similar to AmIRC (Amiga).
SPKG_DESC_CSWxchat-pl  = xChat Perl Plugin
SPKG_DESC_CSWxchat-py  = xChat Python Plugin
SPKG_DESC_CSWxchat-tcl = xChat TCL Plugin
REQUIRED_PKGS_CSWxchat  = CSWdbusglib CSWexpat CSWfconfig CSWftype2 CSWlibntlm
REQUIRED_PKGS_CSWxchat += CSWggettextrt CSWglib2 CSWgtk2 CSWiconv CSWlibatk 
REQUIRED_PKGS_CSWxchat += CSWlibcairo CSWlibdbus CSWlibxft2 CSWlibxrender 
REQUIRED_PKGS_CSWxchat += CSWosslrt CSWpango CSWpng CSWsunmath CSWzlib
REQUIRED_PKGS_CSWxchat-pl   = CSWxchat CSWperl CSWosslrt CSWglib2
REQUIRED_PKGS_CSWxchat-pl  += CSWggettextrt CSWlibntlm
REQUIRED_PKGS_CSWxchat-py   = CSWxchat CSWpython CSWosslrt CSWglib2
REQUIRED_PKGS_CSWxchat-py  += CSWggettextrt CSWlibntlm
REQUIRED_PKGS_CSWxchat-tcl  = CSWxchat CSWtcl CSWosslrt CSWglib2
REQUIRED_PKGS_CSWxchat-tcl += CSWggettextrt CSWlibntlm
PKGFILES_CSWxchat-pl  = $(libdir)/.*/perl.so
PKGFILES_CSWxchat-py  = $(libdir)/.*/python.so
PKGFILES_CSWxchat-tcl = $(libdir)/.*/tcl.so

# We define upstream file regex so we can be notifed of new 
# upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

# Official XChat patches
PATCHFILES  = xc286-smallfixes.diff
PATCHFILES += xchat26-compiletime.diff

LDFLAGS =
NOISALIST = 1
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-openssl=$(prefix)
CONFIGURE_ARGS += --enable-threads=solaris
CONFIGURE_ARGS += --enable-tcl=$(libdir)
CONFIGURE_ARGS += --enable-shm
CONFIGURE_ARGS += --enable-ipv6

## run checkpkg manually
ENABLE_CHECK = 0
TEST_TARGET = check

EXTRA_INC = $(prefix)/bdb44/include
EXTRA_LIB = $(prefix)/bdb44/lib

DISTFILES += fixme.sh
post-configure-modulated:
	@(echo "~~~ Fixing Libtool ~~~")
	@$(DOWNLOADDIR)/fixme.sh $(WORKSRC)
	$(DONADA)

include gar/category.mk
