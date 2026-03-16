# System Architecture (C4 Model)

## Project Title

AI-Powered Fake News Detection System

## Domain

Digital Media and Journalism

## Problem Statement

Online misinformation spreads rapidly across digital platforms, making it difficult for users to verify the credibility of information. The proposed system provides automated analysis of text content to determine whether it may contain misleading information.

---

# C4 Model Architecture

## Level 1 – System Context Diagram

```mermaid
C4Context
title System Context Diagram - Fake News Detection System

Person(user, "User", "Submits news text for credibility analysis")

System(system, "Fake News Detection System", "Analyzes news content using AI")

System_Ext(data, "External News Data Sources", "Datasets used for training models")

Rel(user, system, "Submits article text")
Rel(system, data, "Uses datasets for model training")
```
---

## Level 2 – Container Diagram

```mermaid
C4Container
title Container Diagram - Fake News Detection System

Person(user, "User")

System_Boundary(system, "Fake News Detection System") {

Container(web, "Web Application", "HTML/CSS/JS", "User interface for submitting news text")

Container(api, "Backend API", "Node.js / Python", "Processes requests and controls analysis")

Container(ml, "ML Classification Service", "Python", "Detects fake news using machine learning")

Container(db, "Database", "SQL", "Stores submitted articles and results")

}

Rel(user, web, "Uses")
Rel(web, api, "Sends analysis request")
Rel(api, ml, "Requests classification")
Rel(api, db, "Stores results")
Rel(ml, db, "Reads training data")
```
---

## Level 3 – Component Diagram

```mermaid
C4Component
title Component Diagram - Backend API

Container(api, "Backend API")

Component(controller, "API Controller", "Handles user requests")
Component(preprocess, "Text Preprocessing Module", "Cleans and prepares text")
Component(classifier, "ML Classifier", "Predicts fake or credible")
Component(storage, "Database Manager", "Stores results")

Rel(controller, preprocess, "Sends text")
Rel(preprocess, classifier, "Processed text")
Rel(classifier, storage, "Stores result")
```
