from fastapi import FastAPI
from aiokafka import AIOKafkaConsumer
import asyncio
import logging
from config import settings

logging.basicConfig(level=logging.INFO)

async def consume():
    consumer = AIOKafkaConsumer(
        settings.topic,
        bootstrap_servers=settings.kafka_address,
        group_id="device-managment-group",
        auto_offset_reset='earliest',
        enable_auto_commit=False,
    )
    await consumer.start()
    try:
        async for message in consumer:
            # Обработка сообщения
            logging.info(f"Получено сообщение: {message.value.decode('utf-8')}")
            print(f"Получено сообщение: {message.value.decode('utf-8')}")
            await consumer.commit()
    finally:
        await consumer.stop()

