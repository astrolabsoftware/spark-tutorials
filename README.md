# Learning Apache Spark by the example

Welcome to the series of notebooks on Apache Spark! The main goal of this series is to get familiar with Apache Spark, and in particular its Python API called PySpark. The goal is to introduce few functionalities of interest (and by no means complete!) and I might have done many errors, left many typos, and some parts might be deprecated. Feel free to open an issue ([@JulienPeloton](https://github.com/astrolabsoftware/spark-tutorials/issues/new?body=@JulienPeloton)) if this is the case!

**Under construction**

## Table of content:

- [Part I: Installation and first steps](https://github.com/astrolabsoftware/spark-tutorials/blob/master/spark_tutorial_part1_basics.ipynb)
    - Apache Spark: what it is?
    - Installation @ HOME
    - Using the PySpark shell
    - Your first Spark program
- [Part II: Spark SQL and DataFrames](https://github.com/astrolabsoftware/spark-tutorials/blob/master/spark_tutorial_part2_io.ipynb)
    - Apache Spark Data Sources.
    - Loading and distributing data: Spark SQL and DataFrames.
    - Hands-on: RDD vs DataFrame, partitioning, limits, ...
- [Part III: Data manipulation](https://github.com/astrolabsoftware/spark-tutorials/blob/master/spark_tutorial_part3_manipulation.ipynb)
    - Strict vs non-strict (lazy) evaluation
    - Transformations vs actions
    - User Defined Functions
    - Cache or not cache? That's the question.
- Part IV: Spark UI and debugging
    - Monitoring logs and understanding them
- Part V: Testing Spark applications
    - Testing using doctest.
    - Automating with Travis.
- Part VI: Interfacing with Spark
    - From Spark to PySpark: understanding log4j
    - Interfacing C++ libraries with PySpark
    - C/C++/Fortran to Scala

- [Appendix A: Apache Spark @ NERSC](https://github.com/astrolabsoftware/spark-tutorials/blob/master/spark_tutorial_appA_at_nersc.ipynb)
    - Apache Spark and HPC machines
    - Batch jobs @ NERSC
    - JupyterLab @ NERSC

- Appendix B: Apache Spark @ DESC
    - Some examples on how to use Spark with LSST data

- [FAQ](https://github.com/astrolabsoftware/spark-tutorials/blob/master/spark_tutorial_FAQ.ipynb)

## Bibliography and useful links

### Bibliography

- Databricks: [Research papers](https://databricks.com/resources/type/research-papers/page/2) on Apache Spark (e.g. [foundation](https://pages.databricks.com/rs/094-YMS-629/images/hotcloud_spark.pdf), [rdd](https://pages.databricks.com/rs/094-YMS-629/images/nsdi_spark.pdf))
- HDFS: [The Hadoop distributed file system](http://storageconference.us/2010/Papers/MSST/Shvachko.pdf).
- Scientific Spark: [spark-fits](https://arxiv.org/abs/1804.07501), [Apache Spark for physicists](https://arxiv.org/abs/1807.03078) + see bibliography at the end of those papers.
- Books: Spark, Scala.

### Links

- Apache Spark documentation: https://spark.apache.org/docs/latest/
