
def generate_compliance_letter(address: str, zoning: str, use: str, permission_type: str, summary: str) -> str:
    """
    Generates a formal compliance letter referencing Article 7 procedures based on input.
    """
    letter = f"""
City of Miami Zoning Department
Zoning Compliance Letter

Subject: Land Use Inquiry for {address}

To Whom It May Concern,

This letter serves as a preliminary zoning compliance response regarding the establishment of a "{use}" at the property located at {address}, which falls within zoning designation "{zoning}" per the City of Miami GIS and Miami 21 Zoning Code.

According to Table 3 of Article 4 of the Miami 21 Code, this use is classified under "{use}" and is permitted under this zoning designation via **{permission_type.upper()}**.

Pursuant to Article 7 (Process), an applicant pursuing this use type shall:
- Submit a complete application (Sec. 7.2)
- Follow the review procedure outlined for "{permission_type}" applications (Sec. 7.3)
- Be subject to review by the appropriate decision-making body (Sec. 7.4)

Summary:
{summary}

This letter does not constitute a final determination. For formal approval, submit the required application package via the City's permitting portal or in-person to the Planning & Zoning Department.

Sincerely,
Zoning Officer
City of Miami
"""
    return letter


def get_permission_workflow(permission_type: str) -> str:
    workflows = {
        "BY RIGHT": "No public hearing required. Submit permit application for administrative review.",
        "BY WARRANT": "Requires administrative review and issuance of Warrant by Planning Director.",
        "BY EXCEPTION": "Requires review and approval by Planning & Zoning Board. May involve public hearing.",
        "BY EXCEPTION WITH PUBLIC HEARING": "Full public hearing required by City Commission under Article 7.4."
    }
    return workflows.get(permission_type.upper(), "Review Article 7 for custom processing route.")
