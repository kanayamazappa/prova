from rest_framework.test import APITestCase
from rest_framework import status
from requests.auth import HTTPBasicAuth
import requests

# Create your tests here.
class PersonTest(APITestCase):
    def test_create(self):
        """
        Cadastrando
        """
        
        auth = HTTPBasicAuth('admin', 'prova123')
        response = requests.post('http://localhost:8080/persons/', json={"facebookId": "100005651977435"}, auth=auth)
        
        print "STATUS CODE:"
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_delete(self):
        """
        Deletando
        """
        
        auth = HTTPBasicAuth('admin', 'prova123')
        response = requests.delete('http://localhost:8080/persons/100005651977435/', auth=auth)
        
        print "STATUS CODE:"
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_list(self):
        """
        Listando
        """

        auth = HTTPBasicAuth('admin', 'prova123')
        response = requests.get('http://localhost:8080/persons/', auth=auth)
        
        print "STATUS CODE:"
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_limit(self):
        """
        Listando
        """

        auth = HTTPBasicAuth('admin', 'prova123')
        response = requests.get('http://localhost:8080/persons/?limit=2', auth=auth)
        
        print "STATUS CODE:"
        self.assertEqual(response.status_code, status.HTTP_200_OK)