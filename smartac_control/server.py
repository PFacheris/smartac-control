import json

from flask import Flask, request, jsonify

import smartac
from config import config

app = Flask(__name__)
smartac_controller = smartac.ThinkEcoSmartAC(
    config['smartac']['username'],
    config['smartac']['password'],
    config['smartac']['application_ids']
)


@app.route('/smartac', methods=['POST'])
def smartac():
  data = json.loads(request.data)
  smartac_controller.set_thermostat(data['location'], data['temperature'])

  return jsonify({
    'success': True
  })


if __name__ == "__main__":
  app.run()
