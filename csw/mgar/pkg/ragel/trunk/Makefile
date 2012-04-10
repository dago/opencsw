# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = ragel
VERSION = 6.7
GARTYPE = v2
CATEGORIES = devel

DESCRIPTION = Ragel State Machine Compiler
define BLURB
Ragel compiles executable finite state machines from regular languages.
Ragel targets C, C++, Objective-C, D, Java and Ruby. Ragel state machines
can not only recognize byte sequences as regular expression machines do,
but can also execute code at arbitrary points in the recognition of a
regular language. Code embedding is done using inline operators that
do not disrupt the regular language syntax. 
endef

MASTER_SITES = http://www.complang.org/ragel/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

GARCOMPILER = GNU
CONFIGURE_ARGS = $(DIRPATHS)

RUNTIME_DEP_PKGS += CSWlibgcc-s1
RUNTIME_DEP_PKGS += CSWlibstdc++6

include gar/category.mk

