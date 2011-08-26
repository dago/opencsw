# $Id$
NAME = aria2
VERSION = 1.12.1
CATEGORIES = utils

DESCRIPTION = The Next Generation Download Utility
define BLURB
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tar.xz

# The build is stuck at a rather complicated issue described here:
#   http://web.archiveorange.com/archive/v/IOUkmsEuESHJAAo1xjyi
# "/opt/SUNWspro/prod/include/CC/stlport4/stl/_function.h", line 164: Error: Formal argument __r of type aria2::SelectEventPoll::CommandEvent& in call to std::mem_fun1_ref_t<void, aria2::SelectEventPoll::CommandEvent, int>::operator()(aria2::SelectEventPoll::CommandEvent&, int) const requires an lvalue.
# "/opt/SUNWspro/prod/include/CC/stlport4/stl/_algo.h", line 65:     Where: While instantiating "std::binder2nd<std::mem_fun1_ref_t<void, aria2::SelectEventPoll::CommandEvent, int>>::operator()(const aria2::SelectEventPoll::CommandEvent&) const".
# "/opt/SUNWspro/prod/include/CC/stlport4/stl/_algo.h", line 65:     Where: Instantiated from non-template code.
PATCHFILES += 0001-Port-patches-to-1.12.1.patch

#PATCHFILES += 0001-Remove-tailing-commas-in-enum.patch
#PATCHFILES += 0002-Use-inttypes-if-stdint-is-not-available.patch
#PATCHFILES += 0003-Skip-Wall-for-Sun-Studio.patch
#PATCHFILES += 0004-Include-string.h-if-available.patch
#PATCHFILES += 0005-Add-missing-includes.patch

EXTRA_CXXFLAGS += -library=stlport4
EXTRA_CXXFLAGS += -features=zla

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
