name: Frontend Continuous Integration

on:
  pull_request:
    branches: [main]
    paths:
      - 'starter/frontend/**'
  workflow_dispatch:

jobs:
  lint-and-test:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: starter/frontend

    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Setup Node.js 18
        uses: actions/setup-node@v4
        with:
          node-version: '18'
          cache: 'npm'
          cache-dependency-path: starter/frontend/package-lock.json

      - name: Install Dependencies
        run: npm ci

      - name: Run Linter
        run: npm run lint

      - name: Run Tests
        run: CI=true npm test
