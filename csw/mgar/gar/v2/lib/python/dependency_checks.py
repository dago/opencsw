# $Id$

import checkpkg
import os.path
import re

DEPRECATED_LIBRARY_LOCATIONS = (
    ("/opt/csw/lib", "libdb-4.7.so", "Deprecated Berkeley DB location"),
    ("/opt/csw/lib/mysql", "libmysqlclient_r.so.15",
     "Please use /opt/csw/mysql5/..."),
    ("/opt/csw/lib/sparcv9/mysql", "libmysqlclient_r.so.15",
     "Please use /opt/csw/mysql5/..."),
    ("/opt/csw/lib/mysql", "libmysqlclient.so.15",
     "Please use /opt/csw/mysql5/..."),
)

DLOPEN_LIB_LOCATIONS = (
    r'^opt/csw/lib/python/site-packages.*',
)

def Libraries(pkg_data, error_mgr, logger, messenger, path_and_pkg_by_basename):
  pkgname = pkg_data["basic_stats"]["pkgname"]
  logger.debug("Libraries(): pkgname = %s", repr(pkgname))
  orphan_sonames = []
  required_deps = []
  isalist = pkg_data["isalist"]
  ldd_emulator = checkpkg.LddEmulator()
  for binary_info in pkg_data["binaries_dump_info"]:
    binary_path, binary_basename = os.path.split(binary_info["path"])
    for soname in binary_info["needed sonames"]:
      resolved = False
      path_list = path_and_pkg_by_basename[soname].keys()
      logger.debug("%s @ %s: looking for %s in %s",
                   soname,
                   binary_info["path"],
                   binary_info["runpath"],
                   path_list)
      runpath_tuple = (tuple(binary_info["runpath"])
                      + tuple(checkpkg.SYS_DEFAULT_RUNPATH))
      runpath_history = []
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
          logger.debug("%s needed by %s:",
                 soname, binary_info["path"])
          logger.debug("=> %s provided by %s",
              resolved_path, path_and_pkg_by_basename[soname][resolved_path])
          resolved = True
          req_pkg = path_and_pkg_by_basename[soname][resolved_path][-1]
          reason = ("provides %s/%s needed by %s"
                    % (resolved_path, soname, binary_info["path"]))
          for bad_path, bad_soname, msg in DEPRECATED_LIBRARY_LOCATIONS:
            if resolved_path == bad_path and soname == bad_soname:
              logger.debug("Bad lib found: %s/%s", bad_path, bad_soname)
              error_mgr.ReportError(
                  pkgname,
                  "deprecated-library",
                  ("%s %s %s/%s"
                   % (binary_info["path"], msg, resolved_path, soname)))
          required_deps.append((req_pkg, reason))
          break
      if not resolved:
        orphan_sonames.append((soname, binary_info["path"]))
        if path_list:
          path_msg = "was available at the following paths: %s." % path_list
        else:
          path_msg = ("was not present on the filesystem, "
                      "nor in the packages under examination.")
        messenger.Message(
            "%s could not be resolved for %s, with rpath %s, expanded to %s, "
            "while the file %s"
            % (soname, binary_info["path"], runpath_tuple, runpath_history, path_msg))
  orphan_sonames = set(orphan_sonames)
  for soname, binary_path in orphan_sonames:
    error_mgr.ReportError(
        pkgname, "soname-not-found",
        "%s is needed by %s" % (soname, binary_path))
  # TODO: Report orphan sonames here
  return required_deps

def ByFilename(pkg_data, error_mgr, logger, messenger, path_and_pkg_by_basename):
  pkgname = pkg_data["basic_stats"]["pkgname"]
  req_pkgs_reasons = []
  dep_regexes = [(re.compile(x), x, y)
                 for x, y in checkpkg.DEPENDENCY_FILENAME_REGEXES]
  for regex, regex_str, dep_pkgname in dep_regexes:
    for pkgmap_entry in pkg_data["pkgmap"]:
      if pkgmap_entry["path"] and regex.match(pkgmap_entry["path"]):
        msg = ("found file(s) matching %s, e.g. %s"
               % (regex_str, repr(pkgmap_entry["path"])))
        req_pkgs_reasons.append((dep_pkgname, msg))
        break
  return req_pkgs_reasons
