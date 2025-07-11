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


# ✅ Step 1: Extract Article 7 (Process) for RAG Ingestion
# This step has been completed separately in `Miami21_RAG_KnowledgeChunks.md`


# ✅ Step 2: Begin Drafting Compliance Letter Generator

def generate_compliance_letter(address: str, zoning: str, use: str, permission_type: str, summary: str) -> str:
    """
    Generates a formal compliance letter referencing Article 7 procedures based on input.
    """
    letter = f"""
City of Miami Zoning Department
Zoning Compliance Letter

Subject: Land Use Inquiry for {address}

To Whom It May Concern,

This letter serves as a preliminary zoning compliance response regarding the establishment of a \"{use}\" at the property located at {address}, which falls within zoning designation \"{zoning}\" per the City of Miami GIS and Miami 21 Zoning Code.

According to Table 3 of Article 4 of the Miami 21 Code, this use is classified under \"{use}\" and is permitted under this zoning designation via **{permission_type.upper()}**.

Pursuant to Article 7 (Process), an applicant pursuing this use type shall:
- Submit a complete application (Sec. 7.2)
- Follow the review procedure outlined for \"{permission_type}\" applications (Sec. 7.3)
- Be subject to review by the appropriate decision-making body (Sec. 7.4)

Summary:
{summary}

This letter does not constitute a final determination. For formal approval, submit the required application package via the City's permitting portal or in-person to the Planning & Zoning Department.

Sincerely,
Zoning Officer
City of Miami
"""
    return letter


# ✅ Step 3: Compliance Logic Tree (Simplified)

def get_permission_workflow(permission_type: str) -> str:
    workflows = {
        "BY RIGHT": "No public hearing required. Submit permit application for administrative review.",
        "BY WARRANT": "Requires administrative review and issuance of Warrant by Planning Director.",
        "BY EXCEPTION": "Requires review and approval by Planning & Zoning Board. May involve public hearing.",
        "BY EXCEPTION WITH PUBLIC HEARING": "Full public hearing required by City Commission under Article 7.4."
    }
    return workflows.get(permission_type.upper(), "Review Article 7 for custom processing route.")
