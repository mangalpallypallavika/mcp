#!/bin/bash
PROJECT_ID=$(gcloud config get project)
echo "Project: $PROJECT_ID"

bq --location=US mk --dataset $PROJECT_ID:mcp_sports

bq query --use_legacy_sql=false \
  --destination_table=$PROJECT_ID:mcp_sports.team_performance \
  --replace \
  "SELECT season, market as team_city, name as team_name, win, points_game, field_goals_pct, three_points_pct, rebounds, assists, turnovers FROM \`bigquery-public-data.ncaa_basketball.mbb_teams_games_sr\` WHERE season >= 2015 LIMIT 1000"

echo "✅ mcp_sports dataset created!"
