from fastapi import Request, Response, FastAPI, status
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

import writer

myapp = FastAPI()


@myapp.get('/ifa/user/{id}', status_code=200)
async def getUser(id: str, request: Request, response: Response):
    tmp = writer.Writer()
    tmp_file = ""
    try:
        tmp_file = tmp.readerStr(id, 'r')
    except AssertionError:
        response.status_code = 400
        return JSONResponse({'error': 'le fichier n existe pas'})
    except:
        return JSONResponse({'error': 'error intern'})
    return JSONResponse({'text': tmp_file})


@myapp.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    # print(await request.json(), exc.status_code)
    return JSONResponse({"message": "endpoint not found" })


# tasks = {"foo": "Listen to the Bar Fighters"}
#
#
# @myapp.put("/get-or-create-task/{task_id}", status_code=200)
# def get_or_create_task(task_id: str, response: Response):
#     if task_id not in tasks:
#         tasks[task_id] = "This didn't exist before"
#         response.status_code = status.HTTP_201_CREATED
#     return tasks[task_id]
