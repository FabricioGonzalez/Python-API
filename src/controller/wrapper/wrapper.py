from flask import Flask, request, jsonify

app = Flask("HTTP-API")

def agente_de_respostas(dados):
  
  response = Flask.make_response(Flask,dados)

  response.headers['Content-Type'] = 'application/json; charset=utf8'
  
  return response