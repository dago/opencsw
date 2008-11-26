##Mplayer and $ISAEXEC makefile example###
#
# This makefile has a lot of notes and extra information in it, as I've been
# using it as documentation while working away at this project. It will be 
# tidied up before I submit it for official review.

GARNAME = MPlayer
GARVERSION = 1.0rc2
SPKG_REVSTAMP = ,REV=$(shell date '+%Y.%m.%d').rc2
CATEGORIES = apps

DESCRIPTION = MPlayer is a movie player which runs on many systems
define BLURB
MPlayer is a movie player which runs on many systems (see the documentation). It plays most MPEG/VOB, AVI, Ogg/OGM, VIVO, ASF/WMA/WMV, QT/MOV/MP4, RealMedia, Matroska, NUT, NuppelVideo, FLI, YUV4MPEG, FILM, RoQ, PVA files, supported by many native, XAnim, and Win32 DLL codecs. You can watch VideoCD, SVCD, DVD, 3ivx, DivX 3/4/5 and even WMV movies..
endef

MASTER_SITES = http://www3.mplayerhq.hu/MPlayer/releases/ http://www3.mplayerhq.hu/MPlayer/skins/

GARCOMPILER = GNU
GNU_CC_HOME = /opt/csw/gcc4

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += Blue-1.7.tar.bz2
DISTFILES += $(call admfiles,CSWmplayer,depend)

PATCHFILES = fix-configure.diff
PATCHFILES += fix-libavcodec-gcc-bug.diff
PATCHFILES += fix-manpage-macros.diff
PATCHFILES += sparc-v8-novis.diff
#Sol8 only PATCHFILES += stdint-wrapper.diff

CONFIGURE_ARGS  = --prefix=/opt/csw
CONFIGURE_ARGS += --with-extraincdir=/usr/X11/include
CONFIGURE_ARGS += --with-extraincdir=/usr/include
CONFIGURE_ARGS += --mandir=$(BUILD_PREFIX)/share/man
CONFIGURE_ARGS += --enable-gui
CONFIGURE_ARGS += --disable-win32dll
CONFIGURE_ARGS += --disable-libvorbis #Having trouble compiling it
#CONFIGURE_ARGS += --disable-libcdio
#CONFIGURE_ARGS += --disable-iconv #Solaris libc has iconv already

# Mplayer sparc-specific patches
# Openal for sparc is broken
# OpenGL isn't working on osiris
ifeq ($(shell uname -p),sparc)
CONFIGURE_ARGS += --disable-openal 
CONFIGURE_ARGS += --disable-gl
endif

###Framework for an $ISAEXEC optimised build###
# To allow for the same build to run multiple times without each version
# clobbering the non-unique work/cookie folders each time, we append the
# target $ISA to each foldername.
#
# 1) gmake optbuild: runs the standard gar framework through the optbuild for 
#	loop. This loop allows for each of the targets in $ISATARGET to be built
#	using the appropriate compiler flags for optimisation.
#	The optbuild target takes us to the end of the install step.
#	When all the building is done, we're going to only want the one package,
#	(not N versions). All the resultant binaries from each $ISATARGET are 
#	merged into the $BASEISA $DESTDIR by the merge-opt-bins target.
#	It's this $BASEISA that will be used for the final resultant ISAEXEC pkg
#
#	Gar currently merges and overlaps the install & package targets.
#	We want the install phase to be run in a for loop, but the package
#	phase to run only once (on our $BASEISA), so I've had to explictly
#	split the phases.
#
# 2) gmake only-package: Runs the standard packing steps on the $BASEISA	
#	install dir ($DESTDIR), however I've run into a problem with the
#	mkpackage perl script's handling of the prototype file; we need it to
#	merge both our standard directory structure, and also the added isaexec
#	hardlinks.
#	The isa-post-package step adds the appropriate lines to the prototype
#	however mkpackage will then either 1) overwrite it anyway, or 
#	2) in merge mode, it will take our 2 isaexec lines, and only append 
#	those 2 lines (ignoring all the standard files in our package).
#
#	My sneaky workaround for this is to add the extra lines in the 
# 	isa-post-package target, followed by re-running the package-create step.
#	The package-create target the prototype already contains a full 
#	file/dir layout and our isaexec hardlink(s), so mkpackage simply
#	merges(appends)	the key isaexec links.
#	In fact, the admfiles are actually already there (from the first trip
#	through package-create), but mkpackage is smart enough to remove the
#	duplicate lines! :)

### Makefile target order ###
# 1) "gmake optbuild" runs the following gar steps on each of the $ISALIST
#	build (and all of it's dependanies - extract/patch/etc etc)
#	pre-install (calls timestamp, skins, fonts, and merge-opt-bins)
#	 ===> timestamp (creates timestamp to track the new files for packaging)
#	 ===> skins (copies the Mplayer skins into the install dirs)
#	 ===> fonts (creates a symlink for the Mplayer OSD font)
#	 ===> merge-opt-bins (Moves the optimised $ISAEXEC_BINS from $ISALIST
#			into the appropriate $ISAEXEC_DIR within the $BASEISA)
#	install (standard install target)
#	post-install (calls strip/fixconfig)
# The $BASISA $DESTDIR now contain all ISAEXEC'ed bins, in the correct layout,
# reading for packaging.
#
# 2) gmake only-package (which won't run through the optbuild loop) will just
#	act apon the $BASEISA. It will run the following steps:
#	pre-package 	(empty)
#	package-create	(creates the package as per normal)
#	post-package	(Sneakily adds the isaexec symlinks, and reruns package-create)
#	package-check	(Standard target)


# Gar uses the $DESTIMG variable to create these directory names, so we need to
# change that variable to reflect a unique $ISATARGET name.
# $DESTDIR is where the package is installed to prior to packaging. We also 
# need to make this directory name unique for each $ISA.
# $DESTDIR is defined in the core GAR makefile, which hasn't been included yet,
# so I have to set this variable after the main include.

# Disabling for non-isaexec build, it breaks the depend generation path
# DESTIMG=$(GARNAME)-$(ISA)

###Optimisation section###
#
# This gar package builds a plain non-optimised version of Mplayer by default.
# To build the fully optimised $ISAEXEC version use "gmake optbuild"
# 
# $ISATARGETS represents the optimised cpu targets.
# These targets can be used in a couple of ways. We need to feed a desired 
# optimisation target into our compiler, but we also need to create and copy
# the binaries into the `isalist` dir structure for the final install layout.
#
# Unfortunately for GCC at least, these names don't match, and 64-bit is even
# worse.
#
# $BASEISA is used for the base build, and for legacy use with plain "gmake".
# The $BASEISA represents the minimum optimisation level, but it's also used as
# the base (master) template for creating the package. All other $ISATARGET 
# builds will have their binaries and libraries copied into the $BASEISA 
# install dir, prior to final packaging.
#
# In theory, I should be able to just use the first string in $ISATARGET.
# Need to work out if Makefiles support this function.

ifeq ($(shell uname -p),i386)
 ISATARGETS ?= pentium pentium-mmx pentium2
 BASEISA ?= pentium
else
 ISATARGETS ?= v8 ultrasparc ultrasparc3
 BASEISA ?= v8
endif

# Mapping
# Do Makefiles have a concept of a hash table for matching these?
# $ISAEXEC name: | GCC mtune name:
# pentium=pentium
# pentium+mmx=pentium-mmx
# pentium_pro+mmx=pentium2
# 64-bit is athlon=amd64 but I expect -m64 will be what we're after.

#If statement for gcc needed here!
pentium_dir 	= pentium
pentium-mmx_dir = pentium+mmx
pentium2_dir 	= pentium_pro+mmx

#Sparc
v8_dir 	= sparcv8
# ?? 	= sparcv8plus
# ?? 	= sparcv8plus+vis
ultrasparc_dir 	= sparcv9
ultrasparc3_dir	= sparcv9+vis
#v9_dir	= sparcv9+vis2 


ISAEXEC_DIR = $($(ISA)_dir)

# If you just typed gmake, this will build the stardard BASEISA build.
# For a single optimised build use gmake ISA=your-target-here.
# For all optimised versions ($ISAEXEC), use gmake optbuild 
ISA ?= $(BASEISA)

#Which binaries do you want to use $ISAEXEC for?
# Note: These must be the full paths!
ISAEXEC_BINS = opt/csw/bin/mplayer opt/csw/bin/mencoder


# Inclue all standard GAR variables and functionality from here onward:
include gar/category.mk

# See earlier, we needed to set this VAR _after_ the category.mk include
BASE_DESTDIR :=$(DESTDIR)-$(BASEISA)
DESTDIR := $(DESTDIR)-$(ISA)

####Mplayer specific optimisation notes####

# Mplayer uses -mtune, not -march

# Compiler options 
ifeq ($(GARCH),i386)
 CFLAGS = -O2 -pipe -mtune=$(ISA)
else # I.E sparc
CFLAGS = -O2 -pipe -mcpu=$(ISA)
endif

#CPPFLAGS = $(CFLAGS)
#CXXFLAGS = $(CFLAGS)
#ASFLAGS = $(CFLAGS)
#OPTFLAGS = $(CFLAGS)

# Makefile debugging/testing
showvars:
	@echo " CFLAGS: $(CFLAGS)"
	@echo " PATCHFILES: $(PATCHFILES)"

###Fix the standard POST_INSTALL_TARGET Definition##
# By default Gar uses the install: target to install and then create a package.
# The package target simply points at install: (????)
# With this ISAEXEC framework, we actually need to separate these steps out!
#
# By setting the POST_INSTALL_TARGETS to the below, we're stripping off the
# packaging phase of the install: target.
# With the packaging steps striped, make install only installs the package into
# it's $DESTDIR as you would expect.
#
# We save the full unedited definiton of $PACKAGE for later, as we still to need
# to build a package at the end. Actually, no, I just define it manually...
# I've created a full-package: target which runs $(FULL_PACKAGE). This will be the final step

PLAIN_PACKAGE := $(POST_INSTALL_TARGETS)
POST_INSTALL_TARGETS := strip fixconfig

# This is the main target used by this Makefile for creating $ISAEXEC format pkgs.
# This for loop is very important for handling the $DESTDIR var as it applies in
# the post-install steps (I.E the ISA-specific dirs)

optbuild:
	(for TARGET in $(ISATARGETS); do \
	gmake -e ISA=$$TARGET build only-install; done)


# This target is copied from gar.pkg.mk, just with $(POST_INSTALL_TARGETS) stripped
# from the end. This prevents the install target from kicking off the packaging step.
only-install:  $(addprefix dep-$(GARDIR)/,$(INSTALLDEPS)) test $(INSTALL_DIRS) $(PRE_INSTALL_TARGETS) pre-install $(INSTALL_TARGETS) isa-post-install


###Tidy ups and files below
# We need the skins dir copied into the master install dir
# We need the default font copied into the master install dir
# Finally, merge in all the optimised binaries

#Isaexec version
isa-post-install: skins fonts merge-opt-bins

#Standard package version
post-install: skins fonts

#### Skins, Fonts, Codecs and below all need to be run from optbuild to inherit
#	the expanded $(DESTDIR) variable which includes their expanded path
#	In Mplayer's case we don't actually need the skins/fonts in each ISA build
#	but pulling them out of the loop is proving tricky 


skins:
	(mkdir -p $(DESTDIR)$(BUILD_PREFIX)/share/mplayer/skins/default)
	(cp -r $(WORKSRC)/../Blue/* $(DESTDIR)$(BUILD_PREFIX)/share/mplayer/skins/default)

fonts:
	(ln -f -s /usr/openwin/lib/X11/fonts/TrueType/Arial.ttf $(DESTDIR)$(BUILD_PREFIX)/share/mplayer/subfont.ttf)

#Codecs aren't currently being bundled
codecs:
	(mkdir -p $(DESTDIR)$(BUILD_PREFIX)/lib/codecs)
	(cp -r $(WORKSRC)/../all-20061022/* $(DESTDIR)$(BUILD_PREFIX)/share/codecs) 

merge-opt-bins:
	@echo "====> Running merge-opt-bins <===="
	(mkdir -p $(BASE_DESTDIR)$(BUILD_PREFIX)/bin/$(ISAEXEC_DIR))
	(cd $(DESTDIR); if test ! -f $(BASE_DESTDIR)$(BUILD_PREFIX)/bin/$(ISAEXEC_DIR)/* ; then mv $(ISAEXEC_BINS) $(BASE_DESTDIR)$(BUILD_PREFIX)/bin/$(ISAEXEC_DIR); fi )

	

# This sets up the protype file correctly, but you'll have to do the depend manually.
# In Mplayer's case, I have to hard code the filename, as the tarball has it
# as "MPlayer", not "mplayer", so I can't simply use $(GARNAME)
#

#Should be able to use the ISA_BINS var here, maybe a foreach loop?
isa-post-package:
	@echo " ===> Starting Mplayer post-package phase <==="
	@if test ! -f  $(COOKIEDIR)/post-package ; then \
	echo "l none /opt/csw/bin/mplayer=isaexec" >> $(WORKSRC)/../CSWmplayer.prototype; \
	echo "l none /opt/csw/bin/mencoder=isaexec" >> $(WORKSRC)/../CSWmplayer.prototype; \
	touch $(COOKIEDIR)/post-package; fi
	#Sneaky wrapper to re-run package-create with our newly added isaexecs!
	rm $(COOKIEDIR)/package-create
	@echo " Running gmake package-create for a second time"
	gmake package-create


#A edited packaging target that doesn't re-run all the install steps.
only-package:
	gmake pre-package package-create isa-post-package package-check


#The whole shabang! Start to finish, in one line: gmake all-in-one
all-in-one: optbuild only-package


###not yet implemented, mplayer specific
## --enable-runtime-cpudetection allows the binary to run anywhere, use for i386?
#run-anywhere-build:
#	(gmake ISA=pentium)
#CONFIGURE_ARGS += --enable-runtime-cpudetection
