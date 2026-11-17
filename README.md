\# PaperNest - IDOR Security Lab



\## Project Overview



PaperNest is a beginner-friendly Python application demonstrating Insecure Direct Object Reference (IDOR).



It compares a vulnerable application with a secure application using two fictional users.



Everything runs locally on 127.0.0.1.



\## Learning Objectives



\- Understand authentication and authorization.

\- Demonstrate an IDOR vulnerability.

\- Test access controls using two accounts.

\- Inspect HTTP requests and responses.

\- Implement server-side ownership checks.

\- Document security findings.



\## Lab Environment



\- Operating System: Windows 11

\- Language: Python

\- Testing tool: curl.exe

\- Network: Localhost only

\- Port: 8765



\## Fictional Accounts



| User | Token | Invoice |

|---|---|---|

| Alice | alice-demo-token | inv\_A17 |

| Bob | bob-demo-token | inv\_B29 |



\## Run the Application



Start vulnerable mode:



`py .\\papernest.py vulnerable`



Start secure mode:



`py .\\papernest.py secure`



Stop the application using Ctrl+C.



\## IDOR Test



Bob requests Alice's invoice:



`curl.exe -i -H "Authorization: Bearer bob-demo-token" http://127.0.0.1:8765/invoice/inv\_A17`



\### Vulnerable result



HTTP 200 OK. Alice's invoice is exposed.



\### Secure result



HTTP 404 Not Found. Access is denied.



\## Root Cause



The vulnerable implementation authenticates Bob but does not verify whether he owns the requested invoice.



\## Remediation



The secure implementation checks invoice ownership before returning invoice information.



\## Evidence



See the evidence folder:



\- vulnerable-response.txt

\- secure-response.txt



\## Skills Demonstrated



\- Python

\- HTTP

\- REST API security

\- Authentication

\- Authorization

\- IDOR testing

\- Security reporting

\- Secure coding



\## Safety



This educational project uses fictional data and localhost only.



Only test systems for which you have explicit authorization.

