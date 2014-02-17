"""A shared space for errors we might want to throw and handle."""

class Error(Exception):
  """A generic error."""


class StdoutSyntaxError(Error):
  """A problem parsing stdout from a command."""


class DatabaseContentsError(Error):
  """Something is wrong with the contents of the database."""


class DataError(Error):
  """Wrong data have been passed to the function."""
