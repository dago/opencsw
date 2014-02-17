#!/opt/csw/bin/bash

# Creates an allpkg directory based on a package tree.
#
# Useful for a private buildfarm or for testing the buildfarm code on
# in a development environment.

set -e
set -u

target_dir=$1
source_tree=$2

echo "target directory: '$target_dir'"
echo "source tree: '$source_tree'"

function get_prefix {
local f=$1
if echo $f | ggrep -q ^lib; then
  echo ${f:0:4}
else
  echo ${f:0:1}
fi
}

function copy_files_to {
local dest=$1
shift
local f
local dest_dir
while read f; do
  dest_dir="${dest}/$(get_prefix "${f}")"
  if [[ ! -d "${dest_dir}" ]]; then
    echo "mkdir '${dest_dir}'"
    mkdir -p "${dest_dir}"
  fi
  if [[ ! -f "${dest_dir}/${f}" ]]; then
    gcp -v "$f" "${dest_dir}"
  fi
done
}

mkdir -p "${target_dir}"

for catalog in ${source_tree}/*/*/*/catalog; do
  catalog_dir=$(dirname ${catalog})
  cat ${catalog} | gawk '$5 ~ /[0-9a-f]{32}/ { print $4 }' \
    | (cd "${catalog_dir}"; copy_files_to "${target_dir}")
done

echo "Done."
