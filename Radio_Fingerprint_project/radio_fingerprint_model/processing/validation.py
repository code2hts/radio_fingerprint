import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from typing import List, Optional, Tuple, Union

from datetime import datetime
import numpy as np
import pandas as pd
from pydantic import BaseModel, ValidationError

from radio_fingerprint_model.config.core import config
#from radio_fingerprint_model.processing.data_manager import pre_pipeline_preparation


def validate_inputs(*, input_df: pd.DataFrame) -> Tuple[pd.DataFrame, Optional[dict]]:
    """Check model inputs for unprocessable values."""

    #pre_processed = pre_pipeline_preparation(data_frame = input_df)
    #validated_data = pre_processed[config.model_config_.features].copy()
    errors = None

    try:
        # replace numpy nans so that pydantic can validate
        MultipleDataInputs(
            inputs = input_df.replace({np.nan: None}).to_dict(orient="records")
        )
    except ValidationError as error:
        errors = error.json()

    return input_df, errors


class DataInputSchema(BaseModel):
    servingCellID: Optional[int]
    ServingCellRSRP: Optional[int]
    Nbr1CellID: Optional[int]
    Nbr1RSRP: Optional[int]
    Nbr2CellID: Optional[int]
    Nbr2RSRP: Optional[int]
    

class MultipleDataInputs(BaseModel):
    inputs: List[DataInputSchema]