In this repository  we focus on describing ``HTSeq-Hadoop`` which extends the ```HTSeq``<http://www-huber.embl.de/users/anders/HTSeq/doc/index.html>`_ package with Hadoop implementations.
``HTSeq`` provides an Application Programming Interface (API) to manipulate
raw and processed MPS data using the Python programming language. A limitation
of  ``HTSeq`` is that it is generally restricted to a single thread, though
allowing to scale up to a whole multicore node in some cases.


 We modified two widely used tools from ``HTSeq`` in
  RNA-seq analysis: ``htseq-count`` for counting how many reads are mapped to
  the genes and ``htseq-qa`` for  quality assessment of raw or mapped reads.
  These were adapted to run in the Hadoop framework in order to significantly
  increase the scalability. 
  
  The runtime performance of ``HTSeqCount`` under
  Hadoop was compared with the Pig Latin script on the ``Apache Pig``
  platform. 
  The choice of Hadoop-streaming allowed us to involve the
  ```GNU-parallel``<http://www.gnu.org/software/parallel/>`_
  utility to run ``HTSeq-Hadoop`` in  multiple threads on the multicore Linux
  workstations or on a cluster node. 
  
  The documentation for the ``HTSeq-Hadoop`` is available `here <http://raalesir.github.io/sphinxdoc-test>`_.
