import pytest
import os
from app import create_app
from create_db import create_db


@pytest.fixture(scope="session", autouse=True)
def create_test_database(tmp_path_factory):
    tmp_dir = tmp_path_factory.mktemp("tmp")
    database_filename = tmp_dir / "test_database.db"
    create_db(database_filename)
    os.environ['DATABASE_FILENAME'] = str(database_filename)


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app(__name__, test=True)
    flask_app.secret_key = 'test123'
    flask_app.config.update({"TESTING":True,})
    testing_client = flask_app.test_client(use_cookies=False)
    context = flask_app.app_context()
    context.push()
    yield testing_client
    context.pop()

#Test /index
def test_index(test_client):
    # Given
    expected_status_code = 200
    expected_page_title = b"<h3>User Management</h3>"
    # When
    response = test_client.get('/')
    # Then
    assert expected_status_code == response.status_code

#Test /add_user GET
def test_add_user_get(test_client):
    # Given
    expected_status_code = 200
    expected_page_title = b"<h3>Add user</h3>"
    # When
    response = test_client.get('/add_user')
    # Then
    assert expected_status_code == response.status_code
    assert expected_page_title in response.data

#Test /add_user POST
def test_add_user_post(test_client):
    # Given
    expected_status_code = 200
    expected_page_alert = b"User Added"

    data_to_register={
        "uname":"Zeineb",
         "contact":"12345678" 
    }

    # When
    response = test_client.post('/add_user',data=data_to_register,follow_redirects=True )
    # Then
    assert expected_status_code == response.status_code

#Test /edit_user/<string:uid> GET
def test_edit_user_get(test_client):
    # Given
    expected_status_code = 200
    expected_page_title = b"<h3>Edit user</h3>"
    id_user_to_update=1
    # When
    response = test_client.get(f'/edit_user/{id_user_to_update}')
    # Then
    assert expected_status_code == response.status_code
    assert expected_page_title in response.data

#Test /edit_user/<string:uid> POST
def test_edit_user_post(test_client):
    # Given
    expected_status_code = 200
    id_user_to_update=1
    data_to_update = {"uname":"Zeineb", "contact":"24100090" }
    # When
    response = test_client.post(f'/edit_user/{id_user_to_update}',data=data_to_update,follow_redirects=True )
    # Then
    assert expected_status_code == response.status_code
#Test /delete_user/<string:uid> POST
def test_delete_user_post(test_client):
    # Given
    expected_status_code = 200
    id_user_to_delete=1
    # When
    response = test_client.get(f'/delete_user/{id_user_to_delete}',follow_redirects=True)
    # Then
    assert expected_status_code == response.status_code

