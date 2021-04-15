from fastapi import Request, Response, FastAPI, status
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from json import JSONDecodeError

import writer
import generator
import subprocess

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



@myapp.post('/ifa/start')
async def startScripts(request: Request):
    try:
        body = await request.json()
        nameScript = 'nameScript'
        paramsScript = "params"

        for key, value in body.items():
            if nameScript == key:
                if not isinstance(value, str):
                    return JSONResponse({'error': 'Le nom du script ne peut pas être un nombre il faut que se soit une string'})
                if not len(value):
                    return JSONResponse({'error': 'Le nom du script ne peut pas être vide'})
            if paramsScript == key:
                if not isinstance(value, dict):
                    return JSONResponse({'error': 'Les params doivent être un dict'})
                if not len(value):
                    return JSONResponse({'error': 'Les params du dict ne peuvent pas être vides'})
                for pKey, pValue in value.items():
                    if not isinstance(pValue, int):
                        return JSONResponse({'error': 'les params doivent être des nombres / chiffres'})
        params = {'min': 0, 'max': 0, 'lenght': 0}
        for key, value in body[paramsScript].items():
            print(value)
            if key == 'nbMini':
                params['min'] = value
            if key == 'nbMax':
                params['max'] = value
            if key == 'lenght':
                params['lenght'] = value
        scriptInfo = f"{body[nameScript]} {params['min']} {params['max']} {params['lenght']}"
        returnValue = subprocess.call(f"python3 {scriptInfo}", shell=True)

        if returnValue != 0:
            return JSONResponse({'error': "Il y a un problème avec le script, peut être le nom ou trop ou pas assez d'argument"})

        reader = writer.Writer()
        fileGenerated = reader.readerStr('nb.txt', 'r')

        for pos, nb in enumerate(fileGenerated):
            fileGenerated[pos] = int(nb.rstrip())

        return JSONResponse({'datas': fileGenerated})

    except JSONDecodeError:
        return JSONResponse({'error': 'il n y a pas de body pour executer le / les scripts'})
    except:
        return JSONResponse({'error': 'problème interne'})
    return JSONResponse({'test': 'nous sommes dans les scripts'})



@myapp.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
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
