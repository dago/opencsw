# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME    = npth
VERSION = 1.1
GARTYPE = v2

DESCRIPTION = The New GNU Portable Threads Library
define BLURB
  This is a library to provide the GNU Pth API and thus a
  non-preemptive threads implementation.
  In contrast to GNU Pth is is based on the system's standard threads
  implementation.  This allows the use of libraries which are not
  compatible to GNU Pth.  Experience with a Windows Pth emulation
  showed that this is a solid way to provide a co-routine based
  framework.
endef

GARCOMPILER = GCC4

MASTER_SITES = ftp://ftp.gnupg.org/gcrypt/npth/
DISTFILES  = $(DISTNAME).tar.bz2

BUILD64 = 1

CONFIGURE_ARGS = $(DIRPATHS)

EXTRA_CFLAGS = -std=c99
# -pedantic -Wall -W -D__EXTENSIONS__ -D_XPG6

include gar/category.mk

