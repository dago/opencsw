###Mplayer and $ISAEXEC makefile example###
#
# This makefile has a lot of notes and misc. information in it that I've been
# using as I've been working away at this project. It will be tidied up before
# I submit it for official review
#
# Usage
# To simply build mplayer in the conventional manner, use gmake as per normal
#
# To drive all $ISA versions at once, use gmake optbuild ACTION=<action here>
# That will run your standard gmake commands through a loop for all $ISAs

GARNAME = MPlayer
GARVERSION = 1.0rc1
CATEGORIES = APPS

DESCRIPTION = A multimedia player
define BLURB
JW test mplayer build. Very much a work in progress!
endef


MASTER_SITES = http://www3.mplayerhq.hu/MPlayer/releases/ http://www3.mplayerhq.hu/MPlayer/releases/codecs/ http://www.mplayerhq.hu/MPlayer/skins/

GARCOMPILER = GNU

DISTFILES  = $(GARNAME)-1.0rc1.tar.bz2
DISTFILES += Blue-1.7.tar.bz2
DISTFILES += $(call admfiles,CSWmplayer,depend)

PATCHFILES  = fix-configure-variables.diff
PATCHFILES += fix-solaris8-llrint.diff
PATCHFILES += fix-stdint.h-includes.diff
PATCHFILES += fix-configure-stdint.h-detection.diff
PATCHFILES += fix-ffmpeg-gcc-error.diff
PATCHFILES += security-asmrules_fix_20061231.diff
PATCHFILES += security-cddb_fix_20070605.diff

#Sparc Patches
#This forces mplayer to bulid a v8 optimised binary PATCHFILES += sparc-v8build.diff

CONFIGURE_ARGS  = --prefix=/opt/csw
CONFIGURE_ARGS += --with-extraincdir=/usr/X11/include
CONFIGURE_ARGS += --mandir=/share/man
CONFIGURE_ARGS += --enable-gui
CONFIGURE_ARGS += --disable-libcdio
CONFIGURE_ARGS += --disable-win32 ##Until I work out the legal ramifications
#CONFIGURE_ARGS += --with-codecsdir=/opt/csw/share/codecs ## win32 stuff





###Framework for an $ISAEXEC optimised build###
# To allow for the same build to run multiple times without each version
# clobbering the  non-unique work/cookie folders each time, we append the
# target $ISA to each foldername.
# I don't see any value in retaining the hostname in the folder names, as we're
# merging mulitple builds anyway, and i386 build types don't match sparc types.
#
#
###Script functionality/Order###
#
# 1) gmake optbuild runs the standard gar framework through the optbuild for 
#	loop. If you supply no arguements, it will use the default GAR target
#	of "build", which in turn will kick of a seperate build of Mplayer
#	for each of the targets in $ISATARGET, which is i386/sparc specific.
# 2) Once we have a optimised build of each of the $ISATARGETS, we want to 
#	install the $BASEISA into the gar spool dir ($DESTDIR).
#	This works against my little loop. Need to understand this better
#	Later we do want to copy the binaries, which is helped by the install
#	phase. So install is helpful, but post-install really needs to be
#	singular. The cp phase can be run many times but the isaexec symlink
#	really only want to be run once.




#	This gives us an unoptimised build of the entire package, as per normal.
### A standard gmake install should do this, though simply using the lowest
### in the $ISATARGET list (i.e $BASEISA) should achieve the same thing
#
# 3) Next we want to copy the optimised binaries or libraries from our optimised
#	builds, into the the $BASEISA spool, but into an $ISAEXEC compatable
#	directory structure.
#	The gmake post-install step should hopefully take care of this.
### The order of the loop will matter here though, need to be careful
#
#
# 4) Our post-install scripts could in theory take care of this, the next GAR
#	phase is pre-package, which could be another target.
#
# Gar uses the $DESTIMG variable to create these directory  names, so we need to
# change that variable to reflect a unique $ISA name.
# $DESTDIR is where the package is installed to prior to packaging. We also 
# need to make this directory name unique to the $ISA.
# $DESTDIR is defined in the core GAR makefile, which hasn't been included yet,
# so I have to change this variable later on in this script. Will review this...

DESTIMG=$(GARNAME)-$(ISA)


###Optimisation section###
#
# This gar package builds a plain non-optimised version of Mplayer by default.
# To build the fully optimised $ISAEXEC version use "gmake optbuild"
# 
# To create optimised binaries for each of the $ISATARGETS in the final .pkg we
# actually have to build multiple copies of mplayer, only to then simply copy
# only the resultant optimised binaries or libraries to the spool folder, for
# pickup in the packaging phase of the gar build as per normal.
#
# First we need to work out which arch this build host is using and then set
# the both the base ISA target to build for and the desired $ISA targets.
#
# $ISATARGETS represents the optimised cpu targets.
# These targets can be used in a couple of ways. We need to feed a desired 
# optimisation target into our compiler, but we also need to create and copy
# the binaries into the $ISAEXEC folder struction in the final spool layout.
#
# Unfortunately for GCC at least, these names don't match, and 64-bit is even
# worse.
#
# On an AMD64 host, the $ISAEXEC search order is:
# amd64 pentium_pro+mmx pentium_pro pentium+mmx pentium i486 i386 i86 
# I'll need to look at sparc later.
#
#
#
# $BASEISA is used for the base build, and for legacy use by plain "gmake".
# The $BASEISA represents the minimum optimisation level, but it's also used as
# the base (master) template for creating the package. All other $ISATARGET 
# builds will have their binaries and libraries copied into the $BASEISA 
# spool, prior to final packaging.

ifeq ($(shell uname -p),i386)
 ISATARGETS = pentium pentium-mmx pentium2
 BASEISA = pentium
else
 ISATARGETS = -mv7 -mv8 -mv9
 BASEISA = mv7
endif

#Mapping
# Do make files have a concept of a hash for matching these?
# $ISAEXEC name | GCC name
# pentium=pentium
# pentium+mmx=pentium-mmx
# pentium_pro+mmx=pentium2
# 64-bit can be athlon, but I expect -m64 will be what we're after

#If statement for gcc!
pentium_dir 	= pentium
pentium-mmx_dir = pentium+mmx
pentium2_dir 	= pentium_pro+mmx

#Sparc next!
# ?? = sparcv8
# ?? = sparcv8plus
# ?? = sparcv8plus+vis
# ?? = sparcv9
# ?? = sparcv9plus+vis2 

ISAEXEC_DIR = $($(ISA)_dir)

# If you just typed gmake, this will build the stardard BASEISA build.
# For a single optimised build use gmake ISA=your-target-here.
# For all optimised versions ($ISAEXEC), use gmake optbuild 
ISA ?= $(BASEISA)

#Which binaries do you want to use $ISAEXEC for?
# Note: These must be the full paths!
ISAEXEC_BINS = opt/csw/bin/mplayer opt/csw/bin/mencoder


# Inclue all standard GAR variables and functionality from here onward:
include ../category.mk

# See earlier, we needed to set this VAR _after_ the category.mk include
BASE_DESTDIR :=$(DESTDIR)-$(BASEISA)
DESTDIR := $(DESTDIR)-$(ISA)

####Mplayer specific optimisation notes####
# Mplayer uses mtune, not march for optimisation so we want to set this to suit

CFLAGS = -O2 -pipe -mtune=$(ISA)
CPPFLAGS = $(CFLAGS)
CXXFLAGS = $(CFLAGS)
ASFLAGS = $(CFLAGS)
OPTFLAGS = $(CFLAGS)



# This is the main target used by this Makefile for creating $ISAEXEC format pkgs.
# This for loop is very important for handling the $DESTDIR var as it applies in
# the post-install steps (I.E the ISA-specific dirs)

optbuild:
	(for TARGET in $(ISATARGETS); do \
	gmake ISA=$$TARGET $$ACTION; done)


# optpkg is for running the packaging step outside for the optbuild for loop.
# I think this will achieve that. We only want the one package. By this point all
# of the binaries should be where we want them, and the prototype updated to suit
# isaexec of our $ISAEXEC_BINS

optpkg: optbuild package

###Tidy ups and files below
# We need the skins dir copied into the master spool dir
# We need the default font copied into the master spool dir
# Finally, suck in all the optimised binaries

post-install: skins fonts copy-opt-bins

#post-install-optbuild: use-isaexec copy-opt-bins

#### Skins, Fonts, Codecs and below all need to be run from optbuild to inherit
#	the expanded $(DESTDIR) variable which includes their expanded path
#	In Mplayer's case we don't actually need the skins/fonts in each ISA build
#	but pulling them out of the loop is proving tricky 


skins:
	(mkdir -p $(DESTDIR)$(BUILD_PREFIX)/share/mplayer/skins/default)
	(cp -r $(WORKSRC)/../Blue/* $(DESTDIR)$(BUILD_PREFIX)/share/mplayer/skins/default)

fonts:
	(ln -f -s /usr/openwin/lib/X11/fonts/TrueType/Arial.ttf $(DESTDIR)$(BUILD_PREFIX)/share/mplayer/subfont.ttf)

codecs:
	(mkdir -p $(DESTDIR)$(BUILD_PREFIX)/lib/codecs)
	(cp -r $(WORKSRC)/../all-20061022/* $(DESTDIR)$(BUILD_PREFIX)/share/codecs) 

# This should just be run the once
# This sets up the dependancies correctly, but you'll have to do the depend manually
# In Mplayer's case I'm going to have to hard code the name, as the tarball has it
# as "MPlayer", not "mplayer", so I can't simply change the $(GARNAME)
pre-package:
	(echo "l none /opt/csw/bin/mplayer=isaexec" >> $(WORKSRC)/../CSWmplayer.prototype)
	(echo "l none /opt/csw/bin/mencoder=isaexec" >> $(WORKSRC)/../CSWmplayer.prototype)

#use-isaexec:
#	@if test ! -f $(BASE_DESTDIR)$(BUILD_PREFIX)/bin/isaexec ; then cp /opt/csw/bin/isaexec $(BASE_DESTDIR)$(BUILD_PREFIX)/bin; fi
#	(cd $(BASE_DESTDIR)$(BUILD_PREFIX))
#	( for bin in $(ISAEXEC_BINS); do gln -f $(BASE_DESTDIR)$(BUILD_PREFIX)/bin/isaexec  $(BASE_DESTDIR)$(BUILD_PREFIX)/$$bin; done)

# Must be called from optbuild for the DESTDIR var to be inherited, and we need to
# loop this for each ISATARGET
copy-opt-bins:
	(mkdir -p $(BASE_DESTDIR)$(BUILD_PREFIX)/bin/$(ISAEXEC_DIR))
	(cd $(DESTDIR); if test ! -f $(BASE_DESTDIR)$(BUILD_PREFIX)/bin/$(ISAEXEC_DIR)/* ; then mv $(ISAEXEC_BINS) $(BASE_DESTDIR)$(BUILD_PREFIX)/bin/$(ISAEXEC_DIR); fi )



###not yet implemented, mplayer specific
## --enable-runtime-cpudetection allows the binary to run anywhere, use for i386
run-anywhere-build:
	(gmake ISA=pentium)
CONFIGURE_ARGS += --enable-runtime-cpudetection

clean-everything:

#This doesn't clean out our extra DESTDIRS... need fixing
	gmake optbuild ACTION=clean
