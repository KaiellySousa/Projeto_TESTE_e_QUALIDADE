import requests
import pytest

class TestePetstore:
    base_url = "https://petstore.swagger.io/v2"

    
    def teste_manutencao_pet(self):
        pet_id = 202605
        
        payload = {"id": pet_id, "name": "Scooby", "status": "available"}
        res_post = requests.post(f"{self.base_url}/pet", json=payload)
        assert res_post.status_code == 200

        payload["name"] = "Scooby Atualizado"
        res_put = requests.put(f"{self.base_url}/pet", json=payload)
        assert res_put.json()["name"] == "Scooby Atualizado"

        res_get = requests.get(f"{self.base_url}/pet/{pet_id}")
        assert res_get.status_code == 200

        res_delete = requests.delete(f"{self.base_url}/pet/{pet_id}")
        assert res_delete.status_code == 200

    def teste_pedidos_loja(self):
        order_payload = {
            "id": 1,
            "petId": 202605,
            "quantity": 1,
            "status": "placed",
            "complete": True
        }
        res = requests.post(f"{self.base_url}/store/order", json=order_payload)
        assert res.status_code == 200
        assert res.json()["status"] == "placed"

        res_inv = requests.get(f"{self.base_url}/store/inventory")
        assert res_inv.status_code == 200

    def teste_gerenciamento_usuario(self):
        username = "kaielly_qa"
        user_data = {
            "username": username,
            "firstName": "Kaielly",
            "email": "kaielly@gmail.com.com"
        }
        requests.post(f"{self.base_url}/user", json=user_data)
        res = requests.get(f"{self.base_url}/user/{username}")
        assert res.status_code == 200
        assert res.json()["username"] == username
        
    def teste_buscar_pet_inexistente(self):
        id_falso = 999999999
        res = requests.get(f"{self.base_url}/pet/{id_falso}")
        assert res.status_code == 404