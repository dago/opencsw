PACKAGES := $(shell find . -type f | sed "s/^.\///" | grep -v Makefile)

PREPARE  := $(PACKAGES:=.p)
BUILD    := $(PACKAGES:=.b)
CREATE   := $(PACKAGES:=.c)
SHOW     := $(PACKAGES:=.s)

clean: ../scripts/pkghelper.pl
	@echo Do you really want to do this\? Press Ctrl-C to abort
	@read LUTZ
	@../scripts/pkghelper.pl -u

$(PACKAGES): ../scripts/pkghelper.pl
	@../scripts/pkghelper.pl $@

$(PREPARE): ../scripts/pkghelper.pl
	@../scripts/pkghelper.pl -p $(subst .p,,$@)

$(BUILD): ../scripts/pkghelper.pl
	@../scripts/pkghelper.pl -b $(subst .b,,$@)

$(CREATE): ../scripts/pkghelper.pl
	@../scripts/pkghelper.pl -c $(subst .c,,$@)

$(SHOW): ../scripts/pkghelper.pl
	@../scripts/pkghelper.pl -s $(subst .s,,$@)

.PHONY: $(PACKAGES)
