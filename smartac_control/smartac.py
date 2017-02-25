import json

import requests


THINKECO_ROOT_URL = 'https://mymodlet.com'
DEFAULT_HEADERS = {
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'Content-Type': 'application/json; charset=UTF-8'
}


class ThinkEcoSmartAC():
  def __init__(self, username, password, appliance_ids=None):
    if not appliance_ids:
      appliance_ids = {}

    self.username = username
    self.password = password
    self.appliance_ids = appliance_ids

  def get_auth_cookies(self):
    path = '/Account/Login'
    url = THINKECO_ROOT_URL + path
    params = {
      'loginForm.Email': self.username,
      'loginForm.Password': self.password,
      'loginForm.RememberMe': True,
      'ReturnUrl': None
    }

    res = requests.post(url, params=params, headers=DEFAULT_HEADERS)
    cookies = {}
    for history_res in res.history:
        cookies.update(dict(history_res.cookies))

    cookies.update(dict(res.cookies))
    return cookies

  def set_thermostat(self, appliance, temperature, state='on'):
    path = '/SmartAC/UserSettings'
    url = THINKECO_ROOT_URL + path
    data = {
      'applianceId': self.appliance_ids[appliance],
      'targetTemperature': temperature,
      'thermostated': (state is 'on')
    }

    res = requests.post(
        url,
        headers=DEFAULT_HEADERS,
        cookies=self.get_auth_cookies(),
        data=json.dumps(data)
    )
    res.raise_for_status()
