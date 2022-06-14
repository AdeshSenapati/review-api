from fastapi import FastAPI
from fastapi.responses import JSONResponse
import amz_result as ar
import flip_result as fr


app = FastAPI()


x = {
    "name": "Adesh",
    "age": 21,
    "university": "KIIT"
}


@app.get("/")
def home():
    return x


@app.get("/get-amz-results")
def get_amz_results(item: str):
    m = ar.get_results(item)
    headers = {"Access-Control-Allow-Origin": "*", "Access-Control-Allow-Credentials": "true"}
    content = m
    return JSONResponse(content=content, headers=headers, status_code=200)


@app.get("/get-flp-results")
def get_flp_results(item: str):
    m = fr.get_results(item)
    headers = {"Access-Control-Allow-Origin": "*", "Access-Control-Allow-Credentials": "true"}
    content = m
    return JSONResponse(content=content, headers=headers, status_code=200)


# http://localhost:8000 to run
# uvicorn main:app --reload to run webserver
# main is the name of the file that we have to run
# the reload is to automatically reload the webserver on anything changed
