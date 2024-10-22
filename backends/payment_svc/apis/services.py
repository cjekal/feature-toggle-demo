import requests

class UserService:
    def get_user_details(self, user_id):
        response = requests.get(f"http://user_svc:8000/users/{user_id}")
        return response.json()
