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

URLS := $(foreach SITE,$(FILE_SITES) $(MASTER_SITES),$(addprefix $(SITE),$(DISTFILES))) $(foreach SITE,$(FILE_SITES) $(PATCH_SITES) $(MASTER_SITES),$(addprefix $(SITE),$(ALLFILES_PATCHFILES)))

# if the caller has defined _postinstall, etc targets for a package, add
# these 'dynamic script' targets to our fetch list
URLS += $(foreach DYN,$(DYNSCRIPTS),dynscr://$(DYN))

define gitsubst
$(subst git-git,git,$(if $(findstring $(1)://,$(2)),$(patsubst $(1)%,git-$(1)%,$(call URLSTRIP,$(2)))))
endef

ifdef GIT_REPOS
URLS += $(foreach R,$(GIT_REPOS),gitrepo://$(call GITPROJ,$(R)) $(foreach gitproto,git http file ssh,$(call gitsubst,$(gitproto),$(R))))
endif

# Download the file if and only if it doesn't have a preexisting
# checksum file.  Loop through available URLs and stop when you
# get one that doesn't return an error code.
# Note that GAR targets are used to download the URLs, thus:
# 1) we have to strip the colon from the URLs
# 2) the download is very costly with bigger Makefiles as they will be
#    re-evaluated for every URL (nested gmake invocation, room for improvement)
$(DOWNLOADDIR)/%:  
	@if test -f $(COOKIEDIR)/checksum-$*; then : ; else \
		echo " ==> Grabbing $@"; \
		( for i in $(filter %/$*,$(URLS)); do  \
			echo " 	==> Trying $$i"; \
			$(MAKE) -s `echo $$i | tr -d :` || continue; \
			mv $(PARTIALDIR)/$* $@; \
			break; \
		done; ) 2>&1 | grep -v '^$(MAKE)'; \
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
	@git clone --bare http://$* $(PARTIALDIR)/$(call GITPROJ,$*)
	@( cd $(PARTIALDIR)/$(call GITPROJ,$*); \
		git remote add origin http://$*; \
		git config remote.origin.fetch $(if $(GIT_REFS_$(call GITPROJ,$*)),$(GIT_REFS_$(call GITPROJ,$*)),$(GIT_DEFAULT_TRACK)); )

git//%:
	@$(GIT_MAYBEPROXY) git clone --bare git://$* $(PARTIALDIR)/$(call GITPROJ,$*)
	@( cd $(PARTIALDIR)/$(call GITPROJ,$*); \
		git remote add origin git://$*; \
		git config remote.origin.fetch $(if $(GIT_REFS_$(call GITPROJ,$*)),$(GIT_REFS_$(call GITPROJ,$*)),$(GIT_DEFAULT_TRACK)); )

git-file//%:
	@git clone --bare file:///$* $(PARTIALDIR)/$(call GITPROJ,$*)
	@( cd $(PARTIALDIR)/$(call GITPROJ,$*); \
		git remote add origin file://$*; \
		git config remote.origin.fetch $(if $(GIT_REFS_$(call GITPROJ,$*)),$(GIT_REFS_$(call GITPROJ,$*)),$(GIT_DEFAULT_TRACK)); )

git-ssh//%:
	@git clone --bare ssh://$* $(PARTIALDIR)/$(call GITPROJ,$*)
	@( cd $(PARTIALDIR)/$(call GITPROJ,$*); \
		git remote add origin ssh://$*; \
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
# The removal of the download prefix is for legacy checksums. For newstyle
# checksums without path this is not necessary.
checksum-%: $(CHECKSUM_FILE) 
	@echo " ==> Running checksum on $*"
	@if ggrep -- '[ /]$*$$' $(CHECKSUM_FILE); then \
		if cat $(CHECKSUM_FILE) | sed -e 's!download/!!' | (cd $(DOWNLOADDIR); LC_ALL="C" LANG="C" gmd5sum -c 2>&1) | \
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


################### UWATCH VARIABLES ###################
UPSTREAM_MASTER_SITES ?= $(MASTER_SITES)
ENABLE_UPSTREAM_WATCH ?= 1

UW_ARGS = $(addsuffix ',$(addprefix --upstream-url=',$(UPSTREAM_MASTER_SITES)))
REGEXP_ARGS = $(addsuffix ',$(addprefix --regexp=',$(UFILES_REGEX)))
VERSION_ARGS = $(addsuffix ',$(addprefix --current-version=',$(VERSION)))
define versionlist
	$(if $(UFILES_REGEX),$(shell http_proxy=$(http_proxy) ftp_proxy=$(ftp_proxy) $(GARBIN)/upstream_watch get-upstream-version-list $(UW_ARGS) $(REGEXP_ARGS)))
endef

########################################################
# Display uwatch informations
#
get-uwatch-configuration:
	@if [ '$(ENABLE_UPSTREAM_WATCH)' -ne '1' ] ; then \
		echo "$(NAME) - Upstream Watch is disabled" ; \
	else \
		echo "$(NAME) - Upstream Watch is enabled is enabled" ; \
		if [ ! -n '$(UFILES_REGEX)' ]; then \
			echo "$(NAME) - UFILES_REGEX is not set" ; \
		else \
			echo "$(NAME) - UFILES_REGEX is : $(UFILES_REGEX)" ; \
		fi; \
		if [ ! -n '$(UPSTREAM_MASTER_SITES)' ]; then \
			echo "$(NAME) - UPSTREAM_MASTER_SITES is not set" ; \
		else \
			echo "$(NAME) - UPSTREAM_MASTER_SITES is : $(UPSTREAM_MASTER_SITES)" ; \
		fi; \
		if [ ! -n '$(VERSION)' ]; then \
			echo "$(NAME) - VERSION is not set" ; \
		else \
			echo "$(NAME) - Current version is : $(VERSION)" ; \
		fi ; \
	fi ; 

########################################################
# Retrieve the list of upstream versions
#
get-upstream-version-list: VERSIONLIST = $(call versionlist)
get-upstream-version-list:
	@if [ '$(ENABLE_UPSTREAM_WATCH)' -ne '1' ] ; then \
		echo "$(NAME) - Upstream Watch is disabled" ; \
	else \
		if [ ! -n '$(UFILES_REGEX)' ]; then \
			echo "$(NAME) - Error UFILES_REGEX is not set" ; \
			false; \
		fi; \
		if [ ! -n '$(UPSTREAM_MASTER_SITES)' ]; then \
			echo "$(NAME) - Error UPSTREAM_MASTER_SITES is not set" ; \
			false; \
		fi; \
		if [ ! -n '$(VERSION)' ]; then \
			echo "$(NAME) - Error VERSION is not set" ; \
			false; \
		fi; \
		if [ -n "$(VERSIONLIST)" ] ; then \
			for VERSION in $(VERSIONLIST) ""; do \
				if [ ! "$$VERSION" -eq "" ] ; then \
					echo "$$VERSION" ; \
				fi ; \
			done ; \
		else \
			echo "No version found. Please check UPSTREAM_MASTER_SITES and UFILES_REGEX variables in the Makefile" ; \
		fi ; \
	fi ;

########################################################
# Retrieve the newest upstream version
#
LATESTVERSION:=$(shell http_proxy=$(http_proxy) ftp_proxy=$(ftp_proxy) $(GARBIN)/upstream_watch get-upstream-latest-version $(UW_ARGS) $(REGEXP_ARGS))
get-upstream-latest-version:
	@if [ '$(ENABLE_UPSTREAM_WATCH)' -ne '1' ] ; then \
		echo "$(NAME) - Upstream Watch is disabled" ; \
	else \
		if [ ! -n '$(UFILES_REGEX)' ]; then \
			echo "$(NAME) - Error UFILES_REGEX is not set" ; \
			false; \
		fi; \
		if [ ! -n '$(UPSTREAM_MASTER_SITES)' ]; then \
			echo "$(NAME) - Error UPSTREAM_MASTER_SITES is not set" ; \
			false; \
		fi; \
		if [ ! -n '$(VERSION)' ]; then \
			echo "$(NAME) - Error VERSION is not set" ; \
			false; \
		fi; \
		LATEST=$(LATESTVERSION) ; \
		if [ -n "$$LATEST" ] ; then \
			echo $$LATEST ; \
		else \
			echo "No version found. Please check UPSTREAM_MASTER_SITES and UFILES_REGEX variables in the Makefile" ; \
		fi ; \
	fi ;

########################################################
# Compare local and upstream versions
#
CHECKUPSTREAMVERSION=$(shell http_proxy=$(http_proxy) ftp_proxy=$(ftp_proxy) $(GARBIN)/upstream_watch check-upstream $(UW_ARGS) $(REGEXP_ARGS) $(VERSION_ARGS) )
check-upstream:
	@if [ '$(ENABLE_UPSTREAM_WATCH)' -ne '1' ] ; then \
		echo "$(NAME) - Upstream Watch is disabled" ; \
	else \
		if [ ! -n '$(UFILES_REGEX)' ]; then \
			echo "$(NAME) - Error UFILES_REGEX is not set" ; \
			false; \
		fi; \
		if [ ! -n '$(UPSTREAM_MASTER_SITES)' ]; then \
			echo "$(NAME) - Error UPSTREAM_MASTER_SITES is not set" ; \
			false; \
		fi; \
		if [ ! -n '$(VERSION)' ]; then \
			echo "$(NAME) - Error VERSION is not set" ; \
			false; \
		fi; \
		LATEST=$(CHECKUPSTREAMVERSION) ; \
		if [ -n "$$LATEST" ] ; then \
			echo "$(NAME) : a new version of upstream files is available : $$LATEST"; \
		else \
			echo "$(NAME) : Package is up-to-date. Current version is $(VERSION)" ; \
		fi ; \
	fi


########################################################
# Create upgrade branch from current to latest upstream
#
upgrade-to-latest-upstream:
	@echo "In upgrade-to-latest-upstream" ; \
	if [ '$(ENABLE_UPSTREAM_WATCH)' -ne '1' ] ; then \
		echo "$(NAME) - Upstream Watch is disabled" ; \
	else \
		if [ ! -n '$(UFILES_REGEX)' ]; then \
			echo "$(NAME) - Error UFILES_REGEX is not set" ; \
			false; \
		fi; \
		if [ ! -n '$(UPSTREAM_MASTER_SITES)' ]; then \
			echo "$(NAME) - Error UPSTREAM_MASTER_SITES is not set" ; \
			false; \
		fi; \
		if [ ! -n '$(VERSION)' ]; then \
			echo "$(NAME) - Error VERSION is not set" ; \
			false; \
		fi; \
		LATEST=$(CHECKUPSTREAMVERSION) ; \
		if [ ! -f "$(COOKIEDIR)/upgrade-to-latest-upstream-$$LATEST" ] ; then \
			if [ ! -d "../branches/upgrade_from_$(VERSION)_to_$$LATEST" ] ; then \
				echo "Not a dir : ../branches/upgrade_from_$(VERSION)_to_$$LATEST" ; \
				if [ -n "$$LATEST" ] ; then \
					echo "$(NAME) : a new version of upstream files is available. Creating upgrade branch from version $(VERSION) to $$LATEST"; \
					VERSIONUPGRADE="$(shell http_proxy=$(http_proxy) ftp_proxy=$(ftp_proxy) $(GARBIN)/upstream_watch upgrade-to-version --current-version=$(VERSION) --target-version=$(CHECKUPSTREAMVERSION))" ; \
					if [ -n "$$VERSIONUPGRADE" ] ; then \
						echo $$VERSIONUPGRADE ; \
					fi ; \
				else \
					echo "$(NAME) : Package is up-to-date. Upstream site has no version newer than $(VERSION)" ; \
				fi ; \
			else \
				echo "Upgrade branch from version $(VERSION) to version $$LATEST already exist" ; \
			fi ; \
			$(MAKE) upgrade-to-latest-upstream-$$LATEST >/dev/null; \
		else \
			echo "Upgrade branch to version $$LATEST already created by upstream_watch" ; \
		fi ; \
	fi

########################################################
#
get-gar-version:
	@if [ ! -n '$(VERSION)' ]; then \
		echo "$(NAME) - VERSION is not defined" ; \
		false; \
	else \
		echo "$(NAME) - GAR version is $(VERSION)" ; \
	fi ;

upgrade-to-latest-upstream-%:
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

# rule to extract files with tar and xz
tar-xz-extract-%:
	@echo " ==> Extracting $(DOWNLOADDIR)/$*"
	@xz -dc $(DOWNLOADDIR)/$* | gtar $(TAR_ARGS) -xf - -C $(EXTRACTDIR)
	@$(MAKECOOKIE)

# rule to extract files with tar and lz
tar-lz-extract-%:
	@echo " ==> Extracting $(DOWNLOADDIR)/$*"
	@lzip -dc $(DOWNLOADDIR)/$* | gtar $(TAR_ARGS) -xf - -C $(EXTRACTDIR)
	@$(MAKECOOKIE)

# rule to extract files with tar and lzma
tar-lzma-extract-%:
	@echo " ==> Extracting $(DOWNLOADDIR)/$*"
	@lzma -dc $(DOWNLOADDIR)/$* | gtar $(TAR_ARGS) -xf - -C $(EXTRACTDIR)
	@$(MAKECOOKIE)

# extract compressed single files
gz-extract-%:
	@echo " ==> Decompressing $(DOWNLOADDIR)/$*"
	@cp $(DOWNLOADDIR)/$* $(WORKDIR)/
	@gzip -d $(WORKDIR)/$*
	@$(MAKECOOKIE)

gz-extract-%:
	@echo " ==> Decompressing $(DOWNLOADDIR)/$*"
	@cp $(DOWNLOADDIR)/$* $(WORKDIR)/
	@gzip -d $(WORKDIR)/$*
	@$(MAKECOOKIE)

xz-extract-%:
	@echo " ==> Decompressing $(DOWNLOADDIR)/$*"
	@cp $(DOWNLOADDIR)/$* $(WORKDIR)/
	@xz -d $(WORKDIR)/$*
	@$(MAKECOOKIE)

lz-extract-%:
	@echo " ==> Decompressing $(DOWNLOADDIR)/$*"
	@cp $(DOWNLOADDIR)/$* $(WORKDIR)/
	@lzip -d $(WORKDIR)/$*
	@$(MAKECOOKIE)

lzma-extract-%:
	@echo " ==> Decompressing $(DOWNLOADDIR)/$*"
	@cp $(DOWNLOADDIR)/$* $(WORKDIR)/
	@lzma -d $(WORKDIR)/$*
	@$(MAKECOOKIE)

# extra dependency rule for git repos, that will allow the user
# to supply an alternate target at their discretion
git-extract-%:
	@echo " ===> Extracting Git Repo $(DOWNLOADDIR)/$* (Treeish: $(call GIT_TREEISH,$*))"
	git --bare archive --prefix=$(NAME)-$(VERSION)/ --remote=file://$(abspath $(DOWNLOADDIR))/$*/ $(call GIT_TREEISH,$*) | gtar -xf - -C $(EXTRACTDIR)
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
	@# Make sure to keep symlinks and don't traverse recursive ones
	@(cd $(DOWNLOADDIR); tar cf - $*) | (cd $(WORKDIR); tar xf -)
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

extract-archive-%.tar.xz: tar-xz-extract-%.tar.xz
	@$(MAKECOOKIE)

extract-archive-%.tar.lz: tar-lz-extract-%.tar.lz
	@$(MAKECOOKIE)

extract-archive-%.tar.lzma: tar-lzma-extract-%.tar.lzma
	@$(MAKECOOKIE)

extract-archive-%.zip: zip-extract-%.zip
	@$(MAKECOOKIE)

extract-archive-%.ZIP: zip-extract-%.ZIP
	@$(MAKECOOKIE)

extract-archive-%.deb: deb-bin-extract-%.deb
	@$(MAKECOOKIE)

extract-archive-%.gz: gz-extract-%.gz
	@$(MAKECOOKIE)

extract-archive-%.bz2: bz-extract-%.bz2
	@$(MAKECOOKIE)

extract-archive-%.xz: xz-extract-%.xz
	@$(MAKECOOKIE)

extract-archive-%.lz: lz-extract-%.lz
	@$(MAKECOOKIE)

extract-archive-%.lzma: lzma-extract-%.lzma
	@$(MAKECOOKIE)

extract-archive-%.git: git-extract-%.git
	@$(MAKECOOKIE)

extract-copy-%: cp-extract-%
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

# apply xzipped patches
xz-patch-%:
	@echo " ==> Applying patch $(DOWNLOADDIR)/$*"
	@xz -dc $(DOWNLOADDIR)/$* | $(GARPATCH)
	@( cd $(WORKSRC); git add -A; \
		git commit -am "old xz-style patch: $*"; )
	@$(MAKECOOKIE)

# apply bzipped patches
bz-patch-%:
	@echo " ==> Applying patch $(DOWNLOADDIR)/$*"
	@bzip2 -dc $(DOWNLOADDIR)/$* | $(GARPATCH)
	@( cd $(WORKSRC); git add -A; \
		git commit -am "old bz-style patch: $*"; )
	@$(MAKECOOKIE)

# apply gzipped patches
gz-patch-%:
	@echo " ==> Applying patch $(DOWNLOADDIR)/$*"
	@gzip -dc $(DOWNLOADDIR)/$* | $(GARPATCH)
	@( cd $(WORKSRC); git add -A; \
		git commit -am "old gz-style patch: $*"; )
	@$(MAKECOOKIE)

# apply normal patches (git format-patch output or old-style diff -r)
normal-patch-%:
	@echo " ==> Applying patch $(DOWNLOADDIR)/$*"
	@( if ggrep -q 'diff --git' $(abspath $(DOWNLOADDIR)/$*); then \
		cd $(WORKSRC); git am --ignore-space-change --ignore-whitespace $(abspath $(DOWNLOADDIR)/$*); \
	   else \
		echo Adding old-style patch...; \
		$(GARPATCH) < $(DOWNLOADDIR)/$*; \
		cd $(WORKSRC); git add -A; \
		git commit -am "old style patch: $*"; \
	   fi )
	@$(MAKECOOKIE)

### PATCH FILE TYPE MAPPINGS ###
# These rules specify which of the above patch action rules to use for a given
# file extension.  Often support for a given patch format can be handled by
# simply adding a rule here.

patch-extract-%.xz: xz-patch-%.xz
	@$(MAKECOOKIE)

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

# WAF build, for details see http://code.google.com/p/waf/
configure-%/waf:
	@echo " ==> Running waf configure in $*"
	cd $* && $(CONFIGURE_ENV) ./waf configure $(CONFIGURE_ARGS)
	@$(MAKECOOKIE)

#################### BUILD RULES ####################

# build from a standard gnu-style makefile's default rule.
build-%/Makefile:
	@echo " ==> Running make in $*"
	$(BUILD_ENV) $(MAKE) $(PARALLELMFLAGS) $(foreach TTT,$(BUILD_OVERRIDE_VARS),$(TTT)="$(BUILD_OVERRIDE_VAR_$(TTT))") $(foreach TTT,$(BUILD_OVERRIDE_DIRS),$(TTT)="$($(TTT))") -C $* $(BUILD_ARGS)
	@$(MAKECOOKIE)

build-%/makefile:
	@echo " ==> Running make in $*"
	@$(BUILD_ENV) $(MAKE) $(PARALLELMFLAGS) $(foreach TTT,$(BUILD_OVERRIDE_VARS),$(TTT)="$(BUILD_OVERRIDE_VAR_$(TTT))") $(foreach TTT,$(BUILD_OVERRIDE_DIRS),$(TTT)="$($(TTT))") -C $* $(BUILD_ARGS)
	@$(MAKECOOKIE)

build-%/GNUmakefile:
	@echo " ==> Running make in $*"
	@$(BUILD_ENV) $(MAKE) $(PARALLELMFLAGS) $(foreach TTT,$(BUILD_OVERRIDE_VARS),$(TTT)="$(BUILD_OVERRIDE_VAR_$(TTT))")  $(foreach TTT,$(BUILD_OVERRIDE_DIRS),$(TTT)="$($(TTT))") -C $* $(BUILD_ARGS)
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

# WAF build, for details see http://code.google.com/p/waf/
build-%/waf:
	@echo " ==> Running waf build in $*"
	@$(cd $* ; (BUILD_ENV) ./waf build $(BUILD_ARGS) )
	@$(MAKECOOKIE)

# This can be: build, build_py, build_ext, build_clib, build_scripts
# See setup.py --help-commands for details
PYBUILD_CMD ?= build
build-%/setup.py:
	@echo " ==> Running setup.py $(PYBUILD_TYPE) in $*"
	@( cd $* ; $(BUILD_ENV) python ./setup.py $(PYBUILD_CMD) $(BUILD_ARGS) )
	@$(MAKECOOKIE)

#################### CLEAN RULES ####################

CLEAN_ARGS ?= clean
 
# build from a standard gnu-style makefile's default rule.
clean-%/Makefile:
	@echo " ==> Running clean in $*"
	@$(BUILD_ENV) $(MAKE) $(foreach TTT,$(BUILD_OVERRIDE_DIRS),$(TTT)="$($(TTT))") -C $* $(CLEAN_ARGS)
	@rm -f $(COOKIEDIR)/build-$*

clean-%/makefile:
	@echo " ==> Running clean in $*"
	@$(BUILD_ENV) $(MAKE) $(foreach TTT,$(BUILD_OVERRIDE_DIRS),$(TTT)="$($(TTT))") -C $* $(CLEAN_ARGS)
	@rm -f $(COOKIEDIR)/build-$*

clean-%/GNUmakefile:
	@echo " ==> Running clean in $*"
	@$(BUILD_ENV) $(MAKE) $(foreach TTT,$(BUILD_OVERRIDE_DIRS),$(TTT)="$($(TTT))") -C $* $(CLEAN_ARGS)
	@rm -f $(COOKIEDIR)/build-$*

clean-%/Jamfile:
	$(error *** Don't know how to clean Jamfiles)

clean-%/Rakefile:
	$(error *** Don't know how to clean Rakefiles)

clean-%/rakefile:
	$(error *** Don't know how to clean Rakefiles)

clean-%/setup.rb:
	$(error *** Don't know how to clean Ruby setups)

clean-%/setup.py:
	$(error *** Don't know how to clean Python builds)

#################### TEST RULES ####################

TEST_TARGET ?= test

# Run tests on pre-built sources
test-%/Makefile:
	@echo " ==> Running make $(TEST_TARGET) in $*"
	$(TEST_ENV) $(MAKE) $(foreach TTT,$(TEST_OVERRIDE_VARS),$(TTT)="$(TEST_OVERRIDE_VAR_$(TTT))") $(foreach TTT,$(TEST_OVERRIDE_DIRS),$(TTT)="$($(TTT))") -C $* $(TEST_ARGS) $(TEST_TARGET)
	@$(MAKECOOKIE)

test-%/makefile:
	@echo " ==> Running make $(TEST_TARGET) in $*"
	@$(TEST_ENV) $(MAKE) $(foreach TTT,$(TEST_OVERRIDE_VARS),$(TTT)="$(TEST_OVERRIDE_VAR_$(TTT))") $(foreach TTT,$(TEST_OVERRIDE_DIRS),$(TTT)="$($(TTT))") -C $* $(TEST_ARGS) $(TEST_TARGET)
	@$(MAKECOOKIE)

test-%/GNUmakefile:
	@echo " ==> Running make $(TEST_TARGET) in $*"
	@$(TEST_ENV) $(MAKE) $(foreach TTT,$(TEST_OVERRIDE_VARS),$(TTT)="$(TEST_OVERRIDE_VAR_$(TTT))") $(foreach TTT,$(TEST_OVERRIDE_DIRS),$(TTT)="$($(TTT))") -C $* $(TEST_ARGS) $(TEST_TARGET)
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
	@$(INSTALL_ENV) $(MAKE) DESTDIR=$(DESTDIR) $(foreach TTT,$(INSTALL_OVERRIDE_VARS),$(TTT)="$(INSTALL_OVERRIDE_VAR_$(TTT))") $(foreach TTT,$(INSTALL_OVERRIDE_DIRS),$(TTT)="$(DESTDIR)$($(TTT))") -C $* $(INSTALL_ARGS) install
	@$(MAKECOOKIE)

install-%/makefile:
	@echo " ==> Running make install in $*"
	@$(INSTALL_ENV) $(MAKE) DESTDIR=$(DESTDIR) $(foreach TTT,$(INSTALL_OVERRIDE_VARS),$(TTT)="$(INSTALL_OVERRIDE_VAR_$(TTT))") $(foreach TTT,$(INSTALL_OVERRIDE_DIRS),$(TTT)="$(DESTDIR)$($(TTT))") -C $* $(INSTALL_ARGS) install
	@$(MAKECOOKIE)

install-%/GNUmakefile:
	@echo " ==> Running make install in $*"
	@$(INSTALL_ENV) $(MAKE) DESTDIR=$(DESTDIR) $(foreach TTT,$(INSTALL_OVERRIDE_VARS),$(TTT)="$(INSTALL_OVERRIDE_VAR_$(TTT))") $(foreach TTT,$(INSTALL_OVERRIDE_DIRS),$(TTT)="$(DESTDIR)$($(TTT))") -C $* $(INSTALL_ARGS) install
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

# WAF build, for details see http://code.google.com/p/waf/
install-%/waf:
	@echo " ==> Running waf install in $*"
	@$(cd $* ; (INSTALL_ENV) ./waf install $(INSTALL_ARGS) )
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
	mkdir -p $(STAGINGDIR)/$(NAME)
	cp -f $(DESTDIR)$(bindir)/$*-config $(STAGINGDIR)/$(NAME)/
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
