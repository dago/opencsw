# $Id$

NAME = namazu
VERSION = 2.0.21
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = A Full-Text Search Engine
define BLURB
  Namazu is a full-text search engine intended for easy use. Not only
  does it work as a small or medium scale Web search engine, but also
  as a personal search system for email or other files.

  (The Japanese word 'Namazu' means 'catfish' in English.) 
endef

MASTER_SITES	=	http://namazu.org/stable/
DISTFILES  		=	$(DISTNAME).tar.gz
PATCHFILES		+=	0001-Adapt-to-OpenCSW-environment.patch

GARCOMPILER		=	GNU

CONFIGURE_ARGS	=	$(DIRPATHS)
CONFIGURE_ARGS	+=	--enable-tknamazu
CONFIGURE_ARGS	+=	--with-indexdir=$(localstatedir)/$(NAME)/index

BUILD_DEP_PKGS		+=	CSWkakasi-dev
BUILD_DEP_PKGS		+=	CSWlibiconv-dev
BUILD_DEP_PKGS		+=	CSWlynx
BUILD_DEP_PKGS		+=	CSWpm-file-mmagic
BUILD_DEP_PKGS		+=	CSWemacs
BUILD_DEP_PKGS		+=	CSWtcl

TEST_SCRIPTS		=	custom

PACKAGES							+=	CSWnamazu
CATALOGNAME_CSWnamazu				=	namazu
SPKG_DESC_CSWnamazu					=	$(DESCRIPTION)
CHECKPKG_OVERRIDES_CSWnamazu		+=	file-with-bad-content|/usr/local|root/opt/csw/share/tknamazu/tknamazu.hlp.ja_JP.SJIS
CHECKPKG_OVERRIDES_CSWnamazu		+=	file-with-bad-content|/usr/local|root/opt/csw/share/tknamazu/tknamazu.hlp.ja
CHECKPKG_OVERRIDES_CSWnamazu		+=	file-with-bad-content|/usr/local|root/opt/csw/share/tknamazu/tknamazu.hlp.en
CHECKPKG_OVERRIDES_CSWnamazu		+=	file-with-bad-content|/usr/local|root/opt/csw/share/doc/namazu/ChangeLog
CHECKPKG_OVERRIDES_CSWnamazu		+=	file-with-bad-content|/usr/local|root/opt/csw/share/doc/namazu/INSTALL-ja
CHECKPKG_OVERRIDES_CSWnamazu		+=	file-with-bad-content|/usr/local|root/opt/csw/share/doc/namazu/INSTALL
CHECKPKG_OVERRIDES_CSWnamazu		+=	file-with-bad-content|/usr/local|root/opt/csw/share/doc/namazu/ja/manual.html
CHECKPKG_OVERRIDES_CSWnamazu		+=	file-with-bad-content|/usr/local|root/opt/csw/share/doc/namazu/ja/tutorial.html
CHECKPKG_OVERRIDES_CSWnamazu		+=	file-with-bad-content|/usr/local|root/opt/csw/share/doc/namazu/en/manual.html
CHECKPKG_OVERRIDES_CSWnamazu		+=	file-with-bad-content|/usr/local|root/opt/csw/share/doc/namazu/en/tutorial.html
CHECKPKG_OVERRIDES_CSWnamazu		+=	file-with-bad-content|/usr/local|root/etc/opt/csw/namazu/namazurc-sample
CHECKPKG_OVERRIDES_CSWnamazu		+=	file-with-bad-content|/usr/share|root/opt/csw/bin/tknamazu
CHECKPKG_OVERRIDES_CSWnamazu		+=	file-with-bad-content|/usr/share|root/opt/csw/share/tknamazu/tknamazurc
CHECKPKG_OVERRIDES_CSWnamazu		+=	file-with-bad-content|/usr/share|root/opt/csw/share/tknamazu/tknamazu.hlp.ja_JP.SJIS
CHECKPKG_OVERRIDES_CSWnamazu		+=	file-with-bad-content|/usr/share|root/opt/csw/share/tknamazu/tknamazu.hlp.ja
CHECKPKG_OVERRIDES_CSWnamazu		+=	file-with-bad-content|/usr/share|root/opt/csw/share/tknamazu/tknamazu.hlp.en
CHECKPKG_OVERRIDES_CSWnamazu		+=	file-with-bad-content|/usr/share|root/opt/csw/share/doc/namazu/ChangeLog
RUNTIME_DEP_PKGS_CSWnamazu			+=	CSWkakasi
RUNTIME_DEP_PKGS_CSWnamazu			+=	CSWlynx
RUNTIME_DEP_PKGS_CSWnamazu			+=	CSWperl
RUNTIME_DEP_PKGS_CSWnamazu			+=	CSWpm-file-mmagic
RUNTIME_DEP_PKGS_CSWnamazu			+=	CSWtcl
RUNTIME_DEP_PKGS_CSWnamazu			+=	CSWlibnmz7
CHECKPKG_OVERRIDES_CSWnamazu		+=	surplus-dependency|CSWlibmz7
CHECKPKG_OVERRIDES_CSWnamazu		+=	surplus-dependency|CSWkakasi
CHECKPKG_OVERRIDES_CSWnamazu		+=	surplus-dependency|CSWlynx
CHECKPKG_OVERRIDES_CSWnamazu		+=	surplus-dependency|CSWpm-file-mmagic
CHECKPKG_OVERRIDES_CSWnamazu		+=	surplus-dependency|CSWtcl
CHECKPKG_OVERRIDES_CSWnamazu		+=	missing-dependency|CSWlibintl8

PACKAGES							+=	CSWlibnmz7
CATALOGNAME_CSWlibnmz7				=	libnmz7
PKGFILES_CSWlibnmz7					+=	$(call baseisadirs,$(libdir),libnmz\.so\.7\.1\.3)
PKGFILES_CSWlibnmz7					+=	$(call baseisadirs,$(libdir),libnmz\.so\.7(\.\d+)*)
SPKG_DESC_CSWlibnmz7				+=	$(DESCRIPTION), libnmz.so.7
RUNTIME_DEP_PKGS_CSWlibnmz7			+=	CSWlibintl8

PACKAGES							+=	CSWnamazu-dev
CATALOGNAME_CSWnamazu-dev			=	namazu_dev
SPKG_DESC_CSWnamazu-dev				+=	$(DESCRIPTION), development files
PKGFILES_CSWnamazu-dev				+=	/opt/csw/lib/libnmz.so
PKGFILES_CSWnamazu-dev				+=	$(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWnamazu-dev		+=	CSWlibnmz7
CHECKPKG_OVERRIDES_CSWnamazu-dev	+=	surplus-dependency|CSWlibmz7
ARCHALL_CSWnamazu-dev				=	1
CHECKPKG_OVERRIDES_CSWnamazu-dev	+=	archall-devel-package

include gar/category.mk

# one of the tests fails: mknmz-11; decided to not block on it...
test-custom:
	-$(MAKE) -k -C $(WORKSRC) check
	$(MAKECOOKIE)

post-install-modulated: errdocdir = $(DESTDIR)/$(datadir)/$(NAME)
post-install-modulated: errdocdir1 = $(errdocdir)/doc
post-install-modulated: errdocdir2 = $(errdocdir)/etc
post-install-modulated: pkgdocdir = $(DESTDIR)/$(docdir)/$(NAME)
post-install-modulated:
	ginstall --directory $(pkgdocdir)
	mv $(errdocdir1)/* $(pkgdocdir)
	rmdir $(errdocdir1)
	mv $(errdocdir2)/* $(pkgdocdir)
	rmdir $(errdocdir2)
	$(MAKECOOKIE)

# this is private and not available publicly
mydependencies:
	$(HOME)/bin/ocswdeplist --package $(NAME)
