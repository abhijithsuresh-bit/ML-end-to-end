from fastapi import FastAPI , Form , Request
import numpy as np
import pickle
import uvicorn
from pydantic import BaseModel
from House_Price import HousePrice

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
model  = pickle.load(open('model.pkl', 'rb'))
scalar = pickle.load(open('scaler.pkl', 'rb'))
templates = Jinja2Templates(directory="templates")


@app.get('/{name}' , response_class=HTMLResponse)
def home(request: Request , name):
    return templates.TemplateResponse("index.html", {"request": request , 'name': name})

@app.post('/predict_API') # testing our model using API /docs in url
def predict_price(data: HousePrice):
    data = data.dict()
    features = list(data.values())
    
    values = np.array(features).reshape(1, -1)
    final_features = scalar.transform(values)
    prediction = model.predict(final_features)
    return {"predicted_price": float(prediction[0])} # fastapi cannot return numpy data types so we convert to float


@app.post('/predict_form' , response_class=HTMLResponse)
def predict_price_form(request: Request,
                       CRIM = Form(...),
                        ZN = Form(...),
                        INDUS = Form(...), 
                        CHAS = Form(...), 
                        NOX = Form(...), 
                        RM = Form(...), 
                        AGE = Form(...),
                        DIS = Form(...), 
                        RAD = Form(...), 
                        TAX = Form(...), 
                        PTRATIO = Form(...), 
                        B = Form(...), 
                        LSTAT = Form(...)):  
    features = [CRIM , ZN , INDUS , CHAS , NOX , RM , AGE , DIS , RAD , TAX , PTRATIO , B , LSTAT]
    values = np.array(features).reshape(1, -1)
    final_features = scalar.transform(values)
    prediction = model.predict(final_features)

    return templates.TemplateResponse("index.html", {"request": request , 'predicted_price': float(prediction[0])})
                