import requests
import json
import uuid

device_id = str(uuid.uuid4())

def test_set_current_temperature():
  print(f"Тестирование метода set_current_temperature")
  url = "http://192.169.10.10:8000/device-managment/add_device"

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
  url = f"http://192.169.10.10:8000/device-managment/status_device?serial_number={device_id}"

  payload = {}
  headers = {
    'accept': 'application/json'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  if response.status_code != 200:
    print(f"  Error: код ответа - {response.status_code}. Сообщение -{response.text}")
  else:
    print(f"  Статус устройства - {response.text}")

test_set_current_temperature()
test_get_status_device()