.. raw:: html

  <script type="text/javascript" src="js/jquery-1.7.2.min.js"></script>
  <script type="text/javascript" src="js/jquery-shuffle.js"></script>
  <script type="text/javascript" src="js/rst-form.js"></script>
  <script type="text/javascript">$nmbr_prop = 4</script>


==========================================================
Mission X : The datalink layer and the Local Area Network
==========================================================


Question 1. Type of errors in the physical layer.
--------------------------------------------------

Which of the following sentences is not an error in the physical layer
?

.. class:: positive

- 
  The value of a bit transmitted is modified.

- 
  The layer may deliver more bits to the receiver than the number of bits sent
  by the sender.
- 
  The layer may deliver fewer bits to the receiver than the number of bits sent
  by the sender


.. class:: negative

- 
  An inversion of all the bits.
  
  .. class:: comment
        
        even if it's eventually "possible" that a physical layer reverse all
        the bits, it's highly unlikely that this kind of error is caused by the
        physical layer.

- 
  a sequence of bit shifting

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



Question 3. Framing problem - Character stuffing.
-------------------------------------------------

A software-based datalink layer use character stuffing with DLE, STX and ETX as markers. Which one of the following couple original frame - transmitted frame is corect?

  ===========================   =============================================
   Original frame                 Transmitted frame
  ===========================   =============================================


.. class:: positive


-  =========================    =====================================================
   DLE STX 1 2 3 DLE DLE ETX    DLE STX DLE DLE STX 1 2 3 DLE DLE DLE DLE ETX DLE ETX
   =========================    =====================================================

-  ================  ================================================
   DLE DLE DLE DLE   DLE STX DLE DLE DLE DLE DLE DLE DLE DLE DLE ETX 
   ================  ================================================
.. class:: negative

-  =================== ===================================
   1 2 3 4 DLE DLE 7 8 STX 1 2 3 4 DLE DLE DLE DLE 7 8 ETX
   =================== ===================================
-  ================ =======================
   DLE STX DLE ETX  DLE STX DLE DLE ETX
   ================ =======================
-  =========================================== =========================================================================
   DLE A Z R STX DLE ETX ETX DLE 1 1 1 1 0 0 4 DLE STX DLE DLE A Z R DLE STX DLE DLE ETX ETX DLE 1 1 1 1 0 0 4 DLE ETX
   =========================================== =========================================================================



 Question 4. Error detection code
 -----------------------------------

We considere here 16-bits blocs. For each sequence of 3 blocs, we compute parity bloc
where each parity bits of this bloc refer to the bits occupying the same position in the 3 previous blocs.
The parity bloc is therefore used to verify the integrity of the 3 preceiding
blocs, using XOR on the parity bloc received with the parity bloc rebuilded.

Which of these parity blocs is correct ?

.. class:: positive
        
- 
  ..code-block::
        
        1010111011110101
        1110101010101011 
        1111111011111111  
        1011101010100001 => parity bloc

-
  ..code-block::
        
        1010111011110101
        1110101010101011 
        1111111011111111  
        0100010101011110 => parity bloc
        
.. class:: negative

- 
  ..code-block::

        1010101011111001
        0101110110011011
        1010111011111010
        1111111111111111 => parity bloc
-
  ..code-block::

        
        1010111011110101
        1110101010101011 
        1111111011111111  
        1011101001011110 => parity bloc
  
- 
  ..code-block::

        1011101111&10111
        1001011101010101
        1010000011111111
        1010000011111111 => parity bloc

-
  ..code-block::
        
        1011101001100111
        1010101010010101
        1001010111111111
        1011101001100111 => parity bloc



