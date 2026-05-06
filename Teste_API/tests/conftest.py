import pytest
import helpers.base_client as api

@pytest.fixture
def created_pet():
    """Cria um pet para ser usado nos testes que precisam de um pet existente"""
    pet_id = 999999  # use um ID fixo para facilitar
    pet_data = {
        "id": pet_id,
        "name": "FixturePet",
        "category": {"id": 1, "name": "dog"},
        "photoUrls": ["https://picsum.photos/200"],
        "tags": [{"id": 0, "name": "friendly"}],
        "status": "available"
    }
    # Tenta deletar se já existir (apenas para limpeza)
    api.delete(f"/pet/{pet_id}")
    # Cria o pet
    response = api.post("/pet", pet_data)
    assert response.status_code == 200, "Falha ao criar pet para fixture"
    yield pet_data
    # Teardown: deleta o pet após o teste
    api.delete(f"/pet/{pet_id}")