# 🌐 zone_lookup.py — Get Zoning Code by Address (Miami-Dade County GIS)

import requests
import urllib.parse
import json

# Miami-Dade GIS zoning layer (Property Search service - Layer 50)
ZONING_API_URL = "https://maps.miamidade.gov/arcgis/rest/services/PropertySearch/MapServer/50/query"
GEOCODE_API_URL = "https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/findAddressCandidates"


def get_zone_by_address(address: str) -> str:
    """Returns the zoning code (e.g., T3-R) for a given Miami address using ArcGIS Geocoding and Miami-Dade GIS."""
    try:
        # Step 1: Geocode the address using ArcGIS
        geo_params = {
            "f": "json",
            "singleLine": address,
            "outFields": "Match_addr,Addr_type,location"
        }
        geo_response = requests.get(GEOCODE_API_URL, params=geo_params)
        print("🌐 ArcGIS Geocoder status:", geo_response.status_code)
        print("📦 ArcGIS Geocoder response:", geo_response.text)

        geo_data = geo_response.json()
        candidates = geo_data.get("candidates", [])
        if not candidates:
            print("❌ No geocode candidates found.")
            return ""

        top_candidate = candidates[0]
        location = top_candidate.get("location")
        if not location:
            print("❌ No location in top candidate.")
            return ""

        lon = location["x"]
        lat = location["y"]

        # Step 2: Query the Miami-Dade GIS zoning API
        zoning_payload = {
            "f": "json",
            "geometry": json.dumps({"x": lon, "y": lat}),
            "geometryType": "esriGeometryPoint",
            "inSR": 4326,
            "spatialRel": "esriSpatialRelIntersects",
            "outFields": "ZONING",
            "returnGeometry": False,
            "outSR": 4326
    }

        zoning_response = requests.get(ZONING_API_URL, params=zoning_payload)
        print("🏙️ Miami-Dade GIS status:", zoning_response.status_code)
        print("📄 Miami-Dade GIS response:", zoning_response.text)

        if zoning_response.status_code != 200 or not zoning_response.text.strip():
            print("⚠️ Empty or invalid zoning response")
            return ""

        zoning_data = zoning_response.json()
        features = zoning_data.get("features", [])
        if features:
            return features[0]['attributes'].get("ZONING", "")

        return ""

    except Exception as e:
        print("❌ Zone lookup failed:", e)
        return ""
