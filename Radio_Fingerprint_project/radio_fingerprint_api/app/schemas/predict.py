from typing import Any, List, Optional, Union
import datetime

from pydantic import BaseModel


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    #predictions: Optional[List[int]]
    predictions: Optional[int]


class DataInputSchema(BaseModel):
    servingCellID: Optional[int]
    ServingCellRSRP: Optional[int]
    Nbr1CellID: Optional[int]
    Nbr1RSRP: Optional[int]
    Nbr2CellID: Optional[int]
    Nbr2RSRP: Optional[int]
    

class MultipleDataInputs(BaseModel):
    inputs: List[DataInputSchema]
