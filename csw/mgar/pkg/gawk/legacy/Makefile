# This file is from TEMPLATES/createpkg/Makefile.lib
# You MUST build this with gnu make, unfortunately.
# Mainly just because of the ARCH expansion, but also for "?="

# Customize your prototype file(s) as needed

# Organization: variable defintions up top,
# targets in second half.
# Note that assignments with "?=" mean "assign if not already assigned.

# Where do we keep local downloads of software src files
ARCHIVEDIR ?= /home/src
ARCHIVENAME ?= gawk-3.1.8.tar.gz
EXTRACTPROG ?= /usr/sfw/bin/gtar zfx

# Only use ONE here. The name is used for compat with 'gar'.
MASTER_SITES ?= http://ftp.gnu.org/pub/gnu/gawk

ARCH := $(shell /bin/uname -p)

LDFLAGS_COMMON :=

SRCDIR= build/*

# DO NOT specify the arch-64 stuff such as -m64 here.
# the individual targets will do that.

CFLAGS_COMMON   ?= -mt -xnorunpath -fast -xstrconst
CXXFLAGS_COMMON ?= -mt -norunpath  -fast
CFLAGS_sparc    ?= -xarch=v8
CFLAGS_i386     ?= -xarch=386

# Keep this arch-neutral if possible. add arch-specific tweaks
# to arch-specific target
CONFIGURE=./configure --prefix=/opt/csw



CREATEPKG=createpkg -r `pwd`/build/*/cswstage


all:	$(ARCH)-32
#all:	$(ARCH)-32 package

# ARCH-XX handles configure, build, and stage for its own combo
# 

EXTRACTPROG ?= /bin/echo ERROR: need to set EXTRACTPROG ; exit 1 ;



extract:	build/.extract.done

build/.extract.done:
	test -d build || mkdir build
	@if test -f  $(ARCHIVEDIR)/$(ARCHIVENAME) ; then \
		echo Extracting $(ARCHIVENAME) under build dir... ;\
		( cd build && $(EXTRACTPROG) $(ARCHIVEDIR)/$(ARCHIVENAME) ) ; \
	else echo Cannot extract - $(ARCHIVEDIR)/$(ARCHIVENAME) does not exist ;\
		exit 1; \
	fi
	touch build/.extract.done
	

clean distclean:
	@echo Calling $@ in $(SRCDIR)
	$(MAKE) -C $(SRCDIR) $@


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


# split out generic $(ARCH) sections to platform-specific sections if needed.
# but it usually should not be neccessary


$(ARCH)-32 ::   configure-$(ARCH)-32 build-$(ARCH)-32 stage-$(ARCH)-32
	@echo Completed $(ARCH)-32 configure, build and stage
	touch build/.$(ARCH)-32.done



build/.$(ARCH)-32.done:	$(ARCH)-32

# Since we share the same src tree, we should only need to
# pre-configure patching one time for all.
build/.patch-preconf.done:	build/.extract.done
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


# See note about LDFLAGS and ORIGIN, higher up	
build/.build-$(ARCH)-32.done:
	@echo handling $@ target
	LD_OPTIONS='-R$$ORIGIN' $(MAKE) -C $(SRCDIR) $(MFLAGS)
	touch $@



## NOTE: This is a DESTRUCTIVE target build!!
## 'stagepkg'  will destroy any prior "cswstage" directory!!!
## So, we remove all 64bit milestones
build/.stage-$(ARCH)-32.done:
	@echo Handling stage of $(ARCH)-32
	(cd $(SRCDIR) ; MAKE=gmake stagepkg)
	(cd $(SRCDIR); cp COPYING cswstage/.)
	@rm -f build/.*64.done
	touch $@



#These are the easy-to-type targets. They just trigger the real ones.
configure-$(ARCH)-32:	build/.configure-$(ARCH)-32.done
	@echo $@ done
build-$(ARCH)-32:	build/.build-$(ARCH)-32.done
	@echo $@ done
stage-$(ARCH)-32:	build/.stage-$(ARCH)-32.done
	@echo $@ done
