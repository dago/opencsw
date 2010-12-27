# $Id$

import checkpkg
import os.path
import re
import ldd_emul
import sharedlib_utils
import common_constants
import operator
import logging

# This shared library is present on Solaris 10 on amd64, but it's missing on
# Solaris 8 on i386.  It's okay if it's missing.
ALLOWED_ORPHAN_SONAMES = set([u"libm.so.2"])

DEPRECATED_LIBRARY_LOCATIONS = (
    ("/opt/csw/lib", "libdb-4.7.so", "Deprecated Berkeley DB location"),
    ("/opt/csw/lib/mysql", "libmysqlclient_r.so.15",
     "Please use /opt/csw/mysql5/..."),
    ("/opt/csw/lib/mysql", "libmysqlclient.so.15",
     "Please use /opt/csw/mysql5/..."),
    ("/opt/csw/lib", "libnet.so",
     "Please use -L/opt/csw/lib/libnet-new for linking. "
     "See more at http://wiki.opencsw.org/project-libnet"),
)

DLOPEN_LIB_LOCATIONS = (
    r'^opt/csw/lib/python/site-packages.*',
)

DEPENDENCY_FILENAME_REGEXES = (
    (r".*\.pl$",   (u"CSWperl",)),
    (r".*\.pm$",   (u"CSWperl",)),
    (r".*\.py$",   (u"CSWpython",)),
    (r".*\.rb$",   (u"CSWruby",)),
    (r".*\.elc?$", (u"CSWemacscommon",)),
    (r"/opt/csw/apache2/", (u"CSWapache2",)),
)

PREFERRED_DIRECTORY_PROVIDERS = set([u"CSWcommon"])

def ProcessSoname(
    ldd_emulator,
    soname, path_and_pkg_by_basename, binary_info, isalist, binary_path, logger,
    error_mgr,
    pkgname, messenger):
  """This is not an ideal name for this function.

  Returns:
    orphan_sonames
  """
  logging.debug("ProcessSoname(), %s %s"
                % (binary_info["path"], soname))
  orphan_sonames = []
  resolved = False
  path_list = path_and_pkg_by_basename[soname].keys()
  runpath_tuple = (
      tuple(binary_info["runpath"])
      + tuple(checkpkg.SYS_DEFAULT_RUNPATH))
  runpath_history = []
  first_lib = None
  already_resolved_paths = set()
  for runpath in runpath_tuple:
    runpath = ldd_emulator.SanitizeRunpath(runpath)
    runpath_list = ldd_emulator.ExpandRunpath(runpath, isalist, binary_path)
    runpath_list = ldd_emulator.Emulate64BitSymlinks(runpath_list)
    # To accumulate all the runpaths that we were looking at
    runpath_history += runpath_list
    resolved_path = ldd_emulator.ResolveSoname(runpath_list,
                                               soname,
                                               isalist,
                                               path_list,
                                               binary_path)
    if resolved_path:
      if resolved_path in already_resolved_paths:
        continue
      already_resolved_paths.add(resolved_path)
      resolved = True
      reason = ("%s needs the %s soname"
                % (binary_info["path"], soname))
      logger.debug("soname %s found in %s for %s"
                   % (soname, resolved_path, binary_info["path"]))
      error_mgr.NeedFile(pkgname, os.path.join(resolved_path, soname), reason)
      # Looking for deprecated libraries.  However, only alerting if the
      # deprecated library is the first one found in the RPATH.  For example,
      # libdb-4.7.so is found in CSWbdb and CSWbdb47, and it's important to
      # throw an error if the RPATH is ("/opt/csw/lib", "/opt/csw/bdb47/lib"),
      # and not to throw an error if RPATH is ("/opt/csw/bdb47/lib",
      # "/opt/csw/lib")
      if not first_lib:
        first_lib = (resolved_path, soname)
        for bad_path, bad_soname, msg in DEPRECATED_LIBRARY_LOCATIONS:
          if resolved_path == bad_path and soname == bad_soname:
            logger.debug("Bad lib found: %s/%s", bad_path, bad_soname)
            error_mgr.ReportError(
                pkgname,
                "deprecated-library",
                ("%s %s %s/%s"
                 % (binary_info["path"], msg, resolved_path, soname)))
  if not resolved:
    orphan_sonames.append((soname, binary_info["path"]))
    if path_list:
      path_msg = "was available at the following paths: %s." % path_list
    else:
      path_msg = ("was not present on the filesystem, "
                  "nor in the packages under examination.")
    if soname not in ALLOWED_ORPHAN_SONAMES:
      messenger.Message(
          "%s could not be resolved for %s, with rpath %s, expanded to %s, "
          "while the file %s"
          % (soname, binary_info["path"],
             runpath_tuple, runpath_history, path_msg))
  return orphan_sonames


def Libraries(pkg_data, error_mgr, logger, messenger, path_and_pkg_by_basename,
              pkg_by_path):
  """Checks shared libraries.

  Returns:
    [
      (u"CSWfoo", "why is this needed"),
    ]

  New idea, a list of reasons:
    [
      [(u"CSWfoo", "why is it needed"),
       (u"CSWfooalt", "there must be a reason"),
       (u"CSWfooyetanother", "here's another one")],
      [(u"CSWbar", "this serves another purpose")],
    ]
  """
  pkgname = pkg_data["basic_stats"]["pkgname"]
  logger.debug("Libraries(): pkgname = %s", repr(pkgname))
  isalist = pkg_data["isalist"]
  ldd_emulator = ldd_emul.LddEmulator()
  orphan_sonames = []
  for binary_info in pkg_data["binaries_dump_info"]:
    binary_path, binary_basename = os.path.split(binary_info["path"])
    for soname in binary_info["needed sonames"]:
      orphan_sonames_tmp = ProcessSoname(
          ldd_emulator,
          soname, path_and_pkg_by_basename, binary_info, isalist, binary_path, logger,
          error_mgr,
          pkgname, messenger)
      orphan_sonames.extend(orphan_sonames_tmp)
  orphan_sonames = set(orphan_sonames)
  for soname, binary_path in orphan_sonames:
    if soname not in ALLOWED_ORPHAN_SONAMES:
      error_mgr.ReportError(
          pkgname, "soname-not-found",
          "%s is needed by %s" % (soname, binary_path))


def ByFilename(pkg_data, error_mgr, logger, messenger,
               path_and_pkg_by_basename, pkg_by_path):
  pkgname = pkg_data["basic_stats"]["pkgname"]
  dep_regexes = [(re.compile(x), x, y)
                 for x, y in DEPENDENCY_FILENAME_REGEXES]
  for regex, regex_str, dep_pkgnames in dep_regexes:
    for pkgmap_entry in pkg_data["pkgmap"]:
      if pkgmap_entry["path"] and regex.match(pkgmap_entry["path"]):
        reason = ("found file(s) matching %s, e.g. %s"
               % (regex_str, repr(pkgmap_entry["path"])))
        for dep_pkgname in dep_pkgnames:
          error_mgr.NeedPackage(pkgname, dep_pkgname, reason)
        break


def ByDirectory(pkg_data, error_mgr, logger, messenger,
                path_and_pkg_by_basename, pkg_by_path):
  """Finds packages that provide each directory's parent.

  1. For each directory
    1.1. Find the parent
    1.2. Add the parent to the list of packages to depend on.

  This check is currently disabled, because of false positives that it
  generates.
  """
  pkgname = pkg_data["basic_stats"]["pkgname"]
  req_pkgs_reasons = []
  needed_dirs = set()
  # Adding base dirs of all the files to the dirs that need to be checked.
  for pkgmap_entry in pkg_data["pkgmap"]:
    if "path" in pkgmap_entry and pkgmap_entry["path"]:
      base_dir, dirname = os.path.split(pkgmap_entry["path"])
      needed_dirs.add(base_dir)
  for needed_dir in needed_dirs:
    reason_group = []
    # TODO: The preferred directory providers should not depend on other packages to
    # provide directories.
    if pkgname not in PREFERRED_DIRECTORY_PROVIDERS:
      # If the path is provided by CSWcommon or other preferred package, don't
      # mention other packages.
      pkgs_to_mention = []
      preferred_mentioned = False
      for preferred_pkg in PREFERRED_DIRECTORY_PROVIDERS:
        if preferred_pkg in pkg_by_path[needed_dir]:
          pkgs_to_mention.append(preferred_pkg)
          preferred_mentioned = True
      if not preferred_mentioned:
        if not pkg_by_path[needed_dir]:
          # There's no sense in reporting '/' and ''.
          if needed_dir and needed_dir != '/':
            error_mgr.ReportError(pkgname, "base-dir-not-found", repr(needed_dir))
        elif len(pkg_by_path[needed_dir]) < 5:
          pkgs_to_mention = pkg_by_path[needed_dir]
        else:
          pkgs_to_mention = pkg_by_path[needed_dir][:5] + ["and/or others"]
      msg = (u"%s provides directory %s is needed by the package %s"
             % (pkgs_to_mention, needed_dir, pkgname))
      for pkg_to_mention in pkgs_to_mention:
        reason_group.append((pkg_to_mention, msg))
      if reason_group:
        req_pkgs_reasons.append(reason_group)
    else:
      error_mgr.ReportError(pkgname, "base-dir-not-provided-by-any-package", needed_dir)
  return req_pkgs_reasons


def GetPathAndPkgByBasename(error_mgr, logger, basenames,
                            path_and_pkg_by_basename=None):
  """{"<basename>": {"/path/1": ["CSWfoo1"], "/path/2": ["CSWfoo2"]}}"""
  if not path_and_pkg_by_basename:
    path_and_pkg_by_basename = {}
  for basename in basenames:
    path_and_pkg_by_basename[basename] = (
        error_mgr.GetPathsAndPkgnamesByBasename(basename))
  return path_and_pkg_by_basename

def GetPkgByFullPath(error_mgr, logger, paths_to_verify, pkg_by_path):
  """Resolves a list of paths to a mapping between paths and packages.

  Returns: {"/opt/csw/lib": ["CSWcommon", "CSWfoo"]}
  """
  if not pkg_by_path:
    pkg_by_path = {}
  for path in paths_to_verify:
    if path not in pkg_by_path:
      result = error_mgr.GetPkgByPath(path)
      # logger.warning("error_mgr.GetPkgByPath(%s) => %s", repr(path), repr(result))
      pkg_by_path[path] = result
  # logger.warning("New paths: %s" % pprint.pformat(pkg_by_path))
  return pkg_by_path

def MissingDepsFromReasonGroups(reason_groups, declared_deps_set):
  missing_dep_groups = []
  for reason_group in reason_groups:
    dependency_fulfilled = False
    pkgnames = [x for x, y in reason_group]
    for pkgname in pkgnames:
      if pkgname in declared_deps_set:
        dependency_fulfilled = True
        break
    if not dependency_fulfilled:
      missing_dep_groups.append(pkgnames)
  return missing_dep_groups

def SuggestLibraryPackage(error_mgr, messenger,
    pkgname, catalogname,
    description,
    lib_path, lib_basename, soname,
    base_pkgname):
  escaped_soname = sharedlib_utils.EscapeRegex(soname)
  escaped_basename = sharedlib_utils.EscapeRegex(lib_basename)
  messenger.SuggestGarLine("# The following lines define a new package: "
                           "%s" % pkgname)
  messenger.SuggestGarLine("PACKAGES += %s" % pkgname)
  messenger.SuggestGarLine(
      "CATALOGNAME_%s = %s"
      % (pkgname, catalogname))
  # The exact library file (which can be different from what soname suggests)
  messenger.SuggestGarLine(
      r'PKGFILES_%s += '
      r'$(call baseisadirs,$(libdir),%s)'
      % (pkgname, escaped_basename))
  # Name regex based on the soname, plus potential symlinks
  messenger.SuggestGarLine(
      r'PKGFILES_%s += '
      r'$(call baseisadirs,$(libdir),%s(\.\d+)*)'
      % (pkgname, escaped_soname))
  messenger.SuggestGarLine(
      "SPKG_DESC_%s += %s, %s"
      % (pkgname, description, soname))
  messenger.SuggestGarLine(
      "RUNTIME_DEP_PKGS_%s += %s"
      % (base_pkgname, pkgname))
  messenger.SuggestGarLine(
      "# The end of %s definition" % pkgname)


def GetSurplusDeps(pkgname, potential_req_pkgs, declared_deps):
  logging.debug("GetSurplusDeps(%s, potential_req_pkgs=%s, declared_deps=%s)",
                pkgname, declared_deps, potential_req_pkgs)
  # Surplus dependencies
  # In actual use, there should always be some potential dependencies.
  # assert potential_req_pkgs, "There should be some potential deps!"
  surplus_deps = declared_deps.difference(potential_req_pkgs)
  no_report_surplus = set()
  for sp_regex in common_constants.DO_NOT_REPORT_SURPLUS:
    for maybe_surplus in surplus_deps:
      if re.match(sp_regex, maybe_surplus):
        logging.debug(
            "GetSurplusDeps(): Not reporting %s as surplus because it matches %s.",
            maybe_surplus, sp_regex)
        no_report_surplus.add(maybe_surplus)
  surplus_deps = surplus_deps.difference(no_report_surplus)
  # For some packages (such as dev packages) we don't report surplus deps at
  # all.
  if surplus_deps:
    for regex_str in common_constants.DO_NOT_REPORT_SURPLUS_FOR:
      if re.match(regex_str, pkgname):
        logging.debug(
            "GetSurplusDeps(): Not reporting any surplus because "
            "it matches %s", regex_str)
        surplus_deps = frozenset()
        break
  return surplus_deps


def ReportMissingDependencies(error_mgr, pkgname, declared_deps, req_pkgs_reasons):
  """Processes data structures with dependency data and reports errors.

  Processes data specific to a single package.

  Args:
    error_mgr: SetCheckInterface
    pkgname: pkgname, a string
    declared_deps: An iterable with declared dependencies
    req_pkgs_reasons: Groups of reasons

  data structure:
    [
      [
        ("CSWfoo1", "reason"),
        ("CSWfoo2", "reason"),
      ],
      [
        ( ... ),
      ]
    ]
  """
  missing_reasons_by_pkg = {}
  for reason_group in req_pkgs_reasons:
    for pkg, reason in reason_group:
      missing_reasons_by_pkg.setdefault(pkg, [])
      if len(missing_reasons_by_pkg[pkg]) < 4:
        missing_reasons_by_pkg[pkg].append(reason)
      elif len(missing_reasons_by_pkg[pkg]) == 4:
        missing_reasons_by_pkg[pkg].append("...and more.")
  missing_dep_groups = MissingDepsFromReasonGroups(
      req_pkgs_reasons, declared_deps)
  pkgs_to_remove = set()
  for regex_str in common_constants.DO_NOT_REPORT_MISSING_RE:
    regex = re.compile(regex_str)
    for dep_pkgname in reduce(operator.add, missing_dep_groups, []):
      if re.match(regex, dep_pkgname):
        pkgs_to_remove.add(dep_pkgname)
  if pkgname in reduce(operator.add, missing_dep_groups, []):
    pkgs_to_remove.add(pkgname)
  logging.debug("Removing %s from the list of missing pkgs.", pkgs_to_remove)
  new_missing_dep_groups = set()
  for missing_deps in missing_dep_groups:
    new_missing_deps = set()
    for dep in missing_deps:
      if dep not in pkgs_to_remove:
        new_missing_deps.add(dep)
    if new_missing_deps:
      new_missing_dep_groups.add(tuple(new_missing_deps))
  potential_req_pkgs = set(
      (x for x, y in reduce(operator.add, req_pkgs_reasons, [])))
  missing_dep_groups = new_missing_dep_groups
  surplus_deps = GetSurplusDeps(pkgname, potential_req_pkgs, declared_deps)
  # Using an index to avoid duplicated reasons.
  missing_deps_reasons_by_pkg = []
  missing_deps_idx = set()
  for missing_deps in missing_dep_groups:
    error_mgr.ReportErrorForPkgname(
        pkgname, "missing-dependency", " or ".join(missing_deps))
    for missing_dep in missing_deps:
      item = (missing_dep, tuple(missing_reasons_by_pkg[missing_dep]))
      if item not in missing_deps_idx:
        missing_deps_reasons_by_pkg.append(item)
        missing_deps_idx.add(item)
  for surplus_dep in surplus_deps:
    error_mgr.ReportErrorForPkgname(pkgname, "surplus-dependency", surplus_dep)
  return missing_deps_reasons_by_pkg, surplus_deps, missing_dep_groups
