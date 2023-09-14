# QA Cinema

The project goal is to create a cinema website that allows users to buy tickets for movies they wish to see.

## Table of Contents
1. [Introduction](#introduction)
2. [Project Structure](#project-structure)
3. [Tech Stack](#tech-stack)
4. [Requirements Gathering](#requirements-gathering)
5. [Design Choices](#design-choices)
6. [Wireframe](#wireframe)
7. [ERD Diagram](#erd-diagram)
8. [CRUD Features](#crud-features)
9. [Component Diagram](#component-diagram)
10. [Pipeline Diagram](#pipeline-diagram)
11. [Testing](#testing)
12. [Risk Assessment](#risk-assessment)
13. [Code Refactoring](#code-refactoring)
14. [Conclusion](#Conclusion)
15. [Acknowledgements](#acknowledgements)
16. [References](#references)



## 1. Introduction

Introduce the project's purpose, goals, and high-level overview.

In the QA Cinema website project, we have made a design decision to create a separate booking page for movie screenings instead of dynamically generating booking forms on the same page as the movie listings. This decision was made to simplify the user interface, enhance user experience, and improve the maintainability of the website.

---

## 2. Project Structure

- **Directory Structure**: Describe the organizational structure of your directories and files.
- **Main Components**: Explain the primary components/modules of your application and their roles.
- **Flow**: If applicable, describe the flow or sequence in which different parts of your project interact.

---

## 3. Tech Stack

Detail all the technologies you used in this project:

- **Languages**: (Python, JavaScript, HTML, CSS)
- **Frameworks**: (Flask)
- **Databases**: (SQlite, MySQL)
- **Deployment**: ( Docker)
- **Other Tools**: (Github, Jenkins)

---

## 4. Requirements Gathering

Discuss the process by which you gathered requirements for your project:


- **Research**: Did you use existing literature or projects to inform your design?
- **Iterations**: Describe how the requirements might have evolved over time.

---

## 5. Design Choices

Discuss the major design decisions you made for this project:

- **Philosophy**: What were your guiding principles or goals with your design?
- **Specific Choices**: Any specific choices worth noting? Why did you make them?

---

## 6. Wireframe

Present and describe any wireframes, mockups, or design blueprints for your project:

- **[Link to Wireframe]**
- **Design Notes**: Any specific components or flow mechanisms to highlight?

---

## 7. ERD Diagram

Present and discuss your Entity Relationship Diagram:

- **[Link/Embed of ERD Diagram]**
- **Key Entities and Relationships**: Discuss the main tables/entities and their connections.

---
## 8. CRUD Features

Detail the CRUD (Create, Read, Update, Delete) features of your project:

- **Create**: How do users add new data?
- **Read**: How is data retrieved and presented?
- **Update**: How can data be modified?
- **Delete**: How can data be removed? Any safeguards?

---

## 9. Component Diagram

- **VMS Containers**: Jenkins
- **Description**: A brief explanation of the component diagram and its significance.
- **Link/Embed**: Link to or embed the component diagram.

---

## 10. Pipeline Diagram

- **Diagrams**: Webhooks, environments
- **Description**: Describe the pipeline, its stages, and its role in the CI/CD process.
- **Link/Embed**: Link to or embed the pipeline diagram.

---

## 11. Testing

- **What You Did**: Describe the testing steps, scenarios, and any innovative methods applied.
- **Testing Analysis**: Detail the problems you faced during testing and how you overcame them.
- **Strategy**: Explain the testing approach, the types of tests employed (unit, integration, etc.), and any tools or frameworks used.
- **Results**: Summarize key findings, link to detailed results or reports if available.

---

## 12. Risk Assessment

- **Approach**: Describe the methodology used for risk assessment.
- **Key Risks**: Highlight the main risks identified and the proposed mitigation strategies.

The QA Cinemas training project involves the development of a full-stack web application for a cinema chain. This assessment identifies potential technical and learning-related risks that may impact the project's success.
Risk Identification:
1. Technical Complexity
Description: The project's technical requirements, such as integrating third-party services and implementing complex features, may exceed the team's current skill level.
Impact: Delays in development, increased learning curve, and potential project challenges.
Mitigation: Allocate extra time for learning and skill development. Seek guidance from mentors or experienced team members.
2. Scope Creep
Description: Uncontrolled additions or changes to project requirements during development due to a desire for additional features.
Impact: Increased project scope, potential learning overload, and project focus diversion.
Mitigation: Maintain a clear understanding of the project's scope and objectives. Focus on mastering core concepts before adding extra features.
3. Integration Challenges
Description: Difficulty in integrating external services and APIs into the application due to lack of prior experience.
Impact: Delays in development, potential learning barriers, and increased complexity.
Mitigation: Prioritize learning integration techniques and seek assistance from experienced developers or trainers.
4. Resource Constraints
Description: Inadequate availability of training resources, such as documentation or tutorials, for specific technologies.
Impact: Learning challenges, potential project delays, and limited access to knowledge.
Mitigation: Explore a variety of learning resources, such as online tutorials, books, or courses, to bridge knowledge gaps.
5. Learning Curve
Description: The project may involve technologies or concepts that are new to the team, resulting in a steep learning curve.
Impact: Slower progress, potential frustration, and a need for additional time for skill acquisition.
Mitigation: Develop a structured learning plan and allocate time for skill acquisition. Seek guidance from mentors or trainers.
6. External Payment Handling
Description: The project relies on an external payment handler, and no card details will be stored within the application.
Impact: Reduced security responsibilities, but potential challenges in integrating and ensuring seamless payment processing.
7. VM for Apps Stops Functioning
Description: The virtual machine (VM) hosting the application servers may encounter technical issues or crashes, causing disruptions in the application's availability and functionality. This could result in downtime and affect users' access to the application.
Impact: Moderate Likelihood, High Impact
Risk Level: Moderate
8. Pushing Sensitive Info to GitHub
Description: There is a risk of accidentally pushing sensitive information, such as API keys, credentials, or confidential data, to a public or private GitHub repository. This can lead to data breaches, security vulnerabilities, and compliance issues.
Impact: Moderate Likelihood, High Impact
Risk Level: Moderate
9. VScode Ceases to Connect to VM
Description: The connection between Visual Studio Code (VScode) and the virtual machine (VM) used for development may fail, preventing developers from accessing and editing code. This can hinder development and collaboration efforts.
Impact: Low Likelihood, High Impact
Risk Level: Moderate
10. Jenkins VM Ceases to Function
Description: The VM hosting the Jenkins continuous integration/continuous deployment (CI/CD) server may experience technical issues, resulting in the disruption of automated build, test, and deployment processes. This can lead to delays in the software development lifecycle.
Impact: Low Likelihood, High Impact
Risk Level: Moderate
11. VM for DB Stops Functioning
Description: The virtual machine (VM) responsible for hosting the database server may encounter problems or crashes, affecting the availability and reliability of the database. This can lead to data unavailability and potential data loss.
Impact: Moderate Likelihood, High Impact
Risk Level: Moderate
12. Database Hack
Description: There is a risk of a malicious actor gaining unauthorized access to the database, potentially leading to data breaches, data manipulation, or data theft. This can have severe consequences for data security and user privacy.
Impact: Low Likelihood, High Impact
Risk Level: Moderate


| Risk                         | Likelihood     | Impact                   | Risk Level |
|------------------------------|----------------|--------------------------|------------|
| Technical Complexity         | High           | Moderate                 | Moderate   |
| Scope Creep                  | Moderate       | Moderate                 | Moderate   |
| Integration Challenges       | Moderate       | Moderate                 | Moderate   |
| Resource Constraints         | Low            | Low                      | Low        |
| Learning Curve               | Moderate       | Moderate                 | Moderate   |
| External Payment Handling    | Low            | High                     | Moderate   |
| Absence                      | Moderate       | High                     | Moderate   |
| VM for Apps Stops Functioning | Moderate       | High                     | Moderate   |
| Pushing Sensitive Info to GitHub | Moderate    | High                     | Moderate   |
| VScode Ceases to Connect to VM | Low          | High                     | Moderate   |
| Jenkins VM Ceases to Function | Low           | High                     | Moderate   |
| VM for DB Stops Functioning   | Moderate       | High                    | Moderate   |
| Database Hack                | Low            | High                     | Moderate   |


Risk Mitigation:

Emphasize team work as the primary goal of the training project. This is because team members often bring different skills, knowledge, and expertise to the table. By working together, they can complement each other's strengths and compensate for weaknesses, resulting in more well-rounded and effective solutions.

Create a supportive learning environment within the team by encouraging communication and learning.

Regular integration and bug fixes to mitigate integration challenges.

---

## 13. Code Refactoring

- **Screenshots**: Consider embedding or linking to before-and-after screenshots to showcase changes.
- **Overview**: Explain the need and benefits of the refactoring, including aspects like efficiency improvements or readability enhancements.
- **Key Changes**: Detail major changes made, with before-and-after code snippets where useful.



---
## 14. Conclusion

The QA Cinemas training project is an opportunity to enhance technical skills and gain practical experience. By proactively addressing potential risks, focusing on collaboration and learning and ensuring a clear understanding of Devops principles, the team can maximize the benefits of this training project.

---
## 15. Acknowledgements

Thank any individuals, organizations, or resources that were instrumental in the project:

- Person/Resource name: Brief description or reason for acknowledgement.

---

## 16. References

List all sources, tools, or libraries you referred to during the project:

1. [Name of Source](URL) - Brief description of the source.


[Footer or any additional notes or links you want to add]

