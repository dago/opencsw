# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! The build instruction for unix are wrong. They reference files that don't
#   exist (srcunx/unx.mak). There isn't any information online about how to
#   build gsview-5.0. We can't build gsview-4.9 because our ghostscript it too
#   new.

NAME = gsview
VERSION = 5.0
GARTYPE = v2

DESCRIPTION = Brief description

MASTER_SITES = http://pages.cs.wisc.edu/~ghost/gsview/download/
DISTFILES  = gsv50src.zip

CONFIGURE_SCRIPTS =

BUILD_SCRIPTS = custom

include gar/category.mk


# post-extract:
# 	cd $(WORKDIR) && \
# 	 	unzip -aa gsv50src.zip && \
# 		unzip -o "gsview-5.0/binary/*"
# 	@$(MAKECOOKIE)

build-custom:
	false
# 	cd $(WORKSRC) && \
# 		cp srcunx/unx.mak Makefile && \
# 		gmake
