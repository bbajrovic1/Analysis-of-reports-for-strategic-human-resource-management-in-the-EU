import os
import re
from collections import defaultdict, Counter
from PyPDF2 import PdfReader
import pandas as pd

# set folder to location where the pdf files are
pdf_folder = "reports"

# set name for excel file
output_excel = "data/keyword_frequencies.xlsx"

# define keyword phrases to analyze
phrase_variants = {
    "human resource(s)": [
        "human resource"
    ],
    "human resource(s) management": [
        "human resource management",
        "human resources management"
    ],
    "poor human resource(s) management": [
        "poor human resource management",
        "poor human resources management"
    ],
    "monitoring human resource(s)": [
        "monitoring human resource"
    ],
    "very limited human resource(s)": [
        "very limited human resource"
    ],
    "human resource(s) management information system(s)": [
        "human resource management information system",
        "human resources management information system"
    ],
    
    # One-to-one mappings for non-variable phrases
    "training": ["training"],
    "staffing": ["staffing"],
    "skills": ["skills"],
    "lack of skills": ["lack of skills"],
    "civil servants": ["civil servants"],
    "strategic planning": ["strategic planning"],
    "monitoring implementation": ["monitoring implementation"],
    "effective management": ["effective management"],
    "limited understanding": ["limited understanding"],
    "effectiveness of governance": ["effectiveness of governance"],
    "effective use of pre-accession funds": ["effective use of pre-accession funds"],
    "ineffective": ["ineffective"],
    "ineffective use of pre-accession funds": ["ineffective use of pre-accession funds"],
    "HRMIS": ["HRMIS"],
    "data on HRM": ["data on HRM"],
    "need to strengthen capacity": ["need to strengthen capacity"],
    "improving capacity": ["improving capacity", "improving capacities"],
    "increase capacity": ["increase capacity", "increase capacities"],
    "lack of capacity": ["lack of capacity", "lack of capacities"],
    "little capacity": ["little capacity", "little capacities"],
    "needs more capacity": ["needs more capacity", "needs more capacities"],
    "insufficient capacity": ["insufficient capacity", "insufficient capacities"],
    "institutional capacity": ["institutional capacity", "institutional capacities"],
    "management capacity": ["management capacity", "management capacities"],
    "competencies": ["competencies", "competency"],
    "administrative capacities": ["administrative capacities", "administrative capacity"],
    "knowledge": ["knowledge"],
    "better training": ["better training"],
    "insufficient training": ["insufficient training"],
    "better training civil servants": ["better training civil servants"],
    "public administration reform": ["public administration reform"]
}



# counter initialization
total_counts = Counter()
yearly_counts = defaultdict(lambda: Counter())

# processing each pdf in folder
for filename in os.listdir(pdf_folder):
    if filename.endswith(".pdf"):
        # get year from pdf title
        match = re.search(r'(\d{4})', filename)
        if not match:
            continue
        year = match.group(1)
        path = os.path.join(pdf_folder, filename)

        reader = PdfReader(path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        normalized_text = text.lower()

        # count all phrases (singular/plural variations)
        for unified_phrase, variants in phrase_variants.items():
            count = 0
            for variant in variants:
                pattern = variant.lower()
                count += normalized_text.count(pattern)
            total_counts[unified_phrase] += count
            yearly_counts[year][unified_phrase] += count


# Total frequencies across all years dataframe
df_total = pd.DataFrame(total_counts.items(), columns=["Phrase", "Total Frequency"]).sort_values(by="Total Frequency", ascending=False)

# Frequencies per year (pivot table) dataframe
all_years = sorted(yearly_counts.keys())
data = {"Phrase": list(phrase_variants.keys())}
for year in all_years:
    data[year] = [yearly_counts[year][phrase] for phrase in phrase_variants.keys()]
df_yearly = pd.DataFrame(data)

# export to csv
df_total.to_csv("data/total_phrase_frequencies.csv", index=False)
df_yearly.to_csv("data/yearly_phrase_frequencies.csv", index=False)

# export to excel
with pd.ExcelWriter(output_excel, engine="openpyxl") as writer:
    df_total.to_excel(writer, sheet_name="Total", index=False)
    df_yearly.to_excel(writer, sheet_name="Per Year", index=False)