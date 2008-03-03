GARNAME = bash_completion
GARVERSION = 20060301
CATEGORIES = xtra

DESCRIPTION = Programmable completion for bash
define BLURB
  Since v2.04, bash has allowed you to intelligently program and extend its standard completion behavior to achieve complex command lines with just a few keystrokes. Imagine typing ssh [Tab] and being able to complete on hosts from your ~/.ssh/known_hosts files. Or typing man 3 str [Tab] and getting a list of all string handling functions in the UNIX manual. mount system: [Tab] would complete on all exported file-systems from the host called system, while make [Tab] would complete on all targets in Makefile. This project was conceived to produce programmable completion routines for the most common Linux/UNIX commands, reducing the amount of typing sysadmins and programmers need to do on a daily basis.
endef

MASTER_SITES = http://www.caliban.org/files/bash/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(shell echo $(GARNAME) | tr '_' '-')-(\d+).tar.gz

DISTFILES  = $(shell echo $(GARNAME) | tr '_' '-')-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWbash_completion,)
DISTFILES += $(shell cd files; for FILE in *.completion; do echo $$FILE; done)

# add blastwave paths
PATCHFILES = blastwave.patch

WORKSRC = $(WORKDIR)/$(GARNAME)

# no configure/Makefile
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = manual
TEST_SCRIPTS =

install-manual:
	@ginstall -d $(DESTDIR)$(sysconfdir)
	@ginstall -d $(DESTDIR)$(sysconfdir)/bash_completion.d
	@ginstall -D $(WORKSRC)/bash_completion $(DESTDIR)$(sysconfdir)/bash_completion
	@( for FILE in $(WORKDIR)/*.completion; do \
		NFILE="`basename $$FILE | sed -e 's/\.completion$$//'`"; \
		ginstall -D $$FILE $(DESTDIR)$(sysconfdir)/bash_completion.d/$$NFILE; \
	done )
	@ginstall -d $(DESTDIR)$(docdir)/$(GARNAME)
	@( for FILE in BUGS README TODO Changelog; do \
		ginstall -D $(WORKSRC)/$$FILE $(DESTDIR)$(docdir)/$(GARNAME)/$$FILE; \
	done )


include ../category.mk
