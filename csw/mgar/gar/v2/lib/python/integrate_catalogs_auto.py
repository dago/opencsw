# Automatically integrate packages from one catalog to another. For instance,
# from unstable to kiel.
#
# Criteria for integration
# - only a complete bundle with all dependencies can be integrated; each
#   dependency triggers a new bundle, so multiple bundles are uploaded at one
#   time; all these package constitute a set
# - all packages from a given set must be in unstable for at least X days (30?)
# - packages without insertion time information are not considered for integration
#
# Questions:
# - Do we upload a bundle using csw-upload-pkg? (as a library or via an invocation)
# - Do we run checkpkg against the bundle and the target catalog?
# - If the checkpkg run fails, what do we do?
# - Do we integrate with the bugtracker? (packages must not have critical bugs)
