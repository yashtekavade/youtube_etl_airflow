# YouTube Comments ETL & Analysis Project

## Overview

This project demonstrates how to build a simple ETL (Extract, Transform, Load) pipeline to retrieve YouTube video comments using the YouTube Data API, process the data, and generate actionable insights. The goal is to extract meaningful feedback from viewers to help content creators improve their videos and better engage their audience.

---

## Motivation

After completing a tutorial on data pipelines, I wanted to give back to a YouTuber whose content helped me learn so much. I discovered that YouTube comments could be extracted programmatically via the YouTube Data API. This sparked the idea of building a pipeline to collect, process, and analyze comments, turning audience feedback into actionable insights.

---

## Features

- **Data Extraction:** Fetches all comments from a specified YouTube video, handling pagination to retrieve large volumes of comments.
- **Data Transformation:** Processes raw API responses to extract relevant information such as comment author, comment text, and timestamps.
- **Data Loading:** Saves the extracted comments into CSV files for easy storage and further analysis.
- **Data Analysis:** Uses ChatGPT to generate prioritized insights from the collected comments, helping identify content strengths, weaknesses, and areas for improvement.
- **Automation:** Optionally integrates Apache Airflow to schedule and automate the ETL workflow.

---

## Technologies Used

- Python 3.x
- [Google API Python Client](https://github.com/googleapis/google-api-python-client)
- Pandas (for data handling)
- Apache Airflow (for orchestration and automation)
- OpenAI ChatGPT (for comment analysis and insight generation)

---

## Setup Instructions

### 1. Enable YouTube Data API & Obtain API Key

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create or select a project.
3. Enable the **YouTube Data API v3**.
4. Navigate to **Credentials** and create an **API Key**.
5. (Optional) Restrict your API key to specific IPs or referrers for security.

### 2. Install Required Python Packages

```bash
pip install google-api-python-client pandas apache-airflow
