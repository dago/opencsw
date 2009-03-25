
AMD_BASE  = $(WORKROOTDIR)/install-isa-i386-5.10/
I386_BASE = $(WORKROOTDIR)/install-isa-i386-5.8/
MPREFIX   = opt/csw/gcc4
APREFIX   = $(AMD_BASE)/$(MPREFIX)
IPREFIX   = $(I386_BASE)/$(MPREFIX)
PPREFIX   = $(PKGROOT)/$(MPREFIX)

AMD_MERGE_TARGETS  = x86-merge-dirs
AMD_MERGE_TARGETS += x86-merge-i386
AMD_MERGE_TARGETS += x86-merge-amd
AMD_MERGE_TARGETS += x86-merge-strip

merge-amd: $(AMD_MERGE_TARGETS)
	@$(DONADA)

x86-merge-dirs:
	@(ginstall -d $(PKGROOT))
	@(ginstall -d $(PPREFIX)/bin/amd64)
	@(ginstall -d $(PPREFIX)/bin/i386)

x86-merge-amd:
	@(echo "===> Merging AMD64")
	@(cd $(AMD_BASE); for dir in `gfind . -name "*solaris2\.10*" -type d` ; do \
		pax -rw $$dir $(PKGROOT); done )
	@(cd $(AMD_BASE); pax -rw $(MPREFIX)/lib/amd64 $(PKGROOT))
	@(cd $(APREFIX)/bin; pax -rw * $(PPREFIX)/bin/amd64)
	@(cd $(APREFIX)/bin/amd64; gln *-solaris2.* ../)

x86-merge-i386:
	@(echo "===> Merging I386")
	@(cd $(I386_BASE); pax -rw $(MPREFIX)/include $(PKGROOT))
	@(cd $(I386_BASE); pax -rw $(MPREFIX)/info $(PKGROOT))
	@(cd $(I386_BASE); pax -rw $(MPREFIX)/man $(PKGROOT))
	@(cd $(I386_BASE); pax -rw $(MPREFIX)/share $(PKGROOT))
	@(cd $(I386_BASE); pax -rw $(MPREFIX)/lib $(PKGROOT))
	@(cd $(I386_BASE); pax -rw $(MPREFIX)/libexec $(PKGROOT))
	@(cd $(IPREFIX)/bin; pax -rw * $(PPREFIX)/bin/i386)
	@(cd $(APREFIX)/bin/i386; gln *-solaris2.* ../)

x86-merge-strip:
	@(echo "===> Stripping Merged Binaries")
	@(stripbin $(PPREFIX)/bin/amd64)
	@(stripbin $(PPREFIX)/bin/i386)

