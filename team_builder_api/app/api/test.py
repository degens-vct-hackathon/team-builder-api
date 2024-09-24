from fastapi import APIRouter
router = APIRouter()

@router.get("/test/")
async def get_orders():
    return {"orders": ["order1", "order2"]}

@router.post("/test/")
async def create_order(order: str):
    return {"message": f"Order {order} created!"}