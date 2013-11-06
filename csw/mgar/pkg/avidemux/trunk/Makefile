# $Id$

NAME	=	avidemux
VERSION	=	2.6.6
GARTYPE	=	v2

DESCRIPTION	=	Video editor designed for simple cutting, filtering and encoding tasks.
define BLURB
  Avidemux is a free video editor designed for simple cutting,
  filtering and encoding tasks. It supports many file types, including
  AVI, DVD compatible MPEG files, MP4 and ASF, using a variety of
  codecs. Tasks can be automated using projects, job queue and
  powerful scripting capabilities.
endef

VENDOR_URL		=	http://fixounet.free.fr/avidemux/index.html
MASTER_SITES	=	$(SF_MIRRORS)
DISTNAME		=	$(NAME)_$(VERSION)
DISTFILES 		=	$(DISTNAME).tar.gz
PATCHFILES		+=	0001-sh-is-not-bash.patch
PATCHFILES		+=	0002-cmake-verbosity-management.patch
PATCHFILES		+=	0003-use-not-as-needed-linker-option.patch
PATCHFILES		+=	0004-fix-processors-cardinality-gathering.patch
PATCHFILES		+=	0005-implement-solaris-crashdump.patch
PATCHFILES		+=	0006-abs-desabiguation.patch
PATCHFILES		+=	0007-abs-desabiguation-2.patch
PATCHFILES		+=	0008-fix-text-relocation-remains-referenced.patch
PATCHFILES		+=	0009-setting-release-build.patch
PATCHFILES		+=	0010-fabs-desambiguation.patch
PATCHFILES		+=	0011-POW10-definition.patch
PATCHFILES		+=	0012-abs-desabiguation-3.patch
PATCHFILES		+=	0013-include-alloca-declaration.patch
PATCHFILES		+=	0014-fix-text-relocation-remains-referenced-2.patch
PATCHFILES		+=	0015-avoid-empty-library.patch
PATCHFILES		+=	0016-avoid-multiple-register-definition.patch
PATCHFILES		+=	0017-abs-desabiguation-4.patch
PATCHFILES		+=	0018-floor-desabiguation.patch
PATCHFILES		+=	0019-fix-linker-script-option.patch
PATCHFILES		+=	0020-fabs-desambiguation-2.patch
PATCHFILES		+=	0021-fix-text-relocation-remains-referenced-3.patch
PATCHFILES		+=	0022-abs-desabiguation-5.patch
PATCHFILES		+=	0023-fix-font-reference.patch

BUILD_DEP_PKGS	+=	CSWcmake
BUILD_DEP_PKGS	+=	CSWgpatch
BUILD_DEP_PKGS	+=	CSWlibfreetype-dev
BUILD_DEP_PKGS	+=	CSWfontconfig-dev
BUILD_DEP_PKGS	+=	CSWggettext-dev
BUILD_DEP_PKGS	+=	CSWqt4-dev
BUILD_DEP_PKGS	+=	CSWlibiconv-dev
BUILD_DEP_PKGS	+=	CSWlibfribidi-dev
BUILD_DEP_PKGS	+=	CSWlibmp3lame-dev
BUILD_DEP_PKGS	+=	CSWlibfaad2
BUILD_DEP_PKGS	+=	CSWlibx264-dev
BUILD_DEP_PKGS	+=	CSWfaac
BUILD_DEP_PKGS	+=	CSWlibsqlite3-dev
BUILD_DEP_PKGS	+=	CSWlibz-dev
BUILD_DEP_PKGS	+=	CSWlibvorbis-dev
BUILD_DEP_PKGS	+=	CSWlibesd0
BUILD_DEP_PKGS	+=	CSWmesa

# SPARC platform is explicitely not supported by the upstream project;
# I'll work on it later to support it (TODO)
#PACKAGING_PLATFORMS	=	solaris10-sparc
PACKAGING_PLATFORMS	+=	solaris10-i386

GARCOMPILER			=	GNU
CONFIGURE_ARGS		=	$(DIRPATHS)
EXTRA_CFLAGS		=	-fPIC -I /usr/X11/include
EXTRA_CXXFLAGS		=	-fPIC -I /usr/X11/include
EXTRA_LDFLAGS		=	-lsocket -lnsl -lxnet -R$(libdir)

CMAKE_ARGS	+=	-DCMAKE_INSTALL_PREFIX=$(prefix)
CMAKE_ARGS	+=	-DCMAKE_C_FLAGS="$(CFLAGS)"
CMAKE_ARGS	+=	-DCMAKE_CXX_FLAGS="$(CXXFLAGS)"
CMAKE_ARGS	+=	-DCMAKE_INCLUDE_PATH="$(includedir)"
CMAKE_ARGS	+=	-DCMAKE_LIBRARY_PATH="$(libdir)"
CMAKE_ARGS	+=	-DCMAKE_BUILD_WITH_INSTALL_RPATH=TRUE
CMAKE_ARGS	+=	-DCMAKE_INSTALL_RPATH=$(libdir)
CMAKE_ARGS	+=	-DCMAKE_VERBOSE_MAKEFILE=ON
CMAKE_ARGS	+=	-DCMAKE_BUILD_TYPE=Release
CMAKE_ARGS	+=	-DCMAKE_EDIT_COMMAND=vim

CONFIGURE_SCRIPTS	=	custom
BUILD_SCRIPTS		=
TEST_SCRIPTS		=
INSTALL_SCRIPTS		=	custom

RUNTIME_DEP_PKGS_CSWavidemux	+=	CSWlibiconv2
RUNTIME_DEP_PKGS_CSWavidemux	+=	CSWlibqtopengl4
RUNTIME_DEP_PKGS_CSWavidemux	+=	CSWlibqtscripttools4
RUNTIME_DEP_PKGS_CSWavidemux	+=	CSWlibfribidi0
RUNTIME_DEP_PKGS_CSWavidemux	+=	CSWlibqtcore4
RUNTIME_DEP_PKGS_CSWavidemux	+=	CSWlibmp3lame0
RUNTIME_DEP_PKGS_CSWavidemux	+=	CSWlibfaad2
RUNTIME_DEP_PKGS_CSWavidemux	+=	CSWlibintl8
RUNTIME_DEP_PKGS_CSWavidemux	+=	CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWavidemux	+=	CSWlibx264-133
RUNTIME_DEP_PKGS_CSWavidemux	+=	CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWavidemux	+=	CSWfaac
RUNTIME_DEP_PKGS_CSWavidemux	+=	CSWlibqtscript4
RUNTIME_DEP_PKGS_CSWavidemux	+=	CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWavidemux	+=	CSWlibz1
RUNTIME_DEP_PKGS_CSWavidemux	+=	CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWavidemux	+=	CSWlibqtgui4
RUNTIME_DEP_PKGS_CSWavidemux	+=	CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWavidemux	+=	CSWlibesd0
RUNTIME_DEP_PKGS_CSWavidemux	+=	CSWlibvorbisenc2
RUNTIME_DEP_PKGS_CSWavidemux	+=	CSWmesa
RUNTIME_DEP_PKGS_CSWavidemux	+=	CSWlibgcc-s1

# these are here because I don't wish to have separate packages for
# all these libraries which are private; however, making them really
# private is a real pain and anyhow they are not in conflict with
# past, present or future ones:

CHECKPKG_OVERRIDES_CSWavidemux	+=	shared-lib-pkgname-mismatch|file=opt/csw/lib/libADM6avcodec.so.54|soname=libADM6avcodec.so.54|pkgname=CSWavidemux|expected=CSWlibadm6avcodec54
CHECKPKG_OVERRIDES_CSWavidemux	+=	shared-lib-pkgname-mismatch|file=opt/csw/lib/libADM6avformat.so.54|soname=libADM6avformat.so.54|pkgname=CSWavidemux|expected=CSWlibadm6avformat54
CHECKPKG_OVERRIDES_CSWavidemux	+=	shared-lib-pkgname-mismatch|file=opt/csw/lib/libADM6avutil.so.52|soname=libADM6avutil.so.52|pkgname=CSWavidemux|expected=CSWlibadm6avutil52
CHECKPKG_OVERRIDES_CSWavidemux	+=	shared-lib-pkgname-mismatch|file=opt/csw/lib/libADM6postproc.so.52|soname=libADM6postproc.so.52|pkgname=CSWavidemux|expected=CSWlibadm6postproc52
CHECKPKG_OVERRIDES_CSWavidemux	+=	shared-lib-pkgname-mismatch|file=opt/csw/lib/libADM6swscale.so.2|soname=libADM6swscale.so.2|pkgname=CSWavidemux|expected=CSWlibadm6swscale2
CHECKPKG_OVERRIDES_CSWavidemux	+=	shared-lib-pkgname-mismatch|file=opt/csw/lib/libADM_UIQT46.so|soname=libADM_UIQT46.so|pkgname=CSWavidemux|expected=CSWlibadm-uiqt46
CHECKPKG_OVERRIDES_CSWavidemux	+=	shared-lib-pkgname-mismatch|file=opt/csw/lib/libADM_UI_Cli6.so|soname=libADM_UI_Cli6.so|pkgname=CSWavidemux|expected=CSWlibadm-ui-cli6
CHECKPKG_OVERRIDES_CSWavidemux	+=	shared-lib-pkgname-mismatch|file=opt/csw/lib/libADM_audioParser6.so|soname=libADM_audioParser6.so|pkgname=CSWavidemux|expected=CSWlibadm-audioparser6
CHECKPKG_OVERRIDES_CSWavidemux	+=	shared-lib-pkgname-mismatch|file=opt/csw/lib/libADM_core6.so|soname=libADM_core6.so|pkgname=CSWavidemux|expected=CSWlibadm-core6
CHECKPKG_OVERRIDES_CSWavidemux	+=	shared-lib-pkgname-mismatch|file=opt/csw/lib/libADM_coreAudio6.so|soname=libADM_coreAudio6.so|pkgname=CSWavidemux|expected=CSWlibadm-coreaudio6
CHECKPKG_OVERRIDES_CSWavidemux	+=	shared-lib-pkgname-mismatch|file=opt/csw/lib/libADM_coreAudioDevice6.so|soname=libADM_coreAudioDevice6.so|pkgname=CSWavidemux|expected=CSWlibadm-coreaudiodevice6
CHECKPKG_OVERRIDES_CSWavidemux	+=	shared-lib-pkgname-mismatch|file=opt/csw/lib/libADM_coreAudioEncoder6.so|soname=libADM_coreAudioEncoder6.so|pkgname=CSWavidemux|expected=CSWlibadm-coreaudioencoder6
CHECKPKG_OVERRIDES_CSWavidemux	+=	shared-lib-pkgname-mismatch|file=opt/csw/lib/libADM_coreAudioFilterAPI6.so|soname=libADM_coreAudioFilterAPI6.so|pkgname=CSWavidemux|expected=CSWlibadm-coreaudiofilterapi6
CHECKPKG_OVERRIDES_CSWavidemux	+=	shared-lib-pkgname-mismatch|file=opt/csw/lib/libADM_coreDemuxer6.so|soname=libADM_coreDemuxer6.so|pkgname=CSWavidemux|expected=CSWlibadm-coredemuxer6
CHECKPKG_OVERRIDES_CSWavidemux	+=	shared-lib-pkgname-mismatch|file=opt/csw/lib/libADM_coreDemuxerMpeg6.so|soname=libADM_coreDemuxerMpeg6.so|pkgname=CSWavidemux|expected=CSWlibadm-coredemuxermpeg6
CHECKPKG_OVERRIDES_CSWavidemux	+=	shared-lib-pkgname-mismatch|file=opt/csw/lib/libADM_coreImage6.so|soname=libADM_coreImage6.so|pkgname=CSWavidemux|expected=CSWlibadm-coreimage6
CHECKPKG_OVERRIDES_CSWavidemux	+=	shared-lib-pkgname-mismatch|file=opt/csw/lib/libADM_coreImageLoader6.so|soname=libADM_coreImageLoader6.so|pkgname=CSWavidemux|expected=CSWlibadm-coreimageloader6
CHECKPKG_OVERRIDES_CSWavidemux	+=	shared-lib-pkgname-mismatch|file=opt/csw/lib/libADM_coreJobs.so|soname=libADM_coreJobs.so|pkgname=CSWavidemux|expected=CSWlibadm-corejobs
CHECKPKG_OVERRIDES_CSWavidemux	+=	shared-lib-pkgname-mismatch|file=opt/csw/lib/libADM_coreMuxer6.so|soname=libADM_coreMuxer6.so|pkgname=CSWavidemux|expected=CSWlibadm-coremuxer6
CHECKPKG_OVERRIDES_CSWavidemux	+=	shared-lib-pkgname-mismatch|file=opt/csw/lib/libADM_coreScript.so|soname=libADM_coreScript.so|pkgname=CSWavidemux|expected=CSWlibadm-corescript
CHECKPKG_OVERRIDES_CSWavidemux	+=	shared-lib-pkgname-mismatch|file=opt/csw/lib/libADM_coreSocket6.so|soname=libADM_coreSocket6.so|pkgname=CSWavidemux|expected=CSWlibadm-coresocket6
CHECKPKG_OVERRIDES_CSWavidemux	+=	shared-lib-pkgname-mismatch|file=opt/csw/lib/libADM_coreSqlLight3.so|soname=libADM_coreSqlLight3.so|pkgname=CSWavidemux|expected=CSWlibadm-coresqllight3
CHECKPKG_OVERRIDES_CSWavidemux	+=	shared-lib-pkgname-mismatch|file=opt/csw/lib/libADM_coreUI6.so|soname=libADM_coreUI6.so|pkgname=CSWavidemux|expected=CSWlibadm-coreui6
CHECKPKG_OVERRIDES_CSWavidemux	+=	shared-lib-pkgname-mismatch|file=opt/csw/lib/libADM_coreUtils6.so|soname=libADM_coreUtils6.so|pkgname=CSWavidemux|expected=CSWlibadm-coreutils6
CHECKPKG_OVERRIDES_CSWavidemux	+=	shared-lib-pkgname-mismatch|file=opt/csw/lib/libADM_coreVDPAU6.so|soname=libADM_coreVDPAU6.so|pkgname=CSWavidemux|expected=CSWlibadm-corevdpau6
CHECKPKG_OVERRIDES_CSWavidemux	+=	shared-lib-pkgname-mismatch|file=opt/csw/lib/libADM_coreVideoCodec6.so|soname=libADM_coreVideoCodec6.so|pkgname=CSWavidemux|expected=CSWlibadm-corevideocodec6
CHECKPKG_OVERRIDES_CSWavidemux	+=	shared-lib-pkgname-mismatch|file=opt/csw/lib/libADM_coreVideoEncoder6.so|soname=libADM_coreVideoEncoder6.so|pkgname=CSWavidemux|expected=CSWlibadm-corevideoencoder6
CHECKPKG_OVERRIDES_CSWavidemux	+=	shared-lib-pkgname-mismatch|file=opt/csw/lib/libADM_coreVideoFilter6.so|soname=libADM_coreVideoFilter6.so|pkgname=CSWavidemux|expected=CSWlibadm-corevideofilter6
CHECKPKG_OVERRIDES_CSWavidemux	+=	shared-lib-pkgname-mismatch|file=opt/csw/lib/libADM_render6_cli.so|soname=libADM_render6_cli.so|pkgname=CSWavidemux|expected=CSWlibadm-render6cli
CHECKPKG_OVERRIDES_CSWavidemux	+=	shared-lib-pkgname-mismatch|file=opt/csw/lib/libADM_render6_qt4.so|soname=libADM_render6_qt4.so|pkgname=CSWavidemux|expected=CSWlibadm-render6qt4
CHECKPKG_OVERRIDES_CSWavidemux	+=	soname-equals-filename|file=/opt/csw/lib/libADM_UIQT46.so
CHECKPKG_OVERRIDES_CSWavidemux	+=	soname-equals-filename|file=/opt/csw/lib/libADM_UI_Cli6.so
CHECKPKG_OVERRIDES_CSWavidemux	+=	soname-equals-filename|file=/opt/csw/lib/libADM_audioParser6.so
CHECKPKG_OVERRIDES_CSWavidemux	+=	soname-equals-filename|file=/opt/csw/lib/libADM_core6.so
CHECKPKG_OVERRIDES_CSWavidemux	+=	soname-equals-filename|file=/opt/csw/lib/libADM_coreAudio6.so
CHECKPKG_OVERRIDES_CSWavidemux	+=	soname-equals-filename|file=/opt/csw/lib/libADM_coreAudioDevice6.so
CHECKPKG_OVERRIDES_CSWavidemux	+=	soname-equals-filename|file=/opt/csw/lib/libADM_coreAudioEncoder6.so
CHECKPKG_OVERRIDES_CSWavidemux	+=	soname-equals-filename|file=/opt/csw/lib/libADM_coreAudioFilterAPI6.so
CHECKPKG_OVERRIDES_CSWavidemux	+=	soname-equals-filename|file=/opt/csw/lib/libADM_coreDemuxer6.so
CHECKPKG_OVERRIDES_CSWavidemux	+=	soname-equals-filename|file=/opt/csw/lib/libADM_coreDemuxerMpeg6.so
CHECKPKG_OVERRIDES_CSWavidemux	+=	soname-equals-filename|file=/opt/csw/lib/libADM_coreImage6.so
CHECKPKG_OVERRIDES_CSWavidemux	+=	soname-equals-filename|file=/opt/csw/lib/libADM_coreImageLoader6.so
CHECKPKG_OVERRIDES_CSWavidemux	+=	soname-equals-filename|file=/opt/csw/lib/libADM_coreJobs.so
CHECKPKG_OVERRIDES_CSWavidemux	+=	soname-equals-filename|file=/opt/csw/lib/libADM_coreMuxer6.so
CHECKPKG_OVERRIDES_CSWavidemux	+=	soname-equals-filename|file=/opt/csw/lib/libADM_coreScript.so
CHECKPKG_OVERRIDES_CSWavidemux	+=	soname-equals-filename|file=/opt/csw/lib/libADM_coreSocket6.so
CHECKPKG_OVERRIDES_CSWavidemux	+=	soname-equals-filename|file=/opt/csw/lib/libADM_coreSqlLight3.so
CHECKPKG_OVERRIDES_CSWavidemux	+=	soname-equals-filename|file=/opt/csw/lib/libADM_coreUI6.so
CHECKPKG_OVERRIDES_CSWavidemux	+=	soname-equals-filename|file=/opt/csw/lib/libADM_coreUtils6.so
CHECKPKG_OVERRIDES_CSWavidemux	+=	soname-equals-filename|file=/opt/csw/lib/libADM_coreVDPAU6.so
CHECKPKG_OVERRIDES_CSWavidemux	+=	soname-equals-filename|file=/opt/csw/lib/libADM_coreVideoCodec6.so
CHECKPKG_OVERRIDES_CSWavidemux	+=	soname-equals-filename|file=/opt/csw/lib/libADM_coreVideoEncoder6.so
CHECKPKG_OVERRIDES_CSWavidemux	+=	soname-equals-filename|file=/opt/csw/lib/libADM_coreVideoFilter6.so
CHECKPKG_OVERRIDES_CSWavidemux	+=	soname-equals-filename|file=/opt/csw/lib/libADM_render6_cli.so
CHECKPKG_OVERRIDES_CSWavidemux	+=	soname-equals-filename|file=/opt/csw/lib/libADM_render6_qt4.so

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

# these targets are an adaptation of the bootStrap.sh provided by
# the project; beside the byzantine content of the script, this
# adaptation makes it easier to adapt to gar.


TOP				=	$(PWD)/$(WORKSRC)
FAKEROOT_DIR	=	$(PWD)/$(WORKSRC)/install
BUILDER			=	Unix Makefiles
CMAKE_ARGS		+=	-DFAKEROOT=$(FAKEROOT_DIR)
CMAKE_ARGS		+=	-DAVIDEMUX_SOURCE_DIR=$(TOP)
#CMAKE_ARGS		+=	--trace

ADM				=	$(COOKIEROOTDIR)/$(MODULATION)/

# configuration is also build...
configure-custom:	\
					$(ADM)core \
					$(ADM)qt4 \
					$(ADM)cli \
					$(ADM)plugins
	@$(MAKECOOKIE)

define configureRule =
	$(info configure rule for '$(1)')
	cd $(WORKSRC) && rm -rf $(BUILDDIR) && \
	mkdir -p $(BUILDDIR)
	cd $(WORKSRC)/$(BUILDDIR) && \
	/usr/bin/env -i \
		$(CONFIGURE_ENV) \
		cmake \
		$(CMAKE_ARGS) \
		-G "$(BUILDER)" \
		$(1)
	: $@ done
endef

define buildRule =
	cd $(WORKSRC)/$(BUILDDIR) && \
	/usr/bin/env -i \
		$(CONFIGURE_ENV) \
		$(MAKE)
	: $@ done
endef

define installRule =
	cd $(WORKSRC)/$(BUILDDIR) && \
	/usr/bin/env -i \
		$(CONFIGURE_ENV) \
		$(MAKE) install DESTDIR=$(FAKEROOT_DIR)
	: $@ done
endef

coreBuildDirectory	=	buildCore

$(ADM)core: BUILDDIR	=	$(coreBuildDirectory)
$(ADM)core:	\
		$(ADM)fake-configure-core \
		$(ADM)fake-build-core \
		$(ADM)fake-install-core
	: $@ done
	@$(MAKECOOKIE)

$(ADM)fake-configure-core: BUILDDIR	=	$(coreBuildDirectory)
$(ADM)fake-configure-core:
	$(call configureRule,../avidemux_core)
	@$(MAKECOOKIE)

$(ADM)fake-build-core: BUILDDIR	=	$(coreBuildDirectory)
$(ADM)fake-build-core:
	gsed --in-place --regexp-extended --expression 's;^#![[:space:]]*/bin/sh[[:space:]]*;#!/usr/bin/env bash;' $(WORKSRC)/$(BUILDDIR)/ffmpeg/source/version.sh
	gsed --in-place --regexp-extended --expression 's;-Wl,-rpath-link=.*$$;;' $(WORKSRC)/$(BUILDDIR)/ffmpeg/build/config.mak
	$(buildRule)
	@$(MAKECOOKIE)

$(ADM)fake-install-core: BUILDDIR	=	$(coreBuildDirectory)
$(ADM)fake-install-core:
	$(installRule)
	@$(MAKECOOKIE)

qt4BuildDirectory	=	buildQt4

$(ADM)qt4: BUILDDIR	=	$(qt4BuildDirectory)
$(ADM)qt4:	\
		$(ADM)fake-configure-qt4 \
		$(ADM)fake-build-qt4 \
		$(ADM)fake-install-qt4
	: $@ done
	@$(MAKECOOKIE)

$(ADM)fake-configure-qt4: BUILDDIR	=	$(qt4BuildDirectory)
$(ADM)fake-configure-qt4:
	$(call configureRule,../avidemux/qt4)
	@$(MAKECOOKIE)

$(ADM)fake-build-qt4: BUILDDIR	=	$(qt4BuildDirectory)
$(ADM)fake-build-qt4:
	$(buildRule)
	@$(MAKECOOKIE)

$(ADM)fake-install-qt4: BUILDDIR	=	$(qt4BuildDirectory)
$(ADM)fake-install-qt4:
	$(installRule)
	@$(MAKECOOKIE)

cliBuildDirectory	=	buildCli

$(ADM)cli: BUILDDIR	=	$(cliBuildDirectory)
$(ADM)cli:	\
		$(ADM)fake-configure-cli \
		$(ADM)fake-build-cli \
		$(ADM)fake-install-cli
	: $@ done
	@$(MAKECOOKIE)

$(ADM)fake-configure-cli: BUILDDIR	=	$(cliBuildDirectory)
$(ADM)fake-configure-cli:
	$(call configureRule,../avidemux/cli)
	: $@ done
	@$(MAKECOOKIE)

$(ADM)fake-build-cli: BUILDDIR	=	$(cliBuildDirectory)
$(ADM)fake-build-cli:
	$(buildRule)
	@$(MAKECOOKIE)

$(ADM)fake-install-cli: BUILDDIR	=	$(cliBuildDirectory)
$(ADM)fake-install-cli:
	$(installRule)
	@$(MAKECOOKIE)

# requires GTK 3 which is not available in our offering
gtkBuildDirectory	=	buildGtk

$(ADM)gtk: BUILDDIR	=	$(gtkBuildDirectory)
$(ADM)gtk:	\
		$(ADM)fake-configure-gtk \
		$(ADM)fake-build-gtk \
		$(ADM)fake-install-gtk
	: $@ done
	@$(MAKECOOKIE)

$(ADM)fake-configure-gtk: BUILDDIR	=	$(gtkBuildDirectory)
$(ADM)fake-configure-gtk:
	$(call configureRule,../avidemux/gtk)
	@$(MAKECOOKIE)

$(ADM)fake-build-gtk: BUILDDIR	=	$(gtkBuildDirectory)
$(ADM)fake-build-gtk:
	$(buildRule)
	@$(MAKECOOKIE)

$(ADM)fake-install-gtk: BUILDDIR	=	$(gtkBuildDirectory)
$(ADM)fake-install-gtk:
	$(installRule)
	@$(MAKECOOKIE)

$(ADM)plugins:	\
			$(ADM)plugin-common \
			$(ADM)plugin-qt4 \
			$(ADM)plugin-cli \
			$(ADM)plugin-settings
	: $@ done
	@$(MAKECOOKIE)

plugin-commonBuildDirectory	=	buildPluginsCommon

$(ADM)plugin-common: BUILDDIR	=	$(plugin-commonBuildDirectory)
$(ADM)plugin-common:	\
				$(ADM)fake-configure-plugin-common \
				$(ADM)fake-build-plugin-common \
				$(ADM)fake-install-plugin-common
	: $@ done
	@$(MAKECOOKIE)

$(ADM)fake-configure-plugin-common: BUILDDIR	=	$(plugin-commonBuildDirectory)
$(ADM)fake-configure-plugin-common: CMAKE_ARGS	+=	-DPLUGIN_UI=COMMON
$(ADM)fake-configure-plugin-common:
	$(call configureRule,../avidemux_plugins)
	@$(MAKECOOKIE)

$(ADM)fake-build-plugin-common: BUILDDIR	=	$(plugin-commonBuildDirectory)
$(ADM)fake-build-plugin-common:
	$(buildRule)
	@$(MAKECOOKIE)

$(ADM)fake-install-plugin-common: BUILDDIR	=	$(plugin-commonBuildDirectory)
$(ADM)fake-install-plugin-common:
	$(installRule)
	@$(MAKECOOKIE)

plugin-qt4BuildDirectory	=	buildPluginsQt4

$(ADM)plugin-qt4: BUILDDIR	=	$(plugin-qt4BuildDirectory)
$(ADM)plugin-qt4:	\
				$(ADM)fake-configure-plugin-qt4 \
				$(ADM)fake-build-plugin-qt4 \
				$(ADM)fake-install-plugin-qt4
	: $@ done
	@$(MAKECOOKIE)

$(ADM)fake-configure-plugin-qt4: BUILDDIR	=	$(plugin-qt4BuildDirectory)
$(ADM)fake-configure-plugin-qt4: CMAKE_ARGS	+=	-DPLUGIN_UI=QT4
$(ADM)fake-configure-plugin-qt4:
	$(call configureRule,../avidemux_plugins)
	@$(MAKECOOKIE)

$(ADM)fake-build-plugin-qt4: BUILDDIR	=	$(plugin-qt4BuildDirectory)
$(ADM)fake-build-plugin-qt4:
	$(buildRule)
	@$(MAKECOOKIE)

$(ADM)fake-install-plugin-qt4: BUILDDIR	=	$(plugin-qt4BuildDirectory)
$(ADM)fake-install-plugin-qt4:
	$(installRule)
	@$(MAKECOOKIE)

# requires GTK 3 which is not available in our offering
plugin-gtkBuildDirectory	=	buildPluginsGtk

$(ADM)plugin-gtk: BUILDDIR	=	$(plugin-gtkBuildDirectory)
$(ADM)plugin-gtk:	\
				$(ADM)fake-configure-plugin-gtk \
				$(ADM)fake-build-plugin-gtk \
				$(ADM)fake-install-plugin-gtk
	: $@ done
	@$(MAKECOOKIE)

$(ADM)fake-configure-plugin-gtk: BUILDDIR	=	$(plugin-gtkBuildDirectory)
$(ADM)fake-configure-plugin-gtk: CMAKE_ARGS	+=	-DPLUGIN_UI=GTK
$(ADM)fake-configure-plugin-gtk:
	$(call configureRule,../avidemux_plugins)
	@$(MAKECOOKIE)

$(ADM)fake-build-plugin-gtk: BUILDDIR	=	$(plugin-gtkBuildDirectory)
$(ADM)fake-build-plugin-gtk:
	$(buildRule)
	@$(MAKECOOKIE)

$(ADM)fake-install-plugin-gtk: BUILDDIR	=	$(plugin-gtkBuildDirectory)
$(ADM)fake-install-plugin-gtk:
	$(installRule)
	@$(MAKECOOKIE)

plugin-cliBuildDirectory	=	buildPluginsCli

$(ADM)plugin-cli: BUILDDIR	=	$(plugin-cliBuildDirectory)
$(ADM)plugin-cli:	\
				$(ADM)fake-configure-plugin-cli \
				$(ADM)fake-build-plugin-cli \
				$(ADM)fake-install-plugin-cli
	: $@ done
	@$(MAKECOOKIE)

$(ADM)fake-configure-plugin-cli: BUILDDIR	=	$(plugin-cliBuildDirectory)
$(ADM)fake-configure-plugin-cli: CMAKE_ARGS	+=	-DPLUGIN_UI=CLI
$(ADM)fake-configure-plugin-cli:
	$(call configureRule,../avidemux_plugins)
	@$(MAKECOOKIE)

$(ADM)fake-build-plugin-cli: BUILDDIR	=	$(plugin-cliBuildDirectory)
$(ADM)fake-build-plugin-cli:
	$(buildRule)
	@$(MAKECOOKIE)

$(ADM)fake-install-plugin-cli: BUILDDIR	=	$(plugin-cliBuildDirectory)
$(ADM)fake-install-plugin-cli:
	$(installRule)
	@$(MAKECOOKIE)

plugin-settingsBuildDirectory	=	buildPluginsSettings

$(ADM)plugin-settings: BUILDDIR	=	$(plugin-settingsBuildDirectory)
$(ADM)plugin-settings:	\
				$(ADM)fake-configure-plugin-settings \
				$(ADM)fake-build-plugin-settings \
				$(ADM)fake-install-plugin-settings
	: $@ done
	@$(MAKECOOKIE)

$(ADM)fake-configure-plugin-settings: BUILDDIR	=	$(plugin-settingsBuildDirectory)
$(ADM)fake-configure-plugin-settings: CMAKE_ARGS	+=	-DPLUGIN_UI=SETTINGS
$(ADM)fake-configure-plugin-settings:
	$(call configureRule,../avidemux_plugins)
	@$(MAKECOOKIE)

$(ADM)fake-build-plugin-settings: BUILDDIR	=	$(plugin-settingsBuildDirectory)
$(ADM)fake-build-plugin-settings:
	$(buildRule)
	@$(MAKECOOKIE)

$(ADM)fake-install-plugin-settings: BUILDDIR	=	$(plugin-settingsBuildDirectory)
$(ADM)fake-install-plugin-settings:
	$(installRule)
	@$(MAKECOOKIE)

install-custom:
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)
	gtar --directory=$(FAKEROOT_DIR) --create --file=- --exclude=opt/csw/include --exclude=opt/csw/share/ADM6_addons . | \
	gtar --directory=$(DESTDIR) --extract --file=-
	@$(MAKECOOKIE)

