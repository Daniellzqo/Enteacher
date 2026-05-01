from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates


router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/show_list")
def show_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="show_list.html",
        context={}
    )




