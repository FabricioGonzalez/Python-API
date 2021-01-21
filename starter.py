from flask import Flask, request
import controller.routes from controller

app = Flask("HTTP-API")


app.run()

