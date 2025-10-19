# Overview

This is a Flask web application that serves as a **Make.com Scenario Runner**. The application allows users to configure and execute Make.com automation scenarios through a modern web interface with dynamic button creation and management.

**Last Updated:** October 17, 2025

The application includes:
- A Flask-based web server with REST endpoints
- Integration with Make.com API for scenario execution
- Dynamic web interface with customizable scenario buttons
- LocalStorage-based configuration management
- Support for multiple Make.com regions (US1, US2, EU1, EU2, Celonis)
- Historical integration with Feishu/Lark Base (currently disabled)

# User Preferences

Preferred communication style: Simple, everyday language.

# Recent Changes (Oct 17, 2025)

1. **Complete UI Redesign:** 
   - Added "+" button in top-right corner for adding new scenarios
   - Modal configuration form with zone URL selector, API token, scenario ID, optional data, and button remark
   - Dynamic button rendering stored in browser localStorage
   - Modern gradient design with purple/blue color scheme

2. **Backend Updates:**
   - Created `playground/make.py` for Make.com API integration
   - Added `/make_run` POST endpoint for scenario execution
   - Commented out previous `search_and_replace` functionality
   - Enhanced error handling with detailed JSON responses

3. **Features:**
   - Multi-region support for Make.com zones
   - JSON data input validation
   - Per-button configuration deletion
   - Toast notifications for success/error feedback

# System Architecture

## Frontend Architecture

**Technology Stack:**
- HTML/CSS templates using Jinja2 templating engine
- Vanilla JavaScript for client-side interactions
- LocalStorage for persistent configuration
- Template located in `templates/index.html`

**Design Pattern:**
- Server-side rendering with Jinja2
- RESTful API calls from frontend to backend
- Dynamic DOM manipulation for scenario buttons
- Responsive design with CSS gradients and modern UI elements
- Modal-based configuration interface

## Backend Architecture

**Framework:** Flask 2.2.2
- Lightweight Python web framework
- RESTful API endpoints
- Request/response handling with JSON

**Module Structure:**
- `main.py`: Application entry point and route definitions
- `playground/make.py`: Make.com API integration logic
- `playground/search_and_replace.py`: Feishu/Lark Base integration (currently disabled)

**API Endpoints:**
1. `GET /`: Serves the main web interface
2. `POST /make_run`: Triggers Make.com scenario execution
   - Accepts: zone_url, api_token, scenario_id, data (optional JSON)
   - Returns: Execution results or error messages

**Error Handling:**
- Input validation for required parameters
- JSON parsing with fallback handling
- HTTP status codes for different error scenarios (400, 500)

## External Dependencies

**Make.com Integration:**
- **Purpose:** Automation platform for running scenarios/workflows
- **API Endpoint:** `https://{zone_url}/api/v2/scenarios/{scenario_id}/run`
- **Authentication:** API token-based authentication via headers
- **Request Format:** POST with JSON payload containing scenario data
- **Timeout:** 30 seconds per request

**Feishu/Lark Base Integration (Disabled):**
- **SDK:** baseopensdk 0.0.12
- **Purpose:** Previously used for search and replace operations in Feishu Base tables
- **Authentication:** APP_TOKEN and PERSONAL_BASE_TOKEN environment variables
- **Status:** Code commented out, endpoints disabled

**Python Packages:**
- `requests 2.31.0`: HTTP client for external API calls
- `flask 2.2.2`: Web framework
- `baseopensdk 0.0.12`: Feishu/Lark Base SDK (currently unused)

**Development Tools:**
- `debugpy 1.6.5`: Python debugger for development
- Virtual environment managed by Replit

**Configuration:**
- Environment variables for API credentials
- No database currently in use
- Stateless request handling