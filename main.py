import joblib
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sklearn.preprocessing import StandardScaler

app = FastAPI()
templates = Jinja2Templates(directory="templates")

transModel = joblib.load(r"transformModel.pkl")
logistic_model = joblib.load(r'logistic.pkl')

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request, 'isShow': 'False', 'error': ''})

@app.post("/submit", response_class=HTMLResponse)
async def return_form(request: Request, email_content: str = Form(...)):
    if not email_content.strip():
        return templates.TemplateResponse("form.html", {"request": request, "isShow": "False", "error": "Email content cannot be empty"})
    
    transformed_input = transModel.transform([email_content])
    predicted = logistic_model.predict(transformed_input)
    if predicted[0] == 0:
        predicted = "Ham"
    else:
        predicted = 'Spam'
    
    return templates.TemplateResponse("form.html", {"request": request, "predicted": predicted, 'isShow': 'True', 'error': ''})
