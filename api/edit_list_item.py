from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates

from database.show_words import get_word_transl
from database.edit_data_list import update_word, save_word, get_connection
print("SHOW_WORDS ROUTE LOADED")
router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/show_words/{listid}")
def show_words(request: Request, listid: int, lang: str = "en"):

    word = get_word_transl(id)
    word = word[0] if word else None

    return templates.TemplateResponse(
    "show_words.html",
    {
        "request": request,
        "words": words,
        "listid": listid   
    }
)



@router.get("/new_word/{listid}")
def new_word(request: Request, listid: int):

    word = {
        "id": -1,
        "word": "",
        "translation": "",
        "listid": listid
    }

    return templates.TemplateResponse(
        "edit_words.html",
        {
            "request": request,
            "word": word,
            "mode": "new"
        }
    )


@router.get("/edit_words/{id}")
def edit_words(request: Request, id: int, listid: int):

    conn = get_connection()

    row = conn.execute("""
        SELECT id, word
        FROM tbwords
        WHERE id = ?
    """, (id,)).fetchone()

    word = dict(row)

    return templates.TemplateResponse(
        "edit_words.html",
        {
            "request": request,
            "word": word,
            "mode": "edit",
            "listid": listid
        }
    )



@router.post("/api/update_word")
def update_word_route(
    wordid: int = Form(-1),
    word: str = Form(...),
    translation: str = Form(...),
    listid: int = Form(...)
):

    if wordid == -1:
        save_word(listid, word, translation)
    else:
        update_word(wordid, word, translation, listid)

    return {"ok": True}


