```mermaid
flowchart LR

%% Actors (6+)
User([User])
Journalist([Journalist])
Researcher([Researcher])
Admin([Admin])
FactChecker([Fact Checker])
Guest([Guest User])

%% System Boundary
subgraph System["Fake News Detection System"]

Submit["Submit News Text"]
Process["Process Text"]
Classify["Classify News"]
View["View Results"]
Store["Store Results"]
Analyze["Analyze Data"]
Monitor["Monitor System"]
Manage["Manage Database"]
Login["Login"]
ViewHistory["View History"]

end

%% Actor → Use Cases
User --> Submit
User --> View
User --> ViewHistory

Guest --> Submit
Guest --> View

Journalist --> Classify
Journalist --> View

Researcher --> Analyze

FactChecker --> Classify
FactChecker --> Analyze

Admin --> Monitor
Admin --> Manage

%% Internal Relationships
Submit --> Process
Process --> Classify
Classify --> Store
Store --> View

View --> ViewHistory
Analyze --> Store
Login --> Submit
```
## Explanation

The diagram includes six actors: User, Guest User, Journalist, Researcher, Fact Checker, and Admin. Each actor interacts with the system based on their role. For example, Users and Guests can submit news text and view results, while Journalists and Fact Checkers are involved in verifying and classifying news. Researchers analyze stored data, and Administrators monitor system performance and manage the database. The use cases such as "Submit News Text," "Process Text," and "Classify News" demonstrate the system’s core functionality and directly align with the functional requirements defined in the previous assignment.The relationships between use cases show how actions depend on each other. For example, submitting news includes processing text, which leads to classification and storage of results. This ensures that stakeholder concerns such as accuracy, performance, and usability are addressed.

# Use Case Specifications

---

## 1. Use Case: Submit News Text

**Actor:** User / Guest

**Description:** Allows users to submit news text for credibility analysis.

**Preconditions:**

* User is on the system interface

**Postconditions:**

* News text is successfully submitted to the system

**Basic Flow:**

1. User enters news text
2. User clicks submit
3. System receives the text
4. System forwards text for processing

**Alternative Flows:**

* If text field is empty → System displays error message

---

## 2. Use Case: Process Text

**Actor:** System

**Description:** Cleans and prepares submitted text for analysis.

**Preconditions:**

* News text has been submitted

**Postconditions:**

* Text is cleaned and ready for classification

**Basic Flow:**

1. System removes unnecessary characters
2. System tokenizes text
3. System prepares input for model

**Alternative Flows:**

* If text format is invalid → System returns error

---

## 3. Use Case: Classify News

**Actor:** Journalist / Fact Checker

**Description:** Classifies news as real or fake using machine learning.

**Preconditions:**

* Text has been processed

**Postconditions:**

* News is labeled as “Real” or “Fake”

**Basic Flow:**

1. System sends processed text to ML model
2. Model analyzes text
3. Model returns classification result

**Alternative Flows:**

* If model fails → System displays classification error

---

## 4. Use Case: View Results

**Actor:** User / Journalist

**Description:** Displays credibility results to the user.

**Preconditions:**

* Classification is complete

**Postconditions:**

* Results are displayed on screen

**Basic Flow:**

1. System retrieves classification result
2. System displays credibility score
3. User views result

**Alternative Flows:**

* If no result available → System shows message

---

## 5. Use Case: Store Results

**Actor:** System

**Description:** Stores analyzed results in the database.

**Preconditions:**

* Classification has been completed

**Postconditions:**

* Results are saved in database

**Basic Flow:**

1. System receives classification result
2. System connects to database
3. System saves data

**Alternative Flows:**

* If database fails → System logs error

---

## 6. Use Case: Analyze Data

**Actor:** Researcher

**Description:** Allows researchers to analyze stored data for trends.

**Preconditions:**

* Data exists in database

**Postconditions:**

* Insights are generated from data

**Basic Flow:**

1. Researcher requests data analysis
2. System retrieves stored data
3. System processes data
4. System displays insights

**Alternative Flows:**

* If no data available → System shows message

---

## 7. Use Case: Monitor System

**Actor:** Admin

**Description:** Allows administrators to monitor system performance.

**Preconditions:**

* Admin is logged in

**Postconditions:**

* System status is displayed

**Basic Flow:**

1. Admin accesses dashboard
2. System displays logs and metrics
3. Admin reviews system performance

**Alternative Flows:**

* If system error occurs → Alert is displayed

---

## 8. Use Case: Manage Database

**Actor:** Admin

**Description:** Allows admin to manage stored data.

**Preconditions:**

* Admin is authenticated

**Postconditions:**

* Database is updated

**Basic Flow:**

1. Admin accesses database tools
2. Admin updates or deletes records
3. System saves changes

**Alternative Flows:**

* If unauthorized access → System denies action


