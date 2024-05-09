# NightVision MSTeams Importer

## Description

`NightVision MSTeams Importer` is a tool used to automate the process of importing security vulnerability findings from a nightvision scan results file into Microsoft Teams, where it sends discovered issues as notifications to a Microsoft Teams channel via a webhook.


## Installation

1. **Clone the Repository:**
   ```
      git clone https://github.com/jxbt/nightvision_ms_teams_importer.git
      cd nightvision_ms_teams_importer
   ```
1. **Install Dependencies:**
   ```
      python3 -m venv .venv
      source .venv/bin/activate
      pip3 install -r requirements.txt
   ```

## Usage
   To use the NightVision MSTeams Importer, provide the path to your SARIF file along with your Microsoft Teams webhook URL:
   
   ```
     source .venv/bin/activate
     python3 nightvision_teams_importer.py --sarif <path_to_sarif_file> --webhook <webhook_url>
   ```

  ### Flags:

   | Flag            | Description                                                                        | 
   | --------------- |------------------------------------------------------------------------------------|
   | -s, --sarif     |  Path to the SARIF file containing the security scan results.                  |                    
   | -w, --webhook    |  Microsoft Teams webhook URL.   |                                  
