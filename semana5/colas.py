# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 20:52:09 2021

@author: Osvaldo
"""

# FIFO (First Input First Output). 
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry") 
queue.append("Graham") 
queue.popleft()
queue.popleft()
queue