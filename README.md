# Analysis-of-reports-for-strategic-human-resource-management-in-the-EU
This repository includes counting the frequency of relevant terms and phrases inside the given reports, followed by an exploratory analysis of the obtained results


The keyword_frequency.py script goes through the reports inside the /reports folder and counts the frequency of terms and phrases from a predefined list. The output of this script is a set of three files:
- total_phrase_frequencies.csv containing total frequencies across all years/reports
- yearly_phrase_frequencies.csv containing frequencies for each phrase/term per year
- keyword_frequencies.xlsx containing the contents of both CSV files as two separate sheets for easier and direct use

The frequencies_visualizations.ipynb notebook loads the data created by the keyword_frequency.py script and performs exploratory analysis, creating different visualizations to analyze trends over time and most frequent phrases and terms. It is also available in .pdf and .html form for easier use.
