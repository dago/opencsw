# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = fabric
VERSION = 1.0.1
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = Remote deployment and orchestration tool
define BLURB
  Fabric is a Python (2.5 or higher) library and command-line tool for
  streamlining the use of SSH for application deployment or systems
  administration tasks. It provides a basic suite of operations for
  executing local or remote shell commands (normally or via sudo) and
  uploading/downloading files, as well as auxiliary functionality such as
  prompting the running user for input, or aborting execution.
endef

MASTER_SITES = http://code.fabfile.org/projects/fabric/files/
DISTNAME     = Fabric-$(VERSION)
DISTFILES    = $(DISTNAME).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
