from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from database.edit_data_list import insert_list

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/")
def main_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )




