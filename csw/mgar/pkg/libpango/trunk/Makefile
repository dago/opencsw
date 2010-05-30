#This Makefile originally generated from a template under 
# pkg/TEMPLATES/createpkg
#   -- THis is actually  from the "build sparcv9" Makefile,
#  but I cant get v9 build working...

# So rest of this file is a bit of a hack on a hack.

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
#### THis is more complicated than my regular sparcv9 hack, 
# so had to make a custom hack.


BUILDDIR=build/*



STDFILES=pkginfo copyright prototype
FILES=

all:	build package


build:	build/.config.done
	(cd $(BUILDDIR) ; \
	$(MAKE) ; \
	MAKE=$(MAKE) stagepkg ; cp COPYING cswstage/.)


# dummy target for configure
build/.config.done:
	@echo Configuring with:
	@echo CC=$(CC) $(CFLAGS)
	@echo CXX=$(CXX) $(CXXFLAGS)
	(cd $(BUILDDIR) ; \
	test -f ../../patchfile.preconf && \
		gpatch -p0 <../../patchfile.preconf ; \
	./configure --prefix=/opt/csw --disable-static ; \
	if test -f ../../patchfile.postconf ; then \
                 gpatch -p0 <../../patchfile.postconf ; fi)
	touch build/.config.done


# I tried depending this on   $(BUILDDIR)/config.log  but that didnt stick
configure:	build/.config.done

sparcv9:
	(cd $(BUILDDIR) ; \
	gmake clean;  \
	LD_OPTIONS="" gmake CFLAGS='-xstrconst -fast -xarch=v9 -mt' \
	   CXXFLAGS='-fast -xarch=v9 -mt' \
	  LDFLAGS='-R/opt/csw/lib/sparcv9 -L/opt/csw/lib/sparcv9'  ;\
	  cd pango ;\
	  cp `find .libs -type f -name 'lib*.so*'` ../cswstage ;\
	  cd .. ;\
	  for f in *.pc ; do sed 's:libdir=.*:/opt/csw/lib/sparcv9:' $$f>cswstage/$$f.sparcv9 ; \
	  done ;\
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
