==========================================================
Mission X : The datalink layer and the Local Area Network
==========================================================


Question 1. Type of errors in the physical layer.
--------------------------------------------------

Which of the following sentences is not an error in the physical layer
?

.. class:: postive

- The value of a bit transmitted is modified.

- The layer may deliver more bits to the receiver than the number of bits sent
  by the sender.
- The layer may deliver fewer bits to the receiver than the number of bits sent
  by the sender


.. class:: negative

- An inversion of all the bits.
  
  .. class:: comment
        
        even if it's eventually "possible" that a physical layer reverse all
        the bits, it's highly unlikely that this kind of error is caused by the
        physical layer.

- a sequence of bit shifting

Question 2. Framing problem - Bit stuffing.
--------------------------------------------

Let's say that a frame is fixed and composed of 16 bits (In practice this is
not the case).
Using the generic solution called bit stuffing to recover from errors caused by
the physical layer, which of the following transmitted frame is correct. (The frame
boundary marker is 01111110)

   ===========================   =============================================
   Original frame                 Transmitted frame
   ===========================   =============================================

.. class:: positive


-  ================  ================================
   0001001010000110  01111110000100101000011001111110
   ================  ================================

-  ===============================  ========================================================
   1111110110111100110101101110101  01111110111110101101111000111111011010110111010101111110
   ===============================  ========================================================
.. class:: negative

-  ================ ================================
   0111111000101010 01111110011111100010101001111110
   ================ ================================
-  ================ ================
   0111111001111110 0111111001111110
   ================ ================
-  ================================================ =========================================================================
   011111100010101001111001010101011011011101010110 0111111001111101000101010011111100111100101010101011111101011011101010110
   ================================================ =========================================================================