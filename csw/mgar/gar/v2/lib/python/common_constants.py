ARCH_SPARC = "sparc"
ARCH_i386 = "i386"
ARCH_ALL = "all"
PHYSICAL_ARCHITECTURES = [ARCH_SPARC, ARCH_i386]
ARCHITECTURES = PHYSICAL_ARCHITECTURES + [ARCH_ALL]
OS_RELS = (
    u"SunOS5.8",
    u"SunOS5.9",
    u"SunOS5.10",
    u"SunOS5.11",
)
OBSOLETE_OS_RELS = (
    u"SunOS5.8",
)

SYSTEM_SYMLINKS = (
    ("/opt/csw/bdb4",     ("/opt/csw/bdb42",)),
    ("/64",               ("/amd64", "/sparcv9")),
    ("/opt/csw/lib/i386", ("/opt/csw/lib",)),
    ("/opt/csw/lib/sparcv8", ("/opt/csw/lib",)),
)

DEFAULT_INSTALL_CONTENTS_FILE = "/var/sadm/install/contents"
DUMP_BIN = "/usr/ccs/bin/dump"

OWN_PKGNAME_PREFIXES = frozenset(["CSW"])

# TODO: Merge with sharedlib_utils
# Based on 'isalist' output.  These are hardcoded here, so that it's possible to
# index a sparc package on a i386 machine and vice versa.
ISALISTS_BY_ARCH = {
    ARCH_SPARC: frozenset([
        "sparcv9+vis2",
        "sparcv9+vis",
        "sparcv9",
        "sparcv8plus+vis2",
        "sparcv8plus+vis",
        "sparcv8plus",
        "sparcv8",
        "sparcv8-fsmuld",
        "sparcv7",
        "sparc",
        ]),
    ARCH_i386: frozenset([
        "amd64",
        "pentium_pro+mmx",
        "pentium_pro",
        "pentium+mmx",
        "pentium",
        "i486",
        "i386",
        "i86",
    ]),
    ARCH_ALL: frozenset([]),
}

# The list of catalogs to process. Should only contain catalogs as stored in
# the database, and not symlinks on the mirror. For example, 'testing' is
# a symlink, so should not be listed here.
DEFAULT_CATALOG_RELEASES = frozenset([
    'dublin',
    'unstable',
    'legacy',
    ])

# At some point, it was used to prevent people from linking against
# libX11.so.4, but due to issues with 3D acceleration.
DO_NOT_LINK_AGAINST_THESE_SONAMES = set([])

# Regarding surplus libraries reports
DO_NOT_REPORT_SURPLUS = [r"^CSWcommon$", r"^CSWcswclassutils$", r"^CSWcas-", r"^CSWisaexec$"]
DO_NOT_REPORT_SURPLUS_FOR = [r"CSW[a-z\-]+dev(el)?"]
DO_NOT_REPORT_MISSING_RE = [r"\*?SUNW.*"]

PSTAMP_RE = r"(?P<username>\w+)@(?P<hostname>[\w\.-]+)-(?P<timestamp>\d+)"

# The directory with shared, architecture independent data files.
OPENCSW_SHARE = "/opt/csw/share/opencsw"
