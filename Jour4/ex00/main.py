from fastapi import Request, FastAPI
from json import JSONDecodeError
# import JSONDecodeError

from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()

@app.get('/ifa')
def univ():
    return {'info': 'TEST'}


@app.get('/ifa/user/{id}')
def getUser(id: int):
    print(f"l'id est le suivant {id}")
    return {'userpage': True}


@app.get('/start')
async def getInfo(request: Request):
    try:
        data = await request.json()
        for i in data:
            print(i)
    except JSONDecodeError:
        return JSONResponse({'error': 'il n y a pas de body'})
    except:
        return JSONResponse({'error': 'interne depuis le serveur'})
    print(f'{data}')
    return JSONResponse({'test': "test"})


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse({"message": "endpoint not found" })

