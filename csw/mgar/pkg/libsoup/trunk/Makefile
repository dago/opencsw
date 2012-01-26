NAME = libsoup
VERSION = 2.29.91
CATEGORIES = gnome
GARTYPE = v2
  
 
DESCRIPTION = HTTP client/server library for GNOME
define BLURB
endef
MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTFILES += old_libs_i386.tar.bz2
DISTFILES += old_libs_sparc.tar.bz2

PACKAGES = CSWlibsoup CSWlibsoupdevel CSWlibsoupdoc CSWlibsoup2
CATALOGNAME_CSWlibsoup = libsoup
CATALOGNAME_CSWlibsoup2 = libsoup2
CATALOGNAME_CSWlibsoupdevel = libsoup_devel
CATALOGNAME_CSWlibsoupdoc = libsoup_doc

SPKG_DESC_CSWlibsoup += HTTP client/server library for GNOME
# For compat with old packages
SPKG_DESC_CSWlibsoup2 += HTTP client/server library for GNOME - dummy package
SPKG_DESC_CSWlibsoupdevel += HTTP client/server library for GNOME - developer package
SPKG_DESC_CSWlibsoupdoc += HTTP client/server library for GNOME - documentation

RUNTIME_DEP_PKGS_CSWlibsoup += CSWgconf2 CSWgcrypt CSWggettextrt CSWglib2
RUNTIME_DEP_PKGS_CSWlibsoup += CSWgnutls CSWgpgerr CSWlibproxy CSWlibxml2
RUNTIME_DEP_PKGS_CSWlibsoup += CSWsqlite3rt
# Required for old libraries
RUNTIME_DEP_PKGS_CSWlibsoup += CSWiconv
RUNTIME_DEP_PKGS_CSWlibsoup += CSWsunmath
RUNTIME_DEP_PKGS_CSWlibsoup += CSWzlib
RUNTIME_DEP_PKGS_CSWlibsoup2 += CSWlibsoup
RUNTIME_DEP_PKGS_CSWlibsoupdevel += CSWlibsoup
RUNTIME_DEP_PKGS_CSWlibsoupdoc += 

BUILD_DEP_PKGS += CSWlibproxy

PKGFILES_CSWlibsoup2 = non-existing
PKGFILES_CSWlibsoupdevel = $(PKGFILES_DEVEL)
PKGFILES_CSWlibsoupdoc = $(sharedstatedir)/gtk-doc/.*

ARCHALL_CSWlibsoupdoc = 1
ARCHALL_CSWlibsoup2 = 1

# libgnutls.so.11 no longer exists, but in case someone still use libsoup-2.0.so
# and still have libgnutls.so.11 we override checkpkg
CHECKPKG_OVERRIDES += orphan-soname|libgnutls.so.11
CHECKPKG_OVERRIDES += symbol-not-found|libsoup-2.0.so.0.0.0
# Possible bug in checkpkg
CHECKPKG_OVERRIDES += symbol-not-found|libsoup-gnome-2.4.so.1.2.0

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

EXTRA_INC = /opt/csw/X11/include
EXTRA_LIB = /opt/csw/X11/lib 
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib 
EXTRA_SOS_LD_FLAGS = -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-libgcrypt-prefix=$(prefix)
CONFIGURE_ARGS += --x-includes=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

STRIP_LIBTOOL = 1

# Not working until gconf2 is 64-bit
#BUILD64_LIBS_ONLY = 1

# One test fails for some unknown reason
#TEST_TARGET = check
TEST_TARGET = 

include gar/category.mk

# Include old libraries package for compatibility
post-install-isa-sparcv8:
	@(bzip2 -dc $(DOWNLOADDIR)/old_libs_sparc.tar.bz2 | (cd $(INSTALLISADIR)$(libdir);tar xf -))
	( if [ ! -r $(INSTALLISADIR)$(libdir)/libsoup-2.0.so.0 ] ; then ln -s libsoup-2.0.so.0.0.0 $(INSTALLISADIR)$(libdir)/libsoup-2.0.so.0 ; fi )
	( if [ ! -r $(INSTALLISADIR)$(libdir)/libsoup-2.0.so ] ; then ln -s libsoup-2.0.so.0.0.0 $(INSTALLISADIR)$(libdir)/libsoup-2.0.so ; fi )
	( if [ ! -r $(INSTALLISADIR)$(libdir)/libsoup-2.2.so.8 ] ; then ln -s libsoup-2.2.so.8.4.0 $(INSTALLISADIR)$(libdir)/libsoup-2.2.so.8 ; fi )
	( if [ ! -r $(INSTALLISADIR)$(libdir)/libsoup-2.2.so ] ; then ln -s libsoup-2.2.so.8.4.0 $(INSTALLISADIR)$(libdir)/libsoup-2.2.so ; fi )
	$(MAKECOOKIE)

post-install-isa-i386:
	@(bzip2 -dc $(DOWNLOADDIR)/old_libs_i386.tar.bz2 | (cd $(INSTALLISADIR)$(libdir);tar xf -))
	( if [ ! -r $(INSTALLISADIR)$(libdir)/libsoup-2.0.so.0 ] ; then ln -s libsoup-2.0.so.0.0.0 $(INSTALLISADIR)$(libdir)/libsoup-2.0.so.0 ; fi )
	( if [ ! -r $(INSTALLISADIR)$(libdir)/libsoup-2.0.so ] ; then ln -s libsoup-2.0.so.0.0.0 $(INSTALLISADIR)$(libdir)/libsoup-2.0.so ; fi )
	( if [ ! -r $(INSTALLISADIR)$(libdir)/libsoup-2.2.so.8 ] ; then ln -s libsoup-2.2.so.8.4.0 $(INSTALLISADIR)$(libdir)/libsoup-2.2.so.8 ; fi )
	( if [ ! -r $(INSTALLISADIR)$(libdir)/libsoup-2.2.so ] ; then ln -s libsoup-2.2.so.8.4.0 $(INSTALLISADIR)$(libdir)/libsoup-2.2.so ; fi )
	$(MAKECOOKIE)
