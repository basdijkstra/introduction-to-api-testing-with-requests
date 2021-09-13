import requests
import pytest


# Submit a GET request to https://jsonplaceholder.typicode.com/users/1
# Check that the response status code is equal to 200
def test_get_user_with_id_1_check_status_code_equals_200():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.status_code == 200


# Submit a GET request to https://jsonplaceholder.typicode.com/users/1
# Check that the response header 'Content-Type' is equal to 'application/json; charset=utf-8'
def test_get_user_with_id_1_check_content_type_equals_json():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"


# Submit a GET request to https://jsonplaceholder.typicode.com/users/1
# Check that the response body field 'name' exists
def test_get_user_with_id_1_check_name_field_exists():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    response_body = response.json()
    assert 'name' in response_body


# Submit a GET request to https://jsonplaceholder.typicode.com/users/1
# Check that the response body field 'name' has a value equal to 'Leanne Graham'
def test_get_user_with_id_1_check_name_equals_leanne_graham():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    response_body = response.json()
    assert response_body["name"] == "Leanne Graham"


# Submit a GET request to https://jsonplaceholder.typicode.com/users/1
# Check that the response body field 'company.name' has a value equal to 'Romaguera-Crona'
def test_get_user_with_id_1_check_company_name_equals_romaguera_crona():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    response_body = response.json()
    assert response_body["company"]["name"] == "Romaguera-Crona"


# Submit a GET request to https://jsonplaceholder.typicode.com/users
# Check that the response body is a list (an array) containing 10 elements
def test_get_all_users_check_number_of_users_equals_10():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    response_body = response.json()
    assert len(response_body) == 10


# Submit a POST request to https://jsonplaceholder.typicode.com/posts
# to create a new post with a title, body and associated user ID (1-10)
# Check that the response status code equals HTTP 201 (Created)
def test_post_new_post_check_status_code_equals_201():
    new_post = {
        "title": "My awesome new post title",
        "body": "My awesome new post body",
        "userId": 1
    }
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)
    assert response.status_code == 201


test_data_users = [(1, "Leanne Graham"), (2, "Ervin Howell"), (3, "Clementine Bauch")]


# Submit a GET request to retrieve user data for the specified user IDs
# Check that the response body field 'name' is equal to the specified expected name
@pytest.mark.parametrize("userid, expected_name", test_data_users)
def test_get_data_for_user_check_name(userid, expected_name):
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{userid}")
    response_body = response.json()
    assert response_body["name"] == expected_name
