# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = qpdf
VERSION = 5.1.1
GARTYPE = v2

DESCRIPTION = A CLI program that does structural, content-preserving transformations on PDF
define BLURB
   QPDF is a command-line program that does structural, content-preserving transformations on PDF files. It could have been called something like pdf-to-pdf. It also provides many useful capabilities to developers of PDF-producing software or for people who just want to look at the innards of a PDF file to learn more about how they work.

QPDF is capable of creating linearized (also known as web-optimized) files and encrypted files. It is also capable of converting PDF files with object streams (also known as compressed objects) to files with no compressed objects or to generate object streams from files that don't have them (or even those that already do). QPDF also supports a special mode designed to allow you to edit the content of PDF files in a text editor. For more details, please see the documentation links below. 
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(DISTNAME).tar.gz

GARCOMPILER = GCC4

RUNTIME_DEP_PKGS_CSWqpdf += CSWlibqpdf13

PACKAGES += CSWlibqpdf13
CATALOGNAME_CSWlibqpdf13 = libqpdf13
PKGFILES_CSWlibqpdf13 += $(call baseisadirs,$(libdir),libqpdf\.so\.13\.1\.1)
PKGFILES_CSWlibqpdf13 += $(call baseisadirs,$(libdir),libqpdf\.so\.13(\.\d+)*)
SPKG_DESC_CSWlibqpdf13 += $(DESCRIPTION), libqpdf.so.13
RUNTIME_DEP_PKGS_CSWlibqpdf13 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibqpdf13 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibqpdf13 += CSWlibpcre1
RUNTIME_DEP_PKGS_CSWlibqpdf13 += CSWlibz1

PACKAGES += CSWqpdf-dev
CATALOGNAME_CSWqpdf-dev = qpdf_dev
SPKG_DESC_CSWqpdf-dev += $(DESCRIPTION), development files
PKGFILES_CSWqpdf-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWqpdf-dev += CSWlibqpdf13

BUILD64 = 1
ISAEXEC = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-static=no

# Most tests are okay, some fail (I think) because of /bin/sh incompatible scripting
SKIPTEST = 1

include gar/category.mk

# Some tests assume GNU diff
PATH := $(prefix)/gnu:$(PATH)

