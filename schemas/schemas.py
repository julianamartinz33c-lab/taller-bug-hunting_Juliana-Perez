from pydantic import BaseModel, Field
from typing import Optional, List


class MecanicoCreate(BaseModel):
    nombre_completo: str
    especialidad: str


class MecanicoSimple(BaseModel):  #error 7
    id: int
    nombre_completo: str
    especialidad: str
    activo: bool

    model_config = {"from_attributes": True}


class MecanicoResponse(MecanicoCreate):
    id: int
    activo: bool
    ordenes: List["OrdenResponse"] = []

    model_config = {"from_attributes": True}


class OrdenCreate(BaseModel):
    placa: str = Field(..., min_length=5, max_length=6)
    modelo: str
    falla_reportada: str
    mecanico_id: int


class OrdenPatch(BaseModel):
    estado: Optional[str] = None
    costo_reparacion: Optional[float] = Field(None, ge=0)
    falla_reportada: Optional[str] = None


class OrdenResponse(OrdenCreate):
    id: int
    estado: str
    costo_reparacion: Optional[float] = 0.0  # Error 10
    mecanico: Optional[MecanicoSimple] = None  # Error 7

    model_config = {"from_attributes": True}