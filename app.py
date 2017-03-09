from flask import Flask, jsonify
from flask_restful import Resource, Api
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import issue_warnings

app = Flask(__name__)
api = Api(app)


def station_to_dict(s):
    station_dict = {
        'station_id': s.station_id,
        'measure_id': s.measure_id,
        'name': s.name,
        'coord': s.coord,
        'typical_range': s.typical_range,
        'river': s.river,
        'town': s.town,
        'latest_level': s.latest_level
    }
    return station_dict


def build_station_dict():
    stations = build_station_list()
    update_water_levels(stations)
    # return station_to_dict(stations[0])
    return [station_to_dict(s) for s in stations]


station_dict = build_station_dict()


class Station_json(Resource):
    """Defines a resource to be used with restful, contains stations"""

    def get(self):
        return {'stations': station_dict}


class Station_Risk(Resource):

    def get(self):
        stations = build_station_list()
        update_water_levels(stations)
        risk_list = issue_warnings(stations)
        dictionary = build_station_dict()
        for d in dictionary:
            for s, riskv, risk in risk_list:
                if s.name == d['name']:
                    d['risk'] = risk
                    d['risk_value'] = riskv

        return {'stations': dictionary}

api.add_resource(Station_json, '/floodwarning/stationlist')
api.add_resource(Station_Risk, '/floodwarning/risks')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
