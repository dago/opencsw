#This Makefile originally generated from a template under 
# pkg/TEMPLATES/createpkg

#Uncomment one of these definitions. The -b invokation,
# is suitable for use with small packages, where you want to have a few files
# in your top level src directory. It is also suitable for
# "relocateable" packages. see the createpkg docs for more details.
#CREATEPKG=createpkg -b `pwd`
#CREATEPKG=createpkg -r .
CREATEPKG=createpkg -r `pwd`/cswstage

package:	$(STDFILE) $(FILES)
	$(CREATEPKG)
	@echo just for isaexec, we need to UNgzip now...
	gunzip *.pkg.gz  
	touch package

build:
	./configure --prefix=/opt/csw
	$(MAKE)
	cswstage

clean:
	rm -f *.pkg.gz package

STDFILES=pkginfo copyright prototype

FILES=postinstall postremove
