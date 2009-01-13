# Vim 72 patchset
PATCHREV = 082
PATCHDIRLEVEL = 0
GARVERSION = $(DISTVERSION).$(PATCHREV)
PATCHFILES += $(foreach T,$(shell gseq -f "%03g" 001 $(PATCHREV)),$(DISTVERSION).$(T))

# Fix vimtutor
PATCHFILES += vimtutor.diff
