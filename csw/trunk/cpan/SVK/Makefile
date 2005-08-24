GARNAME = SVK
GARVERSION = 0.993
CATEGORIES = cpan
AUTHOR = CLKAO
GARCH = all

DESCRIPTION = a distributed version control system
define BLURB
  SVK is a decentralized version control system written in Perl. It uses the
  Subversion filesystem but provides additional features.
endef

DISTFILES += CSWpmsvk.gspec CSWpmsvk.depend

DEPENDS += utils/subversion
DEPENDS += cpan/Compress-Zlib cpan/FreezeThaw cpan/SVN-Mirror
DEPENDS += cpan/Algorithm-Annotate cpan/Algorithm-Diff cpan/YAML
DEPENDS += cpan/Regexp-Shellish cpan/Data-Hierarchy cpan/Clone
DEPENDS += cpan/Pod-Escapes cpan/Pod-Simple cpan/PerlIO-via-dynamic
DEPENDS += cpan/PerlIO-via-symlink cpan/IO-Digest cpan/SVN-Simple
DEPENDS += cpan/TimeDate cpan/File-Type cpan/PerlIO-eol
DEPENDS += cpan/Locale-Maketext-Lexicon cpan/Locale-Maketext-Simple
DEPENDS += cpan/URI

include ../category.mk

pre-test:
	-@mv -f $(WORKSRC)/t/50dav.t $(WORKSRC)/t/50dav.t.disabled
	@$(MAKECOOKIE)
