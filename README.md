# Analysis-of-reports-for-strategic-human-resource-management-in-the-context-of-EU-integration

Study on the Strategic Human resource Management in the Context of European integration (case study of institutions of Bosnia and Herzegovina - BH) was designed to include analyses of the country reports on progress towards EU issued by European Commission (EC) Annually. The evaluation includes a baseline report from 2005 and reports during the period from 2014 - 2024.
Key phrases are related to the human resource management (HRM) and public sector reforms (since the HR issues were related to this section of EC review).
The research is used to evidence dynamic, trends in the approach of the EC toward the country over the year in the HRM aspect. The occurrence of new phrases indicates the interest of the EC in new areas of the HRM such as information systems ad HR data driven approach.
This model could be used to compare the trends and approach with other countries that are among the ones with an EU candidate status.
The list of phrases/terms was identified based on theory and practice of the research in Strategic human resource management in public institutions, human resource management in the EU institutions and European Administrative Space principles as well as country specific status of the HRM practice and policies.

This repository supports the research of Ernadina Bajrovic, M.A., within her PhD thesis. It includes counting the frequency of relevant terms and phrases inside the given reports, followed by an exploratory analysis of the obtained results.


The keyword_frequency.py script goes through the reports inside the /reports folder and counts the frequency of terms and phrases from a predefined list. The output of this script is a set of three files:
- total_phrase_frequencies.csv containing total frequencies across all years/reports
- yearly_phrase_frequencies.csv containing frequencies for each phrase/term per year
- keyword_frequencies.xlsx containing the contents of both CSV files as two separate sheets for easier and direct use

The frequencies_visualizations.ipynb notebook loads the data created by the keyword_frequency.py script and performs exploratory analysis, creating different visualizations to analyze trends over time and most frequent phrases and terms. It is also available in .pdf and .html form for easier use.
