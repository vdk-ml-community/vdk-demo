# Applying DevOps Practices in Data and ML Engineering


## Table of Contents

- [Purpose](#purpose)
- [Pre-requisites:](#pre-requisites-)
- [Feedback](#feedback)
- [Background](#background)
  * [VDK](#vdk)
    + [Create the Data Job Files](#create-the-data-job-files)
    + [Data Job Code](#data-job-code)
    + [Deploy Data Job](#deploy-data-job)
- [Exercises](#exercises)
- [Lessons Learned](#lessons-learned)
- [Where to Find Us](#where-to-find-us)


<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## Purpose
The purpose of this scenario is to show how to:
* Create a data job with VDK
* Ingest data into a database 
* Process data  
* Process data
* Deploy the data job 
* Develop a plugin that enhance either security or stability

## Pre-requisites:
- Bring your own laptop
- Make sure you connect to the Wi-Fi
- Check that you can open the MyBinder tied to Workshop 1

## Feedback
Please share your feedback : https://bit.ly/vdk-ml-community

Give as a star if you've liked the [project](https://github.com/vmware/versatile-data-kit).


## Background

### Versatile Data Kit 
The Versatile Data Kit framework allows you to implement automated pull ingestion and batch data processing, manage and operate data jobs by applying best DevOps practices.

#### Create the Data Job Files

Data Job directory can contain any files, however there are some files that are treated in a specific way:

* SQL files (.sql) - called SQL steps - are directly executed as queries against your configured database;
* Python files (.py) - called Python steps - are Python scripts that define run function that takes as argument the job_input object;
* config.ini is needed in order to configure the Job. This is the only file required to deploy a Data Job;
* requirements.txt is an optional file needed when your Python steps use external python libraries.

Delete all files you do not need and replace them with your own.

#### Data Job Code

VDK supports having many Python and/or SQL steps in a single Data Job. Steps are executed in ascending alphabetical order based on file names.
Prefixing file names with numbers makes it easy to have meaningful file names while maintaining the steps' execution order.

Run the Data Job from a Terminal:
* Make sure you have vdk installed. See Platform documentation on how to install it.
```
vdk run <path to Data Job directory>
```

#### Deploy Data Job

When a Job is ready to be deployed in a Versatile Data Kit runtime (cloud):
Run the command below and follow its instructions (you can see its options with `vdk --help`)
```python
vdk deploy
```

## Exercises
Please open up MyBinder to get started on the exercises! 

A few tips: 
 - The mybinder notebook has a idle timeout of 10 minutes. One trick to prevent it after launching, open terminal and execute `while echo "foo"; do sleep 100 ; done`
 
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/vdk-ml-community/vdk-demo/HEAD?urlpath=lab/tree/setup.ipynb)


If you have any issue with above link try 
 - [First backup link](http://a1a89deb4a79f44279c470dada8dab7f-727617251.us-west-1.elb.amazonaws.com/v2/gh/versatile-data-kit-amld/linear-regression-example-unsolved/HEAD?urlpath=lab/tree/setup.ipynb)
 - [Second backup link](https://gesis.mybinder.org/v2/gh/versatile-data-kit-amld/linear-regression-example-unsolved/HEAD?urlpath=lab/tree/setup.ipynb)
 

For more information on MyBinder, please visit:

https://mybinder.readthedocs.io 

## Lessons Learned
Through this scenario, you created a data job, which:
* Ingest data using Ingestion API
* Process data using SQL
* Deploy in a managed runtime environment
* Track versions of both system code and user code 
* Create system plugins to affect all deployed jobs

## Where to Find Us
- [GitHub](https://github.com/vmware/versatile-data-kit)
- [YouTube](https://www.youtube.com/channel/UCasf2Q7X8nF7S4VEmcTHJ0Q/about)
- [Twitter](https://twitter.com/vdkproject)
- Relevant Articles
  - [An Overview of Versatile Data Kit](https://towardsdatascience.com/an-overview-of-versatile-data-kit-a812cfb26de7)
  - [Versatile Data Kit Medium ](https://medium.com/versatile-data-kit)

**Congrats!**

