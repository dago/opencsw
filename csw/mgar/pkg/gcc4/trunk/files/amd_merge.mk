
AMD_DEBUG = 1

ifeq ($(AMD_DEBUG),)
	_DBG=@
else
	_DBG=
endif   

AMD_BASE  = $(WORKROOTDIR)/install-isa-i386-5.10-i386/
I386_BASE = $(WORKROOTDIR)/install-isa-i386-5.8-i386/
MPREFIX   = opt/csw/gcc4
APREFIX   = $(AMD_BASE)/$(MPREFIX)
IPREFIX   = $(I386_BASE)/$(MPREFIX)
PPREFIX   = $(PKGROOT)/$(MPREFIX)

AMD_MERGE_TARGETS  = merge-dirs-amd
AMD_MERGE_TARGETS += merge-i386-files
AMD_MERGE_TARGETS += merge-amd64-files
AMD_MERGE_TARGETS += merge-strip-amd

merge-amd: $(AMD_MERGE_TARGETS)
	$(_DBG)$(MAKECOOKIE)

merge-dirs-amd:
	$(_DBG)(ginstall -d $(PKGROOT))
	$(_DBG)(ginstall -d $(PPREFIX)/bin/amd64)
	$(_DBG)(ginstall -d $(PPREFIX)/bin/i386)
	$(_DBG)$(MAKECOOKIE)

merge-amd64-files:
	$(call _pmod,Merging isa-amd64)
	@(echo "[===== Merging isa-amd64: ISA=$(ISA) =====]")
	$(_DBG)(cd $(AMD_BASE); for dir in `gfind . -name "*solaris2\.10*" -type d` ; do \
		/usr/bin/pax -rw $$dir $(PKGROOT); done )
	$(_DBG)(cd $(AMD_BASE); /usr/bin/pax -rw $(MPREFIX)/lib/amd64 $(PKGROOT))
	$(_DBG)(cd $(APREFIX)/bin; /usr/bin/pax -rw * $(PPREFIX)/bin/amd64)
	$(_DBG)$(MAKECOOKIE)

merge-i386-files:
	@(echo "[===== Merging ISA-I386 =====]")
	$(_DBG)(cd $(I386_BASE); /usr/bin/pax -rw $(MPREFIX)/bin $(PKGROOT))
	$(_DBG)(gmv -f $(PPREFIX)/bin/i386-pc* $(PPREFIX)/bin/i386/)
	$(_DBG)(cd $(I386_BASE); /usr/bin/pax -rw $(MPREFIX)/include $(PKGROOT))
	$(_DBG)(cd $(I386_BASE); /usr/bin/pax -rw $(MPREFIX)/info $(PKGROOT))
	$(_DBG)(cd $(I386_BASE); /usr/bin/pax -rw $(MPREFIX)/man $(PKGROOT))
	$(_DBG)(cd $(I386_BASE); /usr/bin/pax -rw $(MPREFIX)/share $(PKGROOT))
	$(_DBG)(cd $(I386_BASE); /usr/bin/pax -rw $(MPREFIX)/lib $(PKGROOT))
	$(_DBG)(cd $(I386_BASE); /usr/bin/pax -rw $(MPREFIX)/libexec $(PKGROOT))
	$(_DBG)$(MAKECOOKIE)

merge-strip-amd:
	@(echo "[===== Stripping Merged Binaries =====]")
	$(_DBG)(stripbin $(PPREFIX)/bin/i386)
	$(_DBG)(stripbin $(PPREFIX)/bin/amd64)
	$(_DBG)(stripbin $(PPREFIX)/bin)
	$(_DBG)$(MAKECOOKIE)

