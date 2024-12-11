from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pandas as pd

app = FastAPI()

# Montar la carpeta static para servir archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# Cargar los datos
data = pd.read_csv('chernobyl_data.csv').to_dict(orient='records')

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "data": data})

@app.get("/graph1", response_class=HTMLResponse)
async def graph1(request: Request):
    return templates.TemplateResponse("graph1.html", {"request": request})

@app.get("/graph2", response_class=HTMLResponse)
async def graph2(request: Request):
    return templates.TemplateResponse("graph2.html", {"request": request})

@app.get("/graph3", response_class=HTMLResponse)
async def graph3(request: Request):
    return templates.TemplateResponse("graph3.html", {"request": request})

@app.get("/graph4", response_class=HTMLResponse)
async def graph4(request: Request):
    return templates.TemplateResponse("graph4.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)