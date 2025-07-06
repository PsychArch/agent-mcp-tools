#!/bin/bash
set -e

# This test runs the writer example.
# It uses the director agent to ask the writer agent to create three documents.

PROMPT=$(cat examples/writer/director.md)

uv run agent-mcp-tools query "$PROMPT" --mcp-config examples/writer/director_mcp.json 