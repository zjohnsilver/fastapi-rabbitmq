#!/usr/bin/env python
import pika
from fastapi import FastAPI, Body, HTTPException

app = FastAPI(app="FastAPI and RabbitMQ")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/messages")
async def post_message(message: str = Body(...)):
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="localhost")
        )
        channel = connection.channel()

        channel.exchange_declare(exchange="logs", exchange_type="fanout")

        channel.basic_publish(exchange="logs", routing_key="", body=message)

        connection.close()

        return "Successfully sended message do queue"
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Error when trying to send message to queue",
        )
