from fastapi import FastAPI, Request
from api import add_list
from pages import main_page

app = FastAPI()

app.include_router(main_page.router)
app.include_router(add_list.router)


