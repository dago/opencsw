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

ifneq ($(abspath /),/)
$(error Your version of 'make' is too old: $(MAKE_VERSION). Please make sure you are using at least 3.81)
endif

$(if $(GARNAME),$(error The deprecated variable 'GARNAME' is defined, please replace it with 'NAME'))
$(if $(GARVERSION),$(error The deprecated variable 'GARVERSION' is defined, please replace it with 'VERSION'))

# $(GARDIR) is pre-set by the top-level category.mk
GARBIN  = $(GARDIR)/bin

DIRSTODOTS = $(subst . /,./,$(patsubst %,/..,$(subst /, ,/$(1))))
ROOTFROMDEST = $(call DIRSTODOTS,$(DESTDIR))
MAKEPATH = $(shell echo $(1) | perl -lne 'print join(":", split)')
TOLOWER = $(shell echo $(1) | tr '[A-Z]' '[a-z]')

# If you call this the value is only evaluated the first time
# Usage: $(call SETONCE,A,MyComplexVariableEvaluatedOnlyOnce)
SETONCE = $(eval $(1) ?= $(2))

#meant to take a git url and return just the $proj.git part
GITPROJ = $(lastword $(subst /, ,$(1)))

# GAR uses PARALLELMFLAGS to propagate make options (judging by the name, mainly
# intended for -j). Options are determined via MFLAGS which also contains other
# options, thus we need to filter harmful ones. e.g. -I breaks upstream builds
# that use non-gnu make (Fatal error: Unknown option `-I'). Info on M*FLAGS:
# http://www.gnu.org/s/hello/manual/make/Options_002fRecursion.html
PARALLELMFLAGS ?= $(shell echo $(MFLAGS) | gsed 's,-I [^ ]*,,g' )
export PARALLELMFLAGS

DISTNAME ?= $(NAME)-$(VERSION)

DYNSCRIPTS := $(foreach PKG,$(SPKG_SPECS),$(foreach SCR,$(ADMSCRIPTS),$(if $(value $(PKG)_$(SCR)), $(PKG).$(SCR))))
_LOCALFILES = $(notdir $(wildcard files/*))
_NOCHECKSUM += $(DYNSCRIPTS) $(_LOCALFILES) $(foreach R,$(GIT_REPOS),$(call GITPROJ,$(R))) $(_EXTRA_GAR_NOCHECKSUM)

DISTFILES += $(_EXTRA_GAR_DISTFILES)

# Allow overriding of only specific components of ALLFILES by clearing e. g. 'ALLFILES_DYNSCRIPTS = '
ALLFILES_DISTFILES ?= $(DISTFILES)
ALLFILES_PATCHFILES ?= $(PATCHFILES) $(foreach M,$(MODULATIONS),$(PATCHFILES_$M))
ALLFILES_DYNSCRIPTS ?= $(DYNSCRIPTS)
ALLFILES_GIT_REPOS ?= $(foreach R,$(GIT_REPOS),$(call GITPROJ,$(R)))
ALLFILES ?= $(sort $(ALLFILES_DISTFILES) $(ALLFILES_PATCHFILES) $(ALLFILES_DYNSCRIPTS) $(ALLFILES_GIT_REPOS) $(EXTRA_ALLFILES) $(_EXTRA_GAR_ALLFILES))

ifeq ($(MAKE_INSTALL_DIRS),1)
INSTALL_DIRS = $(addprefix $(DESTDIR),$(prefix) $(exec_prefix) $(bindir) $(sbindir) $(libexecdir) $(datadir) $(sysconfdir) $(sharedstatedir) $(localstatedir) $(libdir) $(infodir) $(lispdir) $(includedir) $(mandir) $(foreach NUM,1 2 3 4 5 6 7 8, $(mandir)/man$(NUM)) $(sourcedir))
else
INSTALL_DIRS =
endif

# For rules that do nothing, display what dependencies they
# successfully completed
#DONADA = @echo "	[$@] complete.  Finished rules: $+"
#DONADA = @touch $(COOKIEDIR)/$@; echo "	[$@] complete for $(NAME)."
COOKIEFILE = $(COOKIEDIR)/$(patsubst $(COOKIEDIR)/%,%,$1)
DONADA = @touch $(call COOKIEFILE,$@); echo "	[$@] complete for $(NAME)."


# TODO: write a stub rule to print out the name of a rule when it
# *does* do something, and handle indentation intelligently.

# Default sequence for "all" is:  fetch checksum extract patch configure build
all: build

# include the configuration file to override any of these variables
include $(GARDIR)/gar.conf.mk

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

MODULATIONS ?= $(filter-out $(SKIP_MODULATIONS),$(strip $(call modulations,$(strip $(MODULATORS)))))

include $(GARDIR)/gar.lib.mk

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
	@$(MAKE) MODULATION=$(2) $(3) $(1)-modulated
	@# This is MAKECOOKIE expanded to use the name of the rule explicily as the rule has
	@# not been evaluated yet. XXX: Use function _MAKECOOKIE for both
	@mkdir -p $(COOKIEDIR)/$(dir $(1)-$(2)) && date >> $(COOKIEDIR)/$(1)-$(2)
	@# The next line has intentionally been left blank to explicitly terminate this make rule

endef

define _modulate_target_nocookie
$(1)-$(2):
	@$(MAKE) -s MODULATION=$(2) $(3) $(1)-modulated
	@# The next line has intentionally been left blank to explicitly terminate this make rule

endef

# Heads up: Don't use MAKEFLAGS to propagate -I to remote GAR invocations as
# this will also make it visible to the build environment. Some software builds
# use hard-coded non-GNU make which then errs out on -I (unknown option).
define _modulate_merge
$(foreach ASSIGNMENT,$(3),
merge-$(2): $(ASSIGNMENT)
)
merge-$(2): BUILDHOST=$$(call modulation2host)
merge-$(2):
	@echo "[===== Building modulation '$(2)' on host '$$(BUILDHOST)' =====]"
	$$(if $$(and $$(BUILDHOST),$$(filter-out $$(THISHOST),$$(BUILDHOST))),\
		$(SSH) $$(BUILDHOST) "PATH=$$(PATH) $(MAKE) -I $$(GARDIR) -C $$(CURDIR) $(if $(GAR_PLATFORM),GAR_PLATFORM=$(GAR_PLATFORM)) MODULATION=$(2) $(3) merge-modulated",\
		$(MAKE) $(if $(GAR_PLATFORM),GAR_PLATFORM=$(GAR_PLATFORM)) MODULATION=$(2) $(3) merge-modulated\
	)
	@# The next line has intentionally been left blank to explicitly terminate this make rule

endef

define _modulate_do
$(call _modulate_target,extract,$(2),$(4))
$(call _modulate_target,patch,$(2),$(4))
$(call _modulate_target_nocookie,makepatch,$(2),$(4))
$(call _modulate_target,configure,$(2),$(4))
$(call _modulate_target_nocookie,reset-configure,$(2),$(4))
$(call _modulate_target,build,$(2),$(4))
$(call _modulate_target_nocookie,reset-build,$(2),$(4))
$(call _modulate_target,test,$(2),$(4))
$(call _modulate_target_nocookie,reset-test,$(2),$(4))
$(call _modulate_target,install,$(2),$(4))
$(call _modulate_target_nocookie,reset-install,$(2),$(4))
#$(call _modulate_target,merge,$(2),$(4))
$(call _modulate_merge,,$(2),$(4))
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

# --- This next block allows you to use collapsed ISAs in modulations
#   isa-default-...      instead of isa-sparcv8-... and isa-i386-...
#   isa-default64-...    instead of isa-sparcv9-... and isa-amd64-...
#   isa-extra-...        instead of any other ISA (if default64 is undefined it falls back to 'extra')

__collapsedisa = $(strip $(or $(and $(filter $(ISA_DEFAULT_sparc) $(ISA_DEFAULT_i386),$(1)),default),\
                              $(and $(filter $(ISA_DEFAULT64_sparc) $(ISA_DEFAULT64_i386),$(1)),default64),\
                              extra))

__collapsedisa64 = default64
__collapsedisaextra = extra

__isacollapsedmodulation_1 = $(call tolower,$(1))-$(if $(filter ISA,$(1)),$(call $(2),$(ISA)),$($(1)))
__isacollapsedmodulation = $(if $(word 2,$(1)),\
		$(foreach P,$(call __isacollapsedmodulation_1,$(firstword $(1)),$(2)),\
			$(addprefix $(P)-,$(call __isacollapsedmodulation,$(wordlist 2,$(words $(1)),$(1))))\
		),\
		$(call __isacollapsedmodulation_1,$(1),$(2)))

# This is the name of the current modulation but with the ISA i386, sparcv8 and amd64, sparcv9 replaced
# with the collapsed name 'default', 'default64' and everything else as 'extra'.
MODULATION_ISACOLLAPSED = $(strip $(call __isacollapsedmodulation,$(strip $(MODULATORS)),__collapsedisa))

# This is the name of the current modulation but with the ISA replaced with 'default64'
MODULATION_ISACOLLAPSED64 = $(strip $(call __isacollapsedmodulation,$(strip $(MODULATORS)),__collapsedisa64))

# This is the name of the current modulation but with the ISA replaced with 'extra'
MODULATION_ISACOLLAPSEDEXTRA = $(strip $(call __isacollapsedmodulation,$(strip $(MODULATORS)),__collapsedisaextra))

# $(warning Mod: $(MODULATION) ISA: $(ISA) coll: $(MODULATION_ISACOLLAPSED) 64: $(MODULATION_ISACOLLAPSED64) extra: $(MODULATION_ISACOLLAPSEDEXTRA))

# Call this function to get either the modulation-specific value or the default.
# Instead of $(myvar_$(MODULATION)) $(call modulationvalue,myvar)
define modulationvalue
$(strip $(or $($(1)_$(MODULATION)),\
             $($(1)_$(MODULATION_ISACOLLAPSED)),\
             $($(1)_$(MODULATION_ISACOLLAPSEDEXTRA)),\
))
endef

# --- end of collapsed ISA modulations

#################### DIRECTORY MAKERS ####################

# This is to make dirs as needed by the base rules
$(sort $(DOWNLOADDIR) $(PARTIALDIR) $(COOKIEDIR) $(WORKSRC) $(addprefix $(WORKROOTDIR)/build-,global $(MODULATIONS)) $(EXTRACTDIR) $(FILEDIR) $(SCRATCHDIR) $(PKGROOT) $(INSTALL_DIRS) $(INSTALLISADIR) $(GARCHIVEDIR) $(GARPKGDIR) $(STAGINGDIR)):
	@if test -d $@; then : ; else \
		ginstall -d $@; \
		echo "ginstall -d $@"; \
	fi

$(COOKIEDIR)/%:
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
ALL_PREREQ_PKGS = $(PREREQUISITE_BASE_PKGS) $(BUILD_DEP_PKGS) $(DEP_PKGS) $(foreach S,$(_PKG_SPECS),$(DEP_PKGS_$S))
PREREQUISITE_TARGETS =  $(addprefix prerequisite-,$(PREREQUISITE_SCRIPTS))

# Force to be called in global modulation
prerequisite: $(if $(filter global,$(MODULATION)),announce pre-everything $(COOKIEDIR) $(DOWNLOADDIR) $(PARTIALDIR) $(addprefix dep-$(GARDIR)/,$(FETCHDEPS)) pre-prerequisite check-prereqs $(PREREQUISITE_TARGETS) post-prerequisite)
	$(if $(filter-out global,$(MODULATION)),$(MAKE) -s MODULATION=global prerequisite)
	$(DONADA)

check-prereqs:
	@$(abspath $(GARBIN)/check_for_deps) $(ALL_PREREQ_PKGS)
	@$(MAKECOOKIE)

prerequisitepkg-%:
	@echo " ==> Verifying for installed package $*: \c"
	@(pkginfo -q $*; if [ $$? -eq 0 ]; then echo "installed"; else echo "MISSING"; exit 1; fi)
	@$(MAKECOOKIE)

# fetch-list	- Show list of files that would be retrieved by fetch.
# NOTE: DOES NOT RUN pre-everything!
fetch-list:
	@echo "Distribution files: "
	@$(foreach F,$(DISTFILES),echo "	$F";)
	@echo "Patch files: "
	@$(foreach P,$(PATCHFILES),echo "	$P";)
	@$(foreach M,$(MODULATIONS),$(if $(PATCHFILES_$M),echo "  Modulation $M only: $(PATCHFILES_$M)";))
	@echo "Dynamically generated scripts: "
	@$(foreach D,$(DYNSCRIPTS),echo "	$D";)
	@echo "Git Repos tracked: "
	@$(foreach R,$(GIT_REPOS),echo "       $R";)
	@echo "All potential URLS: "
	@$(foreach U,$(URLS),echo "       $U";)

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
CHECKSUM_TARGETS = $(addprefix checksum-,$(filter-out $(_NOCHECKSUM) $(NOCHECKSUM),$(ALLFILES)))

checksum: fetch $(COOKIEDIR) pre-checksum $(CHECKSUM_TARGETS) post-checksum
	@$(DONADA)

checksum-global: $(if $(filter global,$(MODULATION)),checksum)
	$(if $(filter-out global,$(MODULATION)),$(MAKE) -s MODULATION=global checksum)
	@$(DONADA)

# The next rule handles the dependency from the modulated context to
# the contextless checksumming. The rule is called when the cookie
# to the global checksum is requested. If the global checksum has not run,
# then run it. Otherwise it is silently accepted.
checksum-modulated: checksum-global
	@$(DONADA)

# returns true if checksum has completed successfully, false
# otherwise
checksum-p:
	@$(foreach COOKIEFILE,$(CHECKSUM_TARGETS), test -e $(COOKIEDIR)/$(COOKIEFILE) ;)

# makesum		- Generate distinfo (only do this for your own ports!).
GARCHIVE_TARGETS =  $(addprefix $(GARCHIVEDIR)/,$(filter-out $(ALLFILES_DYNSCRIPTS), $(ALLFILES)))

MAKESUM_TARGETS =  $(filter-out $(_NOCHECKSUM) $(NOCHECKSUM),$(ALLFILES))

makesum: fetch $(addprefix $(DOWNLOADDIR)/,$(MAKESUM_TARGETS)) $(GARCHIVE_TARGETS)
	@if test "x$(MAKESUM_TARGETS)" != "x"; then \
		(cd $(DOWNLOADDIR) && gmd5sum $(MAKESUM_TARGETS)) > $(CHECKSUM_FILE) ; \
		echo "Checksums made for $(MAKESUM_TARGETS)" ; \
		cat $(CHECKSUM_FILE) ; \
	else \
		cp /dev/null $(CHECKSUM_FILE) ; \
	fi

# I am always typing this by mistake
makesums: makesum

garchive: checksum $(GARCHIVE_TARGETS) ;

# extract		- Unpacks $(DISTFILES) into $(EXTRACTDIR) (patches are "zcatted" into the patch program)
EXTRACT_TARGETS-global ?= $(addprefix extract-copy-,$(filter-out $(NOEXTRACT),$(DISTFILES) $(DYNSCRIPTS) $(foreach R,$(GIT_REPOS),$(call GITPROJ,$(R)))))
EXTRACT_TARGETS-default = $(addprefix extract-archive-,$(filter-out $(NOEXTRACT),$(DISTFILES) $(DYNSCRIPTS) $(foreach R,$(GIT_REPOS),$(call GITPROJ,$(R)))))
EXTRACT_TARGETS = $(or $(EXTRACT_TARGETS-$(MODULATION)),$(EXTRACT_TARGETS-default))

ifdef REINPLACE_FILES
REINPLACEMENTS ?= default
REINPLACE_MATCH_default ?= $(REINPLACE_MATCH)
REINPLACE_WITH_default ?= $(REINPLACE_WITH)
REINPLACE_FILES_default ?= $(REINPLACE_FILES)
REINPLACE_WHEN_default ?= $(REINPLACE_WHEN)
endif

REINPLACE_MATCH_USRLOCAL = /usr/local
REINPLACE_WITH_USRLOCAL = $(prefix)
REINPLACE_FILES_USRLOCAL = $(REINPLACE_USRLOCAL)

REINPLACE_MATCH_USRSHARE = /usr/share
REINPLACE_WITH_USRSHARE = $(sharedstatedir)
REINPLACE_FILES_USRSHARE = $(REINPLACE_USRSHARE)

_ALL_REINPLACEMENTS = $(REINPLACEMENTS) $(if $(REINPLACE_FILES_USRLOCAL),USRLOCAL) $(if $(REINPLACE_FILES_USRSHARE),USRSHARE)

POSTINSTALL_REINPLACEMENTS = $(foreach R,$(_ALL_REINPLACEMENTS),$(if $(filter postinstall,$(REINPLACE_WHEN_$R)),$R))
POSTEXTRACT_REINPLACEMENTS = $(filter-out $(POSTINSTALL_REINPLACEMENTS),$(_ALL_REINPLACEMENTS))

$(foreach REINPLACEMENT,$(_ALL_REINPLACEMENTS),\
  $(if $(REINPLACE_FILES_$(REINPLACEMENT)),,$(error Reinplacement '$(REINPLACEMENT)' has been set but REINPLACE_FILES_$(REINPLACEMENT) is empty))\
  $(if $(REINPLACE_MATCH_$(REINPLACEMENT)),,$(error Reinplacement '$(REINPLACEMENT)' has been set but REINPLACE_MATCH_$(REINPLACEMENT) is empty))\
)

# We call an additional extract-modulated without resetting any variables so
# a complete unpacked set goes to the global dir for packaging (like gspec)
extract: checksum $(COOKIEDIR) pre-extract $(if $(NOGITPATCH),,pre-extract-git-check) extract-modulated $(addprefix extract-,$(MODULATIONS)) post-extract
	@$(DONADA)

extract-global: $(if $(filter global,$(MODULATION)),extract-modulated)
	$(if $(filter-out global,$(MODULATION)),$(MAKE) -s MODULATION=global extract)
	@$(MAKECOOKIE)

extract-modulated: checksum-modulated $(EXTRACTDIR) $(COOKIEDIR) \
		$(addprefix dep-$(GARDIR)/,$(EXTRACTDEPS)) \
		announce-modulation \
		pre-extract-modulated pre-extract-$(MODULATION) $(EXTRACT_TARGETS) post-extract-$(MODULATION) post-extract-modulated \
		$(if $(filter global,$(MODULATION)),,$(if $(NOGITPATCH),,post-extract-gitsnap)) \
		$(foreach FILE,$(EXPANDVARS),expandvars-$(FILE)) \
		$(foreach REINPLACEMENT,$(POSTEXTRACT_REINPLACEMENTS),\
		  post-extract-reinplace-$(REINPLACEMENT) \
		)
	@$(DONADA)

# This target ensures that the values used by git when making a commit
# are more sane than they _could_ otherwise be by taking the hostname
# to build the email address used.  If you want to submit patches with
# an alternate email address, use git config yourself to override the
# values.
pre-extract-git-check:
	@( g_email=`git config --global user.email`; \
	g_name=`git config --global user.name`; \
	email=$$USER@opencsw.org; \
	name=`getent passwd $$USER | awk -F: '{print $$5}'`; \
	if [ -z "$$g_email" ]; then \
		echo "Setting User Email value to: $$email"; \
		git config --global user.email "$$email"; \
	fi; \
	if [ -z "$$g_name" ]; then \
		echo "Setting User Name value to: $$name"; \
		git config --global user.name "$$name"; \
	fi )
	@$(MAKECOOKIE)

post-extract-gitsnap: $(EXTRACT_TARGETS)
	@( if [ -d "$(PATCHDIR)" ]; then \
		echo ' ==> Snapshotting extracted source tree with git'; \
		cd $(PATCHDIR); git init; git add .; \
		git commit -m "Upstream $(VERSION)"; \
		git tag -am "Upstream $(VERSION)" upstream-$(VERSION); \
		git checkout -b csw; \
	   fi )
	@$(MAKECOOKIE)

# returns true if extract has completed successfully, false
# otherwise
extract-p:
	@$(foreach COOKIEFILE,$(EXTRACT_TARGETS), test -e $(COOKIEDIR)/$(COOKIEFILE) ;)

# The rule takes all files from EXPANDVARS and replaces all occurrences of @<var>@ in the file
# with the values of <var> from the Makefile.
_var_definitions = $(foreach VAR,$(shell perl -ne 'print "$$1 " if( /@([^@]+)@/ )' <$1),$(VAR)="$($(VAR))")

expandvars-%:
	$(call _var_definitions,$(WORKDIR)/$*) perl -i-unexpanded -npe 's/@([^@]+)@/$$ENV{$$1}/eg' $(WORKDIR)/$*
	@$(MAKECOOKIE)

post-extract-reinplace-%:
	-perl -p -i$(REINPLACE_BACKUP_$*) -e 's{$(REINPLACE_MATCH_$*)}{$(REINPLACE_WITH_$*)}g' \
		$(addprefix $(WORKSRC)/,$(REINPLACE_FILES_$*))
	@( if [ -d "$(PATCHDIR)/.git" ]; then \
		echo "Committing reinplacements..."; \
		cd $(PATCHDIR); \
		git commit -am "Reinplacement $*"; \
		git tag -am "Reinplacement $*" reinplacement-$*; \
	  fi )
	@$(MAKECOOKIE)

# checkpatch	- Do a "patch -C" instead of a "patch".  Note
# 				  that it may give incorrect results if multiple
# 				  patches deal with the same file.
# TODO: actually write it!
checkpatch: extract
	@echo "$@ NOT IMPLEMENTED YET"

# patch			- Apply any provided patches to the source.
PATCH_TARGETS = $(addprefix patch-extract-,$(PATCHFILES) $(PATCHFILES_$(MODULATION)))

patch: pre-patch $(addprefix patch-,$(MODULATIONS)) post-patch
	@$(DONADA)

patch-modulated: extract-modulated $(WORKSRC) pre-patch-modulated pre-patch-$(MODULATION) $(PATCH_TARGETS) $(if $(filter global,$(MODULATION)),,$(if $(NOGITPATCH),,post-patch-gitsnap)) post-patch-$(MODULATION) post-patch-modulated
	@$(DONADA)

# returns true if patch has completed successfully, false
# otherwise
patch-p:
	@$(foreach COOKIEFILE,$(PATCH_TARGETS), test -e $(COOKIEDIR)/$(COOKIEFILE) ;)

post-patch-gitsnap: $(PATCH_TARGETS)

	@( if [ -d "$(PATCHDIR)/.git" ]; then \
		echo "Tagging top of current csw patch stack..."; \
		cd $(PATCHDIR); \
		git tag -am "CSW $(VERSION)" csw-$(VERSION); \
	  fi )
	@$(MAKECOOKIE)

makepatch: $(if $(NOGITPATCH),makepatch-nogit,$(addprefix patch-,$(MODULATIONS)) $(addprefix makepatch-,$(MODULATIONS)))
	@$(DONADA)

makepatch-nogit:
	@echo You set NOGITPATCH in your build recipe.  I can't create a patch.
	@$(DONADA)

# Allow generation of patches from modified work source.
makepatch-modulated: $(FILEDIR)
	@( if [ -d "$(PATCHDIR)/.git" ]; then \
		echo " ==> Makepatch: Looking for changes in modulation $(MODULATION)"; \
		cd $(PATCHDIR); \
		git add -u; \
		git diff --cached --quiet; \
		if test $$? -eq 0; then \
			echo "No changes."; \
		else \
			echo "Capturing changes..."; \
			git commit $(GIT_COMMIT_OPTS) && \
			( NEXTPATCH=`git log --pretty=oneline master..HEAD | wc -l | tr -d '[[:space:]]'`; \
			git format-patch --start-number=$$NEXTPATCH csw-$(VERSION); \
			echo Add the following to your recipe and then; \
			NEWPATCHES=`echo 00*-*patch`; \
			FILES_PATCHES=`for p in $$NEWPATCHES; do echo files/$$p; done`; \
			echo rerun: gmake makesums; \
			echo PATCHFILES +=  $$NEWPATCHES; \
			echo "(or maybe PATCHFILES_$(MODULATION) ??)"; \
			echo "Don't forget:"; \
			echo; \
			echo "	svn add" $$FILES_PATCHES; \
			echo; \
			mv $$NEWPATCHES $(abspath $(FILEDIR)); \
			for p in $$NEWPATCHES; do \
				touch $(abspath $(COOKIEDIR))/normal-patch-$$p; \
				touch $(abspath $(COOKIEDIR))/patch-extract-$$p; \
			done; \
			touch $(abspath $(COOKIEDIR))/extract-modulated; \
			touch $(abspath $(COOKIEDIR))/patch-modulated; \
			touch $(abspath $(COOKIEDIR))/post-patch-gitsnap; ) \
		fi; \
	    else \
		echo "No extracted sources so we can't create patches..."; \
	    fi )

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
	@$(DONADA)

configure-modulated: verify-isa patch-modulated $(CONFIGURE_IMGDEPS) $(CONFIGURE_BUILDDEPS) $(CONFIGURE_DEPS) \
		$(addprefix srcdep-$(GARDIR)/,$(SOURCEDEPS)) \
		pre-configure-modulated pre-configure-$(MODULATION) $(CONFIGURE_TARGETS) post-configure-$(MODULATION) post-configure-modulated $(if $(STRIP_LIBTOOL),strip-libtool)
	@$(DONADA)

strip-libtool:
	@echo '[===== Stripping Libtool =====]'
	fixlibtool $(WORKSRC)
	@$(MAKECOOKIE)

.PHONY: reset-configure reset-configure-modulated
reconfigure: reset-configure configure

reset-configure: $(addprefix reset-configure-,$(MODULATIONS))
	@rm -f $(addprefix $(COOKIEDIR)/configure-,$(MODULATIONS))
	@rm -f $(COOKIEDIR)/configure

reset-configure-modulated:
	@rm -f $(foreach C,pre-configure-modulated configure-modulated post-configure-modulated,$(COOKIEDIR)/$C)
	@rm -f $(COOKIEDIR)/pre-configure-$(MODULATION) $(COOKIEDIR)/post-configure-$(MODULATION)
	@rm -f $(addprefix $(COOKIEDIR)/,$(CONFIGURE_TARGETS))

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

.PHONY: reset-build reset-build-modulated
rebuild: reset-build build

reset-build: $(addprefix reset-build-,$(MODULATIONS))
	rm -f $(COOKIEDIR)/build

# XXX: pre-*, post-*
reset-build-modulated: $(patsubst build-%,clean-%,$(BUILD_TARGETS))
	rm -f $(addprefix $(COOKIEDIR)/,pre-build-modulated $(BUILD_TAGRETS) post-build-modulated))

# returns true if build has completed successfully, false
# otherwise
build-p:
	@$(foreach COOKIEFILE,$(BUILD_TARGETS), test -e $(COOKIEDIR)/$(COOKIEFILE) ;)

TEST_TARGETS = $(addprefix test-,$(TEST_SCRIPTS))

test: pre-test $(addprefix test-,$(MODULATIONS)) post-test
	$(DONADA)

test-modulated: build-modulated pre-test-modulated pre-test-$(MODULATION) $(TEST_TARGETS) post-test-$(MODULATION) post-test-modulated
	$(DONADA)

# XXX: retest

# strip - Strip executables
ifneq ($(GARFLAVOR),DBG)
POST_INSTALL_TARGETS := strip $(POST_INSTALL_TARGETS)
endif

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

install-modulated: build-modulated $(addprefix dep-$(GARDIR)/,$(INSTALLDEPS)) test-modulated $(INSTALL_DIRS) $(PRE_INSTALL_TARGETS) \
		pre-install-modulated pre-install-$(MODULATION) \
		$(INSTALL_TARGETS) \
		post-install-$(MODULATION) post-install-modulated \
		$(POST_INSTALL_TARGETS) \
		$(foreach REINPLACEMENT,$(POSTINSTALL_REINPLACEMENTS),\
		  post-install-reinplace-$(REINPLACEMENT) \
		)
	@$(MAKECOOKIE)

post-install-reinplace-%:
	-perl -p -i$(REINPLACE_BACKUP_$*) -e "s($(REINPLACE_MATCH_$*))($(REINPLACE_WITH_$*))g" \
		$(addprefix $(DESTDIR)/,$(REINPLACE_FILES_$*))
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
	@rm -f $(COOKIEDIR)/strip

reset-install-modulated:
	@$(call _pmod,Reset install state)
	@rm -rf $(INSTALLISADIR) $(COOKIEDIR)/install-work
	@rm -f $(foreach C,pre-install-modulated install-modulated post-install-modulated,$(COOKIEDIR)/$C)
	@rm -f $(COOKIEDIR)/pre-install-$(MODULATION) $(COOKIEDIR)/post-install-$(MODULATION)
	@rm -f $(COOKIEDIR)/strip
	@rm -f $(foreach S,$(INSTALL_TARGETS),$(COOKIEDIR)/$S)
	@rm -f $(COOKIEROOTDIR)/global/install-$(MODULATION)
	@rm -f $(addprefix $(COOKIEDIR)/post-install-reinplace-,$(POSTINSTALL_REINPLACEMENTS))

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
# default:       ISA_DEFAULT gets installed in bin/..., all others in bin/$ISA/
# ISAEXEC = 1:   relocate to ISA subdirs if more than one ISA, use isaexec-wrapper for bin/, etc.
#
# Automatic merging is only possible if you have the default modulation "ISA"
# Otherwise you *must* specify merge scripts for all modulations.

ifeq ($(DEBUG_MERGING),)
_DBG_MERGE=@
else
_DBG_MERGE=
endif

ifeq ($(NEEDED_ISAS),$(ISA_DEFAULT))
MERGE_SCRIPTS_isa-default ?= copy-all $(EXTRA_MERGE_SCRIPTS_$(ISA_DEFAULT)) $(EXTRA_MERGE_SCRIPTS)
MERGE_SCRIPTS_isa-$(ISA_DEFAULT) ?= $(MERGE_SCRIPTS_isa-default)
MERGE_SCRIPTS_$(MODULATION) ?= $(MERGE_SCRIPTS_$(MODULATION_ISACOLLAPSED))
else
ISAEXEC_DIRS ?= $(if $(ISAEXEC),$(bindir) $(sbindir) $(libexecdir))
MERGE_DIRS_isa-default ?= $(EXTRA_MERGE_DIRS) $(EXTRA_MERGE_DIRS_isa-$(ISA_DEFAULT))
MERGE_DIRS_isa-extra ?= $(if $(or $(BUILD64),$(ISAEXEC)),$(bindir) $(sbindir) $(libexecdir)) $(libdir) $(EXTRA_MERGE_DIRS) $(EXTRA_MERGE_DIRS_isa-extra) $(EXTRA_MERGE_DIRS_isa-$(ISA))
MERGE_DIRS_$(MODULATION_ISACOLLAPSED64) ?= $(MERGE_DIRS_$(MODULATION_ISACOLLAPSEDEXTRA))
MERGE_DIRS_$(MODULATION) ?= $(MERGE_DIRS_$(MODULATION_ISACOLLAPSED))

MERGE_SCRIPTS_isa-default ?= copy-relocate $(EXTRA_MERGE_SCRIPTS_isa-$(ISA_DEFAULT)) $(EXTRA_MERGE_SCRIPTS)
MERGE_SCRIPTS_isa-extra ?= copy-relocated-only copy-config-only $(EXTRA_MERGE_SCRIPTS_isa-$(ISA)) $(EXTRA_MERGE_SCRIPTS_isa-extra) $(EXTRA_MERGE_SCRIPTS)
MERGE_SCRIPTS_$(MODULATION_ISACOLLAPSED64) ?= $(MERGE_SCRIPTS_$(MODULATION_ISACOLLAPSEDEXTRA))
MERGE_SCRIPTS_$(MODULATION) ?= $(MERGE_SCRIPTS_$(MODULATION_ISACOLLAPSED))
endif

# These directories get relocated into their ISA subdirectories
MERGE_DIRS ?= $(call modulationvalue,MERGE_DIRS)

ifneq ($(COMMON_PKG_DEPENDS),)
_EXTRA_GAR_PKGS += $(COMMON_PKG_DEPENDS)
endif

# These merge-rules are actually processed for the current modulation
MERGE_TARGETS ?= $(addprefix merge-,$(MERGE_SCRIPTS_$(MODULATION))) $(EXTRA_MERGE_TARGETS)

# Include only these files
ifeq ($(origin MERGE_INCLUDE_FILES_$(MODULATION)), undefined)
_MERGE_INCLUDE_FILES = $(MERGE_INCLUDE_FILES)
else
_MERGE_INCLUDE_FILES = $(MERGE_INCLUDE_FILES_$(MODULATION))
endif

# This can be defined in category.mk
MERGE_EXCLUDE_CATEGORY ?= $(_MERGE_EXCLUDE_CATEGORY)

# Support for cswpycompile, skip pre-compiled python files (.pyc, .pyo)
# during the merge phase.
_PYCOMPILE_FILES = /opt/csw/lib/python/site-packages/.*\.py
MERGE_EXCLUDE_PYCOMPILE ?= $(if $(PYCOMPILE), $(addsuffix c,$(_PYCOMPILE_FILES)) $(addsuffix o,$(_PYCOMPILE_FILES)))

MERGE_EXCLUDE_INFODIR ?= $(sharedstatedir)/info/dir
MERGE_EXCLUDE_LIBTOOL ?= $(libdir)/.*\.la
MERGE_EXCLUDE_BACKUPFILES ?= .*\~
MERGE_EXCLUDE_STATICLIBS ?= $(libdir)/.*\.a
# Exclude all other .pc-files apart from the default 32- and 64 bit versions
MERGE_EXCLUDE_EXTRA_ISA_PKGCONFIG ?= $(if $(filter-out $(ISA_DEFAULT) $(ISA_DEFAULT64),$(ISA)),$(libdir)/.*\.pc)
MERGE_EXCLUDE_DEFAULT ?= $(MERGE_EXCLUDE_CATEGORY) $(MERGE_EXCLUDE_INFODIR) $(MERGE_EXCLUDE_LIBTOOL) $(MERGE_EXCLUDE_BACKUPFILES) $(MERGE_EXCLUDE_STATICLIBS) $(MERGE_EXCLUDE_EXTRA_ISA_PKGCONFIG) $(MERGE_EXCLUDE_PYCOMPILE)

# Exclude these files
ifeq ($(origin MERGE_EXCLUDE_FILES_$(MODULATION)), undefined)
_MERGE_EXCLUDE_FILES = $(MERGE_EXCLUDE_FILES)
else
_MERGE_EXCLUDE_FILES = $(MERGE_EXCLUDE_FILES_$(MODULATION))
endif
_MERGE_EXCLUDE_FILES += $(EXTRA_MERGE_EXCLUDE_FILES) $(EXTRA_MERGE_EXCLUDE_FILES_$(MODULATION)) $(MERGE_EXCLUDE_DEFAULT)

# This variable contains parameter for pax to honor global file inclusion/exclusion
# Make sure include overrides are processed first
_INC_EXT_RULE = $(foreach F,$(EXTRA_MERGE_INCLUDE_FILES) $(EXTRA_MERGE_INCLUDE_FILES_$(MODULATION)),-i "^\.$F$$")
# Exclude by replacing files with the empty string
_INC_EXT_RULE += $(foreach F,$(_MERGE_EXCLUDE_FILES),-s ',^\.$F$$,,')
# Replace files by itself terminating on first match
_INC_EXT_RULE += $(foreach F,$(_MERGE_INCLUDE_FILES),-s ",^\(\.$F\)$$,\1,")

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


_PAX_ARGS = $(_INC_EXT_RULE) $(_EXTRA_PAX_ARGS) $(call modulationvalue,EXTRA_PAX_ARGS) $(EXTRA_PAX_ARGS)

define killprocandparent
cpids() { \
  P=$1 \
  PPIDS=$P \
  PP=`ps -eo pid,ppid | awk "BEGIN { ORS=\" \" } \\$2 == $P { print \\$1 }\"` \
  while [ -n "$PP" ]; do \
    PQ=$PP \
    PP= \
    for q in $PQ; do \
      PPIDS="$PPIDS $q" \
      PP=$PP\ `ps -eo pid,ppid | awk "BEGIN { ORS=\" \" } \\$2 == $q { print \\$1 }\"` \
    done \
  done \
 \
  echo $PPIDS \
}
endef


# The basic merge merges the compiles for all ISAs on the current architecture
merge: checksum pre-merge merge-do merge-license merge-classutils merge-checkpkgoverrides merge-alternatives $(if $(COMPILE_ELISP),compile-elisp) $(if $(NOSOURCEPACKAGE),,merge-src) merge-distfile-README.CSW merge-distfile-changelog.CSW merge-obsolete $(if $(AP2_MODS),post-merge-ap2mod) $(if $(PHP5_EXT),post-merge-php5ext) post-merge
	@banner merge
	@$(MAKECOOKIE)

.PHONY: merge-do
merge-do: $(if $(PARALLELMODULATIONS),merge-parallel,merge-sequential)

.PHONY: merge-sequential
merge-sequential: $(addprefix merge-,$(MODULATIONS))

.PHONY: merge-parallel
merge-parallel: _PIDFILE=$(WORKROOTDIR)/build-global/multitail.pid
merge-parallel: merge-watch
	$(_DBG_MERGE)trap "kill -9 `cat $(_PIDFILE) $(foreach M,$(MODULATIONS),$(WORKROOTDIR)/build-$M/build.pid) 2>/dev/null`;stty sane" INT;\
		$(foreach M,$(MODULATIONS),($(MAKE) merge-$M >$(WORKROOTDIR)/build-$M/build.log 2>&1; echo $$? >$(WORKROOTDIR)/build-$M/build.ret) & echo $$! >$(WORKROOTDIR)/build-$M/build.pid; ) wait
	$(_DBG_MERGE)if [ -f $(_PIDFILE) ]; then kill `cat $(_PIDFILE)`; stty sane; fi
	$(_DBG_MERGE)$(foreach M,$(MODULATIONS),if [ "`cat $(WORKROOTDIR)/build-$M/build.ret`" -ne 0 ]; then \
		echo "Build error in modulation $M. Please see"; \
		echo "  $(WORKROOTDIR)/build-$M/build.log"; \
		echo "for details:"; \
		echo; \
		tail -100 $(WORKROOTDIR)/build-$M/build.log; \
		exit "Return code: `cat $(WORKROOTDIR)/build-$M/build.ret`"; \
	fi;)

.PHONY: merge-watch
merge-watch: _USEMULTITAIL=$(shell test -x $(MULTITAIL) && test -x $(TTY) && $(TTY) >/dev/null 2>&1; if [ $$? -eq 0 ]; then echo yes; fi)
merge-watch: $(addprefix $(WORKROOTDIR)/build-,global $(MODULATIONS))
	$(_DBG_MERGE)$(if $(_USEMULTITAIL),\
		$(MULTITAIL) --retry-all $(foreach M,$(MODULATIONS),$(WORKROOTDIR)/build-$M/build.log) -t "build(s) in progress" -wh 1 -j & echo $$! > $(WORKROOTDIR)/build-global/multitail.pid,\
		echo "Building all ISAs in parallel. Please see the individual logfiles for details:";$(foreach M,$(MODULATIONS),echo "- $(WORKROOTDIR)/build-$M/build.log";)\
	)

post-merge-ap2mod:
	$(GARBIN)/ap2mod_build_scripts $(PKGROOT) $(AP2_MODFILES)
	@$(MAKECOOKIE)

post-merge-php5ext:
	$(GARBIN)/php5ext_build_scripts $(PKGROOT) $(PHP5_EXTFILES)
	@$(MAKECOOKIE)

# This merges the 
merge-modulated: install-modulated pre-merge-modulated pre-merge-$(MODULATION) $(MERGE_TARGETS) post-merge-$(MODULATION) post-merge-modulated
	$(warning M: $(MERGE_DIRS))
	@$(MAKECOOKIE)

# Copy the whole tree verbatim
merge-copy-all: $(PKGROOT) $(INSTALLISADIR)
	$(_DBG_MERGE)(cd $(INSTALLISADIR)$(if $(ALLOW_RELOCATE),$(RELOCATE_PREFIX)); umask 022 && pcopy $(_PAX_ARGS) \
		$(foreach DIR,$(MERGE_DIRS),-s ",^\(\.$(DIR)/\),.$(call mergebase,$(DIR))/,p") \
		. $(PKGROOT))
	@$(MAKECOOKIE)

# Copy only the merge directories
merge-copy-only: $(PKGROOT)
	$(_DBG_MERGE)(cd $(INSTALLISADIR)$(if $(ALLOW_RELOCATE),$(RELOCATE_PREFIX)); umask 022 && pcopy $(_PAX_ARGS) \
		$(foreach DIR,$(MERGE_DIRS),-s ",^\(\.$(DIR)/\),.$(call mergebase,$(DIR))/,p") -m \
		. $(PKGROOT) \
	)
	@$(MAKECOOKIE)

# Copy the whole tree and relocate the directories in $(MERGE_DIRS)
merge-copy-relocate: $(PKGROOT) $(INSTALLISADIR)
	$(_DBG_MERGE)(cd $(INSTALLISADIR)$(if $(ALLOW_RELOCATE),$(RELOCATE_PREFIX)); umask 022 && pcopy $(_PAX_ARGS) \
		$(foreach DIR,$(MERGE_DIRS),-s ",^\(\.$(DIR)/\),.$(call mergebase,$(DIR))/$(ISA)/,p") \
		. $(PKGROOT) \
	)
	@$(MAKECOOKIE)

# Copy only the relocated directories
merge-copy-relocated-only: $(PKGROOT) $(INSTALLISADIR)
	$(_DBG_MERGE)(cd $(INSTALLISADIR)$(if $(ALLOW_RELOCATE),$(RELOCATE_PREFIX)); umask 022 && pcopy $(_PAX_ARGS) \
		$(foreach DIR,$(MERGE_DIRS),-s ",^\(\.$(DIR)/\),.$(call mergebase,$(DIR))/$(ISA)/,p") -m \
		 . $(PKGROOT) \
	)
	@$(MAKECOOKIE)

DEVEL_EXECUTABLES ?= $(bindir)/.*_config $(bindir)/.*-config

# Copy 
merge-copy-config-only:
	$(_DBG_MERGE)(cd $(INSTALLISADIR)$(if $(ALLOW_RELOCATE),$(RELOCATE_PREFIX)); umask 022 && pcopy \
		-m $(foreach C,$(DEVEL_EXECUTABLES),-s ",^\(\.$C\)\$$,\1,p" ) \
		. $(PKGROOT) \
	)
	@$(MAKECOOKIE)

.PHONY: remerge reset-merge reset-merge-modulated
remerge: reset-merge merge

reset-merge: reset-package $(addprefix reset-merge-,$(MODULATIONS)) reset-merge-license reset-merge-classutils reset-merge-checkpkgoverrides reset-merge-alternatives reset-merge-distfile-README.CSW reset-merge-distfile-changelog.CSW reset-merge-obsolete reset-merge-ap2mod reset-merge-php5ext reset-merge-src
	rm -f $(COOKIEDIR)/pre-merge $(foreach M,$(MODULATIONS),$(COOKIEDIR)/merge-$M) $(COOKIEDIR)/merge $(COOKIEDIR)/post-merge
	rm -rf $(PKGROOT)

reset-merge-modulated:
	@$(call _pmod,Reset merge state)
	echo rm -f $(COOKIEDIR)/merge-*
	rm -f $(COOKIEDIR)/merge-*

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
	@-rm -rf tmp-deleteme-workdir
	@-mv $(WORKDIR) tmp-deleteme-workdir
	@-rm -rf tmp-deleteme-workdir &

spotless: imageclean
	@echo " ==> Removing $(DESTDIR)"
	@-rm -rf work-old
	@-mv work work-old
	@-rm -rf work-old &

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
	$(_DBG)for gspec in `gfind $(CURDIR) -type f -name '*.gspec' | ggrep files`; do \
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
