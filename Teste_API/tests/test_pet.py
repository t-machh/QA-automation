import helpers.base_client as api

class TestPet:

    def test_create_pet(self):
        payload = {"id": 900002, "name": "Buddy", "status": "available",
                   "photoUrls": ["http://example.com/buddy.jpg"]}
        r = api.post("/pet", payload)
        assert r.status_code == 200
        assert r.json()["name"] == "Buddy"

    def test_get_pet_by_id(self, created_pet):
        pet_id = created_pet["id"]
        r = api.get(f"/pet/{pet_id}")
        assert r.status_code == 200
        assert r.json()["id"] == pet_id

    def test_update_pet(self, created_pet):
        payload = {**created_pet, "name": "Rex Updated", "status": "sold"}
        r = api.put("/pet", payload)
        assert r.status_code == 200
        assert r.json()["name"] == "Rex Updated"
        assert r.json()["status"] == "sold"

    def test_find_pets_by_status(self):
        for status in ["available", "pending", "sold"]:
            r = api.get("/pet/findByStatus", params={"status": status})
            assert r.status_code == 200
            assert isinstance(r.json(), list)

    def test_delete_pet(self, created_pet):
        pet_id = created_pet["id"]
        r = api.delete(f"/pet/{pet_id}")
        assert r.status_code == 200

    def test_get_deleted_pet_returns_404(self, created_pet):
        pet_id = created_pet["id"]
        api.delete(f"/pet/{pet_id}")
        r = api.get(f"/pet/{pet_id}")
        assert r.status_code == 404