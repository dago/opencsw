# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = gmtp
VERSION = 1.3.9
GARTYPE = v2

DESCRIPTION = MTP client
define BLURB
   MTP = Media Transfer Protocol. MTP has been adopted by most major MP3 and 
   Mobile Phone manufacturers as the method of talking to devices to
   upload/download files to/from a PC
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(DISTNAME).tar.gz

GARCOMPILER =GCC4

BUILD_DEP_PKGS +=  CSWlibgconf-dev


RUNTIME_DEP_PKGS_CSWgmtp += CSWlibid3tag0
RUNTIME_DEP_PKGS_CSWgmtp += CSWlibgconf2-4
RUNTIME_DEP_PKGS_CSWgmtp += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWgmtp += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgmtp += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgmtp += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgmtp += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgmtp += CSWlibvorbisfile3
RUNTIME_DEP_PKGS_CSWgmtp += CSWlibmtp9
RUNTIME_DEP_PKGS_CSWgmtp += CSWlibflac8


CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-gtk2

include gar/category.mk

