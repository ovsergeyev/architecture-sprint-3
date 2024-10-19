from fastapi import FastAPI
from aiokafka import AIOKafkaConsumer
import asyncio
import logging
from config import settings

config = settings.config

KAFKA_BROKER = 'localhost:9092'  # Укажите ваш брокер
TOPIC_NAME = 'your_topic'  # Укажите имя вашего топика

async def consume():
    consumer = AIOKafkaConsumer(
        config.topic,
        bootstrap_servers=config.kafka_address,
        auto_offset_reset='earliest',
        enable_auto_commit=True,
    )
    await consumer.start()
    try:
        async for message in consumer:
            # Обработка сообщения
            print(f"Получено сообщение: {message.value.decode('utf-8')}")
    finally:
        await consumer.stop()

