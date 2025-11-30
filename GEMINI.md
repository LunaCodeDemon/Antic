# Gemini Guidelines

This document provides guidelines for the Gemini AI assistant to follow while working on this project.

## Project Overview

This project is a Discord bot developed in Python using the [Hikari](https://www.hikari-py.dev/) library and the [Tanjun](https://tanjun.cursed.solutions/) command handler.

The goal of the project is to create a Discord bot with various features. (Please ask the user for more details about the features).

## General AI Guidelines

*   **Be proactive:** Don't just fulfill the request, try to anticipate the user's needs and suggest improvements.
*   **Be consistent:** Follow the coding style and conventions already present in the codebase.
*   **Be safe:** Do not expose any sensitive information like API keys or tokens.
*   **Explain your changes:** When you make changes, explain why you made them.
*   **Ask for clarification:** If a request is ambiguous, ask for more details before proceeding.
*   **Test your code:** Always write tests for the code you write.

## Python Coding Conventions

*   Follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide.
*   Use type hints for all function signatures.
*   Use f-strings for string formatting.
*   Use a linter like `flake8` or `pylint` to check your code.

## Testing

*   Use the `pytest` framework for testing.
*   Write unit tests for all new features and bug fixes.
*   Ensure that the tests cover all edge cases.

## Commit Messages

*   Follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification.
*   The first line of the commit message should be a short summary of the change (less than 50 characters).
*   The body of the commit message should provide more details about the change.
*   Use the imperative mood in the subject line (e.g., "add: new feature" instead of "added: new feature").
