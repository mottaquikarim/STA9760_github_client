import requests

from github_client.conf import API_BASE

def get_user(username):
  """Get user data from API"""
  r = requests.get(f"{API_BASE}/users/{username}")
  return r.status_code, r.json()