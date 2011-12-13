# This file based from TEMPLATES/createpkg/Makefile.lib
# but only handles 32bit build.
# You MUST build this with gnu make, unfortunately.
# Mainly just because of the ARCH expansion, but also for "?="

# Customize your prototype file(s) as needed

# Organization: variable defintions up top,
# targets in second half.
# Note that assignments with "?=" mean "assign if not already assigned.

# because of intltool nonsense
PATH := /opt/csw/gnu:$(PATH)

#COMPILED_SUBDIRS:=gimp_minimal gimplibs gimp_gnomeplugins gimp_python
COMPILED_SUBDIRS:=gimp_minimal gimplibs gimplibs_doc
SUBDIRS = $(COMPILED_SUBDIRS) gimp_i18n

# Where do we keep local downloads of software src files
ARCHIVEDIR ?= /home/src
ARCHIVENAME ?= gimp-2.6.8.tar.bz2
EXTRACTPROG ?= /usr/sfw/bin/gtar jfx

# Only use ONE here. The name is used for compat with 'gar'.
MASTER_SITES ?= ftp://ftp.gimp.org/pub/gimp/v2.6

ARCH := $(shell /bin/uname -p)

LDFLAGS_COMMON :=

SRCDIR= build/*

CFLAGS_COMMON   ?= -mt -xnorunpath -xO3
CXXFLAGS_COMMON ?= -mt -norunpath  -xO3
CFLAGS_sparc    ?= -xarch=v8
CFLAGS_i386     ?= -xarch=386

# Keep this arch-neutral if possible. add arch-specific tweaks
# to arch-specific target
CONFIGURE=./configure --prefix=/opt/csw --enable-static=no \
  CPPFLAGS=-I/opt/csw/include --without-alsa --disable-python

#I want to actualy compile python stuff but our dev support is broken
# somehow

##  --without-gnomevfs --without-gvfs --without-webkit --disable-python \
##  --without-dbus --without-libcurl \


CREATEPKG=createpkg -r `pwd`/build/*/cswstage


all:	$(ARCH)-32 package

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
	for dir in $(SUBDIRS) ; do \
		(cd $$dir; createpkg -r `pwd`/../build/*/cswstage ) ;\
	done
	$(CREATEPKG)
	mv -i */*.pkg.gz .

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
build/.stage-$(ARCH)-32.done:
	@echo Handling stage of $(ARCH)-32
	(cd $(SRCDIR) ; MAKE=gmake stagepkg -m)
	(cd  $(SRCDIR); cp COPYING cswstage/COPYING.gimp)
	(cd  $(SRCDIR); cp libgimp/COPYING cswstage/COPYING.libgimp)
	@rm -f build/.*64.done
	touch $@


#These are the easy-to-type targets. They just trigger the real ones.
configure-$(ARCH)-32:	build/.configure-$(ARCH)-32.done
	@echo $@ done
build-$(ARCH)-32:	build/.build-$(ARCH)-32.done
	@echo $@ done
stage-$(ARCH)-32:	build/.stage-$(ARCH)-32.done
	@echo $@ done

configure:	configure-$(ARCH)-32

build:		build-$(ARCH)-32

stage:		stage-$(ARCH)-32


GIMPLIBS_EXPR='(/opt/csw/lib/lib|/opt/csw/lib/pkgconfig|/opt/csw/include)'

LIBDOC_EXPR='gtk-doc/html/lib'
#GIMP_GNOME_EXPR='depend'
#GIMP_PYTHON_EXPR='depend'

# Manual target. Run after stage step, to generate all the prototype files
# There is some complicated stuff that cant be done
# in any easier way.
# You should only need to run this the first time a new version is compiled.
# Then just svn commit the prototypes, IF they look okay.
pkgproto:
	cp $(SRCDIR)/cswstage/prototype prototype.tmp
	for d in $(COMPILED_SUBDIRS) gimp_i18n ; do \
	  echo setting up $$d ;\
	  (echo "i pkginfo";echo "i depend";echo "i copyright") >$$d/prototype ;\
	done
	egrep $(GIMPLIBS_EXPR) prototype.tmp >>gimplibs/prototype
	egrep $(LIBDOC_EXPR) prototype.tmp >>gimplibs_doc/prototype
	egrep -v $(GIMPLIBS_EXPR) prototype.tmp | \
		egrep -v $(LIBDOC_EXPR)  | \
		egrep -v locale	>gimp_minimal/prototype
	egrep locale/en prototype.tmp >>gimp_minimal/prototype
	egrep locale prototype.tmp |egrep -v locale/en >>gimp_i18n/prototype
	for dir in gimplibs gimp_minimal ; do \
		(cd $$dir; cat prototype.add >>prototype) ;\
	done
	##rm prototype.tmp
	## egrep $(GIMP_GNOME_EXPR) prototype.tmp >>gimp_gnomeplugins/prototype
	## egrep $(GIMP_PYTHON_EXPR) prototype.tmp >>gimp_python/prototype


