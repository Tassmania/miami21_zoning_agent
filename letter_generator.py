# 📝 letter_generator.py — Article 7-Style Zoning Compliance Letter

def format_letter(user_question: str, zone: str, zoning_response: str) -> str:
    """
    Formats GPT zoning response into a formal Article 7-style compliance letter.
    """
    return f"""
City of Miami Planning Department
Zoning Compliance Review

Subject: Zoning Inquiry — {zone}

To Whom It May Concern,

This letter addresses the zoning inquiry regarding:
"{user_question.strip()}"

Based on a review of the Miami 21 Zoning Code and applicable zoning regulations for Zone {zone},
the following information applies:

{zoning_response.strip()}

This response is provided based on current code interpretation, including Tables 3, 4, and 13,
as well as supplemental and procedural guidance under Article 7.

Please note: certain uses may still be subject to review by the Planning Director or the Zoning Board,
and additional permits or site plan approvals may be required.

Sincerely,
GPT-Generated Zoning Assistant
For use in compliance pre-screening only.
"""

def generate_compliance_letter(...):
    # implementation here

def get_permission_workflow(...):
    # implementation here
