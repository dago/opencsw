
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

GARDIR ?= gar
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
COOKIEFILE = $(COOKIEDIR)/$(patsubst $(COOKIEDIR)/%,%,$1)
DONADA = @touch $(call COOKIEFILE,$@); echo "	[$@] complete for $(GARNAME)."


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
	@gmake MODULATION=$(2) $(3) $(1)-modulated
	@# This is MAKECOOKIE expanded to use the name of the rule explicily as the rule has
	@# not been evaluated yet. XXX: Use function _MAKECOOKIE for both
	@mkdir -p $(COOKIEDIR)/$(dir $(1)-$(2)) && date >> $(COOKIEDIR)/$(1)-$(2)
	@# The next line has intentionally been left blank to explicitly terminate this make rule

endef

define _modulate_target_nocookie
$(1)-$(2):
	@gmake -s MODULATION=$(2) $(3) $(1)-modulated
	@# The next line has intentionally been left blank to explicitly terminate this make rule

endef

define _modulate_do
$(call _modulate_target,extract,$(2),$(4))
$(call _modulate_target,patch,$(2),$(4))
$(call _modulate_target,configure,$(2),$(4))
$(call _modulate_target_nocookie,reset-configure,$(2),$(4))
$(call _modulate_target,build,$(2),$(4))
$(call _modulate_target_nocookie,reset-build,$(2),$(4))
$(call _modulate_target,test,$(2),$(4))
$(call _modulate_target,install,$(2),$(4))
$(call _modulate_target_nocookie,reset-install,$(2),$(4))
$(call _modulate_target,merge,$(2),$(4))
$(call _modulate_target_nocookie,reset-merge,$(2),$(4))
$(call _modulate_target_nocookie,clean,$(2),$(4))
$(call _modulate_target_nocookie,_modenv,$(2),$(4))
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

define _pmod
	@echo "[ $1 for modulation $(MODULATION): $(foreach M,$(MODULATORS),$M=$($M)) ]"
endef

$(eval $(call _modulate,$(MODULATORS)))


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
EXTRACT_TARGETS-global ?= $(foreach SPEC,$(SPKG_SPECS),$(filter $(SPEC).%,$(DISTFILES)))
EXTRACT_TARGETS = $(addprefix extract-archive-,$(filter-out $(NOEXTRACT),$(if $(EXTRACT_TARGETS-$(MODULATION)),$(EXTRACT_TARGETS-$(MODULATION)),$(DISTFILES))))

# We call an additional extract-modulated without resetting any variables so
# a complete unpacked set goes to the global dir for packaging (like gspec)
extract: checksum $(COOKIEDIR) pre-extract extract-modulated $(addprefix extract-,$(MODULATIONS)) post-extract
	@$(DONADA)

extract-modulated: checksum-modulated $(EXTRACTDIR) $(COOKIEDIR) \
		$(addprefix dep-$(GARDIR)/,$(EXTRACTDEPS)) \
		announce-modulation \
		pre-extract-modulated pre-extract-$(MODULATION) $(EXTRACT_TARGETS) post-extract-$(MODULATION) post-extract-modulated
	@$(DONADA)

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

patch: pre-patch $(addprefix patch-,$(MODULATIONS)) post-patch
	@$(DONADA)

patch-modulated: extract-modulated $(WORKSRC) pre-patch-modulated pre-patch-$(MODULATION) $(PATCH_TARGETS) post-patch-$(MODULATION) post-patch-modulated

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

configure-modulated: verify-isa patch-modulated $(CONFIGURE_IMGDEPS) $(CONFIGURE_BUILDDEPS) $(CONFIGURE_DEPS) \
		$(addprefix srcdep-$(GARDIR)/,$(SOURCEDEPS)) \
		pre-configure-modulated pre-configure-$(MODULATION) $(CONFIGURE_TARGETS) post-configure-$(MODULATION) post-configure-modulated

.PHONY: reset-configure reset-configure-modulated
reconfigure: reset-configure configure

reset-configure: $(addprefix reset-configure-,$(MODULATIONS))
	rm -f $(COOKIEDIR)/configure

reset-configure-modulated:
	rm -f $(addprefix $(COOKIEDIR)/,$(CONFIGURE_TARGETS))

# returns true if configure has completed successfully, false
# otherwise
configure-p:
	@$(foreach COOKIEFILE,$(CONFIGURE_TARGETS), test -e $(COOKIEDIR)/$(COOKIEFILE) ;)

# build			- Actually compile the sources.
BUILD_TARGETS = $(addprefix build-,$(BUILD_CHECK_SCRIPTS)) $(addprefix build-,$(BUILD_SCRIPTS))

build: pre-build $(addprefix build-,$(MODULATIONS)) post-build
	$(DONADA)

# Build for a specific architecture
build-modulated-check:
	$(if $(filter ERROR,$(ARCHFLAGS_$(GARCOMPILER)_$*)),                                            \
		$(error Code for the architecture $* can not be produced with the compiler $(GARCOMPILER))      \
	)

build-modulated: verify-isa configure-modulated pre-build-modulated pre-build-$(MODULATION) $(BUILD_TARGETS) post-build-$(MODULATION) post-build-modulated
	@$(MAKECOOKIE)

# returns true if build has completed successfully, false
# otherwise
build-p:
	@$(foreach COOKIEFILE,$(BUILD_TARGETS), test -e $(COOKIEDIR)/$(COOKIEFILE) ;)

TEST_TARGETS = $(addprefix test-,$(TEST_SCRIPTS))

test: pre-test $(addprefix test-,$(MODULATIONS)) post-test
	$(DONADA)

test-modulated: build-modulated pre-test-modulated pre-test-$(MODULATION) $(TEST_TARGETS) post-test-$(MODULATION) post-test-modulated
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
INSTALL_TARGETS = $(addprefix install-,$(INSTALL_SCRIPTS))

install: pre-install $(addprefix install-,$(MODULATIONS)) post-install
	$(DONADA)

install-modulated: build-modulated $(addprefix dep-$(GARDIR)/,$(INSTALLDEPS)) test-modulated $(INSTALL_DIRS) $(PRE_INSTALL_TARGETS) pre-install-modulated pre-install-$(MODULATION) $(INSTALL_TARGETS) post-install-$(MODULATION) post-install-modulated $(POST_INSTALL_TARGETS) 
	@$(MAKECOOKIE)

# returns true if install has completed successfully, false
# otherwise
install-p:
	@$(foreach COOKIEFILE,$(INSTALL_TARGETS), test -e $(COOKIEDIR)/$(COOKIEFILE) ;)



# reinstall		- Install the results of a build, ignoring
# 				  "already installed" flag.
.PHONY: reinstall reset-install reset-install-modulated
reinstall: reset-install install

reset-install: reset-merge $(addprefix reset-install-,$(MODULATIONS))
	@rm -f $(foreach M,$(MODULATIONS),$(COOKIEDIR)/install-$M) $(COOKIEDIR)/install $(COOKIEDIR)/post-install

reset-install-modulated:
	@$(call _pmod,Reset install state)
	@rm -rf $(INSTALLISADIR) $(COOKIEDIR)/install-work
	@rm -f $(COOKIEDIR)/install-modulated

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
#
# Automatic merging is only possible if you have the default modulation "ISA"
# Otherwise you *must* specify merge scripts for all modulations.

ifeq ($(NEEDED_ISAS),$(ISA_DEFAULT))
MERGE_SCRIPTS_isa-$(ISA_DEFAULT) ?= copy-all $(EXTRA_MERGE_SCRIPTS_$(ISA_DEFAULT)) $(EXTRA_MERGE_SCRIPTS)
else
ISAEXEC_DIRS ?= $(if $(NO_ISAEXEC),,$(bindir) $(sbindir) $(libexecdir))
MERGE_DIRS_isa-$(ISA_DEFAULT) ?=
MERGE_DIRS_isa-$(ISA) ?= $(bindir) $(sbindir) $(libexecdir) $(libdir)
MERGE_SCRIPTS_isa-$(ISA_DEFAULT) ?= copy-relocate $(EXTRA_MERGE_SCRIPTS_isa-$(ISA)) $(EXTRA_MERGE_SCRIPTS)
MERGE_SCRIPTS_isa-$(ISA) ?= copy-relocated-only $(EXTRA_MERGE_SCRIPTS_isa-$(ISA)) $(EXTRA_MERGE_SCRIPTS)
endif

# These directories get relocated into their ISA subdirectories
MERGE_DIRS ?= $(MERGE_DIRS_$(MODULATION))

# These files get relocated and will be replaced by the isaexec-wrapper
_ISAEXEC_FILES = $(filter-out $(foreach F,$(ISAEXEC_EXCLUDE_FILES),$(PKGROOT)$(F)), \
			$(wildcard $(foreach D,$(ISAEXEC_DIRS),$(PKGROOT)$(D)/* )) \
		)
ISAEXEC_FILES ?= $(if $(_ISAEXEC_FILES),$(patsubst $(PKGROOT)%,%,		\
	$(shell for F in $(_ISAEXEC_FILES); do		\
		if test -f "$$F"; then echo $$F; fi;	\
	done)),)

ifneq ($(ISAEXEC_FILES),)
_EXTRA_GAR_PKGS += CSWisaexec
endif

# These merge-rules are actually processed for the current modulation
MERGE_TARGETS ?= $(addprefix merge-,$(MERGE_SCRIPTS_$(MODULATION))) $(EXTRA_MERGE_TARGETS)

# Include only these files
ifeq ($(origin MERGE_INCLUDE_FILES_$(MODULATION)), undefined)
_MERGE_INCLUDE_FILES = $(MERGE_INCLUDE_FILES)
else
_MERGE_INCLUDE_FILES = $(MERGE_INCLUDE_FILES_$(MODULATION))
endif
_MERGE_INCLUDE_FILES += $(EXTRA_MERGE_INCLUDE_FILES) $(EXTRA_MERGE_INCLUDE_FILES_$(MODULATION))

# This can be defined in category.mk
MERGE_EXCLUDE_CATEGORY ?= $(_MERGE_EXCLUDE_CATEGORY)

MERGE_EXCLUDE_INFODIR ?= $(sharedstatedir)/info/dir
MERGE_EXCLUDE_LIBTOOL ?= $(libdir)/.*\.la
MERGE_EXCLUDE_BACKUPFILES ?= .*\~
MERGE_EXCLUDE_STATICLIBS ?= $(libdir)/.*\.a
MERGE_EXCLUDE_DEFAULT ?= $(MERGE_EXCLUDE_CATEGORY) $(MERGE_EXCLUDE_INFODIR) $(MERGE_EXCLUDE_LIBTOOL) $(MERGE_EXCLUDE_BACKUPFILES) $(MERGE_EXCLUDE_STATICLIBS)

# Exclude these files
ifeq ($(origin MERGE_EXCLUDE_FILES_$(MODULATION)), undefined)
_MERGE_EXCLUDE_FILES = $(MERGE_EXCLUDE_FILES)
else
_MERGE_EXCLUDE_FILES = $(MERGE_EXCLUDE_FILES_$(MODULATION))
endif
_MERGE_EXCLUDE_FILES += $(EXTRA_MERGE_EXCLUDE_FILES) $(EXTRA_MERGE_EXCLUDE_FILES_$(MODULATION)) $(MERGE_EXCLUDE_DEFAULT)

# This variable contains parameter for pax to honor global file inclusion/exclusion
# Exclude by replacing files with the empty string
_INC_EXT_RULE = $(foreach F,$(_MERGE_EXCLUDE_FILES),-s ',^\.$F$$,,')
# Replace files by itself terminating on first match
_INC_EXT_RULE += $(foreach F,$(_MERGE_INCLUDE_FILES),-s ",^\(\.$F\)\$,\1,")

# These are used during merge phase to determine the base installation directory
MERGEBASE_$(bindir)     ?= $(bindir_install)
MERGEBASE_$(sbindir)    ?= $(sbindir_install)
MERGEBASE_$(libexecdir) ?= $(libexecdir_install)
MERGEBASE_$(libdir)     ?= $(libdir_install)

define mergebase
$(if $(MERGEBASE_$(1)),$(MERGEBASE_$(1)),$(1))
endef

# A package is compiled for the pathes defined in $(bindir), $(libdir), etc.
# These may not be the standard pathes, because specific ISA compilation
# could have appended e. g. /64 for .pc-pathes to be correct. Anyway these
# pathes may need to be rewritten e. g. from lib/64 to lib/amd64. Here,
# $(libdir) has the memorymodel-directory appended, whereas $(libdir_install)
# has not, so we use this one for appending.


_PAX_ARGS = $(_INC_EXT_RULE) $(EXTRA_PAX_ARGS)

# The basic merge merges the compiles for all ISAs on the current architecture
merge: checksum pre-merge $(addprefix merge-,$(MODULATIONS)) merge-license post-merge
	@$(DONADA)

# This merges the 
merge-modulated: install-modulated pre-merge-modulated pre-merge-$(MODULATION) $(MERGE_TARGETS) post-merge-$(MODULATION) post-merge-modulated
	@$(MAKECOOKIE)

# Copy the whole tree verbatim
merge-copy-all: $(PKGROOT) $(INSTALLISADIR)
	@(cd $(INSTALLISADIR); pax -r -w -v $(_PAX_ARGS) \
		$(foreach DIR,$(MERGE_DIRS),-s ",^\(\.$(DIR)/\),.$(call mergebase,$(DIR))/,p") \
		. $(PKGROOT))
	@$(MAKECOOKIE)

# Copy only the merge directories
merge-copy-only: $(PKGROOT)
	@(cd $(INSTALLISADIR); pax -r -w -v $(_PAX_ARGS) \
		$(foreach DIR,$(MERGE_DIRS),-s ",^\(\.$(DIR)/\),.$(call mergebase,$(DIR))/,p") -s ",.*,," \
		. $(PKGROOT) \
	)
	@$(MAKECOOKIE)

# Copy the whole tree and relocate the directories in $(MERGE_DIRS)
merge-copy-relocate: $(PKGROOT) $(INSTALLISADIR)
	@(cd $(INSTALLISADIR); pax -r -w -v $(_PAX_ARGS) \
		$(foreach DIR,$(MERGE_DIRS),-s ",^\(\.$(DIR)/\),.$(call mergebase,$(DIR))/$(ISA)/,p") \
		. $(PKGROOT) \
	)
	@$(MAKECOOKIE)

# Copy only the relocated directories
merge-copy-relocated-only: $(PKGROOT) $(INSTALLISADIR)
	@(cd $(INSTALLISADIR); pax -r -w -v $(_PAX_ARGS) \
		$(foreach DIR,$(MERGE_DIRS),-s ",^\(\.$(DIR)/\),.$(call mergebase,$(DIR))/$(ISA)/,p") -s ",.*,," \
		 . $(PKGROOT) \
	)
	@$(MAKECOOKIE)

.PHONY: remerge reset-merge reset-merge-modulated
remerge: reset-merge merge

reset-merge: reset-package $(addprefix reset-merge-,$(MODULATIONS))
	@rm -f $(foreach M,$(MODULATIONS),$(COOKIEDIR)/merge-$M) $(COOKIEDIR)/merge
	@rm -rf $(PKGROOT)

reset-merge-modulated:
	@$(call _pmod,Reset merge state)
	@rm -f $(COOKIEDIR)/merge-*

# The clean rule.  It must be run if you want to re-download a
# file after a successful checksum (or just remove the checksum
# cookie, but that would be lame and unportable).

clean: $(addprefix clean-,$(MODULATIONS))
	@rm -rf $(WORKROOTDIR) $(COOKIEROOTDIR) $(DOWNLOADDIR)

clean-modulated:
	$(call _pmod,Cleaning )
	@rm -rf $(WORKSRC) $(EXTRACTDIR) \
		   $(SCRATCHDIR) $(SCRATCHDIR)-$(COOKIEDIR) \
		   $(SCRATCHDIR)-build $(SCRATCHDIR)-$(COOKIEROOTDIR) \
		   $(LOGDIR) *~
	@rm -rf $(COOKIEDIR)


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
