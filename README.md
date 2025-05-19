# TCGProjects

This is a for fun project where I simulate different TCG concepts in Python. The end goal is a comprehensive library of classes that covers different TCGs (primarily Yu-Gi-Oh! and Magic the Gathering).

## Selvala Flip Simulator

A web application that simulates the Selvala, Explorer Returned ability in Magic: The Gathering Commander games. The simulator allows users to track mana production across multiple decks in a game.

### Features

- Simulate Selvala's ability across multiple decks
- Track mana production history
- Reset decks to their initial state

### Technical Stack

- Frontend: React with TypeScript
- Backend: FastAPI (Python)
- API Endpoints:
  - `GET /flip`: Simulates a Selvala flip and returns mana produced
  - `POST /reset`: Resets all decks to their initial state

### Setup

1. Backend:

   ```bash
   cd backend
   pip install -r requirements.txt
   uvicorn main:app --reload
   ```

2. Frontend:
   ```bash
   cd frontend
   npm install
   npm start
   ```

The application will be available at http://localhost:3000, with the API running at http://localhost:8000.
