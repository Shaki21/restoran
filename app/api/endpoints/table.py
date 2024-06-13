from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.controller.table import TableController
from app.schemas.table import TableCreate, TableDisplay, TableDelete
from app.core.database import get_db

router = APIRouter(
    prefix='/tables',
    tags=['tables']
)


@router.post("/", response_model=TableDisplay)
async def create_table(request: TableCreate, db: Session = Depends(get_db)):
    return TableController(db=db).create_table(request=request)


@router.get("/{id}", response_model=TableDisplay)
async def get_table(id: int, db: Session = Depends(get_db)):
    return TableController(db=db).get_table_by_id(id=id)


@router.get("/", response_model=list[TableDisplay])
async def get_tables(db: Session = Depends(get_db)):
    return TableController(db=db).get_all_tables()


@router.delete("/{id}", response_model=TableDelete)
async def delete_table(id: int, db: Session = Depends(get_db)):
    return TableController(db=db).delete_table(id=id)