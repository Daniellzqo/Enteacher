from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from database.edit_data_list import insert_list

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/add_list")
def edit_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="add_list.html",
        context={}
    )

@router.post("/api/save_list")
def save_list(
    listname: str = Form(...),
    worden: str = Form(...),
    wordpl: str = Form(...),
):

    list_id = insert_list(listname, worden, wordpl)
    return {
        "listname": listname,
        "worden": worden,
        "wordpl": wordpl,
        "list_id": list_id
    }


