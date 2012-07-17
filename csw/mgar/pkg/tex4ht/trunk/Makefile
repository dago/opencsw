# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = tex4ht
VERSION = 1.0.2009_06_11_1038
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = LaTeX and TeX for Hypertext (HTML)
define BLURB
  TeX4ht is a highly configurable TeX-based authoring system dedicated mainly
  to produce hypertext. It interacts with TeX-based applications through style
  files and postprocessors, leaving the processing of the source files to the
  native TeX compiler. Consequently, TeX4ht can handle the features of
  TeX-based systems in general, and of the LaTeX and AMS style files in
  particular.

  Pre-tailored configurations are offered for different output formats,
  including (X)HTML, MathML, OpenDocument, and DocBook. 
endef

MASTER_SITES		=	http://tug.org/applications/tex4ht/
DISTFILES			=	$(NAME).zip
DISTFILES			+=	COPYING
DISTFILES			+=	tex4ht.1

PACKAGING_PLATFORMS	=	solaris10-sparc
PACKAGING_PLATFORMS	+=	solaris10-i386

BUILD_DEP_PKGS		+=	CSWtetex

GARCOMPILER			=	GNU

CONFIGURE_SCRIPTS	=
BUILD_SCRIPTS		=	custom
TEST_SCRIPTS		=
INSTALL_SCRIPTS		=	custom

PACKAGES								+=	CSWtex4ht-common
CATALOGNAME_CSWtex4ht-common			=	tex4ht_common
SPKG_DESC_CSWtex4ht-common				+=	$(DESCRIPTION), architecture neutral components
ARCHALL_CSWtex4ht-common				=	1
OBSOLETED_BY_CSWtex4ht-common			=	CSWtex4htcommon
CATALOGNAME_CSWtex4htcommon				=	tex4ht_common_stub
RUNTIME_DEP_PKGS_CSWtex4ht-common		+=	CSWimagemagick
CHECKPKG_OVERRIDES_CSWtex4ht-common		+=	surplus-dependency|CSWimagemagick
RUNTIME_DEP_PKGS_CSWtex4ht-common		+=	CSWnetpbm
CHECKPKG_OVERRIDES_CSWtex4ht-common		+=	surplus-dependency|CSWnetpbm
RUNTIME_DEP_PKGS_CSWtex4ht-common		+=	CSWperl
CHECKPKG_OVERRIDES_CSWtex4ht-common		+=	surplus-dependency|CSWperl
RUNTIME_DEP_PKGS_CSWtex4ht-common		+=	CSWpstoedit
CHECKPKG_OVERRIDES_CSWtex4ht-common		+=	surplus-dependency|CSWpstoedit
RUNTIME_DEP_PKGS_CSWtex4ht-common		+=	CSWtetex
CHECKPKG_OVERRIDES_CSWtex4ht-common		+=	surplus-dependency|CSWtetex

PACKAGES								+=	CSWtex4ht
CATALOGNAME_CSWtex4ht					=	tex4ht
SPKG_DESC_CSWtex4ht						+=	$(DESCRIPTION)
PKGFILES_CSWtex4ht						+=	/opt/csw/bin/tex4ht
PKGFILES_CSWtex4ht						+=	/opt/csw/bin/t4ht
RUNTIME_DEP_PKGS						+=	CSWtex4ht-common
CHECKPKG_OVERRIDES_CSWtex4ht			+=	surplus-dependency|CSWtex4ht-common

include gar/category.mk

genBins		=	\
				$(WORKSRC)/src/tex4ht \
				$(WORKSRC)/src/t4ht

envBase		=	$(NAME).env
envFile		=	$(WORKSRC)/$(envBase)
origEnvFile	=	$(WORKSRC)/texmf/$(NAME)/base/unix/$(envBase)

build-custom:	\
				$(genBins) \
				$(envFile)
	$(MAKECOOKIE)

confdir		=	$(sysconfdir)
sharedir	=	$(sharedstatedir)
libexecdir	=	$(sharedir)/$(NAME)
docdir		=	$(sharedir)/doc/$(NAME)
texdir		=	$(texmflocaldir)
libdir		=	$(texdir)/$(NAME)

LDFLAGS		+=	-lkpathsea

$(WORKSRC)/src/tex4ht:	\
						$(WORKSRC)/src/tex4ht.c
	$(CC) $(CFLAGS) -DENVFILE='"$(confdir)/tex4ht.env"' -DKPATHSEA -DHAVE_DIRENT_H $^ -o $@ $(LDFLAGS)

$(WORKSRC)/src/t4ht:	\
						$(WORKSRC)/src/t4ht.c
	$(CC) $(CFLAGS) -DENVFILE='"$(confdir)/tex4ht.env"' -DKPATHSEA -DHAVE_DIRENT_H $^ -o $@ $(LDFLAGS)

$(envFile):	\
			$(origEnvFile)
	gsed	\
		-e 's:^tpath/tex/texmf/fonts/tfm/!$$:t$(sharedir)/texmf-dist/fonts/tfm/!:' \
		-e 's:^i~/tex4ht.dir/texmf/tex4ht:i$(libdir):' \
		$^ > $@

install-custom: pkgmandir = $(mandir)/man1
install-custom:
	ginstall --directory $(DESTDIR)/$(bindir)
	ginstall $(genBins) $(DESTDIR)/$(bindir)
	ginstall	\
					$(WORKSRC)/bin/ht/unix/htlatex \
					$(WORKSRC)/bin/ht/unix/httex \
					$(WORKSRC)/bin/unix/ht \
					$(WORKSRC)/bin/unix/httexi \
					$(WORKSRC)/bin/unix/mk4ht \
					$(DESTDIR)/$(bindir)
	ginstall --directory $(DESTDIR)/$(confdir)
	ginstall $(envFile) $(DESTDIR)/$(confdir)
	ginstall --directory $(DESTDIR)/$(libexecdir)
	ginstall $(WORKSRC)/bin/unix/mk4ht $(DESTDIR)/$(libexecdir)
	ginstall $(WORKSRC)/texmf/tex4ht/bin/tex4ht.jar $(DESTDIR)/$(libexecdir)
	find $(WORKSRC)/bin/ht/unix -type f -exec ginstall {} $(DESTDIR)/$(libexecdir) \;
	ginstall --directory $(DESTDIR)/$(libdir)
	gtar	\
				--directory $(WORKSRC)/texmf/tex4ht \
				--create \
				--file=- \
				ht-fonts \
				xtpipes \
				| \
	gtar	\
				--directory $(DESTDIR)/$(libdir) \
				--extract \
				--file=-
	gtar	\
				--directory $(WORKSRC)/texmf \
				--create \
				--file=- \
				tex \
				| \
	gtar	\
				--directory $(DESTDIR)/$(texdir) \
				--extract \
				--file=-
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(pkgmandir)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(FILEDIR)/tex4ht.1 $(DESTDIR)/$(pkgmandir)
	$(MAKECOOKIE)

# this is private and not available publicly
mydependencies:
	for package in $(PACKAGES); do echo '___' $${package}; $(HOME)/bin/ocswdeplist --depth 1 --dependencies --packaging --csw --prototype $(HOME)/opencsw/$(NAME)/trunk/work/build-global/$${package}.prototype --target $(HOME)/opencsw/$(NAME)/trunk/work/pkgroot; done
