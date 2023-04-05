from fastapi import FastAPI

router = FastAPI()

@router.get('/')
def root():
    return {"message": "sagar"}

@router.post('/')
def post_method():
    return {"data":"tomar"}

@router.put('/{id}')
def update():
    return {"message":"bind mount works!!! sort of 123456789944545"}
