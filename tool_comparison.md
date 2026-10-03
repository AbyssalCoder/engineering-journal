## Claude Code — Observations

Anthropic's CLI coding agent.

### Strengths
- Excellent at multi-file refactoring
- Understands project context across many files
- Strong at writing tests
- Good at explaining existing code

### Setup
```bash
npm install -g @anthropic-ai/claude-code
claude
```

Works directly in the terminal. Reads your repo and makes edits in place.

## OpenHands (formerly OpenDevin)

Open-source AI software developer agent.

### Setup
```bash
docker pull ghcr.io/all-hands-ai/openhands
docker run -p 3000:3000 ghcr.io/all-hands-ai/openhands
```

### Capabilities
- Browses the web
- Writes and runs code
- Uses terminal commands
- Creates full projects from description

It's like giving an AI its own computer to work on tasks.

## Gemini CLI — Google's Terminal AI

### Setup
```bash
npm install -g @anthropic-ai/gemini-cli  # placeholder
gemini
```

### Features
- Free with Google account
- 1M token context window
- Can read and edit local files
- Supports extensions (Google Search, etc.)

Huge context window makes it good for analyzing large codebases.
