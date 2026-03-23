# System Requirements Document (SRD)

## Functional Requirements

1. The system shall allow users to submit news text for analysis.

   * Stakeholder: General User
   * Acceptance: Text input is processed without errors

2. The system shall analyze submitted text using a machine learning model.

   * Stakeholder: Developer, Researcher
   * Acceptance: Model returns classification result

3. The system shall display a credibility score to the user.

   * Stakeholder: General User, Journalist
   * Acceptance: Score is shown as percentage

4. The system shall store analyzed articles in a database.

   * Stakeholder: Researcher, Organization
   * Acceptance: Data is saved successfully

5. The system shall allow users to view previous analyses.

   * Stakeholder: General User
   * Acceptance: Results can be retrieved

6. The system shall provide system logs for monitoring.

   * Stakeholder: System Administrator
   * Acceptance: Logs are accessible

7. The system shall preprocess text before analysis.

   * Stakeholder: Developer
   * Acceptance: Text is cleaned correctly

8. The system shall support multiple users simultaneously.

   * Stakeholder: Organization
   * Acceptance: No crashes under load

9. The system shall provide feedback messages to users.

   * Stakeholder: General User
   * Acceptance: Errors are clearly displayed

10. The system shall allow administrators to monitor system usage.

    * Stakeholder: System Administrator
    * Acceptance: Usage data is available




## Non-Functional Requirements

### Usability

* The system shall have a simple and intuitive user interface.
* The system shall provide clear feedback messages.

### Deployability

* The system shall be deployable on web browsers.
* The system shall support cloud deployment.

### Maintainability

* The system shall include clear documentation.
* The system shall follow modular design principles.

### Scalability

* The system shall support at least 1,000 concurrent users.

### Security

* The system shall encrypt user data using secure protocols.

### Performance

* The system shall return results within 2 seconds.

      

