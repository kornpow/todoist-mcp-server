#!/usr/bin/env python3

import os
import logging
from todoist_api_python.api import TodoistAPI

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("todoist-mcp-server")

def get_api_client():
    """
    Initialize and return the Todoist API client.

    Returns:
        TodoistAPI: Initialized Todoist API client

    Raises:
        ValueError: If TODOIST_API_TOKEN environment variable is not set
        Exception: If client initialization fails
    """
    # Fail fast on missing credentials to provide clear setup guidance
    TODOIST_API_TOKEN = os.getenv("TODOIST_API_TOKEN")
    if not TODOIST_API_TOKEN:
        logger.error("TODOIST_API_TOKEN environment variable is required")
        raise ValueError("TODOIST_API_TOKEN environment variable is required")

    try:
        # Create client instance - authentication is validated on first API call
        todoist_client = TodoistAPI(TODOIST_API_TOKEN)
        logger.info("Todoist API client initialized successfully")
        return todoist_client
    except Exception as e:
        logger.error(f"Failed to initialize Todoist client: {e}")
        raise
