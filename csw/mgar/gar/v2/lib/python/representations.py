"""Internal checkpkg representations of objects and abstractions.

Serialized forms might be lists or dicts, but in many cases namedtuples
are a better choice, especially for objects which repeat a lot.
"""

import collections

BinaryDumpInfo = collections.namedtuple(
    'BinaryDumpInfo',
    'path, base_name, soname, needed_sonames, runpath, runpath_rpath_the_same, '
    'rpath_set, runpath_set')

FileMetadata = collections.namedtuple(
    'FileMetadata',
    'path, mime_type, machine_id')

# Full catalog entry, enough to write a line of a catalog file.
CatalogEntry = collections.namedtuple(
    'CatalogEntry', 'catalogname version pkgname basename '
                    'md5_sum size deps category i_deps desc')

PkgmapEntry = collections.namedtuple(
    'PkgmapEntry',
    'line, class_, mode, owner, group, path, target, type_, '
    'major, minor, size, cksum, modtime, pkgnames')

ElfSymInfo = collections.namedtuple('Symbol', ['bind', 'flags', 'shndx',
                                               'soname', 'symbol', 'version'])
