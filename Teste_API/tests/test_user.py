import helpers.base_client as api

class TestUser:

    def test_create_user(self):
        payload = {
            "id": 1001,
            "username": "testuser",
            "firstName": "Test",
            "lastName": "User",
            "email": "test@example.com",
            "password": "12345",
            "phone": "123456789",
            "userStatus": 1
        }
        r = api.post("/user", payload)
        assert r.status_code == 200

    def test_get_user_by_username(self):
        # Primeiro cria o usuário
        payload = {
            "id": 1002,
            "username": "joaosilva",
            "firstName": "João",
            "lastName": "Silva",
            "email": "joao@example.com",
            "password": "123",
            "phone": "999999999",
            "userStatus": 0
        }
        api.post("/user", payload)

        r = api.get("/user/joaosilva")
        assert r.status_code == 200
        assert r.json()["username"] == "joaosilva"

    def test_update_user(self):
        # Cria usuário
        payload = {
            "id": 1003,
            "username": "maria",
            "firstName": "Maria",
            "lastName": "Oliveira",
            "email": "maria@example.com",
            "password": "oldpass",
            "phone": "111111111",
            "userStatus": 1
        }
        api.post("/user", payload)

        # Atualiza
        updated = {
            "id": 1003,
            "username": "maria",
            "firstName": "Maria",
            "lastName": "Santos",
            "email": "maria.santos@example.com",
            "password": "newpass",
            "phone": "222222222",
            "userStatus": 2
        }
        r = api.put("/user/maria", updated)
        assert r.status_code == 200

        # Verifica
        r_get = api.get("/user/maria")
        assert r_get.json()["lastName"] == "Santos"

    def test_delete_user(self):
        # Cria
        payload = {
            "id": 1004,
            "username": "todelete",
            "firstName": "Delete",
            "lastName": "Me",
            "email": "delete@example.com",
            "password": "123",
            "phone": "000000000",
            "userStatus": 0
        }
        api.post("/user", payload)

        # Deleta
        r = api.delete("/user/todelete")
        assert r.status_code == 200

        # Confirma que não existe mais
        r_get = api.get("/user/todelete")
        assert r_get.status_code == 404