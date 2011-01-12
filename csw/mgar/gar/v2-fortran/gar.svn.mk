# vim: ft=make ts=4 sw=4 noet
#
# $Id$
#
# Copyright 2008-2009 OpenCSW
#
# Redistribution and/or use, with or without modification, is
# permitted. This software is without warranty of any kind. The
# author(s) shall not be liable in the event that use of the
# software causes damage.
#
# gar.svn.mk - Targets for working with svn
#

scm-help:
	@cat $(GARDIR)/scm-help

scm-update-all: scm-update-package scm-update-gar

scm-update-package:
	$(SVN) --ignore-externals up

scm-update-gar:
	cd $(GARDIR) && $(SVN) --ignore-externals up

scm-update-ignores:
	$(GARDIR)/bin/svnignore work cookies download

scm-tag-release:
	$(SVN) cp ../trunk ../tags/$(NAME)-$(VERSION)$(SPKG_REVSTAMP)

.PHONY: scm-help scm-update-all scm-update-package scm-update-gar scm-update-ignores scm-tag-release
