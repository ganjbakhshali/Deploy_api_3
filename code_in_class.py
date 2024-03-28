import cv2
import numpy as np
from typing import Union
from fastapi import FastAPI, HTTPException,status
import io
from fastapi.responses import StreamingResponse

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/channel/{item}")
def test(item:Union[str,int]):
    return {"shabake":item}

@app.get("/create-img/{red}/{green}/{blue}")
def createIMG(red:int,green:int,blue:int):
    if(0<=red<=255 and 0<=green<=255 and 0<=blue<=255):
        img=np.zeros((300,200,3),dtype=np.uint8)
        img[:,:]=(red,green,blue)
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        # cv2.imwrite("test.jpg",img)
        _ , img_encode = cv2.imencode(".png",img)
        return StreamingResponse(io.BytesIO(img_encode.tobytes()), media_type="image/png")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="ridi!")
        
    
        
        
        
        
    
    return