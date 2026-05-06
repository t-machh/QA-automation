import helpers.base_client as api

class TestStore:

    def test_get_inventory(self):
        r = api.get("/store/inventory")
        assert r.status_code == 200
        assert isinstance(r.json(), dict)

    def test_create_order(self):
        payload = {"id": 900001, "petId": 1, "quantity": 1,
                   "status": "placed", "complete": True}
        r = api.post("/store/order", payload)
        assert r.status_code == 200
        assert r.json()["status"] == "placed"

    def test_get_order_by_id(self):
        # Cria uma ordem primeiro
        payload = {"id": 900002, "petId": 2, "quantity": 2,
                   "status": "placed", "complete": False}
        api.post("/store/order", payload)

        r = api.get("/store/order/900002")
        assert r.status_code == 200
        assert r.json()["id"] == 900002

    def test_delete_order(self):
        # Cria uma ordem
        payload = {"id": 900003, "petId": 3, "quantity": 1,
                   "status": "placed", "complete": True}
        api.post("/store/order", payload)

        r = api.delete("/store/order/900003")
        assert r.status_code == 200

    def test_get_deleted_order_returns_404(self):
        # Certifique-se de que a ordem 900003 foi deletada
        r = api.get("/store/order/900003")
        assert r.status_code == 404