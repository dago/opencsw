# Eventually, move "Makefile.sparc" to here, and make it 
# generic 64bit capable.?
# you MUST build this with gnu make, unfortunately.
# Mainly just because of the ARCH expansion

# Organization: variable defintions up top,
# targets in second half.

ARCH := $(shell /bin/uname -p)

LDFLAGS_COMMON :=

SRCDIR= build/*

# DO NOT specify the arch-blah stuff such as -m64 here.
# the individual targets will do that.

CFLAGS_COMMON   := -mt -xnorunpath
CXXFLAGS_COMMON := -mt -norunpath

# Keep this arch-neutral if possible. add arch-specific tweaks
# to arch-specific target
CONFIGURE=./configure --prefix=/opt/csw --disable-static

CONFIGURE_64_EXTRAS:= --libdir=/opt/csw/lib/64 --libexecdir=/opt/csw/libexec/sparcv9

all:	$(ARCH)-32 $(ARCH)-64 package

# ARCH-XX handles configure, build, and stage for its own combo
# 

clean distclean:
	$(MAKE) -C $(SRCDIR) $@


<<<<<<< .mine
=======
sparcv9:
	(cd $(BUILDDIR)/src ; \
	gmake clean;  \
	LD_OPTIONS="" gmake CFLAGS='-xstrconst -fast -xarch=v9' \
	  LDFLAGS='-R/opt/csw/lib/sparcv9 -L/opt/csw/lib/sparcv9'  ; \
	  strip .libs/$(RAWLIB); \
	  cp .libs/$(RAWLIB) ../cswstage ; cd .. ;\
	  sed 's:libdir=.*:/opt/csw/lib/sparcv9:' xpm.pc>cswstage/xpm.pc.sparcv9 ; \
	echo sparcv9 build done  )
>>>>>>> .r10271

package patch garchive:
	@echo make $@ not implemented yet
	### potentially want to handle "merge" type stuff in 'package'
	# we also want to handle multi-package thingies.


# initial announce here. more down below for individual targets
sparc-32 sparc-64 i386-32 i386-64::
	@echo Building $@ target


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


# split out generic $(ARCH) sections to specific platform if needed.
# but it usually should not be.

build/.$(ARCH)-32.done:	$(ARCH)-32


build/.stage-$(ARCH)-32.done \
build/.stage-$(ARCH)-64.done ::
	@echo debug: handling $@ target
	touch $@

build/.configure-$(ARCH)-32.done::
	(cd $(SRCDIR) ; \
	  CFLAGS="$(CFLAGS_COMMON)" \
	  CXXFLAGS="$(CXXFLAGS_COMMON)" \
	  $(CONFIGURE) )
	touch $@

build/.configure-$(ARCH)-64.done::
	(cd $(SRCDIR) ; \
	  CFLAGS="$(CFLAGS_COMMON) -m64"  \
	  CXXFLAGS="$(CXXFLAGS_COMMON) -m64" \
	  PKG_CONFIG_PATH=/opt/csw/lib/sparcv9 \
	  $(CONFIGURE) $(CONFIGURE_64_EXTRAS)  )
	touch $@

	
build/.build-$(ARCH)-32.done build/.build-$(ARCH)-64.done::
	(cd $(SRCDIR) ; \
	  $(MAKE) $(MFLAGS) )	
	touch $@

$(ARCH)-32 ::   configure-$(ARCH)-32 build-$(ARCH)-32 stage-$(ARCH)-32
	@echo Completed $(ARCH)-32 configure, build and stage
	touch build/.$(ARCH)-32.done


$(ARCH)-64 ::  stage-$(ARCH)-32 configure-$(ARCH)-64 build-$(ARCH)-64 stage-$(ARCH)-64
	@echo Completed $@ configure, build and stage
	touch build/.$(ARCH)-64.done
