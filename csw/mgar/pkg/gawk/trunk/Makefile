#This Makefile originally generated from a template under 
# pkg/TEMPLATES/createpkg
# You will most likely have to use GNU make to use it.


#Uncomment one of these definitions. The -b invokation,
# is suitable for use with small packages, where you want to have a few files
# in your top level src directory. It is also suitable for
# "relocateable" packages. see the createpkg docs for more details.
#CREATEPKG=createpkg -b `pwd`
CREATEPKG=createpkg -r `pwd`/build/*/cswstage


BUILDDIR=build/*



STDFILES=pkginfo copyright prototype
FILES=

all:	build package


build:	build/.config.done
	(cd $(BUILDDIR) ; \
	$(MAKE) ; \
	stagepkg  )


# dummy target for configure
build/.config.done:
	@echo Configuring with:
	@echo CC=$(CC) $(CFLAGS)
	@echo CXX=$(CXX) $(CXXFLAGS)
	(cd $(BUILDDIR) ; \
	test -f ../../patchfile.preconf && \
		gpatch -p0 <../../patchfile.preconf ; \
	./configure --prefix=/opt/csw ; \
	if test -f ../../patchfile.postconf ; then \
                 gpatch -p0 <../../patchfile.postconf ; fi)
	touch build/.config.done


# I tried depending this on   $(BUILDDIR)/config.log  but that didnt stick
configure:	build/.config.done

package:	$(STDFILE) $(FILES) build
	cp build/gawk*/COPYING `echo build/gawk*/cswstage/opt/csw/share/awk`/COPYING.gawk
	$(CREATEPKG)


pkgclean:
	rm -f *.pkg.gz package

clean:	pkgclean
	cd $(BUILDDIR) && make clean

reallyclean:	clean
	rm -f $BUILDDIR/config.log $BUILDDIR/config.cache $BUILDDIR/config.status
	rm -f build/.config.done	
