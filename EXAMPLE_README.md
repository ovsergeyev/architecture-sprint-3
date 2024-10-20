**1.1.1 Функциональность монолитного приложения:**

**Управление отоплением:**

* Пользователи могут удалённо включать/выключать отопление в своих домах.
* Пользователи могут устанавливать желаемую температуру.
* Система автоматически поддерживает заданную температуру, регулируя подачу тепла.

**Мониторинг температуры:**

* Система получает данные о температуре с датчиков, установленных в домах.
* Пользователи могут просматривать текущую температуру в своих домах через веб-интерфейс.

**1.1.2 Анализ архитектуры монолитного приложения**

* **Язык программирования**: Java. Популярный язык общего назначения. Много готовых решений, фреймворков, проверен временем.
* **База данных**: PostgreSQL. Реляционная БД. Соблюдает принципы ACID, но масштабируется только сторонними расширениями.
* **Архитектура**: Монолитная, все компоненты системы (обработка запросов, бизнес-логика, работа с данными) находятся в рамках одного приложения. Минусы: высокий риск ошибок (изменения в одной части приложения могут непредсказуемо влиять на другие части); длительные циклы разработки и развёртывания (при каждом изменении приходится тестировать всё приложение целиком); трудно масштабировать отдельные компоненты системы; трудно управлять командой.
* **Взаимодействие**: Синхронное, запросы обрабатываются последовательно. Плюсы: простота, предсказуемость, лёгкость отладки и мониторинга. Минусы: возможны высокие задержки, увеличение зависимости между сервисами, ограниченная масштабируемость из-за блокирующих вызовов.
* **Развертывание**: Требует остановки всего приложения. Пользователи могут сталкиваться с недоступностью на время развертывания.

**1.1.3 Домены и границы контекстов**

* **Домен: управление устройствами**

  * Поддомен: управление отоплением
    * Контекст: включение\выключение устройства
    * Контекст: установка необходимой температуры
  * Поддомен: автоматическое поддержание температуры
    * Контекст: регулировка подачи тепла
* **Домен: мониторинг температуры**

  * Поддомен: приём данных с датчиков
    * Контекст: получение данных с датчиков о температуре
  * Поддомен: отображение данных пользователю
    * Контекст: отображение текущей температуры в доме пользователя

**1.1.4 Визуализация контекста системы (С4 System Context diagram, PlantUML)**

[C4 диаграмма (System Context diagram), визуализирующая взаимодействие монолитного приложения с внешним миром](diagrams/context/SmartHome_Context.puml)

![C4 диаграмма (System Context diagram), визуализирующая взаимодействие монолитного приложения с внешним миром](diagrams/context/SmartHome_Context.png)

# Задание 1.2: Архитектура микросервисов

**1.2.1 Декомпозиция на микросервисы**

1. **Телеметрия** - микросервис, который занимается ведением информации поступающей с датчиков.
2. **Управление устройствами** - микросервис, занимается ведением перечня датчиков и отвечает за выполнение команд пользователя.
3. **Управления пользователями** - микросервис, который отвечает за управление пользователями и домовладениями.

**1.2.2 Определение взаимодействия**

1. Все запросы пользователя поступают в API Gateway.
2. API Gateway маршрутизирует запросы согласно роутингу микросервисам.
3. Микросервисы взаимодействуют с устройствами через модули. Модуль и микросервис общаются через шину данных (kafka).
4. Микросервисы хранят данные, которые заведены пользователями, и получены от устройств, в БД.

**1.2.3 Визуализация архитектуры**

[C4 — Уровень контейнеров (Containers)](diagrams/container/SmartHome_Container.puml)

![C4 — Уровень контейнеров (Containers)](diagrams/container/SmartHome_Container.png)

[C4 — Уровень компонентов (Components)](diagrams/component/SmartHome_Component.puml)

![C4 — Уровень компонентов (Components)](diagrams/component/SmartHome_Component.png)

Отобразим на диаграмме кода взаимодействие сервисного слоя со слоями БД и продюсером. Микросервис Управление устройствами. Смена статуса устройства.

[C4 — Уровень кода (Code)](diagrams/code/SmartHome_Code.puml)

![C4 — Уровень кода (Code)](diagrams/code/SmartHome_Code.png)

# Задание 1.3: ER-диаграмма

**1.3.1 Идентификация сущностей**

* Пользователь (User)
* Дом (House)
* Устройство (Device)
* Тип устройства (DeviceType)
* Модуль (Module)
* Телеметрия (Telemetry)

**1.3.2 Определение атрибутов**

**Сущность "Дом (House)"**

* `id` — уникальный идентификатор дома.
* `user_id` — идентификатор пользователя — внешний ключ к таблице `User`.
* `address` — адрес дома.

**Сущность "Пользователь (User)"**

* `id` — уникальный идентификатор пользователя.
* `name` — имя пользователя.

**Сущность "Модуль (Module)"**

* `id` — уникальный идентификатор модуля.
* `house_id` — идентификатор дома, в котором установлен модуль — внешний ключ к таблице `House`.
* `device_type_id` — идентификатор типа устройства — внешний ключ к таблице `DeviceType`.
* `serial_number` — серийный номер модуля.
* `title` — название модуля.

**Сущность "Тип устройства (DeviceType)"**

* `id` — уникальный идентификатор типа устройства.
* `code` — код типа устройства.
* `description` — описание типа устройства.

**Сущность "Устройство (Device)"**

* `id` — уникальный идентификатор устройства.
* `module_id` — идентификатор модуля, к которому подключено устройство — внешний ключ к таблице `Module`.
* `serial_number` — серийный номер устройства.
* `status` — текущее состояние устройства (включено/выключено).

**Сущность "Телеметрия (Telemetry)"**

* `id` — уникальный идентификатор данных телеметрии.
* `device_id` — идентификатор устройства, который отправляет данные — внешний ключ к таблице `Device`.
* `datetime` — дата и время получения данных
* `data` — данные телеметрии

**1.3.3 Описание связей**

* **Пользователь — Дом:** один-ко-многим, один пользователь может иметь доступ к нескольким домам, но каждый дом связан только с одним пользователем.
* **Модуль — Дом:** один-ко-многим, в одном доме может быть установлено несколько модулей, но каждый модуль связан только с одним домом.
* **Модуль — Тип устройства:** один-ко-многим, один тип устройства может быть у нескольких модулей, но к одному модулю могут быть подключены устройства только одного типа.
* **Устройство — Модуль:** один-ко-многим, к одному модулю могут быть подключены несколько устройств, но каждое устройство связано только с одним модулем.
* **Телеметрия — Устройство:** один-ко-многим, одно устройство генерирует несколько единиц данных телеметрии, но одна единица данных может быть создана только одним устройством.

**1.3.4 Построение ER-диаграммы**

[ER-диаграмма](diagrams/er/SmartHome_ER.puml)

![ER-диаграмма](diagrams/er/SmartHome_ER.png)

# Задание 1.4: Создание и документирование API

**1.4.1 Выбор типов API**
В системе SmartHome будем использовать комбинированный тип API.
REST API для взаимодействия с пользователем, а Async API для взаимодействия с устройствами.

**1.4.2, 1.4.4 Проектирование API для микросервиса «Управление устройствами»**

**Пользовательский API**

<details open>
  <summary>
    Создание типа устройства
  </summary>

* **Эндпойнт:** /device-types
* **Метод:** POST
* **Описание:** Создаёт тип устройства
* **Формат запроса:**
  * `code`
  * `description`
* **Формат ответа:**
  * `id`
* **Коды ответа:** 200 — успех, 500 — ошибка сервера
* **Примеры запросов и ответов:**

<table>
  <tr>
    <th>Запрос</th>
    <th>Метод</th>
    <th>Тело запроса</th>
    <th>Код ответа</th>
    <th>Тело ответа</th>
  </tr>
  <tr>
    <td>/modules</td>
    <td>POST</td>
    <td>{"code": "heating", "description": "Контроль температуры"}</td>
    <td>200</td>
    <td>{"id": 1}</td>
  </tr>
</table>
</details>

<details open>
  <summary>
    Создание модуля
  </summary>

* **Эндпойнт:** /modules
* **Метод:** POST
* **Описание:** Создаёт модуль
* **Формат запроса:**
  * `house_id`
  * `device_type_id`
  * `serial_number`
  * `title`
* **Формат ответа:**
  * `id`
* **Коды ответа:** 200 — успех, 500 — ошибка сервера
* **Примеры запросов и ответов:**

<table>
  <tr>
    <th>Запрос</th>
    <th>Метод</th>
    <th>Тело запроса</th>
    <th>Код ответа</th>
    <th>Тело ответа</th>
  </tr>
  <tr>
    <td>/modules</td>
    <td>POST</td>
    <td>{"house_id": 1, "device_type_id": 1, "serial_number": "m111", "title": "Модуль отопления"}</td>
    <td>200</td>
    <td>{"id": 1}</td>
  </tr>
</table>
</details>

<details open>
  <summary>
    Создание устройства
  </summary>

* **Эндпойнт:** /devices
* **Метод:** POST
* **Описание:** Создаёт устройство
* **Формат запроса:**
  * `module_id`
  * `serial_number`
* **Формат ответа:**
  * `id`
* **Коды ответа:** 200 — успех, 500 — ошибка сервера
* **Примеры запросов и ответов:**

<table>
  <tr>
    <th>Запрос</th>
    <th>Метод</th>
    <th>Тело запроса</th>
    <th>Код ответа</th>
    <th>Тело ответа</th>
  </tr>
  <tr>
    <td>/devices</td>
    <td>POST</td>
    <td>{"module_id": 1, "serial_number": "d111"}</td>
    <td>200</td>
    <td>{"id": 1}</td>
  </tr>
</table>
</details>

<details open>
  <summary>
    Получение информации об устройстве
  </summary>

* **Эндпойнт:** /device/{device_id}
* **Метод:** GET
* **Описание:** Возвращает подробную информацию о конкретном устройстве по его ID.
* **Формат запроса:** -
* **Формат ответа:**
  * `id`
  * `module_id`
  * `serial_number`
  * `status`
* **Коды ответа:** 200 — успех, 404 — устройство не найдено, 500 — ошибка сервера
* **Примеры запросов и ответов:**

<table>
  <tr>
    <th>Запрос</th>
    <th>Метод</th>
    <th>Тело запроса</th>
    <th>Код ответа</th>
    <th>Тело ответа</th>
  </tr>
  <tr>
    <td>/device/1</td>
    <td>GET</td>
    <td>-</td>
    <td>200</td>
    <td>{"id": 1, "module_id": 1, "serial_number": "111", "status": "off"}</td>
  </tr>
  <tr>
    <td>/device/11111</td>
    <td>GET</td>
    <td>-</td>
    <td>404</td>
    <td>"Устройство не найдено"</td>
  </tr>
  <tr>
    <td>/device/123400000000000000123123123</td>
    <td>GET</td>
    <td>-</td>
    <td>500</td>
    <td>"Ошибка сервера"</td>
  </tr>
</table>
</details>

<details open>
  <summary>
    Обновление состояния устройства
  </summary>

* **Эндпойнт:** /device/{device_id}/status
* **Метод:** PUT
* **Описание:** Обновляет статус устройства
* **Формат запроса:**
  * `status`
* **Формат ответа:** -
* **Коды ответа:** 200 — успех, 404 — устройство не найдено, 500 — ошибка сервера
* **Примеры запросов и ответов:**

<table>
  <tr>
    <th>Запрос</th>
    <th>Метод</th>
    <th>Тело запроса</th>
    <th>Код ответа</th>
    <th>Тело ответа</th>
  </tr>
  <tr>
    <td>/device/1/status</td>
    <td>PUT</td>
    <td>{"status": "on"}</td>
    <td>200</td>
    <td>-</td>
  </tr>
</table>
</details>

<details open>
  <summary>
    Отправка команды устройству
  </summary>

* **Эндпойнт:** /device/{device_id}/commands
* **Метод:** POST
* **Описание:** Отправляет команду устройству
* **Формат запроса:**
  * `command`
* **Формат ответа:** -
* **Коды ответа:** 200 — успех, 404 — устройство не найдено, 500 — ошибка сервера
* **Примеры запросов и ответов:**

<table>
  <tr>
    <th>Запрос</th>
    <th>Метод</th>
    <th>Тело запроса</th>
    <th>Код ответа</th>
    <th>Тело ответа</th>
  </tr>
  <tr>
    <td>/device/1/commands</td>
    <td>PUT</td>
    <td>{"command": "установить температуру 22 градуса"}</td>
    <td>200</td>
    <td>-</td>
  </tr>
</table>
</details>

**API для взаимодействия с устройствами**

<details open>
  <summary>
    Отправка команды устройству
  </summary>

* **Топик:** devices.commands
* **Метод:** Publish
* **Описание:** Отправляет команду устройству
* **Формат сообщения:**
  * `device_id`
  * `command`
* **Примеры сообщений**

<table>
  <tr>
    <th>Топик</th>
    <th>Метод</th>
    <th>Сообщение</th>
  </tr>
  <tr>
    <td>devices.commands</td>
    <td>Publish</td>
    <td>{"device_id": 1, "command": "установить температуру 22 градуса"}</td>
  </tr>
</table>
</details>

**1.4.3, 1.4.4 Проектирование API для микросервиса «Телеметрия»**

**Пользовательский API**

<details open>
  <summary>
    Получение последних данных телеметрии
  </summary>

* **Эндпойнт:** /telemetry/latest?device={device_id}
* **Метод:** GET
* **Описание:** Возвращает последнее полученное значение телеметрии для устройства.
* **Формат запроса:** -
* **Формат ответа:**
  * `id`
  * `device_id`
  * `datetime`
  * `data`
* **Коды ответа:** 200 — успех, 404 — данные не найдены, 500 — ошибка сервера
* **Примеры запросов и ответов:**

<table>
  <tr>
    <th>Запрос</th>
    <th>Метод</th>
    <th>Тело запроса</th>
    <th>Код ответа</th>
    <th>Тело ответа</th>
  </tr>
  <tr>
    <td>/devices/1/telemetry/latest</td>
    <td>GET</td>
    <td>-</td>
    <td>200</td>
    <td>{"id": 1, "device_id": 1, "datetime": 1727210751214, "data": {"temperature": "22C"}}</td>
  </tr>
  <tr>
    <td>/devices/11111telemetry/latest</td>
    <td>GET</td>
    <td>-</td>
    <td>404</td>
    <td>"Устройство не найдено"</td>
  </tr>
</table>
</details>

<details open>
  <summary>
    Получение исторических данных телеметрии
  </summary>

* **Эндпойнт:** /telemetry?device={device_id}&from={from}&until={until}
* **Метод:** GET
* **Описание:** Возвращает исторические данные телеметрии для устройства за определённый период времени.
* **Формат запроса:** -
* **Формат ответа:** список элементов
  * `id`
  * `device_id`
  * `datetime`
  * `data`
* **Коды ответа:** 200 — успех, 500 — ошибка сервера
* **Примеры запросов и ответов:**

<table>
  <tr>
    <th>Запрос</th>
    <th>Метод</th>
    <th>Тело запроса</th>
    <th>Код ответа</th>
    <th>Тело ответа</th>
  </tr>
  <tr>
    <td>/devices/1/telemetry?from=2024-09-23&until=2024-09-25</td>
    <td>GET</td>
    <td>-</td>
    <td>200</td>
    <td>[{"id": 1, "device_id": 1, "datetime": 1727210751214, "data": {"temperature": "22C"}}]</td>
  </tr>
  <tr>
    <td>/devices/11111/telemetry?from=2024-09-23&until=2024-09-25</td>
    <td>GET</td>
    <td>-</td>
    <td>404</td>
    <td>"Устройство не найдено"</td>
  </tr>
</table>
</details>

**API для взаимодействия с устройствами**

<details open>
  <summary>
    Получение телеметрии
  </summary>

* **Топик:** telemetry
* **Метод:** Subscribe
* **Описание:** Получает данные телеметрии
* **Формат сообщения:**
  * `device_id`
  * `data`
* **Примеры сообщений**

<table>
  <tr>
    <th>Топик</th>
    <th>Метод</th>
    <th>Сообщение</th>
  </tr>
  <tr>
    <td>telemetry</td>
    <td>Subscribe</td>
    <td>{"device_id": 1, "data": {"temperature": "22C"}}</td>
  </tr>
</table>
</details>

**1.4.5 Документирование API:**

[Open API](/docs-api/open-api.yaml)

[Async API](/docs-api/async-api.yaml)

# Задание 2 Разработка MVP

Для удобного запуска и демонстрации работы MVP были подготовлены файлы `docker-compose.yaml` и `test.sh`

Чтобы воспользоваться ими, необходимо выполнить простые действия
1. В файле `docker-compose.yaml` у сервисов `telemetry-service` и `device-service` установить переменную окружения `KAFKA: <local ip>:29092`, где `<local ip>` - ip адрес компьютера. localhost и 128.0.0.1 устанавливать нельзя.
2. Выполнить в корне проекта запуск скрипта `./test.sh`

# Задание 2.1 Новые микросервисы и интеграция с монолитом
1. Язык программирования - JS (Node JS)
2. Проекты созданы. Директории telemetry-service и device-service
3. API разработано
4. Логика реализована. (для простоты реализации была использована in memory db)
5. Разработанное API поддерживает интеграцию с монолитом через REST и Kafka
6. Развертывание выполнено в docker-compose

# Задание 2.3 Подготовка 3rd party сервисов для связи микросервисов
1-2. Kafka развёрнута и настроена

3-4. API Gateway Kong развёрнут и настроен

5. Интеграция микросервисов выполнена

6. MVP протестировано. Подготовлен файл. `test.sh`


---