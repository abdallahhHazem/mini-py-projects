import numpy as np
from flask import Flask, render_template, request
from PIL import Image
import io
import matplotlib.colors as mcolors

app = Flask(__name__)

def get_top_colors(image, n_colors=10):
    # Convert image to RGB
    img = image.convert("RGB")
    img_array = np.array(img)

    # Flatten to list of pixels
    pixels = img_array.reshape(-1, 3)

    # Count unique colors
    colors, counts = np.unique(pixels, axis=0, return_counts=True)

    # Sort by frequency
    sorted_idx = np.argsort(-counts)
    top_colors = colors[sorted_idx][:n_colors]

    # Convert to HEX
    hex_colors = [mcolors.to_hex(c/255) for c in top_colors]
    return hex_colors

@app.route("/", methods=["GET", "POST"])
def index():
    colors = []
    if request.method == "POST":
        file = request.files["image"]
        if file:
            image = Image.open(io.BytesIO(file.read()))
            colors = get_top_colors(image)
    return render_template("index.html", colors=colors)

if __name__ == "__main__":
    app.run(debug=True)
