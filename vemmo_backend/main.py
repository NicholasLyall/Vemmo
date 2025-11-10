from fastapi import FastAPI, APIRouter

app = FastAPI(debug=True)
router = APIRouter()




@router.get("/payment_info")
async def get_payment_info(payment_id: str):
    return {"payment_id": payment_id, "status": "Processed"}

