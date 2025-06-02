# UCLA Tennis Consulting Season Overview
<p align="center">
  <a href="https://match-viewing-dashboard.web.app/">
    <img src="logo.avif" width="" alt="BSA Logo">
  </a>
</p>

Affiliated with BSA and BTC.
# Aim
The purpose of this repo is to generate season-reports for the UCLA D1 Tennis Team. 

Generates data to populate figma templates.

# Setup
Clone the repo with 
```
git clone https://github.com/cjgimena/consulting-spring2025.git
```
Ensure you have the correct packages with(not really needed)
```
pip3 install -r requirements.txt
```
Create a new branch in the format `[name]\[issue]`.

# Organization

There are 4 main folders.
## Notebooks
Practice notebooks to understand numpy, pandas, python, jupyter, and Vscode.
## Visuals
Contains html + json code to generate visuals using d3.js.

Currently contains
- **Singles Record** - PNG of season records
- **Ratings** - Prototype of ATP ratings
- **Serve Zones** - N/A
- **Serve Percentage** - PNG of first/second serve %
- **Serve Placement** - Placement of shots w/ in, out, clinch
- **Serve Distribution** - Placement of W,T,B
- **Dist and Zone** - Combo of Placement + Dist

Json Data is generated through [fill in]

## Data
Contains individual swingvision matches for the mens / womens team located in `data/mens(womens)/[player]`. There is also a combined csv with all matches in one sheet.

Also contains
- **matches_2025.csv** - Data of all UCLA matches scraped from UCLA website.
- **mens_results.csv** - Data of all UTR supported matches scraped from UTR website.
- **tennis_matches_data.csv** - Data of all UCLA matches scraped from UCLA website. Slightly different columns from 1st spreadsheet.

## Season_Report

Contains top level files to generate data. Specifically
- **ucla_data.py / ucla_data.ipynb** - Scrape UCLA website, generate aforementioned csvs.
- **loaddata.py** - N/A
- **getdata.py** - Creates combined csvs for players.

### Index Page
- Generates overall summary data.
### Return Page
- Generates return data.
### Serve Page
- Generates serve data through `serve.ipynb`
### Summary Page
- Generates summary data through `summary.ipynb` and WIP `summary.py`

# Other
Created initially Spring Quarter 2025.
Contact - [uclatennisconsulting@gmail.com](mailto:uclatennisconsulting@gmail.com)
