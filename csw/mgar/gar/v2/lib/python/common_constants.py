ARCH_SPARC = "sparc"
ARCH_i386 = "i386"
ARCH_ALL = "all"
PHYSICAL_ARCHITECTURES = [ARCH_SPARC, ARCH_i386]
ARCHITECTURES = PHYSICAL_ARCHITECTURES + [ARCH_ALL]
OS_REL_58 = u"SunOS5.8"
OS_REL_59 = u"SunOS5.9"
OS_REL_510 = u"SunOS5.10"
OS_REL_511 = u"SunOS5.11"
OS_RELS = (
    OS_REL_58,
    OS_REL_59,
    OS_REL_510,
    OS_REL_511,
)
OBSOLETE_OS_RELS = (
    OS_REL_58,
)
SVR4_OS_RELS = (
    OS_REL_58,
    OS_REL_59,
    OS_REL_510,
)
IPS_OS_RELS = (
    OS_REL_511,
)

SYSTEM_SYMLINKS = (
    ("/opt/csw/bdb4",     ("/opt/csw/bdb42",)),
    ("/64",               ("/amd64", "/sparcv9")),
    ("/opt/csw/lib/i386", ("/opt/csw/lib",)),
    ("/opt/csw/lib/sparcv8", ("/opt/csw/lib",)),
)

DEFAULT_INSTALL_CONTENTS_FILE = "/var/sadm/install/contents"
DUMP_BIN = "/usr/ccs/bin/dump"
ELFDUMP_BIN = "/usr/ccs/bin/elfdump"

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
    'beanie',
    'dublin',
    'unstable',
    'legacy',
    'kiel',
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

SPARCV8_PATHS = (
    'sparcv8',
    'sparcv8-fsmuld',
    'sparcv7',
    'sparc')
SPARCV8PLUS_PATHS = (
    'sparcv8plus+vis2',
    'sparcv8plus+vis',
    'sparcv8plus')
SPARCV9_PATHS = (
    'sparcv9+vis2',
    'sparcv9+vis',
    'sparcv9')
INTEL_386_PATHS = (
    'i486',
    'i386',
    'i86')
INTEL_PENTIUM_PATHS = (
    'pentium_pro+mmx',
    'pentium_pro',
    'pentium+mmx',
    'pentium')
AMD64_PATHS = ('amd64',)

# Settings for binary placements: which architectures can live in which
# directories.
BASE_BINARY_PATHS = ('bin', 'sbin', 'lib', 'libexec', 'cgi-bin')

MACHINE_ID_METADATA = {
    # id: (name, allowed_paths, disallowed_paths)
    -1: {"name": "Unknown",
         "allowed": {
           OS_REL_58: (),
           OS_REL_59: (),
           OS_REL_510: (),
           OS_REL_511: (),
         }, "disallowed": (),
         "type": "unknown"},
     2: {"name": "sparcv8",
         "type": ARCH_SPARC,
         "allowed": {
           OS_REL_58: BASE_BINARY_PATHS + SPARCV8_PATHS,
           OS_REL_59: BASE_BINARY_PATHS + SPARCV8_PATHS,
           OS_REL_510: BASE_BINARY_PATHS + SPARCV8_PATHS,
           OS_REL_511: BASE_BINARY_PATHS + SPARCV8_PATHS,
         },
         "disallowed": SPARCV9_PATHS + INTEL_386_PATHS + AMD64_PATHS,
        },
     # pentium_pro binaries are also identified as 3.
     3: {"name": "i386",
         "type": ARCH_i386,
         "allowed": {
           OS_REL_58: BASE_BINARY_PATHS + INTEL_386_PATHS,
           OS_REL_59: BASE_BINARY_PATHS + INTEL_386_PATHS,
           OS_REL_510: BASE_BINARY_PATHS + INTEL_386_PATHS,
           OS_REL_511: BASE_BINARY_PATHS + INTEL_386_PATHS,
         },
         "disallowed": SPARCV8_PATHS + SPARCV8PLUS_PATHS +
                       SPARCV9_PATHS + AMD64_PATHS,
        },
     6: {"name": "i486",
         "type": ARCH_i386,
         "allowed": {
           OS_REL_58: INTEL_386_PATHS,
           OS_REL_59: INTEL_386_PATHS,
           OS_REL_510: INTEL_386_PATHS,
           OS_REL_511: INTEL_386_PATHS,
         },
         "disallowed": SPARCV8_PATHS + SPARCV8PLUS_PATHS +
                       SPARCV9_PATHS + AMD64_PATHS,
         },
    18: {"name": "sparcv8+",
         "type": ARCH_SPARC,
         "allowed": {
           OS_REL_58: SPARCV8PLUS_PATHS,
           OS_REL_59: SPARCV8PLUS_PATHS,
           # We allow sparcv8+ as the base architecture on Solaris 10+.
           OS_REL_510: BASE_BINARY_PATHS + SPARCV8PLUS_PATHS,
           OS_REL_511: BASE_BINARY_PATHS + SPARCV8PLUS_PATHS,
         },
         "disallowed": SPARCV8_PATHS + SPARCV9_PATHS +
                       AMD64_PATHS + INTEL_386_PATHS,
        },
    43: {"name": "sparcv9",
         "type": ARCH_SPARC,
         "allowed": {
           OS_REL_58: SPARCV9_PATHS,
           OS_REL_59: SPARCV9_PATHS,
           OS_REL_510: SPARCV9_PATHS,
           OS_REL_511: SPARCV9_PATHS,
         },
         "disallowed": INTEL_386_PATHS + AMD64_PATHS,
        },
    62: {"name": "amd64",
         "type": ARCH_i386,
         "allowed": {
           OS_REL_58: AMD64_PATHS,
           OS_REL_59: AMD64_PATHS,
           OS_REL_510: AMD64_PATHS,
           OS_REL_511: AMD64_PATHS,
         },
         "disallowed": SPARCV8_PATHS + SPARCV8PLUS_PATHS +
                       SPARCV9_PATHS,
        },
}
