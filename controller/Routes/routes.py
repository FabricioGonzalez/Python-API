from controller.wrapper import app

@app.route("/",methods=["GET"])
def ola():
  return "Olá"