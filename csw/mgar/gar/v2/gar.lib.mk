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
#

# cookies go here, so we have to be able to find them for
# dependency checking.
VPATH += $(COOKIEDIR)

# convenience variable to make the cookie.
MAKECOOKIE = mkdir -p $(COOKIEDIR)/$(@D) && date >> $(COOKIEDIR)/$@

URLSTRIP = $(subst ://,//,$(1))

# if you need to proxy git:// connections, set GIT_USE_PROXY.  There is a
# default proxy script that works with the (squid?) proxy at the BO buildfarm.
# override GIT_PROXY_SCRIPT to something else if you need to.
GIT_MAYBEPROXY = $(if $(GIT_USE_PROXY),GIT_PROXY_COMMAND=$(GIT_PROXY_SCRIPT))
GIT_TREEISH = $(if $(GIT_TREEISH_$(1)),$(GIT_TREEISH_$(1)),HEAD)

#################### FETCH RULES ####################

URLS = $(call URLSTRIP,$(foreach SITE,$(FILE_SITES) $(MASTER_SITES),$(addprefix $(SITE),$(DISTFILES))) $(foreach SITE,$(FILE_SITES) $(PATCH_SITES) $(MASTER_SITES),$(addprefix $(SITE),$(PATCHFILES) $(foreach M,$(MODULATIONS),$(PATCHFILES_$M)))))

# if the caller has defined _postinstall, etc targets for a package, add
# these 'dynamic script' targets to our fetch list
URLS += $(foreach DYN,$(DYNSCRIPTS),dynscr//$(DYN))

ifdef GIT_REPOS
URLS += $(foreach R,$(GIT_REPOS),gitrepo//$(call GITPROJ,$(R)) $(subst http,git-http,$(call URLSTRIP,$(R))))
endif

# Download the file if and only if it doesn't have a preexisting
# checksum file.  Loop through available URLs and stop when you
# get one that doesn't return an error code.
$(DOWNLOADDIR)/%:  
	@if test -f $(COOKIEDIR)/checksum-$*; then : ; else \
		echo " ==> Grabbing $@"; \
		for i in $(filter %/$*,$(URLS)); do  \
			echo " 	==> Trying $$i"; \
			$(MAKE) -s $$i || continue; \
			mv $(PARTIALDIR)/$* $@; \
			break; \
		done; \
		if test -r $@ ; then : ; else \
			echo '(!!!) Failed to download $@!' 1>&2; \
			false; \
		fi; \
	fi

gitrepo//%:
	@( if [ -d $(GARCHIVEDIR)/$(call GITPROJ,$*) ]; then \
		( cd $(GARCHIVEDIR)/$(call GITPROJ,$*); \
			$(GIT_MAYBEPROXY) git --bare fetch ) && \
		gln -s $(GARCHIVEDIR)/$(call GITPROJ,$*)/ $(PARTIALDIR)/$(call GITPROJ,$*); \
	   else \
		false; \
	  fi )

# the git remote add commands are so that we can later do a fetch
# to update the code.
# we possibly proxy the git:// references depending on GIT_USE_PROXY
git-http//%:
	@$git clone --bare http://$* $(PARTIALDIR)/$(call GITPROJ,$*)
	@( cd $(PARTIALDIR)/$(call GITPROJ,$*); \
		git remote add origin http://$*; \
		git config remote.origin.fetch $(if $(GIT_REFS_$(call GITPROJ,$*)),$(GIT_REFS_$(call GITPROJ,$*)),$(GIT_DEFAULT_TRACK)); )

git//%:
	@$(GIT_MAYBEPROXY) git clone --bare git://$* $(PARTIALDIR)/$(call GITPROJ,$*)
	@( cd $(PARTIALDIR)/$(call GITPROJ,$*); \
		git remote add origin git://$*; \
		git config remote.origin.fetch $(if $(GIT_REFS_$(call GITPROJ,$*)),$(GIT_REFS_$(call GITPROJ,$*)),$(GIT_DEFAULT_TRACK)); )

# create ADMSCRIPTS 'on the fly' from variables defined by the caller
# This version is private and should only be called from the non-private
# version directly below
_dynscr//%:
	$($(subst .,_,$*))

dynscr//%:
	$(MAKE) --no-print-directory -n _$@ > $(PARTIALDIR)/$*

# download an http URL (colons omitted)
http//%: 
	@wget $(WGET_OPTS) -T 30 -c -P $(PARTIALDIR) http://$*

https//%: 
	@wget $(WGET_OPTS) -T 30 -c -P $(PARTIALDIR) https://$*

# download an ftp URL (colons omitted)
#ftp//%: 
#	@wget -T 30 -c --passive-ftp -P $(PARTIALDIR) ftp://$*
ftp//%: 
	@wget $(WGET_OPTS) -T 30 -c -P $(PARTIALDIR) ftp://$*

# link to a local copy of the file
# (absolute path)
file///%: 
	@if test -f /$*; then \
		gln -sf /$* $(PARTIALDIR)/$(notdir $*); \
	else \
		false; \
	fi

# link to a local copy of the file
# (relative path)
file//%: 
	@if test -f $*; then \
		gln -sf "$(CURDIR)/$*" $(PARTIALDIR)/$(notdir $*); \
	else \
		false; \
	fi

# Using Jeff Waugh's rsync rule.
# DOES NOT PRESERVE SYMLINKS!
rsync//%: 
	@rsync -azvLP rsync://$* $(PARTIALDIR)/

# Using Jeff Waugh's scp rule
scp//%:
	@scp -C $* $(PARTIALDIR)/

# Fetch a SVN repo via http
svn-http//%:
	@svn co $(SVNHTTP_CO_ARGS) http://$* $(PARTIALDIR)/$(notdir $*)

svn-https//%:
	@svn co $(SVNHTTP_CO_ARGS) https://$* $(PARTIALDIR)/$(notdir $*)

#################### CHECKSUM RULES ####################

# check a given file's checksum against $(CHECKSUM_FILE) and
# error out if it mentions the file without an "OK".
checksum-%: $(CHECKSUM_FILE) 
	@echo " ==> Running checksum on $*"
	@if ggrep -- '/$*$$' $(CHECKSUM_FILE); then \
		if LC_ALL="C" LANG="C" gmd5sum -c $(CHECKSUM_FILE) 2>&1 | \
			ggrep -- '$*' | ggrep -v ':[ ]\+OK'; then \
			echo '(!!!) $* failed checksum test!' 1>&2; \
			false; \
		else \
			echo 'file $* passes checksum test!'; \
			$(MAKECOOKIE); \
		fi \
	else \
		echo '(!!!) $* not in $(CHECKSUM_FILE) file!' 1>&2; \
		false; \
	fi

#################### CHECKNEW RULES ####################

UPSTREAM_MASTER_SITES ?= $(MASTER_SITES)
UW_ARGS = $(addprefix -u ,$(UPSTREAM_MASTER_SITES))
SF_ARGS = $(addprefix -s ,$(UPSTREAM_USE_SF))

define files2check
$(if $(UFILES_REGEX),$(shell http_proxy=$(http_proxy) ftp_proxy=$(ftp_proxy) $(GARBIN)/upstream_watch $(UW_ARGS) $(SF_ARGS) $(addsuffix ',$(addprefix ',$(UFILES_REGEX)))))
endef

check-upstream-and-mail: FILES2CHECK = $(call files2check)
check-upstream-and-mail:
	@if [ -n '$(FILES2CHECK)' ]; then \
		NEW_FILES=""; \
		PACKAGE_UP_TO_DATE=0; \
		for FILE in $(FILES2CHECK) ""; do \
			[ -n "$$FILE" ] || continue; \
			if test -f $(COOKIEDIR)/checknew-$$FILE ; then \
				PACKAGE_UP_TO_DATE=1; \
			else \
				if echo $(DISTFILES) | grep -w $$FILE >/dev/null; then \
					PACKAGE_UP_TO_DATE=1; \
					echo "$(GARNAME) : Package is up-to-date. Current version is $$FILE" ; \
				else \
					NEW_FILES="$$FILE $$NEW_FILES"; \
				fi; \
			fi; \
			$(MAKE) checknew-$$FILE >/dev/null; \
		done; \
		if test -z "$$NEW_FILES" ; then \
			if [ ! -n '$(UFILES_REGEX)' ]; then \
				echo "$(GARNAME) : Warning UFILES_REGEX is not set : $(UFILES_REGEX)" ; \
#				{ echo ""; \
#				  echo "Hello dear $(GARNAME) maintainer,"; \
#				  echo ""; \
#				  echo "The upstream notification job has detected that $(GARNAME) is not configured for automatic upstream file update detection."; \
#				  echo ""; \
#				  echo "Please consider updating your package. Documentation is available from this link : http://www.opencsw.org" ; \
#				  echo ""; \
#				  echo "--"; \
#				  echo "Kindest regards"; \
#				  echo "upstream notification job"; } | $(GARBIN)/mail2maintainer -s '[svn] $(GARNAME) upstream update notification' $(GARNAME); \
			else \
				if [ "$$PACKAGE_UP_TO_DATE" -eq "0" ]; then \
					echo "$(GARNAME) : Warning no files to check ! $(FILES2CHECK)" ; \
					echo "$(GARNAME) :     UPSTREAM_MASTER_SITES is $(UPSTREAM_MASTER_SITES)" ; \
					echo "$(GARNAME) :     DISTNAME is $(DISTNAME)" ; \
					echo "$(GARNAME) :     UFILES_REGEX is : $(UFILES_REGEX)" ; \
					echo "$(GARNAME) : Please check configuration" ; \
				fi; \
			fi; \
		else \
			echo "$(GARNAME) : new upstream files available: $$NEW_FILES"; \
			{	echo ""; \
				echo "Hello dear $(GARNAME) maintainer,"; \
				echo ""; \
				echo "The upstream notification job has detected the availability of new files for $(GARNAME)."; \
				echo ""; \
				echo "The following upstream file(s):"; \
				echo "    $$NEW_FILES"; \
				echo ""; \
				echo "is/are available at the following url(s):"; \
				echo "    $(UPSTREAM_MASTER_SITES)"; \
				echo ""; \
				echo "Please consider updating your package." ; \
				echo ""; \
				echo "--"; \
				echo "Kindest regards"; \
				echo "upstream notification job"; } | $(GARBIN)/mail2maintainer -s '[svn] $(GARNAME) upstream update notification' $(GARNAME); \
		fi; \
	fi
		
check-upstream: FILES2CHECK = $(call files2check)
check-upstream: 
	@if [ -n '$(FILES2CHECK)' ]; then \
		NEW_FILES=""; \
		PACKAGE_UP_TO_DATE=0; \
		for FILE in $(FILES2CHECK) ""; do \
			[ -n "$$FILE" ] || continue; \
			if test -f $(COOKIEDIR)/checknew-$$FILE ; then \
				PACKAGE_UP_TO_DATE=1; \
			else \
				if echo $(DISTFILES) | grep -w $$FILE >/dev/null; then \
					PACKAGE_UP_TO_DATE=1; \
					echo "$(GARNAME) : Package is up-to-date. Current version is $$FILE" ; \
				else \
					NEW_FILES="$$FILE $$NEW_FILES"; \
				fi; \
			fi; \
			$(MAKE) checknew-$$FILE >/dev/null; \
		done; \
		if test -z "$$NEW_FILES" ; then \
			if [ ! -n '$(UFILES_REGEX)' ]; then \
				echo "$(GARNAME) : Warning UFILES_REGEX is not set : $(UFILES_REGEX)" ; \
			else \
				if [ "$$PACKAGE_UP_TO_DATE" -eq "0" ]; then \
					echo "$(GARNAME) : Warning no files to check ! $(FILES2CHECK)" ; \
					echo "$(GARNAME) :     UPSTREAM_MASTER_SITES is $(UPSTREAM_MASTER_SITES)" ; \
					echo "$(GARNAME) :     DISTNAME is $(DISTNAME)" ; \
					echo "$(GARNAME) :     UFILES_REGEX is : $(UFILES_REGEX)" ; \
					echo "$(GARNAME) : Please check configuration" ; \
				fi; \
			fi; \
		else \
			echo "$(GARNAME) : new upstream files available: $$NEW_FILES"; \
		fi; \
	fi
	
checknew-%:
	@$(MAKECOOKIE)


#################### GARCHIVE RULES ####################

# while we're here, let's just handle how to back up our
# checksummed files

$(GARCHIVEDIR)/%: $(GARCHIVEDIR)
	@if [ -h $(DOWNLOADDIR)/$* ]; then :; else \
		gcp -Lr $(DOWNLOADDIR)/$* $@; \
	fi


#################### EXTRACT RULES ####################

TAR_ARGS = --no-same-owner

# rule to extract uncompressed tarballs
tar-extract-%:
	@echo " ==> Extracting $(DOWNLOADDIR)/$*"
	@gtar $(TAR_ARGS) -xf $(DOWNLOADDIR)/$* -C $(EXTRACTDIR)
	@$(MAKECOOKIE)

# rule to extract files with tar xzf
tar-gz-extract-%:
	@echo " ==> Extracting $(DOWNLOADDIR)/$*"
	@gzip -dc $(DOWNLOADDIR)/$* | gtar $(TAR_ARGS) -xf - -C $(EXTRACTDIR)
	@$(MAKECOOKIE)

# rule to extract files with tar and bzip
tar-bz-extract-%:
	@echo " ==> Extracting $(DOWNLOADDIR)/$*"
	@bzip2 -dc $(DOWNLOADDIR)/$* | gtar $(TAR_ARGS) -xf - -C $(EXTRACTDIR)
	@$(MAKECOOKIE)

# extract compressed single files
bz-extract-%:
	@echo " ==> Decompressing $(DOWNLOADDIR)/$*"
	@cp $(DOWNLOADDIR)/$* $(WORKDIR)/
	@bzip2 -d $(WORKDIR)/$*
	@$(MAKECOOKIE)

gz-extract-%:
	@echo " ==> Decompressing $(DOWNLOADDIR)/$*"
	@cp $(DOWNLOADDIR)/$* $(WORKDIR)/
	@gzip -d $(WORKDIR)/$*
	@$(MAKECOOKIE)

# extra dependency rule for git repos, that will allow the user
# to supply an alternate target at their discretion
git-extract-%:
	@echo " ===> Extracting Git Repo $(DOWNLOADDIR)/$* (Treeish: $(call GIT_TREEISH,$*))"
	git --bare archive --prefix=$(GARNAME)-$(GARVERSION)/ --remote=file://$(abspath $(DOWNLOADDIR))/$*/ $(call GIT_TREEISH,$*) | gtar -xf - -C $(EXTRACTDIR)
	@$(MAKECOOKIE)

# rule to extract files with unzip
zip-extract-%:
	@echo " ==> Extracting $(DOWNLOADDIR)/$*"
	@unzip $(DOWNLOADDIR)/$* -d $(EXTRACTDIR)
	@$(MAKECOOKIE)

# this is a null extract rule for files which are constant and
# unchanged (not archives)
cp-extract-%:
	@echo " ==> Copying $(DOWNLOADDIR)/$*"
	@cp -rp $(DOWNLOADDIR)/$* $(WORKDIR)/
	@$(MAKECOOKIE)

#gets the meat of a .deb into $(WORKSRC)
deb-bin-extract-%:
	@echo " ==> Extracting $(DOWNLOADDIR)/$*"
	@ar x $(DOWNLOADDIR)/$*
	@rm debian-binary && \
		mv *.tar.gz $(DOWNLOADDIR) && \
			mkdir $(WORKSRC) && \
				gtar $(TAR_ARGS) -xvz -C $(WORKSRC) \
					-f $(DOWNLOADDIR)/data.tar.gz
	@$(MAKECOOKIE)

### EXTRACT FILE TYPE MAPPINGS ###
# These rules specify which of the above extract action rules to use for a
# given file extension.  Often support for a given extract type can be handled
# by simply adding a rule here.

extract-archive-%.tar: tar-extract-%.tar
	@$(MAKECOOKIE)

extract-archive-%.tar.gz: tar-gz-extract-%.tar.gz
	@$(MAKECOOKIE)

extract-archive-%.tar.Z: tar-gz-extract-%.tar.Z
	@$(MAKECOOKIE)

extract-archive-%.tgz: tar-gz-extract-%.tgz
	@$(MAKECOOKIE)

extract-archive-%.taz: tar-gz-extract-%.taz
	@$(MAKECOOKIE)

extract-archive-%.tar.bz: tar-bz-extract-%.tar.bz
	@$(MAKECOOKIE)

extract-archive-%.tar.bz2: tar-bz-extract-%.tar.bz2
	@$(MAKECOOKIE)

extract-archive-%.tbz: tar-bz-extract-%.tbz
	@$(MAKECOOKIE)

extract-archive-%.zip: zip-extract-%.zip
	@$(MAKECOOKIE)

extract-archive-%.ZIP: zip-extract-%.ZIP
	@$(MAKECOOKIE)

extract-archive-%.deb: deb-bin-extract-%.deb
	@$(MAKECOOKIE)

extract-archive-%.bz2: bz-extract-%.bz2
	@$(MAKECOOKIE)

extract-archive-%.gz: gz-extract-%.gz
	@$(MAKECOOKIE)

extract-archive-%.git: git-extract-%.git
	@$(MAKECOOKIE)

# anything we don't know about, we just assume is already
# uncompressed and unarchived in plain format
extract-archive-%: cp-extract-%
	@$(MAKECOOKIE)

#################### PATCH RULES ####################

PATCHDIR ?= $(WORKSRC)
PATCHDIRLEVEL ?= 1
PATCHDIRFUZZ ?= 2
GARPATCH = gpatch -d$(PATCHDIR) -p$(PATCHDIRLEVEL) -F$(PATCHDIRFUZZ)
BASEWORKSRC = $(shell basename $(WORKSRC))

# apply bzipped patches
bz-patch-%:
	@echo " ==> Applying patch $(DOWNLOADDIR)/$*"
	@bzip2 -dc $(DOWNLOADDIR)/$* | $(GARPATCH)
	@$(MAKECOOKIE)

# apply gzipped patches
gz-patch-%:
	@echo " ==> Applying patch $(DOWNLOADDIR)/$*"
	@gzip -dc $(DOWNLOADDIR)/$* | $(GARPATCH)
	@$(MAKECOOKIE)

# apply normal patches
normal-patch-%:
	@echo " ==> Applying patch $(DOWNLOADDIR)/$*"
	$(GARPATCH) < $(DOWNLOADDIR)/$*
	@$(MAKECOOKIE)

# This is used by makepatch
%/gar-base.diff:
	@echo " ==> Creating patch $@"
	@EXTRACTDIR=$(SCRATCHDIR) COOKIEDIR=$(SCRATCHDIR)-$(COOKIEDIR) $(MAKE) extract
	@PATCHDIR=$(SCRATCHDIR)/$(BASEWORKSRC) COOKIEDIR=$(SCRATCHDIR)-$(COOKIEDIR) $(MAKE) patch
	@mv $(SCRATCHDIR)/$(BASEWORKSRC) $(WORKSRC_FIRSTMOD).orig
	@( cd $(WORKDIR_FIRSTMOD); \
		if gdiff --speed-large-files --minimal -Nru $(BASEWORKSRC).orig $(BASEWORKSRC) > gar-base.diff; then :; else \
			cd $(CURDIR); \
			mv -f $(WORKDIR_FIRSTMOD)/gar-base.diff $@; \
		fi )

### PATCH FILE TYPE MAPPINGS ###
# These rules specify which of the above patch action rules to use for a given
# file extension.  Often support for a given patch format can be handled by
# simply adding a rule here.

patch-extract-%.bz: bz-patch-%.bz
	@$(MAKECOOKIE)

patch-extract-%.bz2: bz-patch-%.bz2
	@$(MAKECOOKIE)

patch-extract-%.gz: gz-patch-%.gz
	@$(MAKECOOKIE)

patch-extract-%.Z: gz-patch-%.Z
	@$(MAKECOOKIE)

patch-extract-%.diff: normal-patch-%.diff
	@$(MAKECOOKIE)

patch-extract-%.patch: normal-patch-%.patch
	@$(MAKECOOKIE)

patch-extract-%: normal-patch-%
	@$(MAKECOOKIE)

#################### CONFIGURE RULES ####################

TMP_DIRPATHS = --prefix=$(prefix) --exec_prefix=$(exec_prefix) --bindir=$(bindir) --sbindir=$(sbindir) --libexecdir=$(libexecdir) --datadir=$(datadir) --sysconfdir=$(sysconfdir) --sharedstatedir=$(sharedstatedir) --localstatedir=$(localstatedir) --libdir=$(libdir) --infodir=$(infodir) --lispdir=$(lispdir) --includedir=$(includedir) --mandir=$(mandir)

NODIRPATHS += --lispdir

DIRPATHS = $(filter-out $(addsuffix %,$(NODIRPATHS)), $(TMP_DIRPATHS))

# configure a package that has an autoconf-style configure
# script.
configure-%/configure:
	@echo " ==> Running configure in $*"
	cd $* && $(CONFIGURE_ENV) ./configure $(CONFIGURE_ARGS)
	@$(MAKECOOKIE)

configure-%/autogen.sh:
	@echo " ==> Running autogen.sh in $*"
	@cd $* && $(CONFIGURE_ENV) ./autogen.sh $(CONFIGURE_ARGS)
	@$(MAKECOOKIE)

# configure a package that uses imake
# FIXME: untested and likely not the right way to handle the
# arguments
configure-%/Imakefile: 
	@echo " ==> Running xmkmf in $*"
	@cd $* && $(CONFIGURE_ENV) xmkmf $(CONFIGURE_ARGS)
	@$(MAKECOOKIE)

configure-%/setup.rb:
	@echo " ==> Running setup.rb config in $*"
	@( cd $* ; $(CONFIGURE_ENV) ruby ./setup.rb config $(CONFIGURE_ARGS) )
	@$(MAKECOOKIE)

#################### BUILD RULES ####################

# build from a standard gnu-style makefile's default rule.
build-%/Makefile:
	@echo " ==> Running make in $*"
	@$(BUILD_ENV) $(MAKE) $(PARALLELMFLAGS) $(foreach TTT,$(BUILD_OVERRIDE_DIRS),$(TTT)="$($(TTT))") -C $* $(BUILD_ARGS)
	@$(MAKECOOKIE)

build-%/makefile:
	@echo " ==> Running make in $*"
	@$(BUILD_ENV) $(MAKE) $(PARALLELMFLAGS) $(foreach TTT,$(BUILD_OVERRIDE_DIRS),$(TTT)="$($(TTT))") -C $* $(BUILD_ARGS)
	@$(MAKECOOKIE)

build-%/GNUmakefile:
	@echo " ==> Running make in $*"
	@$(BUILD_ENV) $(MAKE) $(PARALLELMFLAGS) $(foreach TTT,$(BUILD_OVERRIDE_DIRS),$(TTT)="$($(TTT))") -C $* $(BUILD_ARGS)
	@$(MAKECOOKIE)

build-%/Jamfile:
	@echo " ==> Running bjam in $*"
	@( cd $* ; $(BUILD_ENV) bjam $(JAMFLAGS) $(BUILD_ARGS) )
	@$(MAKECOOKIE)

# Ruby makefiles
build-%/Rakefile:
	@echo " ==> Running rake in $*"
	@( cd $* ; $(BUILD_ENV) rake $(RAKEFLAGS) $(BUILD_ARGS) )
	@$(MAKECOOKIE)

build-%/rakefile:
	@echo " ==> Running rake in $*"
	@( cd $* ; $(BUILD_ENV) rake $(RAKEFLAGS) $(BUILD_ARGS) )
	@$(MAKECOOKIE)

build-%/setup.rb:
	@echo " ==> Running setup.rb setup in $*"
	@( cd $* ; $(BUILD_ENV) ruby ./setup.rb setup $(BUILD_ARGS) )
	@$(MAKECOOKIE)

# This can be: build, build_py, build_ext, build_clib, build_scripts
# See setup.py --help-commands for details
PYBUILD_CMD ?= build
build-%/setup.py:
	@echo " ==> Running setup.py $(PYBUILD_TYPE) in $*"
	@( cd $* ; $(BUILD_ENV) python ./setup.py $(PYBUILD_CMD) $(BUILD_ARGS) )
	@$(MAKECOOKIE)

#################### TEST RULES ####################

TEST_TARGET ?= test

# Run tests on pre-built sources
test-%/Makefile:
	@echo " ==> Running make $(TEST_TARGET) in $*"
	@$(TEST_ENV) $(MAKE) $(foreach TTT,$(TEST_OVERRIDE_DIRS),$(TTT)="$($(TTT))") -C $* $(TEST_ARGS) $(TEST_TARGET)
	@$(MAKECOOKIE)

test-%/makefile:
	@echo " ==> Running make $(TEST_TARGET) in $*"
	@$(TEST_ENV) $(MAKE) $(foreach TTT,$(TEST_OVERRIDE_DIRS),$(TTT)="$($(TTT))") -C $* $(TEST_ARGS) $(TEST_TARGET)
	@$(MAKECOOKIE)

test-%/GNUmakefile:
	@echo " ==> Running make $(TEST_TARGET) in $*"
	@$(TEST_ENV) $(MAKE) $(foreach TTT,$(TEST_OVERRIDE_DIRS),$(TTT)="$($(TTT))") -C $* $(TEST_ARGS) $(TEST_TARGET)
	@$(MAKECOOKIE)

# Ruby makefiles
test-%/Rakefile:
	@echo " ==> Running rake $(TEST_TARGET) in $*"
	@( cd $* ; $(TEST_ENV) rake $(RAKEFLAGS) $(TEST_ARGS) $(TEST_TARGET) )
	@$(MAKECOOKIE)

test-%/rakefile:
	@echo " ==> Running rake $(TEST_TARGET) in $*"
	@( cd $* ; $(TEST_ENV) rake $(RAKEFLAGS) $(TEST_ARGS) $(TEST_TARGET) )
	@$(MAKECOOKIE)

test-%/setup.py:
	@echo " ==> Running setup.py test in $*"
	@( cd $* ; $(TEST_ENV) python ./setup.py test $(TEST_ARGS) )
	@$(MAKECOOKIE)

################# INSTALL RULES ####################

# just run make install and hope for the best.
install-%/Makefile:
	@echo " ==> Running make install in $*"
	@$(INSTALL_ENV) $(MAKE) DESTDIR=$(DESTDIR) $(foreach TTT,$(INSTALL_OVERRIDE_DIRS),$(TTT)="$(DESTDIR)$($(TTT))") -C $* $(INSTALL_ARGS) install
	@$(MAKECOOKIE)

install-%/makefile:
	@echo " ==> Running make install in $*"
	@$(INSTALL_ENV) $(MAKE) DESTDIR=$(DESTDIR) $(foreach TTT,$(INSTALL_OVERRIDE_DIRS),$(TTT)="$(DESTDIR)$($(TTT))") -C $* $(INSTALL_ARGS) install
	@$(MAKECOOKIE)

install-%/GNUmakefile:
	@echo " ==> Running make install in $*"
	@$(INSTALL_ENV) $(MAKE) DESTDIR=$(DESTDIR) $(foreach TTT,$(INSTALL_OVERRIDE_DIRS),$(TTT)="$(DESTDIR)$($(TTT))") -C $* $(INSTALL_ARGS) install
	@$(MAKECOOKIE)

# Ruby makefiles
install-%/Rakefile:
	@echo " ==> Running rake install in $*"
	@( cd $* ; $(INSTALL_ENV) rake $(RAKEFLAGS) $(INSTALL_ARGS) )
	@$(MAKECOOKIE)

install-%/rakefile:
	@echo " ==> Running rake install in $*"
	@( cd $* ; $(INSTALL_ENV) rake $(RAKEFLAGS) $(INSTALL_ARGS) )
	@$(MAKECOOKIE)

install-%/setup.rb:
	@echo " ==> Running setup.rb install in $*"
	@( cd $* ; $(INSTALL_ENV) ruby ./setup.rb install --prefix=$(DESTDIR) )
	@$(MAKECOOKIE)

# This can be: install, install_lib, install_headers, install_scripts,
# or install_data.  See setup.py --help-commands for details.
PYINSTALL_CMD ?= install
install-%/setup.py:
	@echo " ==> Running setup.py $(PYINSTALL_CMD) in $*"
	@( cd $* ; $(INSTALL_ENV) python ./setup.py $(PYINSTALL_CMD) $(INSTALL_ARGS) )
	@$(MAKECOOKIE)

# pkg-config scripts
install-%-config:
	mkdir -p $(STAGINGDIR)/$(GARNAME)
	cp -f $(DESTDIR)$(bindir)/$*-config $(STAGINGDIR)/$(GARNAME)/
	$(MAKECOOKIE)

######################################
# Use a manifest file of the format:
# src:dest[:mode[:owner[:group]]]
#   as in...
# ${WORKSRC}/nwall:${bindir}/nwall:2755:root:tty
# ${WORKSRC}/src/foo:${sharedstatedir}/foo
# ${WORKSRC}/yoink:${sysconfdir}/yoink:0600

# Okay, so for the benefit of future generations, this is how it
# works:
#
# First of all, we have this file with colon-separated lines.
# The $(shell cat foo) routine turns it into a space-separated
# list of words.  The foreach iterates over this list, putting a
# colon-separated record in $(ZORCH) on each pass through.
#
# Next, we have the macro $(MANIFEST_LINE), which splits a record
# into a space-separated list, and $(MANIFEST_SIZE), which
# determines how many elements are in such a list.  These are
# purely for convenience, and could be inserted inline if need
# be.
MANIFEST_LINE = $(subst :, ,$(ZORCH)) 
MANIFEST_SIZE = $(words $(MANIFEST_LINE))

# So the install command takes a variable number of parameters,
# and our records have from two to five elements.  Gmake can't do
# any sort of arithmetic, so we can't do any really intelligent
# indexing into the list of parameters.
# 
# Since the last three elements of the $(MANIFEST_LINE) are what
# we're interested in, we make a parallel list with the parameter
# switch text (note the dummy elements at the beginning):
MANIFEST_FLAGS = notused notused --mode= --owner= --group=

# The following environment variables are set before the
# installation boogaloo begins.  This ensures that WORKSRC is
# available to the manifest and that all of the location
# variables are suitable for *installation* (that is, using
# DESTDIR)

MANIFEST_ENV += WORKSRC=$(WORKSRC)
# This was part of the "implicit DESTDIR" regime.  However:
# http://gar.lnx-bbc.org/wiki/ImplicitDestdirConsideredHarmful
#MANIFEST_ENV += $(foreach TTT,prefix exec_prefix bindir sbindir libexecdir datadir sysconfdir sharedstatedir localstatedir libdir infodir lispdir includedir mandir,$(TTT)=$(DESTDIR)$($(TTT)))

# ...and then we join a slice of it with the corresponding slice
# of the $(MANIFEST_LINE), starting at 3 and going to
# $(MANIFEST_SIZE).  That's where all the real magic happens,
# right there!
#
# following that, we just splat elements one and two of
# $(MANIFEST_LINE) on the end, since they're the ones that are
# always there.  Slap a semicolon on the end, and you've got a
# completed iteration through the foreach!  Beaujolais!

# FIXME: using -D may not be the right thing to do!
install-$(MANIFEST_FILE):
	@echo " ==> Installing from $(MANIFEST_FILE)"
	$(MANIFEST_ENV) ; $(foreach ZORCH,$(shell cat $(MANIFEST_FILE)), ginstall -Dc $(join $(wordlist 3,$(MANIFEST_SIZE),$(MANIFEST_FLAGS)),$(wordlist 3,$(MANIFEST_SIZE),$(MANIFEST_LINE))) $(word 1,$(MANIFEST_LINE)) $(word 2,$(MANIFEST_LINE)) ;)
	@$(MAKECOOKIE)

#################### DEPENDENCY RULES ####################

# These two lines are here to grandfather in all the packages that use
# BUILDDEPS
IMGDEPS += build
build_DEPENDS = $(BUILDDEPS)

# Standard deps install into the standard install dir.  For the
# BBC, we set the includedir to the build tree and the libdir to
# the install tree.  Most dependencies work this way.

$(GARDIR)/%/$(COOKIEDIR)/install:
	@echo ' ==> Building $* as a dependency'
	@$(MAKE) -C $(GARDIR)/$* install DESTIMG=$(DESTIMG)

# builddeps need to have everything put in the build DESTIMG
#$(GARDIR)/%/$(COOKIEROOTDIR)/build.d/install:
#	@echo ' ==> Building $* as a build dependency'
#	@$(MAKE) -C $(GARDIR)/$* install	DESTIMG=build

# Source Deps grab the source code for another package
# XXX: nobody uses this, but it should really be more like
# $(GARDIR)/%/cookies/patch:
srcdep-$(GARDIR)/%:
	@echo ' ==> Grabbing source for $* as a dependency'
	@$(MAKE) -C $(GARDIR)/$* patch-p extract-p > /dev/null 2>&1 || \
	 $(MAKE) -C $(GARDIR)/$* patch

# Image deps create dependencies on package installations in
# images other than the current package's DESTIMG.
IMGDEP_TARGETS = $(foreach TTT,$($*_DEPENDS),$(subst xyzzy,$(TTT),$(GARDIR)/xyzzy/$(COOKIEROOTDIR)/$*.d/install))
imgdep-%:
	@test -z "$(strip $(IMGDEP_TARGETS))" || $(MAKE) DESTIMG="$*" $(IMGDEP_TARGETS)

# Igor's info and man gzipper rule
gzip-info-man: gzip-info gzip-man

gzip-info:
	gfind $(DESTDIR) -type f -iname *.info* -not -iname *.gz | \
		gxargs -r gzip --force

gzip-man:
	gfind $(DESTDIR) -type f -iname *.[1-8] -size +2 -print | \
		gxargs -r gzip --force

compile-elisp:
	@(for d in $(ELISP_DIRS); do \
		echo " ===> Compiling .el files in $$d"; \
		cd $(PKGROOT)/$$d; \
		for f in `find . -name "*el"`; do \
			bf=`basename $$f`; \
			bd=`dirname $$f`; \
			cd $$bd; \
			emacs -L $(PKGROOT)/$$d -L $(PKGROOT)/$$d/$$bd $(EXTRA_EMACS_ARGS) -batch -f batch-byte-compile "$$bf"; \
			cd $(PKGROOT)/$$d; \
		done; \
	done)

include $(addprefix $(GARDIR)/,$(EXTRA_LIBS))

# Mmm, yesssss.  cookies my preciousssss!  Mmm, yes downloads it
# is!  We mustn't have nasty little gmakeses deleting our
# precious cookieses now must we?
.PRECIOUS: $(DOWNLOADDIR)/% $(COOKIEDIR)/% $(FILEDIR)/%
