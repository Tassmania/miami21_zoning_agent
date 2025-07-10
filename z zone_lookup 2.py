# 🌐 zone_lookup.py — Get Zoning Code by Address (Miami GIS API)

import requests
import urllib.parse

API_URL = "https://gis.miamigov.com/arcgis/rest/services/Hosted/Zoning/FeatureServer/0/query"

def get_zone_by_address(address: str) -> str:
    """Returns the zoning code (e.g., T4-R) for a given Miami address."""
    try:
        encoded = urllib.parse.quote(address)
        url = f"https://nominatim.openstreetmap.org/search?q={encoded}&format=json&limit=1"

        print(f"🔎 Calling Nominatim with: {url}")
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        print("🌐 Response status:", response.status_code)
        print("📦 Raw response:", response.text)

        loc_data = response.json()

        if not loc_data:
            return ""

        lat = loc_data[0]['lat']
        lon = loc_data[0]['lon']

        payload = {
            "f": "json",
            "geometry": f"{{\"x\":{lon},\"y\":{lat}}}",
            "geometryType": "esriGeometryPoint",
            "inSR": 4326,
            "spatialRel": "esriSpatialRelIntersects",
            "outFields": "Zoning",
            "returnGeometry": False
        }

        zoning_resp = requests.get(API_URL, params=payload).json()
        features = zoning_resp.get("features", [])

        if features:
            return features[0]['attributes'].get("Zoning", "")
        return ""

    except Exception as e:
        print("❌ Zone lookup failed:", e)
        return ""
