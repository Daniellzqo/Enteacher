from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from database.show_data import get_lists
from database.show_words import get_words

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/show_list")
def show_page(request: Request):
     
    lists = get_lists()
    
    return templates.TemplateResponse(
    request=request,
    name="show_list.html",
    context={
        "lists": lists
    }
)

@router.get("/show_words/{id}")
def show_words(request: Request, id: int):

    words = get_words(id)

    return templates.TemplateResponse(
    request=request,
    name="show_words.html",
    context={
        "words": words
    }
)




