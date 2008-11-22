# Vim 71 patchset
PATCHREV = 147
PATCHDIRLEVEL = 2
#PATCHFILES += 7.1.001-$(PATCHREV)
GARVERSION = $(DISTVERSION).$(PATCHREV)

DISTPATCHES += $(foreach T,$(shell gseq -w 001 145),$(DISTVERSION).$(T))
NOPATCH  = 7.1.015 7.1.021 7.1.040 7.1.042 7.1.052 7.1.063 7.1.071 7.1.120
NOPATCH += 7.1.114
DISTPATCHES := $(filter-out $(NOPATCH),$(DISTPATCHES))
SUPERPATCH = $(DISTVERSION).001-$(PATCHREV)

# Vim distributed patches, minus ones that won't apply cleanly.
PATCHFILES += $(SUPERPATCH)

# Fix vimtutor
PATCHFILES += vimtutor.diff

#DISTPATCHFILES = $(addprefix files/,$(DISTPATCHES))
#superpatch:
#	@echo " ==> Creating $(SUPERPATCH)"
#	@echo " ==> Skipping patches: $(NOPATCH)"
#	@-rm -f files/$(SUPERPATCH)
#	@for p in $(DISTPATCHFILES) ; do \
#	    cat $$p >> files/$(SUPERPATCH) ; \
#	done

