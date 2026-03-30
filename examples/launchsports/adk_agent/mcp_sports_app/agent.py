import os
import dotenv
import tools

dotenv.load_dotenv()
project_id = os.getenv('GOOGLE_CLOUD_PROJECT', 'my-project-81240-491718')

maps_toolset = tools.get_maps_mcp_toolset()
bigquery_toolset = tools.get_bigquery_mcp_toolset()

from google.adk.agents import LlmAgent

root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='root_agent',
    instruction=f"""
        You are an NCAA Basketball Sports Analytics Assistant.
        Help users analyze basketball team performance data.

        1. **BigQuery toolset:** Access sports data in the mcp_sports dataset.
           Table: mcp_sports.team_performance
           Columns:
           - season (2015-2019)
           - team_city, team_name
           - win (true/false)
           - points_game, field_goals_pct, three_points_pct
           - rebounds, assists, turnovers

           Run all queries from project id: {project_id}.
           Only use dataset: mcp_sports.

        2. **Maps Toolset:** Find stadiums and arenas for teams.
           Include a map hyperlink in responses.

        Show results as numbered list with emojis 🏀.
        Default season: 2018 if not mentioned.
    """,
    tools=[maps_toolset, bigquery_toolset]
)

examples/launchsports/setup/setup_bigquery.sh
