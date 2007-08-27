# vim: ft=make ts=4 sw=4 noet
#
# $Id$
#
# Copyright (C) 2001 Nick Moffitt
# 
# Redistribution and/or use, with or without modification, is
# permitted.  This software is without warranty of any kind.  The
# author(s) shall not be liable in the event that use of the
# software causes damage.

# Comment this out to make much verbosity
#.SILENT:

#ifeq ($(origin GARDIR), undefined)
#GARDIR := $(CURDIR)/../..
#endif

GARDIR ?= ../..
GARBIN  = $(GARDIR)/bin
FILEDIR ?= files
DOWNLOADDIR ?= download
PARTIALDIR ?= $(DOWNLOADDIR)/partial
COOKIEROOTDIR ?= cookies
COOKIEDIR ?= $(COOKIEROOTDIR)/$(DESTIMG).d
WORKROOTDIR ?= work
WORKDIR ?= $(WORKROOTDIR)/$(DESTIMG).d
WORKSRC ?= $(WORKDIR)/$(DISTNAME)
EXTRACTDIR ?= $(WORKDIR)
SCRATCHDIR ?= tmp
CHECKSUM_FILE ?= checksums
MANIFEST_FILE ?= manifest
LOGDIR ?= log

DIRSTODOTS = $(subst . /,./,$(patsubst %,/..,$(subst /, ,/$(1))))
ROOTFROMDEST = $(call DIRSTODOTS,$(DESTDIR))
MAKEPATH = $(shell echo $(1) | perl -lne 'print join(":", split)')
TOLOWER = $(shell echo $(1) | tr '[A-Z]' '[a-z]')

PARALLELMFLAGS ?= $(MFLAGS)
export PARALLELMFLAGS

DISTNAME ?= $(GARNAME)-$(GARVERSION)

ALLFILES ?= $(DISTFILES) $(PATCHFILES)

ifeq ($(MAKE_INSTALL_DIRS),1)
INSTALL_DIRS = $(addprefix $(DESTDIR),$(prefix) $(exec_prefix) $(bindir) $(sbindir) $(libexecdir) $(datadir) $(sysconfdir) $(sharedstatedir) $(localstatedir) $(libdir) $(infodir) $(lispdir) $(includedir) $(mandir) $(foreach NUM,1 2 3 4 5 6 7 8, $(mandir)/man$(NUM)) $(sourcedir))
else
INSTALL_DIRS =
endif

# For rules that do nothing, display what dependencies they
# successfully completed
#DONADA = @echo "	[$@] complete.  Finished rules: $+"
DONADA = @touch $(COOKIEDIR)/$@; echo "	[$@] complete for $(GARNAME)."

# TODO: write a stub rule to print out the name of a rule when it
# *does* do something, and handle indentation intelligently.

# Default sequence for "all" is:  fetch checksum extract patch configure build
all: build

# include the configuration file to override any of these variables
include $(GARDIR)/gar.conf.mk
include $(GARDIR)/gar.lib.mk

#################### DIRECTORY MAKERS ####################

# This is to make dirs as needed by the base rules
$(sort $(DOWNLOADDIR) $(PARTIALDIR) $(COOKIEDIR) $(WORKSRC) $(WORKDIR) $(EXTRACTDIR) $(FILEDIR) $(SCRATCHDIR) $(INSTALL_DIRS) $(GARCHIVEDIR) $(GARPKGDIR) $(STAGINGDIR)) $(COOKIEDIR)/%:
	@if test -d $@; then : ; else \
		ginstall -d $@; \
		echo "ginstall -d $@"; \
	fi

# These stubs are wildcarded, so that the port maintainer can
# define something like "pre-configure" and it won't conflict,
# while the configure target can call "pre-configure" safely even
# if the port maintainer hasn't defined it.
# 
# in addition to the pre-<target> rules, the maintainer may wish
# to set a "pre-everything" rule, which runs before the first
# actual target.
pre-%:
	@true

post-%:
	@true

# Call any arbitrary rule recursively for all dependencies
deep-%: %
	@for target in "" $(DEPEND_LIST) ; do \
		test -z "$$target" && continue ; \
		$(MAKE) -C ../../$$target DESTIMG=$(DESTIMG) $@ ; \
	done
	@$(foreach IMG,$(filter-out $(DESTIMG),$(IMGDEPS)),for dep in "" $($(IMG)_DEPENDS); do test -z "$$dep" && continue ; $(MAKE) -C ../../$$dep DESTIMG=$(IMG) $@; done; )

# ========================= MAIN RULES ========================= 
# The main rules are the ones that the user can specify as a
# target on the "make" command-line.  Currently, they are:
#	fetch-list fetch checksum makesum extract checkpatch patch
#	build install reinstall uninstall package
# (some may not be complete yet).
#
# Each of these rules has dependencies that run in the following
# order:
# 	- run the previous main rule in the chain (e.g., install
# 	  depends on build)
#	- run the pre- rule for the target (e.g., configure would
#	  then run pre-configure)
#	- generate a set of files to depend on.  These are typically
#	  cookie files in $(COOKIEDIR), but in the case of fetch are
#	  actual downloaded files in $(DOWNLOADDIR)
# 	- run the post- rule for the target
# 
# The main rules also run the $(DONADA) code, which prints out
# what just happened when all the dependencies are finished.

announce:
	@echo "[===== NOW BUILDING:	$(DISTNAME)	=====]"

# fetch-list	- Show list of files that would be retrieved by fetch.
# NOTE: DOES NOT RUN pre-everything!
fetch-list:
	@echo "Distribution files: "
	@for i in $(DISTFILES); do echo "	$$i"; done
	@echo "Patch files: "
	@for i in $(PATCHFILES); do echo "	$$i"; done

# fetch			- Retrieves $(DISTFILES) (and $(PATCHFILES) if defined)
#				  into $(DOWNLOADDIR) as necessary.
FETCH_TARGETS =  $(addprefix $(DOWNLOADDIR)/,$(ALLFILES))

fetch: announce pre-everything $(COOKIEDIR) $(DOWNLOADDIR) $(PARTIALDIR) $(addprefix dep-$(GARDIR)/,$(FETCHDEPS)) pre-fetch $(FETCH_TARGETS) post-fetch
	$(DONADA)

# returns true if fetch has completed successfully, false
# otherwise
fetch-p:
	@$(foreach COOKIEFILE,$(FETCH_TARGETS), test -e $(COOKIEDIR)/$(COOKIEFILE) ;)

# checksum		- Use $(CHECKSUMFILE) to ensure that your
# 				  distfiles are valid.
CHECKSUM_TARGETS = $(addprefix checksum-,$(filter-out $(NOCHECKSUM),$(ALLFILES)))

checksum: fetch $(COOKIEDIR) pre-checksum $(CHECKSUM_TARGETS) post-checksum
	$(DONADA)

# returns true if checksum has completed successfully, false
# otherwise
checksum-p:
	@$(foreach COOKIEFILE,$(CHECKSUM_TARGETS), test -e $(COOKIEDIR)/$(COOKIEFILE) ;)

# makesum		- Generate distinfo (only do this for your own ports!).
MAKESUM_TARGETS =  $(addprefix $(DOWNLOADDIR)/,$(filter-out $(NOCHECKSUM),$(ALLFILES))) 

makesum: fetch $(MAKESUM_TARGETS)
	@if test "x$(MAKESUM_TARGETS)" != "x "; then \
		gmd5sum $(MAKESUM_TARGETS) > $(CHECKSUM_FILE) ; \
		echo "Checksums made for $(MAKESUM_TARGETS)" ; \
		cat $(CHECKSUM_FILE) ; \
	fi

# I am always typing this by mistake
makesums: makesum

GARCHIVE_TARGETS =  $(addprefix $(GARCHIVEDIR)/,$(ALLFILES))

garchive: checksum $(GARCHIVE_TARGETS) ;

# extract		- Unpacks $(DISTFILES) into $(EXTRACTDIR) (patches are "zcatted" into the patch program)
EXTRACT_TARGETS = $(addprefix extract-,$(filter-out $(NOEXTRACT),$(DISTFILES)))

extract: checksum $(EXTRACTDIR) $(COOKIEDIR) $(addprefix dep-$(GARDIR)/,$(EXTRACTDEPS)) pre-extract $(EXTRACT_TARGETS) post-extract
	$(DONADA)

# returns true if extract has completed successfully, false
# otherwise
extract-p:
	@$(foreach COOKIEFILE,$(EXTRACT_TARGETS), test -e $(COOKIEDIR)/$(COOKIEFILE) ;)

# checkpatch	- Do a "patch -C" instead of a "patch".  Note
# 				  that it may give incorrect results if multiple
# 				  patches deal with the same file.
# TODO: actually write it!
checkpatch: extract
	@echo "$@ NOT IMPLEMENTED YET"

# patch			- Apply any provided patches to the source.
PATCH_TARGETS = $(addprefix patch-,$(PATCHFILES))

patch: extract $(WORKSRC) pre-patch $(PATCH_TARGETS) post-patch
	$(DONADA)

# returns true if patch has completed successfully, false
# otherwise
patch-p:
	@$(foreach COOKIEFILE,$(PATCH_TARGETS), test -e $(COOKIEDIR)/$(COOKIEFILE) ;)

# makepatch		- Grab the upstream source and diff against $(WORKSRC).  Since
# 				  diff returns 1 if there are differences, we remove the patch
# 				  file on "success".  Goofy diff.
makepatch: $(SCRATCHDIR) $(FILEDIR) $(FILEDIR)/gar-base.diff
	$(DONADA)

# this takes the changes you've made to a working directory,
# distills them to a patch, updates the checksum file, and tries
# out the build (assuming you've listed the gar-base.diff in your
# PATCHFILES).  This is way undocumented.  -NickM
beaujolais: makepatch makesum clean build
	$(DONADA)

update: makesum garchive clean

# configure		- Runs either GNU configure, one or more local
# 				  configure scripts or nothing, depending on
# 				  what's available.
CONFIGURE_TARGETS = $(addprefix configure-,$(CONFIGURE_SCRIPTS))

# Limit dependencies to all but one category or to exclude one category
ALL_CATEGORIES = apps cpan devel gnome lang lib net server utils extra
ifneq ($(BUILD_CATEGORY),)
NOBUILD_CATEGORY = $(filter-out $(BUILD_CATEGORY),$(ALL_CATEGORIES))
endif

DEPEND_LIST = $(filter-out $(addsuffix /%,$(NOBUILD_CATEGORY)),$(DEPENDS) $(LIBDEPS) $(BUILDDEPS))

ifneq ($(SKIPDEPEND),1)
CONFIGURE_DEPS = $(addprefix $(GARDIR)/,$(addsuffix /$(COOKIEDIR)/install,$(DEPEND_LIST)))
CONFIGURE_IMGDEPS = $(addprefix imgdep-,$(filter-out $(DESTIMG),$(IMGDEPS)))
#CONFIGURE_BUILDDEPS = $(addprefix $(GARDIR)/,$(addsuffix /$(COOKIEROOTDIR)/build.d/install,$(BUILDDEPS)))
endif

configure: patch $(CONFIGURE_IMGDEPS) $(CONFIGURE_BUILDDEPS) $(CONFIGURE_DEPS) $(addprefix srcdep-$(GARDIR)/,$(SOURCEDEPS)) pre-configure $(CONFIGURE_TARGETS) post-configure
	$(DONADA)

# returns true if configure has completed successfully, false
# otherwise
configure-p:
	@$(foreach COOKIEFILE,$(CONFIGURE_TARGETS), test -e $(COOKIEDIR)/$(COOKIEFILE) ;)

# build			- Actually compile the sources.
BUILD_TARGETS = $(addprefix build-,$(BUILD_SCRIPTS))

build: configure pre-build $(BUILD_TARGETS) post-build
	$(DONADA)

# returns true if build has completed successfully, false
# otherwise
build-p:
	@$(foreach COOKIEFILE,$(BUILD_TARGETS), test -e $(COOKIEDIR)/$(COOKIEFILE) ;)

TEST_TARGETS = $(addprefix test-,$(TEST_SCRIPTS))
test: build pre-test $(TEST_TARGETS) post-test
	$(DONADA)

# strip - Strip executables
POST_INSTALL_TARGETS := strip $(POST_INSTALL_TARGETS)
strip:
	@for target in $(STRIP_DIRS) $(DESTDIR)$(bindir) $(DESTDIR)$(sbindir) ; \
	do \
		stripbin $$target ; \
	done
	$(DONADA)

# fixconfig - Remove build-time paths config files
POST_INSTALL_TARGETS := fixconfig $(POST_INSTALL_TARGETS)
FIXCONFIG_DIRS    ?= $(DESTDIR)$(libdir) $(DESTDIR)$(bindir)
FIXCONFIG_RMPATHS ?= $(DESTDIR) $(CURDIR)/$(WORKSRC)
fixconfig:
	@if test "x$(FIXCONFIG_DIRS)" != "x" ; then \
		for path in $(FIXCONFIG_DIRS) ; do \
			if test -d $$path ; then \
				echo "  ==> fixconfig: $$path" ; \
				replacer $$path $(FIXCONFIG_RMPATHS) ; \
			fi ; \
		done ; \
	fi

# install		- Test and install the results of a build.
INSTALL_TARGETS = $(addprefix install-,$(INSTALL_SCRIPTS)) $(addprefix install-license-,$(subst /, ,$(LICENSE)))

install: build $(addprefix dep-$(GARDIR)/,$(INSTALLDEPS)) test $(INSTALL_DIRS) $(PRE_INSTALL_TARGETS) pre-install $(INSTALL_TARGETS) post-install $(POST_INSTALL_TARGETS) 
	$(DONADA)

# returns true if install has completed successfully, false
# otherwise
install-p:
	@$(foreach COOKIEFILE,$(INSTALL_TARGETS), test -e $(COOKIEDIR)/$(COOKIEFILE) ;)

# reinstall		- Install the results of a build, ignoring
# 				  "already installed" flag.
reinstall: build
	rm -rf $(COOKIEDIR)/*install*
	$(MAKE) install

# The clean rule.  It must be run if you want to re-download a
# file after a successful checksum (or just remove the checksum
# cookie, but that would be lame and unportable).

CLEAN_SCRIPTS ?= all
CLEAN_TARGETS  = $(addprefix clean-,$(CLEAN_SCRIPTS))

clean: $(CLEAN_TARGETS)

# Backwards compatability
cookieclean: clean-cookies
buildclean:  clean-build
sourceclean: clean-source

clean-all: clean-cookies
	@rm -rf $(DOWNLOADDIR)

clean-cookies: clean-build
	@rm -rf $(COOKIEROOTDIR)

clean-build:
	@rm -rf $(WORKSRC) $(WORKROOTDIR) $(EXTRACTDIR) \
		   $(SCRATCHDIR) $(SCRATCHDIR)-$(COOKIEDIR) \
		   $(SCRATCHDIR)-build $(SCRATCHDIR)-$(COOKIEROOTDIR) \
		   $(LOGDIR) *~

SRC_CLEAN_TARGET ?= clean
clean-source:
	@if test -d $(WORKSRC) ; then \
		( $(MAKE) -C $(WORKSRC) $(SRC_CLEAN_TARGET) || true ) ; \
	fi

# Remove specified files/directories
clean-dirs:
	@for target in "" $(REMOVE_DIRS) ; do \
		test -z "$$target" && continue ; \
		rm -rf $$target ; \
	done ; \

# Clean an image
imageclean:
	@-rm -rf $(COOKIEDIR) $(WORKDIR)

# Print package dependencies
PKGDEP_LIST = $(filter-out $(BUILDDEPS),$(DEPEND_LIST))
printdepends:
	@for depend in "" $(PKGDEP_LIST) ; do \
		test -z "$$depend" && continue ; \
		echo "  $$depend" ; \
		if test -n "$(DEPFILE)" ; then \
			check_pkgdb -o $(DEPFILE) $$depend ; \
		else \
			check_pkgdb $$depend ; \
		fi ; \
	done

# Update inter-package depends
makedepend:
	@for gspec in `gfind $(CURDIR) -type f -name '*.gspec' | ggrep files`; do \
		pkgname=`basename $$gspec .gspec` ; \
		pkgfiles=`dirname $$gspec` ; \
		pkgdir=`dirname $$pkgfiles` ; \
		pkgbuild=`basename $$pkgdir` ; \
		pkgdep="$$pkgname.depend" ; \
		echo " ==> $$pkgbuild ($$pkgname)" ; \
		( cd $$pkgdir ; \
		  rm -f /tmp/$$pkgdep ; \
		  if test -f $$pkgfiles/$$pkgdep ; then \
		  	cat $$pkgfiles/$$pkgdep > /tmp/$$pkgdep ; \
		  fi ; \
		  DEPFILE=/tmp/$$pkgdep $(MAKE) printdepends ; \
		  if test -f /tmp/$$pkgdep ; then \
		  	sort /tmp/$$pkgdep | uniq > $$pkgfiles/$$pkgname.depend ; \
		  fi ) ; \
	done

love:
	@echo "not war!"

# these targets do not have actual corresponding files
.PHONY: all fetch-list beaujolais fetch-p checksum-p extract-p patch-p configure-p build-p install-p package-p love

# apparently this makes all previous rules non-parallelizable,
# but the actual builds of the packages will be, according to
# jdub.
.NOTPARALLEL:
