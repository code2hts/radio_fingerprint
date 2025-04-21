
"""
Note: These tests will fail if you have not first trained the model.
"""

import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

import numpy as np
from radio_fingerprint_model.config.core import config
from radio_fingerprint_model.processing.features import OutlierHandler


def test_sample(sample_input_data):
    # Given
    assert np.size(sample_input_data[0]) == 1548
    assert np.size(sample_input_data[0].columns) == 6
    #assert sample_input_data[0].columns[1] == 'servingCellRSR'
    assert sample_input_data[0]['ServingCellRSRP'].any() < 50

# def test_windspeed_variable_outlierhandler(sample_input_data):
#     # Given
#     encoder = OutlierHandler(variable = config.model_config_.servCellRSRP_var)
#     q1, q3 = np.percentile(sample_input_data[0]['ServingCellRSRP'], q=[25, 75])
#     iqr = q3 - q1
#     #assert sample_input_data[0].loc[2] > q3 + (1.5 * iqr)
#     assert sample_input_data[0]['ServingCellRSRP'].any() > 0
#     # When
#     subject = encoder.fit(sample_input_data[0]).transform(sample_input_data[0])

#     # Then
#     assert subject.loc[1, 'ServingCellRSRP'] <= q3 + (1.5 * iqr)
