NAME = Net-CUPS
VERSION = 0.61
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DHAGEMAN

DESCRIPTION = Common Unix Printing System Interface
define BLURB
  Net::CUPS is an object oriented interface to the Common Unix Printing System.
endef

LICENSE_TEXT = This module is licensed under the perl license

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386
PACKAGES = CSWpm-net-cups
CATALOGNAME = pm_net_cups

REINPLACE_MATCH = /usr/share
REINPLACE_WITH = /opt/csw/share
REINPLACE_FILES = lib/Net/CUPS.pm

BUILD_DEP_PKGS  = CSWcups-dev
RUNTIME_DEP_PKGS += CSWlibgcrypt11
RUNTIME_DEP_PKGS += CSWlibz1
RUNTIME_DEP_PKGS += CSWlibgpg-error0
RUNTIME_DEP_PKGS += CSWlibcom-err3
RUNTIME_DEP_PKGS += CSWlibkrb5-3
RUNTIME_DEP_PKGS += CSWlibgnutls26
RUNTIME_DEP_PKGS += CSWlibcups2
RUNTIME_DEP_PKGS += CSWlibk5crypto3

include gar/category.mk
