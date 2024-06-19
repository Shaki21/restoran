from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.controller.table import TableController
from app.schemas.table import TableDisplay
from app.core.database import get_db
from app.core.auth import is_admin

router = APIRouter(
    prefix='/tables',
    tags=['tables']
)


@router.post("/")
async def create_table(
        number: int,
        order_id: int,
        db: Session = Depends(get_db),
        current_user: TableDisplay = Depends(is_admin)):
    table_controller = TableController(db)
    return table_controller.create_table(number, order_id)


@router.get("/", response_model=List[TableDisplay])
async def get_all_tables(db: Session = Depends(get_db)):
    table_controller = TableController(db)
    return table_controller.get_all_tables()


@router.get("/{table_id}", response_model=TableDisplay)
async def get_table_by_id(
        table_id: int,
        db: Session = Depends(get_db),
        current_user: TableDisplay = Depends(is_admin)):
    table_controller = TableController(db)
    return table_controller.get_table_by_id(table_id)


@router.put("/{table_id}", response_model=TableDisplay)
async def update_table(
        table_id: int,
        number: int,
        order_id: int,
        db: Session = Depends(get_db),
        current_user: TableDisplay = Depends(is_admin)):
    table_controller = TableController(db)
    return table_controller.update_table(table_id, number, order_id)


@router.delete("/{table_id}")
async def delete_table(
        table_id: int,
        db: Session = Depends(get_db),
        current_user: TableDisplay = Depends(is_admin)):
    table_controller = TableController(db)
    return table_controller.delete_table(table_id)
