NAME = cdecl
VERSION = 2.5
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = C declaration guide/tool
define BLURB
endef

MASTER_SITES = http://www.cdecl.org/files/
DISTNAME = cdecl-blocks-$(VERSION)
DISTFILES = $(DISTNAME).tar.gz
PATCHFILES = 0001-Remove-keyword-for-Sun-Studio.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-blocks-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://www.cdecl.org/

LICENSE = README

RUNTIME_DEP_PKGS = CSWreadline
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS)

CONFIGURE_SCRIPTS =

LIBS = -lreadline
EXTRA_CFLAGS = $(CPPFLAGS) $(LDFLAGS) -DUSE_READLINE
BUILD_OVERRIDE_DIRS = CFLAGS CC LIBS

TEST_TARGET = test
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)$(docdir)/$(NAME)
	ginstall $(WORKSRC)/README $(DESTDIR)$(docdir)/$(NAME)
	ginstall -d $(DESTDIR)$(bindir)
	ginstall $(WORKSRC)/cdecl $(DESTDIR)$(bindir)/cdecl
	gln -s cdecl $(DESTDIR)$(bindir)/c++decl
	ginstall -d $(DESTDIR)$(mandir)/man1
	ginstall $(WORKSRC)/cdecl.1 $(DESTDIR)$(mandir)/man1
	gln -s cdecl.1 $(DESTDIR)$(mandir)/man1/c++decl.1
	@$(MAKECOOKIE)
