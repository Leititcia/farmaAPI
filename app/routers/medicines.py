from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db

router = APIRouter()

# Rotas Medicines
@router.get("/medicines", response_model=List[schemas.Medicine])
def list_medicines(db: Session = Depends(get_db)):
    medicines = db.query(models.Medicine).all()
    return medicines

@router.get("/medicines/{medicine_id}", response_model=schemas.Medicine)
def get_medicine(medicine_id: int, db: Session = Depends(get_db)):
    medicine = db.query(models.Medicine).filter(models.Medicine.id == medicine_id).first()
    if medicine is None:
        raise HTTPException(status_code=404, detail="Medicamento não encontrado.")
    return medicine

@router.post("/medicines/{medicine_id}", response_model=schemas.Medicine, status_code=status.HTTP_201_CREATED)
def add_medicine(medicine_id: int, medicine: schemas.MedicineCreate, db: Session = Depends(get_db)):
    saved_medicine = db.query(models.Medicine).filter(models.Medicine.id == medicine_id).first()
    if saved_medicine:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Já existe um medicamento com o ID {medicine_id}."
        )

    new_medicine = models.Medicine(id=medicine_id, **medicine.dict())
    db.add(new_medicine)
    db.commit()
    db.refresh(new_medicine)
    return new_medicine


@router.put("/medicines/{medicine_id}", response_model=schemas.Medicine)
def update_medicine(medicine_id: int, updated_medicine: schemas.MedicineCreate, db: Session = Depends(get_db)):
    medicine = db.query(models.Medicine).filter(models.Medicine.id == medicine_id).first()
    if medicine is None:
        raise HTTPException(status_code=404, detail="Medicamento não encontrado.")
    
    for key, value in updated_medicine.dict(exclude_unset=True).items():
        setattr(medicine, key, value)
    db.commit()
    db.refresh(medicine)
    return medicine

@router.delete("/medicines/{medicine_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_medicine(medicine_id: int, db: Session = Depends(get_db)):
    medicine = db.query(models.Medicine).filter(models.Medicine.id == medicine_id).first()
    if medicine is None:
        raise HTTPException(status_code=404, detail="Medicamento não encontrado.")
    db.delete(medicine)
    db.commit()
    return {"message": "Medicamento removido com sucesso."}