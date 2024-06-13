# Eidolon Git Search Recipe

In this recipe we have created a github copilot who can answer questions about the Eidolon monorepo. It dynamically pulls in information via similarity search to answer user queries.
This is important if you have a body of information that is constantly changing, but you need real time information about (ie, a git repository).

## Core Concepts
* Multi-agent communication
* Sub-component customization
* Dynamic embedding management

## Agents
### Repo Expert
The user facing copilot. Ask this agent questions about a repository, and it will go and find the answer with the 
assistance of the repo search agent.

### Repo Search
Handles loading, embedding, and re-embedding documents ensuring they are up-to-date.

Translates queries into a vector search query and returns the top results.

## Directory Structure

- `resources`: This directory contains additional resources for the project. An example agent is provided for reference.
- `components`: This directory is where any custom code should be placed.

## Running the Server

First you need to clone the project and navigate to the project directory:

```bash
git clone https://github.com/eidolon-ai/agent-git-search.git
cd agent-machine
```

Then run the server in dev mode, use the following command:

```bash
make serve-dev
```

The first time you run this command, you may be prompted to enter credentials that the machine needs 
to run (ie, OpenAI API Key).

This command will download the dependencies required to run your agent machine and start the Eidolon http server in 
"dev-mode".

If the server starts successfully, you should see the following output:
```
Starting Server...
INFO:     Started server process [34623]
INFO:     Waiting for application startup.
INFO - Building machine 'local_dev'
...
INFO - Server Started in 1.50s
```
