from fastapi import FastAPI, APIRouter
import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv('.env.local')  # Load env variables from .env.local

SUPABASE_URL = os.getenv("EXPO_PUBLIC_SUPABASE_URL")
SUPABASE_KEY = os.getenv("EXPO_PUBLIC_SUPABASE_KEY")


supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


app = FastAPI(debug=True)
router = APIRouter()




@router.get("/payment_info")
async def get_payment_info(payment_id: str):
    
    
    
    return {"payment_id": payment_id, "status": "Processed"}

