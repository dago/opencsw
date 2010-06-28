# This file loosely based Makefiles in TEMPLATES/createpkg
# But highly customized.
# You MUST build this with gnu make, unfortunately.
# Mainly just because of the ARCH expansion, but also for "?="

# Customize your prototype file(s) as needed

# Organization: variable defintions up top,
# targets in second half.
# Note that assignments with "?=" mean "assign if not already assigned.

# Where do we keep local downloads of software src files
ARCHIVEDIR ?= /home/src
ARCHIVENAME ?= gimp-help-2.6.0-html-en.tar.bz2
EXTRACTPROG ?= /usr/sfw/bin/gtar jfx

# Only use ONE here. The name is used for compat with 'gar'.
MASTER_SITES ?= ftp://ftp.gimp.org/pub/gimp/help
SRCDIR= build/*


CREATEPKG=createpkg -b `pwd`/build/*

all:	build/.extract.done package


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


package:	copyright
	$(CREATEPKG)


configure build stage:
	@echo no $@ needed


pkgproto:
	(echo "i pkginfo";echo "i copyright") >prototype
	(cd $(SRCDIR); pkgproto html) |sed "s/ $$USER .*/ root bin/">>prototype
	echo "f none COPYING 0644 root bin" >>prototype
