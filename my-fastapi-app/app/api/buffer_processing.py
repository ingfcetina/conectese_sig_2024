from typing import Dict
import arcpy
import json
import os

def buffer_processing(input_features: Dict, distance: float) -> Dict:
    """
    Realiza el procesamiento de buffer utilizando arcpy.

    Args:
        input_features (Dict): Objeto ESRI JSON que representa las características de entrada.
        distance (float): Distancia de buffer en metros.

    Returns:
        Dict: Objeto ESRI JSON que representa las características de salida.

    Raises:
        Exception: Si ocurre un error al realizar la operación de buffer.
    """
    arcpy.env.overwriteOutput = True
    geodatabse_results = r'C:\conectese_sig\data.gdb'
    folder = r'C:\conectese_sig'
    input_json_file = os.path.join(folder,'input.json')
    output_json_file = os.path.join(folder,'output.json')
    entrada = os.path.join(geodatabse_results,"input_fc")
    output_fc = os.path.join(geodatabse_results,"buffer_fc")

    try:
        with open(input_json_file, 'w') as file:
            json.dump(input_features, file)
        arcpy.AddMessage(f"input_json_file: {input_json_file}")
        arcpy.JSONToFeatures_conversion(input_json_file, entrada)
    except Exception as e:
        raise Exception(f"Error al convertir el archivo JSON a feature class: {str(e)}")
    
    arcpy.AddMessage(f"entrada: {entrada}")
    arcpy.AddMessage(f"output_fc: {output_fc}")
    arcpy.Buffer_analysis(entrada, output_fc, f"{distance} Meters")

    arcpy.FeaturesToJSON_conversion(output_fc, output_json_file)
    with open(output_json_file, 'r') as file:
        output_features = json.load(file)
    return output_features

    '''
    finally:
        # Clean up the temporary JSON file and feature classes
        if os.path.exists(input_json_file):
            os.remove(input_json_file)
            os.remove(output_json_file)
        arcpy.management.Delete(entrada)
        arcpy.management.Delete(output_fc)
    

if __name__ == '__main__':
    arcpy.env.overwriteOutput = True
    # Test the function
    input_features = {
        "features": [{
            "geometry": {
                "x": -74.056342,
                "y": 4.678824,
                "spatialReference": {
                    "wkid": 4326,
                    "latestWkid": 4326
                }
            },
            "attributes": {
                "OBJECTID": 1,
                "NOMBRE": "Esri Colombia Trento"
            }
        }]
    }
    distance = 100
    output_features = buffer_processing(input_features, distance)
    print(output_features)
'''