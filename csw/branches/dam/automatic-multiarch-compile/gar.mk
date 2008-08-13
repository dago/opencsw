
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

#GARDIR ?= ../..
#ifeq ($(origin GARDIR), undefined)
#GARDIR := $(CURDIR)/../..
#endif

GARDIR ?= ../..
GARBIN  = $(GARDIR)/bin

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
#DONADA = @touch $(COOKIEDIR)/$@; echo "	[$@] complete for $(GARNAME)."
DONADA = @touch $(COOKIEDIR)/$(patsubst $(COOKIEDIR)/%,%,$@); echo "	[$@] complete for $(GARNAME)."

# TODO: write a stub rule to print out the name of a rule when it
# *does* do something, and handle indentation intelligently.

# Default sequence for "all" is:  fetch checksum extract patch configure build
all: build

# include the configuration file to override any of these variables
include $(GARDIR)/gar.conf.mk
include $(GARDIR)/gar.lib.mk

#################### DIRECTORY MAKERS ####################

# This is to make dirs as needed by the base rules
$(sort $(DOWNLOADDIR) $(PARTIALDIR) $(COOKIEDIR) $(WORKSRC) $(WORKDIR) $(EXTRACTDIR) $(FILEDIR) $(SCRATCHDIR) $(PKGROOT) $(INSTALL_DIRS) $(INSTALLISADIR) $(GARCHIVEDIR) $(GARPKGDIR) $(STAGINGDIR)) $(COOKIEDIR)/%:
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

# ========================= MODULATIONS ======================== 

# The default is to modulate over ISAs
MODULATORS ?= ISA $(EXTRA_MODULATORS) $(EXTRA_MODULATORS_$(GARCH))
MODULATIONS_ISA = $(NEEDED_ISAS)

tolower = $(shell echo $(1) | tr '[A-Z]' '[a-z]')
expand_modulator_1 = $(addprefix $(call tolower,$(1))-,$(MODULATIONS_$(1)))
# This expands to the list of all modulators with their respective modulations
modulations = $(if $(word 2,$(1)),\
	$(foreach P,$(call expand_modulator_1,$(firstword $(1))),\
		$(addprefix $(P)-,$(call modulations,$(wordlist 2,$(words $(1)),$(1))))\
	),\
	$(call expand_modulator_1,$(1)))

MODULATIONS ?= $(strip $(call modulations,$(strip $(MODULATORS))))

# _modulate(ISA STATIC,,,)
# -> _modulate2(STATIC,isa-i386,ISA,ISA=i386)
#    -> _modulate2(,,isa-i386-static-yes,ISA STATIC,ISA=i386 STATIC=yes)
#       -> xxx-isa-i386-static-yes: @gmake xxx ISA=i386 STATIC=yes
#    -> _modulate2(,,isa-i386-static-no,ISA STATIC,ISA=i386 STATIC=no)
#       -> xxx-isa-i386-static-no: @gmake xxx ISA=i386 STATIC=no
# -> _modulate2(STATIC,isa-amd64,ISA,ISA=amd64)
#    -> _modulate2(,,isa-amd64-static-yes,ISA STATIC,ISA=amd64 STATIC=yes)
#       -> xxx-isa-amd64-static-yes: @gmake xxx ISA=amd64 STATIC=yes
#    -> _modulate2(,,isa-amd64-static-no,ISA STATIC,ISA=amd64 STATIC=no)
#       -> xxx-isa-amd64-static-no: @gmake xxx ISA=amd64 STATIC=no

define _modulate_target
$(1)-$(2):
	@gmake -s MODULATION=$(2) $(3) pre-$(1)-$(2) $(1)-modulated post-$(1)-$(2)
	@# This is MAKECOOKIE expanded to use the name of the rule explicily as the rule has
	@# not been evaluated yet. XXX: Use function _MAKECOOKIE for both
	@mkdir -p $(COOKIEDIR)/$(dir $(1)-$(2)) && date >> $(COOKIEDIR)/$(1)-$(2)
	@# The next line has intentionally been left blank to explicitly terminate this make rule

endef

define _modulate_do
xtest-$(2):
	@gmake -s MODULATION=$(2) $(4) _pmod
	@# The next line has intentionally been left blank

$(call _modulate_target,extract,$(2),$(4))
$(call _modulate_target,patch,$(2),$(4))
$(call _modulate_target,configure,$(2),$(4))
$(call _modulate_target,build,$(2),$(4))
$(call _modulate_target,test,$(2),$(4))
$(call _modulate_target,install,$(2),$(4))
$(call _modulate_target,merge,$(2),$(4))
endef

# This evaluates to the make rules for all modulations passed as first argument
# Usage: _modulate( <MODULATORS> )
define _modulate
$(foreach M,$(MODULATIONS_$(firstword $(1))),\
	$(call _modulate2,\
		$(wordlist 2,$(words $(1)),$(1)),\
		$(call tolower,$(firstword $(1)))-$(M),\
		$(firstword $(1)),\
		$(firstword $(1))=$(M)\
	)\
)
endef

# This is a helper for the recursive _modulate
define _modulate2
$(if $(strip $(1)),\
	$(foreach M,$(MODULATIONS_$(firstword $(1))),\
		$(call _modulate2,\
			$(wordlist 2,$(words $(1)),$(1)),\
			$(addprefix $(2)-,$(call tolower,$(firstword $(1)))-$(M)),\
			$(3) $(firstword $(1)),\
			$(4) $(firstword $(1))=$(M)\
		)\
	),\
	$(call _modulate_do,,$(strip $(2)),$(3),$(4))\
)
endef

_pmod:
	@echo "[ Modulation $(MODULATION): $(foreach M,$(MODULATORS),$M=$($M)) ]"

$(eval $(call _modulate,$(MODULATORS)))

moddebug:
	@echo $(strip $(strip $(call _modulate,$(MODULATORS))))

allmod: $(foreach M,$(MODULATIONS),xtest-$(M))


modenv:
	@echo " Modulators: $(MODULATORS)"
	@echo "Modulations: $(MODULATIONS)"
	@echo "M: $(call expand_modulator_1,ISA)"

#patch-isa-%:
#	@echo " ==> Patching for ISA $*"
#	@$(MAKE) ISA=$* pre-patch-isa-$* patch-isa post-patch-isa-$*
#	@$(DONADA)



# ========================= MAIN RULES ========================= 
# The main rules are the ones that the user can specify as a
# target on the "make" command-line.  Currently, they are:
#	prereq fetch-list fetch checksum makesum extract checkpatch patch
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
	@echo "[===== NOW BUILDING: $(DISTNAME) =====]"

#announce-isa:
#	@echo "[===== NOW BUILDING: $(DISTNAME) ISA: $(ISA) =====]"

announce-modulation:
	@echo "[===== NOW BUILDING: $(DISTNAME) MODULATION $(MODULATION): $(foreach M,$(MODULATORS),$M=$($M)) =====]"

# prerequisite	- Make sure that the system is in a sane state for building the package
PREREQUISITE_TARGETS = $(addprefix prerequisitepkg-,$(PREREQUISITE_BASE_PKGS) $(PREREQUISITE_PKGS)) $(addprefix prerequisite-,$(PREREQUISITE_SCRIPTS))

prerequisite: announce pre-everything $(COOKIEDIR) $(DOWNLOADDIR) $(PARTIALDIR) $(addprefix dep-$(GARDIR)/,$(FETCHDEPS)) pre-prerequisite $(PREREQUISITE_TARGETS) post-prerequisite
	$(DONADA)

prerequisitepkg-%:
	@echo " ==> Verifying for installed package $*: \c"
	@(pkginfo -q $*; if [ $$? -eq 0 ]; then echo "installed"; else echo "MISSING"; exit 1; fi)
	@$(MAKECOOKIE)

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

fetch: prerequisite pre-fetch $(FETCH_TARGETS) post-fetch
	@$(DONADA)

# returns true if fetch has completed successfully, false
# otherwise
fetch-p:
	@$(foreach COOKIEFILE,$(FETCH_TARGETS), test -e $(COOKIEDIR)/$(COOKIEFILE) ;)

# checksum		- Use $(CHECKSUMFILE) to ensure that your
# 				  distfiles are valid.
CHECKSUM_TARGETS = $(addprefix checksum-,$(filter-out $(NOCHECKSUM),$(ALLFILES)))

checksum: fetch $(COOKIEDIR) pre-checksum $(CHECKSUM_TARGETS) post-checksum
	@$(DONADA)

# The next rule handles the dependency from the modulated context to
# the contextless checksumming. The rule is called when the cookie
# to the global checksum is requested. If the global checksum has not run,
# then run it. Otherwise it is silently accepted.
checksum-modulated: $(COOKIEDIR)
	@$(MAKE) -s ISA=global checksum
	@$(DONADA)

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
EXTRACT_TARGETS = $(addprefix extract-archive-,$(filter-out $(NOEXTRACT),$(DISTFILES)))

# We call an additional extract-modulated without resetting any variables so
# a complete unpacked set goes to the global dir for packaging (like gspec)
#extract: checksum $(COOKIEDIR) pre-extract extract-isa $(addprefix extract-isa-,$(BUILD_ISAS)) post-extract
extract: checksum $(COOKIEDIR) pre-extract extract-modulated $(addprefix extract-,$(MODULATIONS)) post-extract
	@$(DONADA)

extract-modulated: checksum-modulated $(EXTRACTDIR) $(COOKIEDIR) \
		$(addprefix dep-$(GARDIR)/,$(EXTRACTDEPS)) \
		announce-modulation \
		pre-extract-modulated $(EXTRACT_TARGETS) post-extract-modulated
	@$(DONADA)

#extract-isa-%:
#	@$(MAKE) ISA=$* pre-extract-isa-$* extract-isa post-extract-isa-$*
#	@$(MAKECOOKIE)

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
PATCH_TARGETS = $(addprefix patch-extract-,$(PATCHFILES))

#patch: pre-patch $(addprefix patch-isa-,$(BUILD_ISAS)) post-patch
patch: pre-patch $(addprefix patch-,$(MODULATIONS)) post-patch
	@$(DONADA)

#patch-isa: extract-isa $(WORKSRC) pre-patch-isa $(PATCH_TARGETS) post-patch-isa
patch-modulated: extract-modulated $(WORKSRC) pre-patch-modulated $(PATCH_TARGETS) post-patch-modulated

#patch-isa-%:
#	@echo " ==> Patching for ISA $*"
#	@$(MAKE) ISA=$* pre-patch-isa-$* patch-isa post-patch-isa-$*
#	@$(DONADA)

# returns true if patch has completed successfully, false
# otherwise
patch-p:
	@$(foreach COOKIEFILE,$(PATCH_TARGETS), test -e $(COOKIEDIR)/$(COOKIEFILE) ;)

# makepatch		- Grab the upstream source and diff against $(WORKSRC).  Since
# 				  diff returns 1 if there are differences, we remove the patch
# 				  file on "success".  Goofy diff.
makepatch: $(SCRATCHDIR) $(FILEDIR) $(FILEDIR)/gar-base.diff
	$(DONADA)

# XXX: Allow patching of pristine sources separate from ISA directories
# XXX: Use makepatch on global/

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

configure: pre-configure $(addprefix configure-,$(MODULATIONS)) post-configure
	$(DONADA)

#configure-isa: patch-isa $(CONFIGURE_IMGDEPS) $(CONFIGURE_BUILDDEPS) $(CONFIGURE_DEPS) \
#		$(addprefix srcdep-$(GARDIR)/,$(SOURCEDEPS)) \
#		pre-configure-isa $(CONFIGURE_TARGETS) post-configure-isa
configure-modulated: patch-modulated $(CONFIGURE_IMGDEPS) $(CONFIGURE_BUILDDEPS) $(CONFIGURE_DEPS) \
		$(addprefix srcdep-$(GARDIR)/,$(SOURCEDEPS)) \
		pre-configure-modulated $(CONFIGURE_TARGETS) post-configure-modulated

#configure-isa-%:
#	@echo " ==> Configuring for ISA $*"
#	@$(MAKE) ISA=$* pre-configure-isa-$* configure-isa post-configure-isa-$*
#	@$(DONADA)

.PHONY: reset-configure reset-configure-modulated
reconfigure: reset-configure configure

reset-configure: 

reconfigure-isa-%:

reset-configure:
	@$(foreach ISA,$(NEEDED_ISAS),$(MAKE) -s ISA=$(ISA) reset-configure-isa;)

reconfigure-isa-%:
	@$(MAKE) -s ISA=$* reset-configure-isa configure-isa

#reset-configure-isa:
#	@echo " ==> Reset configure state for ISA $(ISA)"
#	@rm -rf xxx
#	@$(MAKE) -s ISA=$* reset-configure-isa

# returns true if configure has completed successfully, false
# otherwise
configure-p:
	@$(foreach COOKIEFILE,$(CONFIGURE_TARGETS), test -e $(COOKIEDIR)/$(COOKIEFILE) ;)

# build			- Actually compile the sources.
BUILD_TARGETS = $(addprefix build-,$(BUILD_CHECK_SCRIPTS)) $(addprefix build-,$(BUILD_SCRIPTS))

build: pre-build $(addprefix build-,$(MODULATIONS)) post-build
	$(DONADA)

# Build for a specific architecture
#build-isa: configure-isa pre-build-isa $(BUILD_TARGETS) post-build-isa
#	@$(MAKECOOKIE)
build-modulated-check:
	$(if $(filter ERROR,$(ARCHFLAGS_$(GARCOMPILER)_$*)),                                            \
		$(error Code for the architecture $* can not be produced with the compiler $(GARCOMPILER))      \
	)

build-modulated: configure-modulated pre-build-modulated $(BUILD_TARGETS) post-build-modulated
	@$(MAKECOOKIE)

# Build for a certain architecture
#build-isa-%:
#	@echo " ==> Building for ISA $*"
#	$(if $(filter ERROR,$(ARCHFLAGS_$(GARCOMPILER)_$*)),                                            \
#		$(error Code for the architecture $* can not be produced with the compiler $(GARCOMPILER))      \
#	)
#	@$(MAKE) ISA=$* pre-build-isa-$* build-isa post-build-isa-$*
#	@$(MAKECOOKIE)

# returns true if build has completed successfully, false
# otherwise
build-p:
	@$(foreach COOKIEFILE,$(BUILD_TARGETS), test -e $(COOKIEDIR)/$(COOKIEFILE) ;)

TEST_TARGETS = $(addprefix test-,$(TEST_SCRIPTS))

test: $(addprefix test-,$(MODULATIONS))
	$(DONADA)

test-modulated: build-modulated pre-test $(TEST_TARGETS) post-test
	$(DONADA)

#test-isa-%:
#	@echo " ==> Testing for ISA $*"
#	@$(MAKE) ISA=$* test-isa
#	@$(MAKECOOKIE)

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

install: pre-install $(addprefix install-,$(MODULATIONS)) post-install
	$(DONADA)

install-modulated: build-modulated $(addprefix dep-$(GARDIR)/,$(INSTALLDEPS)) test-modulated $(INSTALL_DIRS) $(PRE_INSTALL_TARGETS) pre-install-modulated $(INSTALL_TARGETS) post-install-modulated $(POST_INSTALL_TARGETS) 
	@$(MAKECOOKIE)

#install-isa-%:
#	@echo " ==> Installing for ISA $*"
#	@$(MAKE) ISA=$* pre-install-isa-$* install-isa post-install-isa-$*
#	@$(MAKECOOKIE)

# returns true if install has completed successfully, false
# otherwise
install-p:
	@$(foreach COOKIEFILE,$(INSTALL_TARGETS), test -e $(COOKIEDIR)/$(COOKIEFILE) ;)



# reinstall		- Install the results of a build, ignoring
# 				  "already installed" flag.
.PHONY: reset-install reset-install-isa
reinstall: reset-install install

reset-install:
	@$(foreach ISA,$(NEEDED_ISAS),$(MAKE) -s ISA=$(ISA) reset-install-isa;)

reinstall-isa-%:
	@$(MAKE) -s ISA=$* reset-install-isa install-isa

reset-install-isa:
	@echo " ==> Reset install state for ISA $(ISA)"
	@rm -rf $(INSTALLISADIR) $(COOKIEDIR)/*install*
	@$(MAKE) -s ISA=$* reset-merge-isa

# merge in all isas to the package directory after installation

# Merging in general allows the selection of parts from different ISA builds into the package
# Per default merging is done differently depending on
# (a) if the sources are build for more than one ISA
# (b) if the executables should be replaced by isaexec or not
# 
# - If there is only one ISA to build for everything is copied verbatim to PKGROOT.
# - If there are builds for more than one ISA the destination differs depending on if
#   the binaries should be executed by isaexec. This is usually bin, sbin and libexec.
#
# default:        relocate to ISA subdirs if more than one ISA, use isaexec-wrapper for bin/, etc.
# NO_ISAEXEC = 1: ISA_DEFAULT gets installed in bin/..., all others in bin/$ISA/

ifeq ($(NEEDED_ISAS),$(ISA_DEFAULT))
MERGE_SCRIPTS_$(ISA_DEFAULT) ?= copy-all $(EXTRA_MERGE_SCRIPTS_$(ISA_DEFAULT)) $(EXTRA_MERGE_SCRIPTS)
else
ISAEXEC_DIRS ?= $(if $(NO_ISAEXEC),,$(bindir) $(sbindir) $(libexecdir))
ISA_RELOCATE_DIRS_$(ISA_DEFAULT) ?=
ISA_RELOCATE_DIRS_$(ISA) ?= $(bindir) $(sbindir) $(libexecdir) $(libdir)
MERGE_SCRIPTS_$(ISA_DEFAULT) ?= copy-relocate $(EXTRA_MERGE_SCRIPTS_$(ISA)) $(EXTRA_MERGE_SCRIPTS)
MERGE_SCRIPTS_$(ISA) ?= copy-relocated-only $(EXTRA_MERGE_SCRIPTS_$(ISA)) $(EXTRA_MERGE_SCRIPTS)
_EXTRA_GAR_PKGS += CSWisaexec
endif

# These directories get relocated into their ISA subdirectories
ISA_RELOCATE_DIRS ?= $(ISA_RELOCATE_DIRS_$(ISA))

# These files get relocated and will be replaced by the isaexec-wrapper
_ISAEXEC_FILES = $(wildcard $(foreach D,$(ISAEXEC_DIRS),$(PKGROOT)$(D)/* ))
ISAEXEC_FILES ?= $(if $(_ISAEXEC_FILES),$(patsubst $(PKGROOT)%,%,		\
	$(shell for F in $(_ISAEXEC_FILES); do		\
		if test -f "$$F"; then echo $$F; fi;	\
	done)),)

# These files get relocated.
# ISA_RELOCATE_DIRS is expanded to individual files here. All further
# processing is done using these files.
ISA_RELOCATE_FILES ?= $(patsubst $(PKGROOT)%,%,$(wildcard $(foreach D,$(ISA_RELOCATE_DIRS),$(PKGROOT)$(D)/*))) $(ISAEXEC_FILES) $(EXTRA_ISA_RELOCATE_FILES)

# These merge-rules are actually processed for the current ISA
MERGE_TARGETS = $(addprefix merge-,$(MERGE_SCRIPTS_$(ISA)))

# Include only these files
ifeq ($(origin MERGE_INCLUDE_FILES_$(ISA)), undefined)
_MERGE_INCLUDE_FILES = $(MERGE_INCLUDE_FILES)
else
_MERGE_INCLUDE_FILES = $(MERGE_INCLUDE_FILES_$(ISA))
endif
_MERGE_INCLUDE_FILES += $(EXTRA_MERGE_INCLUDE_FILES) $(EXTRA_MERGE_INCLUDE_FILES_$(ISA))

# Exclude these files
ifeq ($(origin MERGE_EXCLUDE_FILES_$(ISA)), undefined)
_MERGE_EXCLUDE_FILES = $(MERGE_EXCLUDE_FILES)
else
_MERGE_EXCLUDE_FILES = $(MERGE_EXCLUDE_FILES_$(ISA))
endif
_MERGE_EXCLUDE_FILES += $(EXTRA_MERGE_EXCLUDE_FILES) $(EXTRA_MERGE_EXCLUDE_FILES_$(ISA))

# This variable contains parameter for pax to honor global file inclusion/exclusion
# Include first, replace files by itself terminating on first match
_INC_EXT_RULE = $(foreach F,$(_MERGE_INCLUDE_FILES),-s ",^\(\.$F\)\$,\1,")
# Exclude by replacing files with the empty string
_INC_EXT_RULE += $(foreach F,$(_MERGE_EXCLUDE_FILES),-s ',^\.$F$$,,')

_PAX_ARGS = $(_INC_EXT_RULE) $(EXTRA_PAX_ARGS)

# The basic merge merges the compiles for all ISAs on the current architecture
merge: checksum pre-merge $(addprefix merge-,$(MODULATIONS)) post-merge
	@$(DONADA)

# This merges the 
merge-modulated: install-modulated pre-merge-modulated $(MERGE_TARGETS) post-merge-modulated
	@$(MAKECOOKIE)

#merge-isa-%:
#	@echo " ==> Merging ISAs together for packaging"
#	@$(MAKE) ISA=$* pre-merge-isa-$* merge-isa post-merge-isa-$*
#	@$(MAKECOOKIE)

# Copy the whole tree verbatim
merge-copy-all: $(PKGROOT) $(INSTALLISADIR)
	@(cd $(INSTALLISADIR); pax -r -w -v $(_PAX_ARGS) . $(PKGROOT))
	@$(MAKECOOKIE)

# Copy the whole tree and relocate the directories in $(ISA_RELOCATE_DIRS)
merge-copy-relocate: $(PKGROOT) $(INSTALLISADIR)
	@(cd $(INSTALLISADIR); pax -r -w -v $(_PAX_ARGS) \
		$(foreach DIR,$(ISA_RELOCATE_DIRS),-s ",^\(\.$(DIR)/\),\1$(ISA)/,p" ) \
		. $(PKGROOT) \
	)
	@$(MAKECOOKIE)

# Copy only the relocated directories
merge-copy-relocated-only: $(PKGROOT) $(INSTALLISADIR)
	@(cd $(INSTALLISADIR); $(foreach DIR,$(ISA_RELOCATE_DIRS), \
		if [ -d .$(DIR) ]; then pax -r -w -v $(_PAX_ARGS) -s ",^\(\.$(DIR)/\),\1$(ISA)/,p" .$(DIR) $(PKGROOT); fi; \
		) \
	)
	@$(MAKECOOKIE)

remerge: reset-merge remove-timestamp merge

remerge-isa-%:
	@$(MAKE) -s ISA=$* reset-merge-isa

reset-merge:
	@$(foreach ISA,$(NEEDED_ISAS),$(MAKE) -s ISA=$(ISA) reset-merge-isa;)
	@rm -rf $(PKGROOT)

reset-merge-isa:
	@echo " ==> Reset merge state for ISA $(ISA)"
	@rm -f $(COOKIEDIR)/merge $(COOKIEDIR)/merge-*
	@rm -f $(COOKIEROOTDIR)/$(ISA_DEFAULT)/merge-isa-$(ISA)
	@rm -f $(COOKIEROOTDIR)/$(ISA_DEFAULT)/merge-isa

# The clean rule.  It must be run if you want to re-download a
# file after a successful checksum (or just remove the checksum
# cookie, but that would be lame and unportable).

CLEAN_SCRIPTS ?= all
CLEAN_TARGETS  = $(addprefix clean-,$(CLEAN_SCRIPTS))

clean: $(addprefix clean-isa-,$(REQUESTED_ISAS)) clean-all
	@rm -rf $(WORKROOTDIR)

clean-isa: clean-build 
	@rm -rf $(COOKIEDIR)

clean-isa-%:
	@$(MAKE) -s ISA=$* clean-isa

clean-all: clean-cookies
	@rm -rf $(DOWNLOADDIR)

clean-cookies: clean-build
	@rm -rf $(COOKIEROOTDIR)

clean-build:
	@echo " ==> Cleaning ISA $(ISA)"
	@rm -rf $(WORKSRC) $(EXTRACTDIR) \
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
	@echo " ==> Removing $(COOKIEDIR)"
	@-rm -rf $(COOKIEDIR)
	@echo " ==> Removing $(WORKDIR)"
	@-rm -rf $(WORKDIR)

spotless: imageclean
	@echo " ==> Removing $(DESTDIR)"
	@-rm -rf $(DESTDIR)

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

buildstatus:

love:
	@echo "not war!"

# these targets do not have actual corresponding files
.PHONY: all fetch-list beaujolais fetch-p checksum-p extract-p patch-p configure-p build-p install-p package-p love

# apparently this makes all previous rules non-parallelizable,
# but the actual builds of the packages will be, according to
# jdub.
.NOTPARALLEL:
