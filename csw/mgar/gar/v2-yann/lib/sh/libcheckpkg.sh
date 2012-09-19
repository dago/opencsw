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

function short_custom_pkgtrans {
  # This function sometimes fails.  It works on Solaris 9, but likes to fail
  # on Solaris 10.
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


get_header_blocks() {
  dd if="$1" skip=1 \
    | cpio -i -t 2>&1  >/dev/null \
    | nawk '{print $1; exit;}'
}

custom_pkgtrans() {
  local hdrblks
  if [[ ! -d "$2" ]] ; then
    echo ERROR: "$2" is not a directory >/dev/fd/2
    return 1
  fi
  hdrblks=$(get_header_blocks "$1")

  echo "initial hdrblks=$hdrblks"

  hdrblks=$(( $hdrblks + 1 ))
  mkdir $2/$3

  local counter=0
  while :; do
    echo "Attempting ${hdrblks} offset"
    # cpio sometimes returns 1, and we don't want to bail out when it happens.
    dd if="$1" skip="$hdrblks" | (cd $2/$3 ; cpio -ivdm) || true
    if [[ -d "$2/$3/install" ]]; then
      echo "Unpack successful."
      break
    fi
    hdrblks=$(( $hdrblks + 1 ))
    counter=$(( $counter + 1 ))
    # To prevent us from going on forever.
    if [[ "${counter}" -gt 100 ]]; then
      echo "Unpack keeps on being unsuccessful. Bailing out."
      return 1
    fi
    echo "Unpack unsuccessful, trying offset ${hdrblks}"
  done
}
