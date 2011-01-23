#!/bin/bash
#
# $Id$

# A srv4 .pkg file is a header + 2 cpio archives.  The header is 1 (but maybe
# more?) 512 byte block.  The cpio archives use a 512b block size too.  We find
# the end of the first cpio archive (marked by 'TRAILER!!!' inside the last
# block) and then determine how many bytes into the file this is, divide by
# block size to find the number of blocks until the trailer and add another
# block to get the number of blocks in the file to skip so that we're at the
# second cpio archive.
#
# These two options need to be assumed to be set:
# set -e
# set -u

function custom_pkgtrans {
  local outd
  local skipblks
  if ! [[ -d "$2" ]]; then
    echo "'$2' is not a directory"
    exit 1
  fi
  outd=$2/$3
  skipblks=$(expr $(ggrep -a -b -o -m 1 'TRAILER!!!' "$1" \
    | awk -F: '{print $1}') / 512 + 1)
  mkdir -p "${outd}"

  (
    dd if="$1" skip="${skipblks}" 2>/dev/null \
      | (cd "${outd}" ; cpio -ivdm || true)
  ) >/dev/null 2>&1

  if [ ! -d "${outd}/install" ]; then
    echo "Failed to extract '$1' to ${outd}"
    exit 1
  fi
}
