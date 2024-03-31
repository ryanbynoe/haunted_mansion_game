# Haunted Mansion Game

This is a text-based horror adventure game where you navigate the haunted mansion, solving puzzles and making choices that affect the game's outcome. Your goal is to survive the horrors within and escape.

Project demo to display deployment through Docker.

# Docker Deployment Steps

## Step 1: Clone the Repository

First, clone the repository to your local machine using Git:

```bash
git clone https://github.com/ryanbynoe/haunted_mansion_game.git

```

## Step 2: Navigate to the Project Directory

```bash
cd haunted_mansion_game/

```
## Step 3: Build the Docker Image

```bash
docker build -t haunted_mansion_game .

```
## Run Docker Container

```bash
docker run -p 5000:5000 haunted_mansion_game

```
## Step 5: Removal (Optional)
If you need to remove the project from your machine, follow these steps:

First, ensure you are not in the project directory. If you are, navigate back:

```bash
cd ..

```
Then, remove the project directory:

```bash
rm -r haunted_mansion_game/

```



