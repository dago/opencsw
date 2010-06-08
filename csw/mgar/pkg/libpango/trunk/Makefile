# This file is from TEMPLATES/createpkg/Makefile.lib
# You MUST build this with gnu make, unfortunately.
# Mainly just because of the ARCH expansion, but also for "?="


# If you do NOT want to build 64bit libs, remove the $(ARCH)-64 from
# the "all:" target.

# If you DO want to, then leave it in, and also customize your
#  the build/.stage-$(ARCH)-64.done    target(s),
# PLUS, customize your prototype file(s) as needed
# Dont forget to handle any 64bit pkg-config .pc files properly!!

# Organization: variable defintions up top,
# targets in second half.
# Note that assignments with "?=" mean "assign if not already assigned.

# Where do we keep local downloads of software src files
ARCHIVEDIR ?= /home/src
ARCHIVENAME ?= pango-1.28.0.tar.bz2
EXTRACTPROG ?= /usr/sfw/bin/gtar jfx

# Only use ONE here. The name is used for compat with 'gar'.
MASTER_SITES ?= http://ftp.gnome.org/pub/GNOME/sources/pango/1.28

ARCH := $(shell /bin/uname -p)

LDFLAGS_COMMON :=

SRCDIR= build/*
DESTDIR=$(SRCDIR)/cswstage

# DO NOT specify the arch-64 stuff such as -m64 here.
# the individual targets will do that.

CFLAGS_COMMON   ?= -mt -xnorunpath -xO2
CXXFLAGS_COMMON ?= -mt -norunpath  -xO2
CFLAGS_sparc    ?= -xarch=v8
CFLAGS_i386     ?= -xarch=386

# Keep this arch-neutral if possible. add arch-specific tweaks
# to arch-specific target
CONFIGURE=./configure --prefix=/opt/csw --enable-static=no

CONFIGURE_64_sparc=  --libdir=/opt/csw/lib/sparcv9
CONFIGURE_64_i386=   --libdir=/opt/csw/lib/amd64
CONFIGURE_64_EXTRAS:=  $(CONFIGURE_64_$(ARCH)) --enable-introspection=no

PC64DIR_sparc=/opt/csw/lib/sparcv9/pkgconfig
PC64DIR_i386=/opt/csw/lib/amd64/pkgconfig

LDFLAGS_64_sparc := -R/opt/csw/lib/sparcv9 -L/opt/csw/lib/sparcv9
LDFLAGS_64_i386  := -R/opt/csw/lib/amd64 -L/opt/csw/lib/amd64


CREATEPKG=createpkg -r `pwd`/build/*/cswstage


all:	$(ARCH)-32 build/.stage1 $(ARCH)-64 package

# ARCH-XX handles configure, build, and stage for its own combo
# 

EXTRACTPROG ?= /bin/echo ERROR: need to set EXTRACTPROG ; exit 1 ;



extract:
	test -d build || mkdir build
	@if test -f  $(ARCHIVEDIR)/$(ARCHIVENAME) ; then \
		echo Extracting $(ARCHIVENAME) under build dir... ;\
		( cd build && $(EXTRACTPROG) $(ARCHIVEDIR)/$(ARCHIVENAME) ) ; \
	else echo Cannot extract - $(ARCHIVEDIR)/$(ARCHIVENAME) does not exist ;\
		exit 1; \
	fi
	

clean distclean:
	@echo Calling $@ in $(SRCDIR)
	$(MAKE) -C $(SRCDIR) $@

# This is a bit of a hack.. it does a "make clean", 
# only when we're between 32bit and 64bit builds, when doing "make all".
# Once we're IN the 64bit builds, it should not be automatically called.
build/.stage1:
	@echo Doing inter 32-64 bit cleanup
	$(MAKE) -C $(SRCDIR) distclean
	touch $@
	

reallyclean:	distclean
	@echo Removing any milestone files in build as well...
	@rm -f build/.??*
	@echo '(However, leaving src tree intact, with any patches in it)'
	@echo '(If you want, you could rm -r build, then make extract once more)'

garchive:
	@echo Call the fetch target instead: it does the same thing.


# Downloads the source code to the common ARCHIVEDIR
fetch:	$(ARCHIVEDIR)/$(ARCHIVENAME)
	@echo fetch done

$(ARCHIVEDIR)/$(ARCHIVENAME):
	wget -P $(ARCHIVEDIR) $(MASTER_SITES)/$(ARCHIVENAME)

patch:
	@echo patch: patching is handled automatically as part of the configure phase.

package:
	$(CREATEPKG)
	for subdir in devel doc ; do \
	   set +e ;\
	   cd $$subdir ;\
	   createpkg -r ../build/*/cswstage ;\
	   mv *.pkg* .. ; cd .. ;\
	done
#yes I know createpkg will error out because it calls checkpkg

# split out generic $(ARCH) sections to platform-specific sections if needed.
# but it usually should not be neccessary


$(ARCH)-32 ::   configure-$(ARCH)-32 build-$(ARCH)-32 stage-$(ARCH)-32
	@echo Completed $(ARCH)-32 configure, build and stage
	touch build/.$(ARCH)-32.done


$(ARCH)-64 ::  stage-$(ARCH)-32 configure-$(ARCH)-64 build-$(ARCH)-64 stage-$(ARCH)-64
	@echo Completed $@ configure, build and stage
	touch build/.$(ARCH)-64.done

build/.$(ARCH)-32.done:	$(ARCH)-32

build/.$(ARCH)-64.done:	$(ARCH)-64


# Since we share the same src tree, we should only need to
# pre-configure patching one time for all.
build/.patch-preconf.done:
	if test -f patchfile.preconf ; then \
	 gpatch -d $(SRCDIR) -p0  <patchfile.preconf ; fi
	touch $@


#Note: I WANT to use LDFLAGS=-R$$ORIGIN, but stupid libtool
# wont allow it! so force it at build time
build/.configure-$(ARCH)-32.done:	build/.patch-preconf.done
	@echo handling $@ target
	(cd $(SRCDIR) ; \
	  CFLAGS="$(CFLAGS_COMMON) $(CFLAGS_$(ARCH))" \
	  CXXFLAGS="$(CXXFLAGS_COMMON)" \
	  LDFLAGS='-R/opt/csw/lib -L/opt/csw/lib' \
	  $(CONFIGURE) )
	if test -f patchfile.postconf ; then \
	 gpatch -d $(SRCDIR) -p0  <patchfile.postconf ; fi
	touch $@

build/.configure-$(ARCH)-64.done:	build/.patch-preconf.done
	if test "$(ARCH)" = "i386" -a "`uname -r`" != "5.10" ; then \
		echo Error: do 64bit for i386 on sol10 only ; exit 1 ; fi
	@echo handling $@ target
	(cd $(SRCDIR) ; \
	  CFLAGS="$(CFLAGS_COMMON) -m64"  \
	  CXXFLAGS="$(CXXFLAGS_COMMON) -m64" \
	  LDFLAGS="$(LDFLAGS_64_$(ARCH))" \
	  PKG_CONFIG_PATH=/opt/csw/lib/64/pkgconfig \
	  $(CONFIGURE) $(CONFIGURE_64_EXTRAS)  )
	if test -f patchfile.postconf ; then \
	 gpatch -d $(SRCDIR) -p0  <patchfile.postconf ; fi
	touch $@


# See note about LDFLAGS and ORIGIN, higher up	
build/.build-$(ARCH)-32.done build/.build-$(ARCH)-64.done:
	@echo handling $@ target
	LD_OPTIONS='-R$$ORIGIN' $(MAKE) -C $(SRCDIR) $(MFLAGS)
	touch $@



## NOTE: This is a DESTRUCTIVE target build!!
## 'stagepkg'  will destroy any prior "cswstage" directory!!!
## So, we remove all 64bit milestones
build/.stage-$(ARCH)-32.done:
	@echo Handling stage of $(ARCH)-32
	(cd $(SRCDIR) ; MAKE=gmake stagepkg -m)
	@rm -f build/.*64.done
	touch $@


# Note: This is the tricky bit. we cannot just call 
#  "stagepkg": we dont usually want EVERYTHING; just the
# libs that are rebuilt in 64bit, and we need them to go to
# the subdirs, not the regular place!
# SOME things, will have a clean libdir, and respect --libdir,
# and do the right thing easily. However, many will not!
# SO, odds are you'll have to write a customized target
build/.stage-$(ARCH)-64.done:	$(SRCDIR)/cswstage
	@echo ""
	@echo Running special staging customized for pango64
	@(cd $(SRCDIR)/pango;  $(MAKE) DESTDIR=`pwd`/../cswstage install-libLTLIBRARIES)
	@(cd $(SRCDIR)/modules;  $(MAKE) DESTDIR=`pwd`/../cswstage install)
	@(cd $(SRCDIR); mkdir -p cswstage/$(PC64DIR_$(ARCH)) )
	@(cd $(SRCDIR); cp *.pc cswstage/$(PC64DIR_$(ARCH)) )
	@echo ""
	(cd $(SRCDIR); cp COPYING cswstage)
	touch $@



#These are the easy-to-type targets. They just trigger the real ones.
configure-$(ARCH)-32:	build/.configure-$(ARCH)-32.done
	@echo $@ done
build-$(ARCH)-32:	build/.build-$(ARCH)-32.done
	@echo $@ done
stage-$(ARCH)-32:	build/.stage-$(ARCH)-32.done
	@echo $@ done
configure-$(ARCH)-64:	build/.configure-$(ARCH)-64.done
	@echo $@ done
build-$(ARCH)-64:	build/.build-$(ARCH)-64.done
	@echo $@ done
stage-$(ARCH)-64:	build/.stage-$(ARCH)-64.done
	@echo $@ done

