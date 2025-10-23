from fastapi import FastAPI, UploadFile
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return{"message": "Welcome to Main page"}

@app.get("/contact")
def read_contact():
    return{"Message": "Welcome to Contact page"}


@app.post("/upload")
def handleImage(files: list[UploadFile]):
    print(files)
    return{"status" : "File received"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
