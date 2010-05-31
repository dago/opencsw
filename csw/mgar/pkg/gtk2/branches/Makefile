#This Makefile originally generated from a template under 
# pkg/TEMPLATES/createpkg
# You will most likely have to use GNU make to use it.
# This is one specifically hacked to make building sparcv9 packages
# easier.
#
# Steps to use:
# 
# 1. put your normal prototype  as prototype.i386
# 2. copy to prototype.sparc and edit as appropriate
# 3. search for "XXX" and replace with appropriate string
#
# 4. build your package with:
#    "make", "make sparcv9", "make package"


#Uncomment one of these definitions. The -b invokation,
# is suitable for use with small packages, where you want to have a few files
# in your top level src directory. It is also suitable for
# "relocateable" packages. see the createpkg docs for more details.
#CREATEPKG=createpkg -b `pwd`
CREATEPKG=createpkg -r `pwd`/build/*/cswstage

## hax for sparcv9
RAWLIB=libXXX.so.#.#.#


BUILDDIR=build/*



STDFILES=pkginfo copyright prototype
FILES=

all:	build


build:	build/.config.done
	(cd $(BUILDDIR) ; \
	$(MAKE) ; \
	MAKE=$(MAKE) stagepkg  )


# dummy target for configure
build/.config.done:
	@echo Configuring with:
	@echo CC=$(CC) $(CFLAGS)
	@echo CXX=$(CXX) $(CXXFLAGS)
	(cd $(BUILDDIR) ; \
	test -f ../../patchfile.preconf && \
		gpatch -p0 <../../patchfile.preconf ; \
	CPPFLAGS=-I/opt/csw/include ./configure --prefix=/opt/csw --disable-static ; \
	if test -f ../../patchfile.postconf ; then \
                 gpatch -p0 <../../patchfile.postconf ; fi)
	test -f $(BUILDDIR)/config.status && touch build/.config.done


# I tried depending this on   $(BUILDDIR)/config.log  but that didnt stick
configure:	build/.config.done

sparcv9:
	(cd $(BUILDDIR)/src ; \
	gmake clean;  \
	LD_OPTIONS="" gmake CFLAGS='-xstrconst -fast -xarch=v9' \
	  LDFLAGS='-R/opt/csw/lib/sparcv9 -L/opt/csw/lib/sparcv9'  ; \
	  strip .libs/$(RAWLIB); \
	  cp .libs/$(RAWLIB) ../cswstage ; cd .. ;\
	  sed 's:libdir=.*:/opt/csw/lib/sparcv9:' XXX.pc>cswstage/XXX.pc.sparcv9 ; \
	echo sparcv9 build done  )


package:	$(STDFILE) $(FILES)
	$(CREATEPKG)



pkgclean:
	rm -f *.pkg.gz package

clean:	pkgclean
	cd $(BUILDDIR) && make clean

reallyclean:	clean
	rm -f $BUILDDIR/config.log $BUILDDIR/config.cache $BUILDDIR/config.status
	rm -f build/.config.done	
