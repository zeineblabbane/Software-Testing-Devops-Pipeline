import sqlite3
from unittest import TestCase, main
from unittest.mock import patch

from users import add, fetch_one, get_users, edit, delete

class TestGetUsers(TestCase):
    @patch("users.sql")
    def test_fetchall(self, mocked_object):
        # Given
        mocked_object.connect().execute().fetchall.return_value = [(1,'Zeineb','12345678'),(2,'test','test')]
        expected_user = [(1,'Zeineb','12345678'),(2,'test','test')]
        # When
        result_user = get_users()
        # Then
        self.assertEqual(expected_user, result_user)

    @patch("users.sql")
    def test_fetchone(self, mocked_object):
        # Given
        mocked_object.connect().execute().fetchone.return_value = [(1,'Zeineb','12345678')]
        expected_user = [(1,'Zeineb','12345678')]
        # When
        result_user = fetch_one(1)
        # Then
        self.assertEqual(expected_user, result_user)

class TestAddUser(TestCase):
    @patch("users.sql", spec=sqlite3)
    def test_addUser(self, mocked_object):
        # Given
        mock_execute= (mocked_object.connect.return_value.execute)
        # When
        add('zeineb', '12345678')
        # Then
        mock_execute.assert_called_once()

class TestEditUser(TestCase):
    @patch("users.sql", spec=sqlite3)
    def test_updateProduct(self, mocked_object):
        # Given
        mock_execute=(mocked_object.connect.return_value.execute)
        # When
        edit(1,'Zeineb','12345678')
        # Then
        mock_execute.assert_called_once()

class TestDeleteUser(TestCase):
    @patch("users.sql", spec=sqlite3)
    def test_deleteProduct(self, mocked_object):
        # Given
        mock_execute=(mocked_object.connect.return_value.execute)
        # When
        delete(1)
        # Then
        mock_execute.assert_called_once()

if __name__ == '__main__':
    main()