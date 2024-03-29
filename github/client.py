import requests
import json

class GithubClient():
    
    API_BASE_URL = 'http://api.github.com'
    
    @classmethod
    def get_repos_by_user(self, user):
        response = requests.get(
            f'{self.API_BASE_URL}/users/{user}/repos')
        if response.status_code == 200:
            return {"status_code": 200, "body": response.json()}
        else:
            return {"status_code": response.status_code, "body": "Erro while getting repositories"}