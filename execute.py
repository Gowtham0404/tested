import papermill as pm
from config import params  # Import parameters from the config file


pm.execute_notebook(
    input_path='script.ipynb',
    output_path='output_notebook.ipynb',
    parameters=params,
    log_output=True
)