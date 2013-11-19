# $Id$

NAME	=	dictd
VERSION	=	1.12.1
GARTYPE	=	v2

DESCRIPTION	=	DICT Protocol
define BLURB
  Client, server and utilities for the Dictionary Server Protocol
  (DICT), a TCP transaction based query/response protocol that
  provides access to dictionary definitions from a set of natural
  language dictionary databases.
endef

MASTER_SITES	=	$(SF_MIRRORS)
SF_PROJECT		=	dict
DISTFILES 		=	$(DISTNAME).tar.gz
PATCHFILES		+=	0001-fix-and-enhance-documentation.patch
PATCHFILES		+=	0002-test-drivers-use-bash.patch
PATCHFILES		+=	0003-plugin-needs-limits.patch

BUILD_DEP_PKGS	+=	CSWlibmaa-dev
BUILD_DEP_PKGS	+=	CSWlibz-dev
BUILD_DEP_PKGS	+=	CSWlibdbi-dev
BUILD_DEP_PKGS	+=	CSWgroff

GARCOMPILER		=	GNU
CONFIGURE_ARGS	=	$(DIRPATHS)
CONFIGURE_ARGS	+=	--libexecdir=$(libexecdir)/$(NAME)
CONFIGURE_ARGS	+=	--sysconfdir=$(sysconfdir)/$(NAME)
CONFIGURE_ARGS	+=	--datadir=$(datadir)/$(NAME)
CONFIGURE_ARGS	+=	--enable-dictorg
CONFIGURE_ARGS	+=	--with-plugin-dbi

TEST_SCRIPTS	=	custom

EXTRA_MERGE_EXCLUDE_FILES	+=	$(libexecdir)/$(NAME)/.*[.]la
EXTRA_MERGE_EXCLUDE_FILES	+=	$(libexecdir)/$(NAME).*[.]a

PACKAGES					+=	CSWdict
SPKG_DESC_CSWdict			=	$(DESCRIPTION), client
CATALOGNAME_CSWdict			=	dict
PKGFILES_CSWdict			+=	$(bindir)/colorit
PKGFILES_CSWdict			+=	$(bindir)/dict
PKGFILES_CSWdict			+=	$(bindir)/dict_lookup
PKGFILES_CSWdict			+=	$(bindir)/dictl
PKGFILES_CSWdict			+=	$(docdir)/$(CATALOGNAME_CSWdict)/ANNOUNCE
PKGFILES_CSWdict			+=	$(docdir)/$(CATALOGNAME_CSWdict)/ChangeLog
PKGFILES_CSWdict			+=	$(docdir)/$(CATALOGNAME_CSWdict)/NEWS
PKGFILES_CSWdict			+=	$(docdir)/$(CATALOGNAME_CSWdict)/examples/dict1.conf
PKGFILES_CSWdict			+=	$(mandir)/man1/colorit.1
PKGFILES_CSWdict			+=	$(mandir)/man1/dict.1
PKGFILES_CSWdict			+=	$(mandir)/man1/dict_lookup.1
PKGFILES_CSWdict			+=	$(mandir)/man1/dictl.1

RUNTIME_DEP_PKGS_CSWdicd	+= CSWlibmaa3-0-0

PACKAGES						+=	CSWdictfmt
SPKG_DESC_CSWdictfmt			=	$(DESCRIPTION), converter
CATALOGNAME_CSWdictfmt			=	dictfmt
PKGFILES_CSWdictfmt				+=	$(bindir)/dictfmt
PKGFILES_CSWdictfmt				+=	$(bindir)/dictfmt_index2suffix
PKGFILES_CSWdictfmt				+=	$(bindir)/dictfmt_index2word
PKGFILES_CSWdictfmt				+=	$(bindir)/dictunformat
PKGFILES_CSWdictfmt				+=	$(mandir)/man1/dictfmt.1
PKGFILES_CSWdictfmt				+=	$(mandir)/man1/dictfmt_index2suffix.1
PKGFILES_CSWdictfmt				+=	$(mandir)/man1/dictfmt_index2word.1
PKGFILES_CSWdictfmt				+=	$(mandir)/man1/dictunformat.1
RUNTIME_DEP_PKGS_CSWdictfmt		+=	CSWlibmaa3-0-0
RUNTIME_DEP_PKGS_CSWdictfmt		+=	CSWrecode
CHECKPKG_OVERRIDES_CSWdictfmt	+=	surplus-dependency|CSWrecode

PACKAGES					+=	CSWdictzip
SPKG_DESC_CSWdictzip		=	$(DESCRIPTION), compressor
CATALOGNAME_CSWdictzip		=	dictzip
PKGFILES_CSWdictzip			+=	$(bindir)/dictzip
PKGFILES_CSWdictzip			+=	$(mandir)/man1/dictzip.1
RUNTIME_DEP_PKGS_CSWdictzip	+=	CSWlibz1
RUNTIME_DEP_PKGS_CSWdictzip	+=	CSWlibmaa3-0-0

PACKAGES					+=	CSWdictd
SPKG_DESC_CSWdictd			=	$(DESCRIPTION), server
CATALOGNAME_CSWdictd		=	dictd
PKGFILES_CSWdictd			+=	$(sbindir)/.*
PKGFILES_CSWdictd			+=	$(mandir)/man8/.*

PKGFILES_CSWdictd			+=	$(docdir)/$(NAME)/ANNOUNCE
PKGFILES_CSWdictd			+=	$(docdir)/$(NAME)/ChangeLog
PKGFILES_CSWdictd			+=	$(docdir)/$(NAME)/INITSCRIPT
PKGFILES_CSWdictd			+=	$(docdir)/$(NAME)/INSTALL
PKGFILES_CSWdictd			+=	$(docdir)/$(NAME)/NEWS
PKGFILES_CSWdictd			+=	$(docdir)/$(NAME)/README
PKGFILES_CSWdictd			+=	$(docdir)/$(NAME)/TODO
PKGFILES_CSWdictd			+=	$(docdir)/$(NAME)/.*[.]txt
PKGFILES_CSWdictd			+=	$(docdir)/$(NAME)/.*[.]ps
PKGFILES_CSWdictd			+=	$(docdir)/$(NAME)/security.doc
PKGFILES_CSWdictd			+=	$(docdir)/$(NAME)/examples/dictd.*
PKGFILES_CSWdictd			+=	$(libexecdir)/$(NAME)/.*
RUNTIME_DEP_PKGS_CSWdictd	+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWdicd	+=	CSWlibmaa3-0-0
RUNTIME_DEP_PKGS_CSWdictd	+=	CSWlibz1
RUNTIME_DEP_PKGS_CSWdictd	+=	CSWlibdbi1
RUNTIME_DEP_PKGS_CSWdictd	+=	CSWdictzip
CHECKPKG_OVERRIDES_CSWdictd	+=	surplus-dependency|CSWdictzip
CHECKPKG_OVERRIDES_CSWdictd	+=	no-direct-binding|/opt/csw/libexec/dictd/dictdplugin_exit.so.0.0.0|is|not|directly|bound|to|soname|libgcc_s.so.1
CHECKPKG_OVERRIDES_CSWdictd	+=	no-direct-binding|/opt/csw/libexec/dictd/dictdplugin_exit.so.0.0.0|is|not|directly|bound|to|soname|libmaa.so.3
CHECKPKG_OVERRIDES_CSWdictd	+=	no-direct-binding|/opt/csw/libexec/dictd/dictdplugin_popen.so.0.0.0|is|not|directly|bound|to|soname|libgcc_s.so.1
CHECKPKG_OVERRIDES_CSWdictd	+=	no-direct-binding|/opt/csw/libexec/dictd/dictdplugin_popen.so.0.0.0|is|not|directly|bound|to|soname|libmaa.so.3

PACKAGES						+=	CSWdictd-dev
CATALOGNAME_CSWdictd-dev		=	dictd_dev
SPKG_DESC_CSWdictd-dev			+=	$(DESCRIPTION), server plugins development files
PKGFILES_CSWdictd-dev			+=	$(bindir)/dictdplugin-config
PKGFILES_CSWdictd-dev			+=	$(PKGFILES_DEVEL)
ARCHALL_CSWdictd-dev			=	1
CHECKPKG_OVERRIDES_CSWdictd-dev	+=	archall-devel-package

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

post-build:
	cd $(WORKSRC) && \
	/usr/bin/env -i $(BUILD_ENV) && $(MAKE) -C $(OBJDIR) samples
	cd $(WORKSRC)/doc && \
	/usr/bin/env -i $(BUILD_ENV) && $(MAKE) -C $(OBJDIR) all rfc.ps dicf dicf.ps
	$(MAKECOOKIE)

test-custom:
	cd $(WORKSRC) && /usr/bin/env -i $(BUILD_ENV) && $(MAKE) -C $(OBJDIR) test
	$(MAKECOOKIE)

post-install: pkgsdocdir	=	$(docdir)/$(NAME)
post-install: pkgcdocdir	=	$(docdir)/$(CATALOGNAME_CSWdict)
post-install: pkgsexdir		=	$(docdir)/$(NAME)/examples
post-install: pkgcexdir		=	$(docdir)/$(CATALOGNAME_CSWdict)/examples
post-install:
	cd $(WORKSRC) && \
	/usr/bin/env -i $(INSTALL_ENV) && $(MAKE) DESTDIR=$(DESTDIR) -C $(OBJDIR) install.samples
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(pkgsdocdir)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/ANNOUNCE $(DESTDIR)/$(pkgsdocdir)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/ChangeLog $(DESTDIR)/$(pkgsdocdir)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/INITSCRIPT $(DESTDIR)/$(pkgsdocdir)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/INSTALL $(DESTDIR)/$(pkgsdocdir)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/NEWS $(DESTDIR)/$(pkgsdocdir)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/README $(DESTDIR)/$(pkgsdocdir)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/TODO $(DESTDIR)/$(pkgsdocdir)
	cd $(WORKSRC)/doc && \
	ginstall --preserve-timestamps --mode=u=rwx,go=r dicf.txt dicf.ps rfc.txt rfc.ps security.doc $(DESTDIR)/$(pkgsdocdir)
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(pkgcdocdir)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/ANNOUNCE $(DESTDIR)/$(pkgcdocdir)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/ChangeLog $(DESTDIR)/$(pkgcdocdir)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/NEWS $(DESTDIR)/$(pkgcdocdir)
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(pkgsexdir)
	cd $(WORKSRC)/examples && \
	ginstall --preserve-timestamps --mode=u=rwx,go=r dictd* $(DESTDIR)/$(pkgsexdir)
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(pkgcexdir)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/examples/dict1.conf $(DESTDIR)/$(pkgcexdir)
	$(MAKECOOKIE)
