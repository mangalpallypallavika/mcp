import os
import dotenv
from mcp_sports_app import tools
from google.adk.agents import LlmAgent

dotenv.load_dotenv()
PROJECT_ID = os.getenv('GOOGLE_CLOUD_PROJECT', 'project_not_set')

maps_toolset = tools.get_maps_mcp_toolset()
bigquery_toolset = tools.get_bigquery_mcp_toolset()

root_agent = LlmAgent(
    model='gemini-3.1-pro-preview',
    name='sports_agent',
    instruction=f"""
Help the user answer questions by strategically combining insights from two sources:

1. **BigQuery toolset:** 
Access NCAA basketball performance data stored in the `mcp_sports` dataset.
Use the table: mcp_sports.team_performance
Columns available: season, team_city, team_name, win, points_game, 
field_goals_pct, three_points_pct, rebounds, assists, turnovers.
Do not use any other dataset.
Run all query jobs from project id: {PROJECT_ID}.

2. **Maps Toolset:** 
Use this for real-world location analysis, finding stadiums, arenas,
and calculating travel routes between locations.
Include a hyperlink to an interactive map in your response where appropriate.
""",
    tools=[maps_toolset, bigquery_toolset]
)
