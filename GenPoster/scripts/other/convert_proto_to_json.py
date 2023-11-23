import argparse
import json
from google.transit import gtfs_realtime_pb2

def convert_protobuf_to_json(input_path, output_path):
    try:
        # Crea una instancia de FeedMessage
        feed = gtfs_realtime_pb2.FeedMessage()

        # Lee y carga los datos desde el archivo protobuf de entrada
        with open(input_path, 'rb') as proto_file:
            feed.ParseFromString(proto_file.read())

        # Convierte el objeto FeedMessage a un diccionario JSON
        json_data = {
            "header": {
                "gtfs_realtime_version": feed.header.gtfs_realtime_version,
                "incrementality": feed.header.incrementality,
                "timestamp": feed.header.timestamp,
            },
            "entity": [
                {
                    "id": entity.id,
                    "is_deleted": entity.is_deleted,
                    "trip_update": {
                        "trip": {
                            "trip_id": entity.trip_update.trip.trip_id,
                            "start_date": entity.trip_update.trip.start_date,
                            "route_id": entity.trip_update.trip.route_id,
                        },
                        "stop_time_update": [
                            {
                                "stop_sequence": stop_time.stop_sequence,
                                "arrival": {
                                    "delay": stop_time.arrival.delay,
                                    "time": stop_time.arrival.time,
                                },
                                "departure": {
                                    "delay": stop_time.departure.delay,
                                    "time": stop_time.departure.time,
                                },
                                "stop_id": stop_time.stop_id,
                            }
                            for stop_time in entity.trip_update.stop_time_update
                        ],
                    },
                }
                for entity in feed.entity
            ],
        }

        # Guarda el JSON en el archivo de salida
        with open(output_path, 'w') as json_file:
            json.dump(json_data, json_file, indent=2)

        print(f"Se ha generado el archivo JSON en {output_path}")
    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Convierte un archivo protobuf a JSON.")
    parser.add_argument("--input_file", required=True, help="Ruta al archivo protobuf de entrada.")
    parser.add_argument("--output_file", required=True, help="Ruta al archivo JSON de salida.")
    
    args = parser.parse_args()
    
    convert_protobuf_to_json(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
