#!/opt/csw/bin/python2.6
#
# $Id$
#
# A check for dependencies between shared libraries.

import checkpkg
import os
import os.path
import copy
import re
import subprocess
import logging

DUMP_BIN = "/usr/ccs/bin/dump"
NEEDED_SONAMES = "needed sonames"
RUNPATH = "runpath"

def main():
  logging.basicConfig(level=logging.DEBUG)
  options, args = checkpkg.GetOptions()
  pkgnames = args
  checkers = []
  for pkgname in pkgnames:
    checker = checkpkg.CheckpkgBase(options.extractdir, pkgname)
    checkers.append(checker)
  binaries = []
  for checker in checkers:
    binaries.extend(checker.ListBinaries())
  # Make them unique
  binaries = set(binaries)
  ws_re = re.compile(r"\s+")

  # if [[ "$goodarch" = "yes" ]] ; then
  #   # man ld.so.1 for more info on this hack
  #   export LD_NOAUXFLTR=1
  # 
  #   listbinaries $EXTRACTDIR/$pkgname >$EXTRACTDIR/elflist
  #   # have to do this for ldd to work. arrg.
  #   if [ -s "$EXTRACTDIR/elflist" ] ; then
  #     chmod 0755 `cat $EXTRACTDIR/elflist`
  # 
  #     cat $EXTRACTDIR/elflist| xargs dump -Lv |nawk '$2=="NEEDED"{print $3}' |
  #       sort -u | egrep -v $EXTRACTDIR >$EXTRACTDIR/liblist
  # 
  #       
  # 
  #     print libraries used are:
  #     cat $EXTRACTDIR/liblist
  #     print "cross-referencing with depend file (May take a while)"
  #   else
  #     print No dynamic libraries in the package
  #   fi
  # fi
   
  env = copy.copy(os.environ)
  env["LD_NOAUXFLTR"] = "1"
  binaries_by_name = {}
  # Assembling a data structure with the data about binaries.
  # {
  #   <binary1 name>: {NEEDED_SONAMES: [...],
  #                   RUNPATH:     [...]},
  #   <binary2 name>: ...,
  #   ...
  # }
  #
  for binary in binaries:
    binary_base_name = binary.split("/")[-1]
    if binary_base_name not in binaries_by_name:
      binaries_by_name[binary_base_name] = {}
    binary_data = binaries_by_name[binary_base_name]
    args = [DUMP_BIN, "-Lv", binary]
    dump_proc = subprocess.Popen(args, stdout=subprocess.PIPE)
    stdout, stderr = dump_proc.communicate()
    ret = dump_proc.wait()
    for line in stdout.splitlines():
      fields = re.split(ws_re, line)
      logging.debug("%s says: %s", DUMP_BIN, fields)
      if len(fields) < 3:
        continue
      if fields[1] == "NEEDED":
        if NEEDED_SONAMES not in binary_data:
          binary_data[NEEDED_SONAMES] = []
        binary_data[NEEDED_SONAMES].append(fields[2])
      elif fields[1] == "RUNPATH":
        if RUNPATH not in binary_data:
          binary_data[RUNPATH] = []
        binary_data[RUNPATH].extend(fields[2].split(":"))
        # Adding the default runtime path search option.
        binary_data[RUNPATH].append("/usr/lib")
  print binaries_by_name

  # Building indexes
  runpath_by_needed_soname = {}
  # {"foo.so": ["/opt/csw/lib/gcc4", "/opt/csw/lib", ...],
  #  ...
  # }
  needed_sonames = set()
  binaries_by_soname = {}
  for binary_name, data in binaries_by_name.iteritems():
    for soname in data[NEEDED_SONAMES]:
      needed_sonames.add(soname)
      if soname not in runpath_by_needed_soname:
        runpath_by_needed_soname[soname] = []
      runpath_by_needed_soname[soname].extend(data[RUNPATH])
      if soname not in binaries_by_soname:
        binaries_by_soname[soname] = []
      binaries_by_soname[soname].append(binary_name)

  pkgmap = checkpkg.SystemPkgmap()
  paths_by_soname = pkgmap.paths_by_soname

  logging.debug("Determining soname-file relationships.")
  # lines by soname is an equivalent of $EXTRACTDIR/shortcatalog
  lines_by_soname = {}
  for soname in needed_sonames:
    if soname in paths_by_soname:
      logging.debug("%s found", repr(soname))
      # Finding the first matching path
      for runpath in runpath_by_needed_soname[soname]:
        if runpath in paths_by_soname[soname]:
          logging.debug("%s found in %s", runpath, paths_by_soname[soname])
          logging.debug("line found: %s", repr(paths_by_soname[soname][runpath]))
          lines_by_soname[soname] = paths_by_soname[soname][runpath]
          break
    else:
      logging.debug("%s not found in the soname list!", soname)
  for soname in needed_sonames:
    if soname in binaries:
    	print "%s is provided by the package itself" % soname
    elif soname in lines_by_soname:
      print ("%s is required by %s and provided by %s" 
             % (soname,
                binaries_by_soname[soname],
                repr(lines_by_soname[soname])))
    else:
    	print ("%s is required by %s, but we don't know what provides it."
    	       % (soname, binaries_by_soname[soname]))
  # TODO: extract package names from the pkgmap lines
  # TODO: print per-package deps (requires the transition: pkgname -> soname ->
  # pkgname)

  # for lib in `cat $EXTRACTDIR/liblist` ; do
  #   grep "[/=]$lib[ =]" $EXTRACTDIR/$pkgname/pkgmap
  #   if [[ $? -eq 0 ]] ; then
  #     echo $lib provided by package itself
  #     continue
  #   else
  #       grep "[/=]$lib[ =]" $SETLIBS
  #       if [[ $? -eq 0 ]]; then
  #     echo "$lib provided by package set being evaluated."
  #     continue
  #       fi
  #   fi
  # 
  #   libpkg=`grep /$lib $EXTRACTDIR/shortcatalog |
  #         sed 's/^.* \([^ ]*\)$/\1/' |sort -u`
  # 
  #   if [[ -z "$libpkg" ]] ; then
  #     echo "$lib $pkgname" >> $SETLIBS.missing
  #     print Cannot find package providing $lib.  Storing for delayed validation.
  #   else
  #     print $libpkg | fmt -1 >>$EXTRACTDIR/libpkgs
  #   fi
  # done
  # 
  # sort -u $EXTRACTDIR/libpkgs >$EXTRACTDIR/libpkgs.x
  # mv $EXTRACTDIR/libpkgs.x $EXTRACTDIR/libpkgs
  # 
  # diff $EXTRACTDIR/deppkgs $EXTRACTDIR/libpkgs >/dev/null
  # if [[ $? -ne 0 ]] ; then
  #   print SUGGESTION: you may want to add some or all of the following as depends:
  #   print '   (Feel free to ignore SUNW or SPRO packages)'
  #   diff $EXTRACTDIR/deppkgs $EXTRACTDIR/libpkgs | fgrep '>'
  # fi
  # 
  # 
  # 
  # if [[ "$basedir" != "" ]] ; then
  #   print
  #   if [[ -f $EXTRACTDIR/elflist ]] ; then
  #     print "Checking relocation ability..."
  #     xargs strings < $EXTRACTDIR/elflist| grep /opt/csw
  #     if [[ $? -eq 0 ]] ; then
  #       errmsg package build as relocatable, but binaries have hardcoded /opt/csw paths in them
  #     else
  #       print trivial check passed
  #     fi
  #   else
  #     echo No relocation check done for non-binary relocatable package.
  #   fi
  # fi
  #
  # ...
  # 
  # if [ -s $SETLIBS.missing ]; then
  #     print "Doing late evaluations of package library dependencies."
  #     while read ldep; do
  #   lib=`echo $ldep | nawk '{print $1}'`
  #         [ "$lib" = "libm.so.2" ] && continue
  #   pkg=`echo $ldep | nawk '{print $2}'`
  #   /usr/bin/grep "[/=]$lib[ =]" $SETLIBS >/dev/null
  #   if [ $? -ne 0 ]; then
  #       errmsg "Couldn't find a package providing $lib"
  #   else
  #       print "A package in the set being evaluated provides $lib"
  #   fi
  #     done < $SETLIBS.missing
  # fi


if __name__ == '__main__':
  main()
