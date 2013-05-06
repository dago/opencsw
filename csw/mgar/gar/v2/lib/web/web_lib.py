# A common library for web apps.

connected_to_db = False

def ConnectToDatabase():
  """Connect to the database only if necessary.

  One problem with this approach might be that if the connection is lost, the
  script will never try to reconnect (unless it's done by the ORM).
  """
  global connected_to_db
  if not connected_to_db:
    configuration.SetUpSqlobjectConnection()
    connected_to_db = True
