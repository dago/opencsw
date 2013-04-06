NAME = xchat
VERSION = 2.8.8
CATEGORIES = gnome
GARTYPE = v2

DESCRIPTION = GTK+ based IRC client, similar to AmIRC (Amiga).
define BLURB
  X-Chat is a fully-featured graphical IRC client using the GTK toolkit.
  Optionally it can be compiled to use GNOME and Perl scripting.
endef

MASTER_SITES  = http://xchat.org/files/source/2.8/
MASTER_SITES += http://xchat.org/files/source/2.8/patches/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

PACKAGES = CSWxchat CSWxchat-pl CSWxchat-py CSWxchat-tcl
CATALOGNAME_CSWxchat     = xchat
CATALOGNAME_CSWxchat-pl  = xchat_pl
CATALOGNAME_CSWxchat-py  = xchat_py
CATALOGNAME_CSWxchat-tcl = xchat_tcl
SPKG_DESC_CSWxchat     = GTK+ based IRC client, similar to AmIRC (Amiga).
SPKG_DESC_CSWxchat-pl  = X-Chat Perl Plugin
SPKG_DESC_CSWxchat-py  = X-Chat Python Plugin
SPKG_DESC_CSWxchat-tcl = X-Chat TCL Plugin
RUNTIME_DEP_PKGS_CSWxchat  = CSWlibgtk-x11-2-0-0 CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWxchat += CSWlibglib2-0-0 CSWlibdbus-glib1-2 CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWxchat += CSWlibintl8 CSWlibgdk-pixbuf2-0-0 CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWxchat += CSWpango CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWxchat-pl   = CSWperl
RUNTIME_DEP_PKGS_CSWxchat-py   = CSWlibpython2-6-1-0 CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWxchat-tcl  = CSWlibtcl8-5
PKGFILES_CSWxchat-pl  = $(libdir)/.*/perl.so
PKGFILES_CSWxchat-py  = $(libdir)/.*/python.so
PKGFILES_CSWxchat-tcl = $(libdir)/.*/tcl.so


# We define upstream file regex so we can be notifed of new 
# upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

# Fix some compilation problem under Solaris
PATCHFILES = xchat26-compiletime.diff

# Patch taken http://trac.macports.org/ticket/33959 and updated
# to be able to compile against a more recent version of glib
PATCHFILES += patch-glib-2.32.diff

LDFLAGS =
NOISALIST = 1
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-openssl=$(prefix)
CONFIGURE_ARGS += --enable-threads=solaris
CONFIGURE_ARGS += --enable-tcl=$(libdir)
CONFIGURE_ARGS += --enable-shm
CONFIGURE_ARGS += --enable-ipv6

## run checkpkg manually
EXTRA_INC = $(prefix)/bdb44/include
EXTRA_LIB = $(prefix)/bdb44/lib

DISTFILES += fixme.sh
post-configure-modulated:
	@(echo "~~~ Fixing Libtool ~~~")
	@$(DOWNLOADDIR)/fixme.sh $(WORKSRC)
	$(DONADA)

post-merge:
	rm -f $(PKGROOT)/$(libdir)/charset.alias
	rm -f $(PKGROOT)/$(sharedstatedir)/locale/locale.alias

include gar/category.mk
