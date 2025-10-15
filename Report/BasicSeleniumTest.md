# 📝 Selenium End-to-End Test Report (Basic)

## Part 1: Automated Selenium Testing of the Todo List App

This report documents the creation and execution of an automated Selenium test for the Todo List App, following best practices in test design, debugging, and error handling.

---

### 1. Project & Team Information

| Field | Value |
| :---- | :---- |
| **Assignment Name** | Basic Selenium Test for Todo List App |
| **Course** | Software Testing (Autumn 2025) |
| **Group Members** | Muditha Kumara, Chuks Henry |
| **Date Submitted** | 15/10/2025 |
| **App Version/Commit** | v1.0 (index.html, script.js, styles.css) |
| **Code Repository** | N/A (local files) |

---

### 2. Roles & Responsibilities

| Member | Role |
| :----- | :--- |
| Muditha Kumara | Test Author, Environment Setup |
| Chuks Henry | Reviewer, Debugging |

---

### 3. Test Scenario & Acceptance Criteria

The following user scenario and acceptance criteria were selected for automated testing:

```yaml
user_scenario:
  description: As a user, I can add a new regular task to the Todo List App.
  acceptance_criteria:
    - The app loads successfully in the browser.
    - The input field (ID: taskInput) and "Add Task" button are present.
    - A new task can be entered and added to the list.
    - The new task appears in the list after submission.
    - Error handling is present for empty input.
```

---

### 4. Selenium Test Plan & Test Cases

The following test plan and cases were derived from the acceptance criteria:

```yaml
test_cases:
  - id: TC1
    description: Add a valid task to the list.
    steps:
      - Open index.html in Chrome using Selenium.
      - Locate the input field and "Add Task" button.
      - Enter "Buy groceries" and click "Add Task".
      - Wait for the new task to appear in the list.
    expected_results:
      - "Buy groceries" appears in the task list.
      - No errors are shown.
    actual_results:
      - Task added and visible in the list.
      - Pass

  - id: TC2
    description: Attempt to add an empty task.
    steps:
      - Leave input field empty and click "Add Task".
    expected_results:
      - Alert or error message is shown.
    actual_results:
      - Alert appears for empty input.
      - Pass
```

---

### 5. Test Execution & Debugging

#### Environment Preparation
- Python 3.x installed
- Selenium installed via `pip install selenium`
- ChromeDriver downloaded and added to system PATH
- Todo List App files served locally (file:// or HTTP server)

#### Test Script Summary
- Python script initializes ChromeDriver and opens index.html
- Locates input field and button by ID
- Uses `send_keys` and `click` to add a task
- Implements explicit waits for DOM updates
- Uses assertions to verify task addition
- Configures logging and captures screenshots on error
- Headless mode tested for CI/CD compatibility

#### Debugging Strategies
- Logging used to capture info and errors
- Screenshots saved on exceptions
- Explicit waits used for dynamic elements
- Robust locators (ID, partial text) for reliability

---

### 6. Reflections & Lessons Learned

#### Challenges
- Handling dynamic DOM updates and waits
- Ensuring ChromeDriver compatibility
- Debugging element not found errors

#### Observations
- Explicit waits improve test reliability
- Error handling and logging are essential for debugging
- Headless mode is useful for automation

#### Lessons Learned
- Selenium tests require robust locators and waits
- Debugging tools (logs, screenshots) speed up error resolution
- Preparing for CI/CD integration is valuable

#### Recommendations
- Use more advanced selectors for complex apps
- Integrate with CI/CD for automated test runs
- Compare Selenium with Cypress/Playwright for future improvements

---

### 7. Attachments & Evidence

- Python test script (basic_selenium_test.py)
- Screenshots of test runs (success, error)
- Log files (if available)

---

*End of Report*
