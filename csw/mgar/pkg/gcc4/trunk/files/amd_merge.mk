
AMD_BASE  = $(WORKROOTDIR)/install-isa-i386-5.10-i386/
I386_BASE = $(WORKROOTDIR)/install-isa-i386-5.8-i386/
MPREFIX   = opt/csw/gcc4
APREFIX   = $(AMD_BASE)/$(MPREFIX)
IPREFIX   = $(I386_BASE)/$(MPREFIX)
PPREFIX   = $(PKGROOT)/$(MPREFIX)

AMD_MERGE_TARGETS  = x86-merge-dirs
AMD_MERGE_TARGETS += x86-merge-i386
AMD_MERGE_TARGETS += x86-merge-amd
AMD_MERGE_TARGETS += x86-merge-strip

merge-amd: $(AMD_MERGE_TARGETS)
	@$(MAKECOOKIE)

x86-merge-dirs:
	@(ginstall -d $(PKGROOT))
	@(ginstall -d $(PPREFIX)/bin/amd64)
	@(ginstall -d $(PPREFIX)/bin/i386)
	@$(MAKECOOKIE)

x86-merge-amd:
	@(echo "[===== Merging AMD64 =====]")
	@(cd $(AMD_BASE); for dir in `gfind . -name "*solaris2\.10*" -type d` ; do \
		/usr/bin/pax -rw $$dir $(PKGROOT); done )
	@(cd $(AMD_BASE); /usr/bin/pax -rw $(MPREFIX)/lib/amd64 $(PKGROOT))
	@(cd $(APREFIX)/bin; /usr/bin/pax -rw * $(PPREFIX)/bin/amd64)
	@$(MAKECOOKIE)

x86-merge-i386:
	@(echo "[===== Merging I386 =====]")
	@(cd $(I386_BASE); /usr/bin/pax -rw $(MPREFIX)/include $(PKGROOT))
	@(cd $(I386_BASE); /usr/bin/pax -rw $(MPREFIX)/info $(PKGROOT))
	@(cd $(I386_BASE); /usr/bin/pax -rw $(MPREFIX)/man $(PKGROOT))
	@(cd $(I386_BASE); /usr/bin/pax -rw $(MPREFIX)/share $(PKGROOT))
	@(cd $(I386_BASE); /usr/bin/pax -rw $(MPREFIX)/lib $(PKGROOT))
	@(cd $(I386_BASE); /usr/bin/pax -rw $(MPREFIX)/libexec $(PKGROOT))
	@(cd $(I386_BASE); /usr/bin/pax -rw $(MPREFIX)/bin $(PKGROOT))
	@$(MAKECOOKIE)

x86-merge-strip:
	@(echo "[===== Stripping Merged Binaries =====]")
	@(stripbin $(PPREFIX)/bin)
	@(stripbin $(PPREFIX)/bin/amd64)
	@$(MAKECOOKIE)

