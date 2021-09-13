

# Submit a GET request to https://jsonplaceholder.typicode.com/users/1
# Check that the response status code is equal to 200
def test_get_user_with_id_1_check_status_code_equals_200():
    assert False


# Submit a GET request to https://jsonplaceholder.typicode.com/users/1
# Check that the response header 'Content-Type' is equal to 'application/json; charset=utf-8'
def test_get_user_with_id_1_check_content_type_equals_json():
    assert False


# Submit a GET request to https://jsonplaceholder.typicode.com/users/1
# Check that the response body field 'name' exists
def test_get_user_with_id_1_check_name_field_exists():
    assert False


# Submit a GET request to https://jsonplaceholder.typicode.com/users/1
# Check that the response body field 'name' has a value equal to 'Leanne Graham'
def test_get_user_with_id_1_check_name_equals_leanne_graham():
    assert False


# Submit a GET request to https://jsonplaceholder.typicode.com/users/1
# Check that the response body field 'company.name' has a value equal to 'Romaguera-Crona'
def test_get_user_with_id_1_check_company_name_equals_romaguera_crona():
    assert False


# Submit a GET request to https://jsonplaceholder.typicode.com/users
# Check that the response body is a list (an array) containing 10 elements
def test_get_all_users_check_number_of_users_equals_10():
    assert False


# Submit a POST request to https://jsonplaceholder.typicode.com/posts
# to create a new post with a title, body and associated user ID (1-10)
# Check that the response status code equals HTTP 201 (Created)
def test_post_new_post_check_status_code_equals_201():
    assert False


test_data_users = [(1, "Leanne Graham"), (2, "Ervin Howell"), (3, "Clementine Bauch")]


# Submit a GET request to retrieve user data for the specified user IDs
# Check that the response body field 'name' is equal to the specified expected name
def test_get_data_for_user_check_name():
    assert False
