from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import cv2
import numpy as np
import base64
from skimage.exposure import match_histograms

app = FastAPI()

def goruntu_isleme(img1_bytes, img2_bytes):
    
    img1 = cv2.imdecode(np.frombuffer(img1_bytes, np.uint8), cv2.IMREAD_COLOR)
    img2 = cv2.imdecode(np.frombuffer(img2_bytes, np.uint8), cv2.IMREAD_COLOR)

   
    matched = match_histograms(img2, img1, channel_axis=-1)

    _, thresh1 = cv2.threshold(img1, 110, 255, cv2.THRESH_BINARY)
    _, thresh2 = cv2.threshold(matched, 110, 255, cv2.THRESH_BINARY)

    blur1 = cv2.GaussianBlur(thresh1, (3, 3), 0)
    blur2 = cv2.GaussianBlur(thresh2, (3, 3), 0)

    diff_edges = cv2.absdiff(blur1, blur2)

    _, thresh = cv2.threshold(diff_edges, 100, 255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    heat = cv2.applyColorMap(diff_edges, cv2.COLORMAP_JET)
    heat_rgb = cv2.cvtColor(heat, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(heat_rgb, cv2.COLOR_RGB2GRAY)
      
    

    return heat_rgb, img_gray

def encode_image(image: np.ndarray) -> str:
    _, buffer = cv2.imencode(".png", image)
    return base64.b64encode(buffer).decode("utf-8")

@app.post("/detect")
async def detect(pre: UploadFile = File(...), post: UploadFile = File(...)):
    print(" API çağrıldı")

    pre_bytes = await pre.read()
    post_bytes = await post.read()

    print(" Görseller alındı")

    heat_rgb, img_gray = goruntu_isleme(pre_bytes, post_bytes)

    print(" Görüntü işleme tamamlandı")

    heat_encoded = encode_image(heat_rgb)
    gray_encoded = encode_image(img_gray)

    print("Base64 dönüşümü tamamlandı")

    return {
        "heatmap": heat_encoded,
        "graymap": gray_encoded
    }
