#This Makefile originally generated from a template under 
# pkg/TEMPLATES/createpkg

#Uncomment one of these definitions. The -b invokation,
# is suitable for use with small packages, where you want to have a few files
# in your top level src directory. It is also suitable for
# "relocateable" packages. see the createpkg docs for more details.
#CREATEPKG=createpkg -b `pwd`


BUILDDIR=build/*

CREATEPKG=createpkg -r `pwd`/build/*/cswstage


STDFILES=pkginfo copyright prototype
FILES=

package:	$(STDFILE) $(FILES)
	$(CREATEPKG)


build:
	(cd $(BUILDDIR) ; \
	test -f ../../patchfile.preconf && \
		gpatch -p0 <../../patchfile.preconf ; \
	./configure --prefix=/opt/csw ; \
	test -f ../../patchfile.postconf && \
                 gpatch -p0 <../../patchfile.postconf  ; \
	$(MAKE) ; \
	cswstage  )

clean:
	rm -f *.pkg.gz package

