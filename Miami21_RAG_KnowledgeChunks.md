
# Miami 21 Zoning Code - RAG Knowledge Chunks

---

## Article 1: Definitions
(Definitions content goes here...)

---

## Article 4: Table 3 - Allowed Uses by Transect Zone
(Structured table of use categories, zoning codes, and permissions R/W/E for each transect...)

---

## Table 4: Density, Intensity, and Parking Standards
(Complete breakdown for T3, T4, T5, T6, C, D including parking ratios, intensity max, etc.)

---

## Table 13: Use-Specific Regulations by Zone
- T3: Density (UPA), Use Type (e.g. DWELLING UNIT), Accessory Dwelling Units (ADUs) by right or exception
- T4, T5, T6, C, D: Corresponding permitted and restricted uses with public hearing thresholds

Includes fuzzy matched crosswalk between Table 3 categories and Table 13 variations (e.g., "Adult Daycare" vs "ADULT DAY CARE").

---

## Article 6: Supplemental Regulations
- Sec 6.1 through 6.10 summarized for key use-specific siting requirements (e.g., minimum lot area, setbacks, design compatibility)
- Cross-referenced with Table 3 "Community Support Facility" and Article 1 definitions

---

## Article 7: Process
### 7.1 General Provisions
- Describes permit obligations for By-Right, By Warrant, and By Exception

### 7.2 Application Submittal
- Requires full plans, narrative, site context, justification
- Special uses must cite compatibility justification

### 7.3 Review Procedures
- Staff review → Director review → Zoning Board → City Commission (in escalating order)

### 7.4 Review Authorities
- Outlines decision-making body by permit type

### 7.5 Timeframes
- By Warrant ≈ 30–60 days, By Exception ≈ 90–120 days
- Public hearing timelines and re-notification protocol

---

## Quick Reference Permission Matrix

| Zoning Use Type            | Permission Type | Article Reference | Review Body                |
|----------------------------|------------------|--------------------|----------------------------|
| Home Office                | By Right         | Art. 4 Table 3     | Administrative             |
| Community Support Facility| By Warrant       | Art. 4 + Art. 6    | Planning Director          |
| Adult Daycare             | By Exception     | Art. 6 + Table 13  | Planning & Zoning Board    |

---

## Compliance Letter Logic Summary

When responding to a zoning inquiry, check:
1. Address → Zone (via zone_lookup.py)
2. Zone + Use → Match in Table 3
3. Cross-check Table 13 and Article 6 for limitations
4. Determine if R / W / E permission applies
5. If E or W, generate response referencing Article 7 permit procedure
