from fastapi import APIRouter, Body
from pydantic import BaseModel
from .buffer_processing import buffer_processing

router = APIRouter()

class BufferInput(BaseModel):
    input_features: dict
    distance: float

@router.post("/buffer")
def buffer_route(buffer_input: BufferInput = Body(...)):
    """
    Execute buffer geoprocessing using arcpy.
    """
    result = buffer_processing(buffer_input.input_features, buffer_input.distance)
    return {"result": result}