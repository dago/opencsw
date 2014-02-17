"""SQLObject connection closing test.

From http://www.sqlite.org/inmemorydb.html:

  The database is automatically deleted and memory is reclaimed when the last
  connection to the database closes.

"""

import unittest
import sqlobject

class Foo(sqlobject.SQLObject):
  bar = sqlobject.UnicodeCol(length=250, unique=True)


class SqlobjectConnectionUnitTest(unittest.TestCase):

  def setUp(self):
    db_uri = 'sqlite:/:memory:'
    sqo_conn = sqlobject.connectionForURI(db_uri)
    sqlobject.sqlhub.processConnection = sqo_conn
    Foo.createTable()

  def tearDown(self):
    # This seems not to work. When setUp() is run the second time, it gets
    # access to the same in-memory database that was used the first time.
    sqlobject.sqlhub.processConnection.close()
    sqlobject.sqlhub.processConnection = None

  def testNotPresentAndInsert1(self):
    foo_obj = Foo(bar='baz')

  def testNotPresentAndInsert2(self):
    foo_obj = Foo(bar='baz')


if __name__ == '__main__':
  unittest.main()
