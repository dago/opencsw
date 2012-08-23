#####################################################################
# OpenCSW build recipe for bash-completion
#
# Copyright 2009 Yann Rouillard <yann@pleiades.fr.eu.org>
# All rights reserved.  Use is subject to license terms.
#
# Redistribution and/or use, with or without modification, is
# permitted.  This software is without warranty of any kind.  The
# author(s) shall not be liable in the event that use of the
# software causes damage.
#####################################################################

###### Package information #######

NAME = bash_completion
VERSION = 2.0
CATEGORIES = xtra
GARTYPE = v2

DESCRIPTION = Programmable completion for bash
define BLURB
  Since v2.04, bash has allowed you to intelligently program and extend its standard completion behavior to achieve complex command lines with just a few keystrokes. Imagine typing ssh [Tab] and being able to complete on hosts from your ~/.ssh/known_hosts files. Or typing man 3 str [Tab] and getting a list of all string handling functions in the UNIX manual. mount system: [Tab] would complete on all exported file-systems from the host called system, while make [Tab] would complete on all targets in Makefile. This project was conceived to produce programmable completion routines for the most common Linux/UNIX commands, reducing the amount of typing sysadmins and programmers need to do on a daily basis.
endef

ARCHALL=1

PACKAGES = CSWbashcmplt
CATALOGNAME_CSWbashcmplt = bash_completion

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

# We will not change that today
CHECKPKG_OVERRIDES_CSWbashcmplt += catalogname-does-not-match-pkgname|pkgname=CSWbashcmplt|catalogname=bash_completion|expected-catalogname=bashcmplt
# bash will complete if python s
CHECKPKG_OVERRIDES_CSWbashcmplt += missing-dependency|CSWpython

# No remaining /usr/share, /usr/local references are ok
CHECKPKG_OVERRIDES_CSWbashcmplt += file-with-bad-content|/usr/share|root/opt/csw/share/doc/bash_completion/CHANGES
CHECKPKG_OVERRIDES_CSWbashcmplt += file-with-bad-content|/usr/share|root/opt/csw/share/bash-completion/completions/wtf
CHECKPKG_OVERRIDES_CSWbashcmplt += file-with-bad-content|/usr/share|root/opt/csw/share/bash-completion/completions/openssl
CHECKPKG_OVERRIDES_CSWbashcmplt += file-with-bad-content|/usr/share|root/opt/csw/share/bash-completion/completions/dict
CHECKPKG_OVERRIDES_CSWbashcmplt += file-with-bad-content|/usr/share|root/opt/csw/share/bash-completion/completions/lintian
CHECKPKG_OVERRIDES_CSWbashcmplt += file-with-bad-content|/usr/share|root/opt/csw/share/bash-completion/completions/dpkg
CHECKPKG_OVERRIDES_CSWbashcmplt += file-with-bad-content|/usr/share|root/opt/csw/share/bash-completion/completions/mplayer
CHECKPKG_OVERRIDES_CSWbashcmplt += file-with-bad-content|/usr/local|root/opt/csw/share/bash-completion/bash_completion
CHECKPKG_OVERRIDES_CSWbashcmplt += file-with-bad-content|/usr/local|root/opt/csw/share/bash-completion/completions/puppet
CHECKPKG_OVERRIDES_CSWbashcmplt += file-with-bad-content|/usr/local|root/opt/csw/share/bash-completion/completions/sudo
CHECKPKG_OVERRIDES_CSWbashcmplt += file-with-bad-content|/usr/local|root/opt/csw/share/bash-completion/completions/mplayer



###### Upstream and OpenCSW files information #######

MASTER_SITES = http://bash-completion.alioth.debian.org/files/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(shell echo $(NAME) | tr '_' '-')-(\d+).tar.gz

DISTNAME  = $(shell echo $(NAME) | tr '_' '-')-$(VERSION)

DISTFILES  = $(DISTNAME).tar.gz
# we automatically include all 
DISTFILES += $(shell cd files; for FILE in *.completion; do echo $$FILE; done)

DISTFILES += changelog.CSW

# change the paths to use opencsw ones
PATCHFILES = opencsw_paths.patch
PATCHFILES += more_opencsw_paths.patch

##### Build and installation information #####

# the configure script doesn't seem to take in account the prefix
# env variable defined automatically by GAR
CONFIGURE_ARGS += --prefix $(prefix)

# no test script in bash_completion
TEST_SCRIPTS =

post-merge: merge-opencsw-completion merge-additional-docs merge-changelog

# we add some completion scripts for Solaris 
merge-opencsw-completion:
	@( for FILE in $(WORKDIR)/*.completion; do \
	      NFILE="`basename $$FILE | sed -e 's/\.completion$$//'`"; \
	      ginstall -D $$FILE $(PKGROOT)$(sharedstatedir)/bash_completion.d/$$NFILE; \
	done )
	@$(MAKECOOKIE)	


merge-additional-docs:
	@( for FILE in AUTHORS README CHANGES; do \
		ginstall -D "$(WORKSRC_FIRSTMOD)/$$FILE" "$(PKGROOT)$(docdir)/$(NAME)/$$FILE"; \
	done )
	@$(MAKECOOKIE)	

merge-changelog:
	ginstall -D "$(WORKDIR)/changelog.CSW" "$(PKGROOT)$(docdir)/$(NAME)/changelog.CSW"
	@$(MAKECOOKIE)

include gar/category.mk
