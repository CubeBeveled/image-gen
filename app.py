from flask import Flask, request, send_file, redirect
from endpoints import wanted, welcomecard, sharpen, smooth, enhance, contour, find_edges

fallback_avatar = "https://bevels-files.vercel.app/discordblue.png"
app = Flask(__name__)

@app.route("/welcomecard", methods=["GET"])
def generate_image():
  
  text1 = request.args.get("text1")
  text2 = request.args.get("text2")
  background_url = request.args.get("background")
  avatar_url = request.args.get("avatar")
  
  if text1 == None and text2 == None:
    redirect(f"/welcomecard?background=https://cdn.modrinth.com/data/LMIZZNxZ/images/bd57c68a400e0722bc7132575ea7cec66ca529ab.png&text1=Welcome&text2=John Doe&avatar={fallback_avatar}")
    return
  
  if avatar_url == None:
    avatar_url = fallback_avatar
  
  print(f"Generating welcome card...")
  
  return send_file(welcomecard.generate(text1, text2, background_url, avatar_url, fallback_avatar), mimetype="image/png")

@app.route("/wanted", methods=["GET"])
def generate_wanted():
  
  avatar_url = request.args.get("avatar")
  if avatar_url == None:
    avatar_url = fallback_avatar
  
  print(f"Generating wanted card...")
  
  return send_file(wanted.generate(avatar_url, fallback_avatar), mimetype="image/png")

@app.route("/sharpen", methods=["GET"])
def generate_sharp():
  
  image_url = request.args.get("image")
  cycles = request.args.get("cycles")
  
  if image_url == None:
    return redirect(f"/sharpen?image=https://bevels-files.vercel.app/bsl.png&cycles=1")
  
  if cycles == None:
    return redirect(f"/sharpen?image=https://bevels-files.vercel.app/bsl.png&cycles=1")
  
  print(f"Generating sharpened image ({cycles}x)")
  
  return send_file(sharpen.generate(image_url, cycles), mimetype="image/png")

@app.route("/smooth", methods=["GET"])
def generate_smooth():
  
  image_url = request.args.get("image")
  cycles = request.args.get("cycles")
  
  if image_url == None:
    return redirect(f"/smooth?image=https://bevels-files.vercel.app/bsl.png&cycles=1")
  
  if cycles == None:
    return redirect(f"/smooth?image=https://bevels-files.vercel.app/bsl.png&cycles=1")
  
  print(f"Generating smoothed image ({cycles}x)")
  
  return send_file(smooth.generate(image_url, cycles), mimetype="image/png")

@app.route("/edge_enhance", methods=["GET"])
def generate_enhanced():
  
  image_url = request.args.get("image")
  cycles = request.args.get("cycles")
  
  if image_url == None:
    return redirect(f"/edge_enhance?image=https://bevels-files.vercel.app/bsl.png&cycles=1")
  
  if cycles == None:
    return redirect(f"/edge_enhance?image=https://bevels-files.vercel.app/bsl.png&cycles=1")
  
  print(f"Generating enhanced image ({cycles}x)")
  
  return send_file(enhance.generate(image_url, cycles), mimetype="image/png")

@app.route("/contour", methods=["GET"])
def generate_contour():
  
  image_url = request.args.get("image")
  cycles = request.args.get("cycles")
  
  if image_url == None:
    return redirect(f"/contour?image=https://bevels-files.vercel.app/bsl.png&cycles=1")
  
  if cycles == None:
    return redirect(f"/contour?image=https://bevels-files.vercel.app/bsl.png&cycles=1")
  
  print(f"Generating contoured image ({cycles}x)")
  
  return send_file(contour.generate(image_url, cycles), mimetype="image/png")

@app.route("/find_edges", methods=["GET"])
def generate_edge():
  
  image_url = request.args.get("image")
  cycles = request.args.get("cycles")
  
  if image_url == None:
    return redirect(f"/find_edges?image=https://bevels-files.vercel.app/bsl.png&cycles=1")
  
  if cycles == None:
    return redirect(f"/find_edges?image=https://bevels-files.vercel.app/bsl.png&cycles=1")
  
  print(f"Generating edged image ({cycles}x)")
  
  return send_file(find_edges.generate(image_url, cycles), mimetype="image/png")

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=False, port=25265)