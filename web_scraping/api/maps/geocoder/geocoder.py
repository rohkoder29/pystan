import requests
import json
import time
from pathlib import Path


class ReverseGeocoder:
    base_url = "https://nominatim.openstreetmap.org/reverse"
    input_folder = Path("input_data")
    input_file = input_folder / "coordinates.txt"
    output_folder = Path("output_data")
    output_file = output_folder / "reverse_results.json"

    results = []

    def fetch(self, lat, lon):
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
        }
        params = {"format": "geocodejson", "lat": lat, "lon": lon}
        res = requests.get(url=self.base_url, params=params, headers=headers)
        print(
            "HTTP GET request to URL: %s | Status code: %s"
            % (res.url, res.status_code)
        )
        return res if res.status_code == 200 else None

    def parse(self, res, lat, lon):
        data = res["features"][0]["properties"]["geocoding"]
        data["lat"] = lat
        data["lon"] = lon
        self.results.append(data)

    def store_results(self):
        with open(self.output_file, "w") as f:
            f.write(json.dumps(self.results, indent=2))

    def run(self):
        content = ""
        # load coordinates

        # open source coordinates
        with open(self.input_file, "r") as f:
            for line in f.read():
                content += line

        # create coordinates list
        coordinates = content.split("\n")

        # loop over coordinates
        for coordinate in coordinates:
            # extract coordinates
            lon = coordinate.split(",")[0].strip()
            lat = coordinate.split(",")[1].strip()
            # make HTTP req to Nominatim API
            res = self.fetch(lat, lon)
            self.parse(res.json(), lat, lon)
            # respect crawling policies
            time.sleep(1)

        # store results
        self.store_results()


class ForwardGeocoder:
    base_url = "https://nominatim.openstreetmap.org/search"
    input_folder = Path("input_data")
    input_file = input_folder / "addresses.txt"
    output_folder = Path("output_data")
    output_file = output_folder / "forward_results.json"

    results = []

    def fetch(self, address):
        params = {"q": address, "format": "geocodejson"}

        res = requests.get(url=self.base_url, params=params)
        print(
            "HTTP GET request to URL %s | Status code: %s"
            % (res.url, res.status_code)
        )
        return res if res.status_code == 200 else None

    def parse(self, res, address):
        properties = res["features"][0]["properties"]
        geometry = res["features"][0]["geometry"]
        self.results.append(
            {
                "requested data": address,
                "properties": properties,
                "geometry": geometry,
            }
        )

    def store_results(self):
        with open(self.output_file, "w") as f:
            f.write(json.dumps(self.results, indent=2))

    def run(self):
        addresses = ""
        # fetch addresses from file
        with open(self.input_file, "r") as f:
            for line in f.read():
                addresses += line
        # convert addresses to list
        addresses = addresses.split("\n")

        for address in addresses:
            response = self.fetch(address).json()
            self.parse(response, address)
            # respect nominatim crawling policies
            time.sleep(2)

        self.store_results()


if __name__ == "__main__":
    forwardGeocoder = ForwardGeocoder()
    reverseGeocoder = ReverseGeocoder()
    reverseGeocoder.run()
    forwardGeocoder.run()
