from flask_restful import Api, Resource, reqparse
import pandas as pd
import requests
import io
import os


class DataHandlerFunction(Resource):
    '''
    '''
    def get(self):
        result_status, result_data = CSVReaderToJson()
        return {'resultStatus': result_status, 'resultData': result_data}


def CSVReaderToJson():
    result_status = 'FAILURE'
    result_data = []

    try:

        path_data = os.getcwd()+'/flask_bakcend\core\database_1.csv'
        csv_data = pd.read_csv(path_data, sep=';')
        csv_data.fillna('',inplace=True)

        row_count = csv_data.shape[0]
        column_count = csv_data.shape[1]
        column_names = csv_data.columns.tolist()

        final_row_data = []
        for index, rows in csv_data.iterrows():
            final_row_data.append(rows.to_dict())

        json_result = {'rows': row_count, 'cols': column_count, 'columns': column_names, 'rowData': final_row_data}
        result_data.append(json_result)
        result_status = 'SUCCESS'
    except:
        result_data.append({'message': 'Unable to process the request.'})

    return result_status, result_data
