import cv2
from fastapi import FastAPI , HTTPException , status
from fastapi.responses import StreamingResponse 
import io

app=FastAPI()

@app.get("/")
def read_root():
    return "هفت‌سین سفره‌ای متشکل از هفت چیزِ نمادین است که از طبیعت گرفته شده و نام آن‌ها با حرف «سین» آغاز می‌شود و به‌طور سنتی در نوروز، سال نوی ایرانی، گسترانده می‌شود. هفت‌سین از مشهورترین مراسم نوروز است که روی زمین یا میز گذاشته می‌شود و معمولاً اعضای خانواده در زمان گردش سال، در کنار آن می‌نشینند. این سفره از گردهم آوردن و انتخابِ هفت چیز از موارد مقابل است: سیب، سنجد، سماق، سیر، سرکه، سبزه سمنو."

@app.get("/sins")
def sins_name():
    return "sib, senjed, somagh, sir, serke, sabze, samanoo and seke!"
   
@app.get("/sins/{sin_name}")
def sins_description(sin_name:str):
     if sin_name == "sib" :
            return " سیب را نماد زیبایی و تندرستی می‌دانند و ایرانیان برای حفظ سلامتی افراد خانه آن را در کنار سایر نمادهای سفره هفتسین قرار می‌دهند."
     if sin_name == "senjed" :
            return " سنجد در خوان نوروزی نشاندهنده مهر و عشق و نمادی از زایندگی و دلباختگی است."
     if sin_name == "somagh":
            return "سماق نماد مهر و پیوند دلها است و برای عشق بیشتر در میان افراد خانواده بر سفره هفتسین این قرار می‌گیرد."
     if sin_name == "sir" :
            return "سیر را برای پاکیزگی، میکروب زدایی و حفظ سلامت بدن و همینطور از بین بردن چشم زخم در سفره هفت سین قرار می‌دهند."
     if sin_name == "serke" :
            return "سرکه نماد جاودانگی است. در گذشته از سرکه برای باطل کردن سحر و جادو استفاده می شده است. قرار گرفتن این نماد بر روی سفره هفت سین سبب خواهد شد تا ناملایمات سال نو از بین برود."
     if sin_name == "sabzeh" :
            return " سبزه نماد و نشانه‌ای از سبزی و شادابی و پیوند انسان با طبیعت است."
     if sin_name == "samanoo" :
            return "سمنو سَمبل خیر و برکت است. ایرانیان چند روز پیش از شروع سال جدید این ماده را از پخت جوانه های گندم تهیه می کنند و معتقدند که قرار گیری آن بر روی سفره هفت سین، سبب افزونی نعمت و برکت در زندگی آن ها خواهد شد."
     if sin_name == "seke" :
            return " سکه نماد ثروت و برکت، سیر نماد سلامتی و درمان و سنبل نماد شکوفایی و رشد است."
     else:
       raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="دقت کن فرزندم اینکه وارد کردی سین نیس که!")


@app.get("/sins/{sin_name}/image")
def sins_images(sin_name:str):
     if sin_name == "sib"  :
            image = cv2.imread(r".\images\sib.png")      
            _, encode_image = cv2.imencode(".png",image)
            return StreamingResponse(content=io.BytesIO(encode_image.tobytes()), media_type = "image/png")
     if sin_name == "senjed" :
            image = cv2.imread(r".\images\senjed.png")      
            _, encode_image = cv2.imencode(".png",image)
            return StreamingResponse(content=io.BytesIO(encode_image.tobytes()), media_type = "image/png")     
     if sin_name == "somagh" :
            image = cv2.imread(r".\images\somagh.png")      
            _, encode_image = cv2.imencode(".png",image)
            return StreamingResponse(content=io.BytesIO(encode_image.tobytes()), media_type = "image/png")     
     if sin_name == "sir" :
            image = cv2.imread(r".\images\sir.png")      
            _, encode_image = cv2.imencode(".png",image)
            return StreamingResponse(content=io.BytesIO(encode_image.tobytes()), media_type = "image/png")     
     if sin_name == "serke" :
            image = cv2.imread(r".\images\serke.png")      
            _, encode_image = cv2.imencode(".png",image)
            return StreamingResponse(content=io.BytesIO(encode_image.tobytes()), media_type = "image/png")     
     if sin_name == "sabzeh" :
            image = cv2.imread(r".\images\sabze.png")      
            _, encode_image = cv2.imencode(".png",image)
            return StreamingResponse(content=io.BytesIO(encode_image.tobytes()), media_type = "image/png")     
     if sin_name == "samanoo" :
            image = cv2.imread(r".\images\samanoo.png")      
            _, encode_image = cv2.imencode(".png",image)
            return StreamingResponse(content=io.BytesIO(encode_image.tobytes()), media_type = "image/png") 
     if sin_name == "seke" :
            image = cv2.imread(r".\images\seke.png")      
            _, encode_image = cv2.imencode(".png",image)
            return StreamingResponse(content=io.BytesIO(encode_image.tobytes()), media_type = "image/png")     
     else:
       raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="نداریم که!")