#####################################################################
# OpenCSW build recipe for elinks
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

NAME = elinks
VERSION = 0.11.7
CATEGORIES = net
GARTYPE = v2

DESCRIPTION = An advanced text mode web browser
define BLURB
  ELinks is an advanced and well-established feature-rich text mode Web 
  (HTTP, FTP, etc.) browser. It can render both frames and tables, is 
  highly customizable, and can be extended via Lua, Guile, Perl, or Ruby 
  scripts. It has limited support for CSS and Javascript.
endef

PACKAGES = CSWelinks

RUNTIME_DEP_PKGS  = CSWlibbz2-1-0
RUNTIME_DEP_PKGS += CSWlibexpat1
RUNTIME_DEP_PKGS += CSWlibiconv2
RUNTIME_DEP_PKGS += CSWlibidn11
RUNTIME_DEP_PKGS += CSWlibssl1-0-0
RUNTIME_DEP_PKGS += CSWlibz1
RUNTIME_DEP_PKGS += CSWlibjs1-7-0


# paths used in some default path (mailcap search path and lua doc path), this can be safely ignored
# lua doc links could be fixed if lua doc is packaged in opencsw
CHECKPKG_OVERRIDES_CSWelinks += file-with-bad-content|/usr/share|root/opt/csw/bin/elinks
CHECKPKG_OVERRIDES_CSWelinks += file-with-bad-content|/usr/share|root/opt/csw/share/man/man5/elinks.conf.5
CHECKPKG_OVERRIDES_CSWelinks += file-with-bad-content|/usr/local|root/opt/csw/share/man/man5/elinks.conf.5
CHECKPKG_OVERRIDES_CSWelinks += file-with-bad-content|/usr/local|root/opt/csw/bin/elinks

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

###### Upstream and opencsw files information #######

MASTER_SITES = http://elinks.cz/download/

DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTFILES += changelog.CSW
DISTFILES += map.bash

# Debian security path for CVE-2007-2027
PATCHFILES += elinks-417789.diff

# Provided by iconv
MERGE_EXCLUDE_FILES  = .*/charset.alias
MERGE_EXCLUDE_FILES += .*/locale.alias

##### Build and installation information #####

# we use bash instead of sh as the Makefiles
# use "test -e" unsupported with sun sh
CONFIG_SHELL = /bin/bash

#GARCOMPILER = GNU
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-88-colors 
CONFIGURE_ARGS += --enable-256-colors 
# ecma support not stable enough
# CONFIGURE_ARGS += --enable-sm-scripting
CONFIGURE_ARGS += --disable-sm-scripting

EXTRA_LD_OPTIONS = -z ignore -Bdirect -M "$(abspath $(WORKDIR)/map.elinks)"

TEST_SCRIPTS =

include gar/category.mk

# We touch these file to avoid aclocal/autoconf
# configure to be run again
pre-configure:
	touch $(WORKSRC)/aclocal.m4
	touch $(WORKSRC)/configure
	touch $(WORKSRC)/config.status

post-merge:
	@ginstall -D $(WORKDIR_FIRSTMOD)/changelog.CSW $(PKGROOT)$(docdir)/$(NAME)/changelog.CSW 

