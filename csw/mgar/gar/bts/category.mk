# vim: ft=make ts=4 sw=4 noet
#
# This Makefile is the main entry point to GAR and is included by
# each package build description. As such, the file name 'category.mk'
# is slightly misleading and could be subject to future change.
#

# Safety check, we need GNU make >= 3.81 for the magic further below,
# more precisly: 3.80 for $(MAKEFILE_LIST), 3.81 for $(lastword ...)
# c.f.: http://cvs.savannah.gnu.org/viewvc/make/NEWS?root=make&view=markup
ifeq (,$(and $(MAKEFILE_LIST),$(lastword test)))
define error_msg
GNU make >= 3.81 required.
Try "pkgutil -i gmake" and prepend /opt/csw/bin to your $$PATH.
endef
  $(error $(error_msg))
endif

# Determine this file's directory, i.e. the GAR base directory. We
# need to do this dynamically as we don't want to rely on the presence
# of gar/ symlinks in each build directory.
GARDIR := $(dir $(lastword $(MAKEFILE_LIST)))

$(if $(findstring $(CATEGORIES),apps devel lang lib net server utils xorg xtra),\
  $(warning The categories with no special meaning have been renamed to 'default', please remove the CATEGORIES line as for the default case this is no longer necessary)\
)

CATEGORIES ?= default

ifeq (,$(wildcard $(GARDIR)/categories/$(CATEGORIES)/category.mk))
  $(error The category '$(CATEGORIES)' is invalid. Valid categories are: $(patsubst $(GARDIR)/categories/%,%,$(wildcard $(GARDIR)/categories/*)))
endif

include $(GARDIR)/categories/$(CATEGORIES)/category.mk
