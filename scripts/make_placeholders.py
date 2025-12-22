from pathlib import Path
from PIL import Image, ImageDraw

out_dir = Path(__file__).resolve().parent.parent / "graphics"
out_dir.mkdir(parents=True, exist_ok=True)

samples = {
    "pregnancy_risk_image.jpg": "Pregnancy Risk Prediction",
    "fetal_health_image.jpg": "Fetal Health Prediction",
}

for fname, text in samples.items():
    img = Image.new("RGB", (800, 450), color=(240, 245, 252))
    draw = ImageDraw.Draw(img)
    draw.rectangle([20, 20, 780, 430], outline=(70, 120, 200), width=4)
    draw.text((60, 200), text, fill=(30, 60, 120))
    img.save(out_dir / fname, quality=90)

print("Created placeholder images in graphics/")
