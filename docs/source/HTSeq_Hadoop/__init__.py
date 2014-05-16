

"""
This module is aiming to extend two utilities ``htseq-count`` and ``htseq-qa`` from the `HTSeq <http://www-huber.embl.de/users/anders/HTSeq/doc/index.html>`_ package to the Hadoop Map-Reduce platform, thus making possible to apply these utilities to the Next Generation Sequencing (NGS) data in a massively parallel manner.

In order to function the ``HTseq`` package must be installed and available in the Python path.
See the `installation <http://www-huber.embl.de/users/anders/HTSeq/doc/install.html>`_ section in the HTSeq package documentation.

.. moduleauthor:: Alexey Siretskiy <alexey.siretskiy@it.uu.se>

"""


import HTSeqQA_mapper
import HTSeqQA_reducer
import HTSeqCount_mapper
import HTSeqCount_reducer

