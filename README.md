# Complete Ecommerce Data Pipeline

# Introduction & Goals
- The aim of this project is to create an entire data pipeline for an Ecommerce-based field. This will cover all stages from Data Ingestion to Visualisation. 
- Orient this section on the Table of contents
- Write this like an executive summary
  - With what data are you working
  - What tools are you using
  - What are you doing with these tools
  - Once you are finished add the conclusion here as well

# Contents

- [The Data Set](#the-data-set)
- [Used Tools](#used-tools)
  - [Connect](#connect)
  - [Buffer](#buffer)
  - [Processing](#processing)
  - [Storage](#storage)
  - [Visualization](#visualization)
- [Pipelines](#pipelines)
  - [Stream Processing](#stream-processing)
    - [Storing Data Stream](#storing-data-stream)
    - [Processing Data Stream](#processing-data-stream)
  - [Batch Processing](#batch-processing)
  - [Visualizations](#visualizations)
- [Demo](#demo)
- [Conclusion](#conclusion)
- [Follow Me On](#follow-me-on)
- [Appendix](#appendix)


# The Data Set
- Explain the data set
The data set I have elected to use is the 'eCommerce Events History in Cosmetics Shop' from the REES46 Marketing Platform - https://rees46.com/. Each column is an event on the retailers website from the following list:
- a product view
- a product added to cart
- a product removed from cart
- a product purchase

The dataset is fairly large at 2.27GB and ~ 8.5 million rows, but sits below the AWS Free tier boundaries i.e. > 5GB in S3 (https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc), so seems a reasonable choice. 

The dataset can be downloaded from kaggle: https://www.kaggle.com/mkechinov/ecommerce-events-history-in-cosmetics-shop?select=2019-Dec.csv

- Why did you choose it?

This dataset lent itself to a many business cases, such as pricing, churn, RFM clustering etc, which are common high level concepts that are reguarly demanded within the eCommerce space. In addition, simulations of real-time dashboards would be possible i.e. top-level sales, category breakdown, etc. 

- What do you like about it?


- What is problematic?

The timescale of the data is fairly limited (October 2019 - February 2020) which could put limitations on making estimates regarding customer LTV (lifetime value) or extrapolating in order to make predictions. The cyclical nature of eCommerce sales means that this factor is especially significant when considering this dataset. 

- What do you want to do with it?

# Used Tools
- Explain which tools do you use and why
- How do they work (don't go too deep into details, but add links)
- Why did you choose them
- How did you set them up

## Connect
## Buffer
## Processing
## Storage
## Visualization

# Pipelines
- Explain the pipelines for processing that you are building
- Go through your development and add your source code

## Stream Processing
### Storing Data Stream
### Processing Data Stream
## Batch Processing
## Visualizations

# Demo
- You could add a demo video here
- Or link to your presentation video of the project

# Conclusion
Write a comprehensive conclusion.
- How did this project turn out
- What major things have you learned
- What were the biggest challenges

# Follow Me On
Add the link to your LinkedIn Profile

# Appendix

[Markdown Cheat Sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
