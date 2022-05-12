from sanic.response import text, html, json
from sanic import Sanic
from models import Students
app = Sanic.get_app("app", force_create=True)


@app.get("/hello")
async def hello(request):
    return text("Hello World!")


@app.get("stu")
async def stu(request):
    stu = await Students.all()
    return json({"stu": [str(stu) for stu in stu]})


@app.get("new_stu")
async def stu(request):
    stu = await Students.create(name="New Student")
    return json({"stu": str(stu)})
