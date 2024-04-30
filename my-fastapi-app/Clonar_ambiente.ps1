# Clonar el ambiente base de conda
conda create --name geoprocesamiento --clone arcgispro-py3

# Activar el nuevo ambiente
conda activate geoprocesamiento

# Instalar las dependencias requeridas
conda install -c conda-forge fastapi
conda install -c conda-forge uvicorn
conda install -c conda-forge python-multiparty
