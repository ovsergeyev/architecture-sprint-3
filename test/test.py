import requests
import json
import uuid

host = '192.169.10.10'
gateway_port = 8000
device_id = str(uuid.uuid4())
sensor_id = str(uuid.uuid4())

def test_add_device():
  print(f"Тестирование метода add_device")
  url = f"http://{host}:{gateway_port}/device-managment/add_device"

  payload = json.dumps({
    "serial_number": device_id,
    "status": False
  })
  headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  if response.status_code != 200:
    print(f"  Error: код ответа - {response.status_code}. Сообщение -{response.text}")
  else:
    print(f"  Устройство успешно добавлено. Сообщение - {response.text}")

def test_get_status_device():
  print(f"Тестирование метода get_status_device")
  url = f"http://{host}:{gateway_port}/device-managment/status_device?serial_number={device_id}"

  payload = {}
  headers = {
    'accept': 'application/json'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  if response.status_code != 200:
    print(f"  Error: код ответа - {response.status_code}. Сообщение -{response.text}")
  else:
    print(f"  Статус устройства - {response.text}")

def test_change_device_status():
  print(f"Тестирование метода change_device_status")
  url = f"http://{host}:{gateway_port}/device-managment/change_device_status"

  payload = json.dumps({
    "serial_number": device_id,
    "status": True
  })
  headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
  }

  response = requests.request("PUT", url, headers=headers, data=payload)

  if response.status_code != 200:
    print(f"  Error: код ответа - {response.status_code}. Сообщение -{response.text}")
  else:
    print(f"  Статус устройства - {response.text}")

def test_add_sensor():
  print(f"Тестирование метода add_sensor")
  url = f"http://{host}:{gateway_port}/device-managment/add_sensor"

  payload = json.dumps({
    "serial_number": sensor_id,
    "device_id": device_id
  })
  headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  if response.status_code != 200:
    print(f"  Error: код ответа - {response.status_code}. Сообщение -{response.text}")
  else:
    print(f"  Датчик успешно добавлен. Статус датчика - {response.text}")

def test_set_target_temperature():
  print(f"Тестирование метода set_target_temperature")
  url = f"http://{host}:{gateway_port}/device-managment/set_target_temperature"

  payload = json.dumps({
    "device_id": device_id,
    "temperature": 20.2
  })
  headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
  }

  response = requests.request("PUT", url, headers=headers, data=payload)

  if response.status_code != 200:
    print(f"  Error: код ответа - {response.status_code}. Сообщение -{response.text}")
  else:
    print(f"  Целевая температура установлена. Ответ - {response.text}")

def test_get_target_temperature():
  print(f"Тестирование метода get_target_temperature")
  url = f"http://{host}:{gateway_port}/device-managment/get_target_temperature?device_id={device_id}"

  payload = {}
  headers = {
    'accept': 'application/json',
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  if response.status_code != 200:
    print(f"  Error: код ответа - {response.status_code}. Сообщение -{response.text}")
  else:
    print(f"  Целевая температура - {response.text}")

def test_set_current_temperature():
  print(f"Тестирование метода set_current_temperature")
  url = f"http://{host}:{gateway_port}/telemetry/set_current_temperature"

  payload = json.dumps({
    "serial_number": sensor_id,
    "value": 20.0
  })
  headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  if response.status_code != 200:
    print(f"  Error: код ответа - {response.status_code}. Сообщение -{response.text}")
  else:
    print(f"  Температура с датчика установлена. Ответ - {response.text}")

def test_last_temperature():
  print(f"Тестирование метода last_temperature")
  url = f"http://{host}:{gateway_port}/telemetry/last_temperature?serial_number={sensor_id}"

  payload = {}
  headers = {
    'accept': 'application/json',
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  if response.status_code != 200:
    print(f"  Error: код ответа - {response.status_code}. Сообщение -{response.text}")
  else:
    print(f"  Последняя температура с датчика - {response.text}")

test_add_device()
test_get_status_device()
test_change_device_status()
test_add_sensor()
test_set_target_temperature()
test_get_target_temperature()
test_set_current_temperature()
test_last_temperature()