from fastapi import FastAPI


app = FastAPI(title="活动报名 API 入门")


@app.get("/")
def home():
    return {"message": "活动报名服务器已经启动"}
