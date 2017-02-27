import json

from flask import Flask, request, jsonify

import smartac_control.smartac as smartac
from smartac_control.config import config

app = Flask(__name__)
smartac_controller = smartac.ThinkEcoSmartAC(
    config['smartac']['username'],
    config['smartac']['password'],
    config['smartac']['application_ids']
)


@app.route('/smartac', methods=['POST'])
def smartac():
  data = json.load(request.data)
  smartac_controller.set_thermostat(data['location'], data['temperature'])

  return jsonify({
    'success': True
  })


if __name__ == "__main__":
  app.run(host='0.0.0.0')
