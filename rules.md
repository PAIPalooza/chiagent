# ChiAgent Development Guidelines

## Table of Contents
- [1. Development Workflow](#1-development-workflow)
- [2. Code Style](#2-code-style)
- [3. Testing Strategy](#3-testing-strategy)
- [4. Version Control](#4-version-control)
- [5. API Development](#5-api-development)
- [6. Documentation](#6-documentation)

## 1. Development Workflow

### 1.1 Backlog Management
- We use GitHub Issues for tracking work items
- All work items must be linked to an existing issue
- Follow the issue template format for consistency

### 1.2 Branching Strategy
- `main` - Production-ready code
- `develop` - Integration branch for features
- `feature/*` - Feature branches (e.g., `feature/refund-processing`)
- `bugfix/*` - Bug fixes (e.g., `bugfix/order-404`)
- `hotfix/*` - Critical production fixes

### 1.3 Pull Requests
- All changes must go through PR review
- PRs must reference an issue number
- At least one approval required before merging
- All CI checks must pass before merging

## 2. Code Style

### 2.1 Python
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use type hints for all function signatures
- Maximum line length: 88 characters (Black formatter)
- Use f-strings for string formatting
- Use absolute imports

### 2.2 JavaScript/TypeScript
- Use ES6+ syntax
- Use TypeScript for all new code
- Follow [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript)
- Use Prettier for code formatting

## 3. Testing Strategy

### 3.1 Test Types
- **Unit Tests**: Test individual functions/components
- **Integration Tests**: Test API endpoints and service interactions
- **E2E Tests**: Test complete user flows

### 3.2 Test Coverage
- Aim for >80% test coverage
- All new features must include tests
- Bug fixes must include regression tests

### 3.3 Running Tests
```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=app tests/

# Run specific test file
pytest tests/test_refunds.py
```

## 4. Version Control

### 4.1 Commit Messages
Follow [Conventional Commits](https://www.conventionalcommits.org/):
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Build process or tooling changes

Example:
```
feat(api): add refund processing endpoint

- Added POST /api/v1/refunds endpoint
- Implemented validation logic
- Added test coverage

Closes #123
```

### 4.2 Git Hooks
- Pre-commit hooks run:
  - Code formatting (Black)
  - Linting (Flake8, ESLint)
  - Type checking (mypy, TypeScript)

## 5. API Development

### 5.1 REST API Standards
- Use JSON for request/response bodies
- Version all API endpoints (e.g., `/api/v1/...`)
- Use HTTP status codes appropriately
- Follow RESTful design principles

### 5.2 Error Handling
- Return consistent error responses:
  ```json
  {
    "error": {
      "code": "INVALID_REQUEST",
      "message": "Detailed error message",
      "details": {}
    }
  }
  ```
- Log all errors with appropriate severity

## 6. Documentation

### 6.1 Code Documentation
- Use docstrings for all public functions/classes
- Follow Google Style docstrings for Python
- Use JSDoc for JavaScript/TypeScript

### 6.2 API Documentation
- Document all endpoints using OpenAPI/Swagger
- Keep API documentation in sync with code
- Include example requests/responses

### 6.3 Project Documentation
- Keep `README.md` up to date
- Document setup and deployment procedures
- Maintain a `CHANGELOG.md`

## Project-Specific Rules

### E-commerce Platform Integration
- Follow platform-specific best practices for Shopify/WooCommerce
- Store credentials securely using environment variables
- Implement proper error handling for API rate limits

### Database
- Use migrations for all schema changes
- Follow naming conventions:
  - Tables: plural, snake_case (e.g., `refund_requests`)
  - Columns: snake_case
  - Foreign keys: `table_name_id`

### Security
- Never commit sensitive data
- Use environment variables for configuration
- Implement proper input validation
- Use parameterized queries to prevent SQL injection
