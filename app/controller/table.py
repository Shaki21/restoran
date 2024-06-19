from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.model.table import Table


class TableController:
    def __init__(self, db: Session):
        self.db = db

    def create_table(self, number: int, order_id: int):
        try:
            new_table = Table(
                number=number,
                order_id=order_id
            )

            self.db.add(new_table)
            self.db.commit()
            self.db.refresh(new_table)
            return new_table
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    def get_table_by_id(self, id: int):
        table = self.db.query(Table).filter(Table.id == id).first()
        if not table:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'Table with id {id} not found!')
        return table

    def get_all_tables(self):
        tables = self.db.query(Table).all()
        return tables

    def update_table(self, id: int, number: int, order_id: int):
        table = self.db.query(Table).filter(Table.id == id).first()
        if not table:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'Table with id {id} not found!')
        table.number = number
        table.order_id = order_id
        self.db.commit()
        self.db.refresh(table)
        return table

    def delete_table(self, id: int):
        table = self.db.query(Table).filter(Table.id == id).first()
        if not table:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'Table with id {id} not found!')
        self.db.delete(table)
        self.db.commit()
        return {"detail": 'table deleted!'}
