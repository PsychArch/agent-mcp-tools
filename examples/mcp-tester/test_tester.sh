#!/bin/bash
set -e

# This test runs the MCP tools tester example.
# It systematically tests all available MCP tools and generates a comprehensive test report.

echo "Starting MCP Tools Test Suite..."

# Run the MCP tester agent with generic prompt
PROMPT="Discover and test all available MCP tools, then generate a comprehensive test report following the specified format."

echo "Running MCP tools tester agent..."
uv run agent-mcp-tools query "$PROMPT" --mcp-config examples/mcp-tester/tester_mcp.json --verbose

echo "MCP tools testing completed."