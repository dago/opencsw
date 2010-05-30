#This Makefile originally generated from a template under 
# pkg/TEMPLATES/createpkg
# You will most likely have to use GNU make to use it.


#Uncomment one of these definitions. The -b invokation,
# is suitable for use with small packages, where you want to have a few files
# in your top level src directory. It is also suitable for
# "relocateable" packages. see the createpkg docs for more details.
#CREATEPKG=createpkg -b `pwd`
CREATEPKG=createpkg -r `pwd`/build/*/cswstage


BUILDDIR=build/libXpm*


## hax for sparcv9
RAWLIB=libXpm.so.4.11.0
XPM_PC=build/libXpm-3.5.8/cswstage/opt/csw/lib/pkgconfig/xpm.pc


STDFILES=pkginfo copyright prototype
FILES=

all:	build


build:	build/.config.done
	(cd $(BUILDDIR) ; \
	$(MAKE) ; \
	stagepkg  )


sparcv9:
	(cd $(BUILDDIR)/src ; \
	gmake clean;  \
	LD_OPTIONS="" gmake CFLAGS='-xstrconst -fast -xarch=v9' \
	  LDFLAGS='-R/opt/csw/lib/sparcv9 -L/opt/csw/lib/sparcv9'  ; \
	  strip .libs/$(RAWLIB); \
	  cp .libs/$(RAWLIB) ../cswstage ; cd .. ;\
	  sed 's:libdir=.*:/opt/csw/lib/sparcv9:' xpm.pc>cswstage/xpm.pc.sparcv9 ; \
	echo sparcv9 build done  )

hack:
	( cd $(BUILDDIR) ; \
	  sed 's:libdir=.*:/opt/csw/lib/sparcv9:' xpm.pc>cswstage/xpm.pc.sparcv9 )

	
# dummy target for configure
build/.config.done:
	(cd $(BUILDDIR) ; \
	test -f ../../patchfile.preconf && \
		gpatch -p0 <../../patchfile.preconf ; \
	./configure --prefix=/opt/csw --enable-static=no ; \
	test -f ../../patchfile.postconf && \
                 gpatch -p0 <../../patchfile.postconf )
	touch build/.config.done


# I tried depending this on   $(BUILDDIR)/config.log  but that didnt stick
configure:	build/.config.done

package:	$(STDFILE) $(FILES)
	@echo Building package for `uname -p`
	$(CREATEPKG)



pkgclean:
	rm -f *.pkg.gz package

clean:	pkgclean
	cd $(BUILDDIR) && make clean

reallyclean:	clean
	rm -f $BUILDDIR/config.log $BUILDDIR/config.cache $BUILDDIR/config.status
	rm -f build/.config.done	
