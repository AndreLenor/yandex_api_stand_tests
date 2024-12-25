import data
import sender_stand_request

#   Функция для изменения значения в параметре Name
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

#   Функция для получения токена
def get_new_user_token():
    user_body = data.user_body
    resp_user = sender_stand_request.post_new_user(user_body)
    return resp_user.json()["authToken"]

#   Функция для позитивной проверки
def positive_assert(kit_body):
    resp_kit = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert resp_kit.status_code == 201
    assert resp_kit.json()["name"] == kit_body["name"]

#   Функция для негативной проверки
def negative_assert(kit_body):
	resp = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
	assert resp.status_code == 400

#   Допустимое количество символов (1)
def test_create_kit_1_symbol_in_name_get_success_response():
	kit_body = get_kit_body("a")
	positive_assert(kit_body)

#   Допустимое количество символов (511)
def test_create_kit_511_symbols_in_name_get_success_response():
	kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
	positive_assert(kit_body)

#  Количество символов меньше допустимого (0)
def test_create_kit_empty_name_get_error_response():
	kit_body = get_kit_body("")
	negative_assert(kit_body)

#   Количество символов больше допустимого (512)
def test_create_kit_512_symbols_in_name_get_error_response():
	kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
	negative_assert(kit_body)

#   Разрешены английские буквы
def test_create_kit_english_letters_in_name_get_success_response():
	kit_body = get_kit_body("QWErty")
	positive_assert(kit_body)

#   Разрешены русские буквы
def test_create_kit_russian_letters_in_name_get_success_response():
	kit_body = get_kit_body("Мария")
	positive_assert(kit_body)

#   Разрешены спецсимволы
def test_create_kit_has_special_symbols_in_name_get_success_response():
	kit_body = get_kit_body("\"№%@\",")
	positive_assert(kit_body)

#   Разрешены пробелы
def test_create_kit_has_space_in_name_get_success_response():
	kit_body = get_kit_body("Человек и КО")
	positive_assert(kit_body)

#   Разрешены цифры
def test_create_kit_has_number_in_name_get_success_response():
	kit_body = get_kit_body("123")
	positive_assert(kit_body)

#   Параметр не передан в запросе
def test_create_kit_no_name_get_error_response():
	current_kit_body_negative_no_name = data.kit_body.copy()
	current_kit_body_negative_no_name.pop("kit_body")
	negative_assert(current_kit_body_negative_no_name)

#   Передан другой тип параметра (число)
def test_create_kit_numeric_type_name_get_error_response():
	kit_body = get_kit_body(123)
	negative_assert(kit_body)