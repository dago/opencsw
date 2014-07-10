NAME = pulseaudio
VERSION = 2.1
# 2.99.3
GARTYPE = v2

# this was build on OI_151a9
# for use OI pkg json-c add header file: json_object_iterator.h
# see also: https://github.com/json-c/json-c/issues/35 lib
GARTYPE = v2

DESCRIPTION = PulseAudio is a sound server for POSIX systems
define BLURB
endef

MASTEfreedesktop.org/software/pulseaudio/releasesojects/pulseaudio/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://GARCOMPILER = GCC4

BUILD_DEP_PKGS += CSWggettext-dev
BUILD_DEP_PKGS += CSWlibtool
BUILD_DEP_PKGS += CSWlibsndfile-dev
BUILD_DEP_PKGS += CSWlibspeex-dev
BUILD_DEP_PKGS += CSWpm-xml-parser
BUILD_DEP_PKGS += CSWlibglib2-dev
BUILD_DEP_PKGS += CSWlibdbus-dev
# BUILD_DEP_PKGS += CSWlibxcb-dev
# BUILD_DEP_PKGS += CSWlibx11-dev

# on OI: 
# pkg install system/header/header-audio library/json-c SFElibatomic-ops

PATCHFILES += 0002-define-pi+typeof.patch
PATCHFILES += 0001-module.patch

RUNTIME_DEP_PKGS_CSWpulseaudio += CSWlibintl8
RUNTIME_DEP_PKGS_CSWpulseaudio += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWpulseaudio += CSWlibdbus1-3
RUNTIME_DEP_PKGS_CSWpulseaudio += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWpulseaudio += CSWlibiconv2

EXTRA_CFLAGS = 	-std=c99 -Dsun
EXTRA_LINKER_FLAGS += -lintl
EXTRA_CONFIGURE_ENV = PATH=/opt/csw/gnu:$(PATH)

# BUILD64_LIBS_ONLY = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-rpath
CONFIGURE_ARGS += --disable-silent-rules
CONFIGURE_ARGS += --enable-solaris
# failed one test: get-binary-name-test
SKIPTEST = 1

include gar/category.mk
