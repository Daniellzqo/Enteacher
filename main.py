from fastapi import FastAPI, Request
from api import add_list, show_list, edit_list_item
from pages import main_page

app = FastAPI()

app.include_router(main_page.router)
app.include_router(add_list.router)
app.include_router(show_list.router)
app.include_router(edit_list_item.router)


