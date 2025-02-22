#!/bin/bash
# Auto Git Commit and Push

# Navigate to the repository (optional: update with your repo path)
cd /home/luquitas/projects/mathgame || exit

# Add all changes
git add .

# Commit changes with a timestamp
git commit -m "Auto update on $(date)"

# Push to the main branch (change 'main' if your branch is different)
git push origin main

echo "Changes pushed to GitHub!"
