# Vim Patches
PATCHDIRLEVEL = 2
PATCHFILES += $(notdir $(wildcard $(FILEDIR)/vim_*.diff))

# Include the patchrev in the package version
LASTPATCH = $(word $(words $(PATCHFILES)), $(PATCHFILES))
PATCHREV = $(patsubst vim_$(DISTVERSION).%.diff,%,$(LASTPATCH))
GARVERSION = $(DISTVERSION).$(PATCHREV)
