.. raw:: html

  <script type="text/javascript" src="js/jquery-1.7.2.min.js"></script>
  <script type="text/javascript" src="js/jquery-shuffle.js"></script>
  <script type="text/javascript" src="js/rst-form.js"></script>
  <script type="text/javascript">$nmbr_prop = 4</script>


=========================================
Mission X : The Network Layer, Principles
=========================================

These questions aim to let you train yourself on your understanding of the
course material. Be aware that the following questions doesn't cover all the
chapter.

These questions suppose that you have read the control plane part of the fifth
chapter

Question 1. Shortest Path Tree
------------------------------

Consider the following network topology. Only one of the graphs below shows the correct shortest path tree from router A. Which one?

  .. figure:: ../../png/network/qcm1-1-shortestPath.png
     :align: center
     :scale: 100

.. class:: positive

-
  .. figure:: ../../png/network/qcm1-1-solution1.png 
     :align: center
     :scale: 100
  
-
  .. figure:: ../../png/network/qcm1-1-solution2.png 
     :align: center
     :scale: 100

.. class:: negative

-
 .. figure:: ../../png/network/qcm1-1-wrong1.png 
     :align: center
     :scale: 100
-
 .. figure:: ../../png/network/qcm1-1-wrong2.png 
     :align: center
     :scale: 100

Question 2. Distance Vector Routing
------------------------------------

Assume that the network from question 1 uses Distance Vector Routing. After
some time, the routers have build their routing tables.
Only one of these routing tables is correct. Which one?

  .. figure:: ../../png/network/qcm1-1-shortestPath.png
     :align: center
     :scale: 100

.. class:: positive

-
  .. code-block:: c

        Router A: (A=0[local], B=4[South], C=3[South-East], D=6[South-East], E=8[South])

-
  .. code-block:: c

        Router A: (A=0[local], B=4[South], C=3[South-East], D=6[South-East], E=8[South-East])
     
-
  .. code-block:: c

        Router C: (C=0[local], A=3[North-West], B=7[North-West], D=3[Noth-East], E=5[South-East])
     
-
  .. code-block:: c

        Router D: (D=0[local], A=6[South-West], C=3[South-West], B=10[South-West], E=8[South-West])
     

.. class:: negative

-
  .. code-block:: c

        Router A: (B=4[South], C=3[South-East], D=6[South-East], E=8[South])
-
  .. code-block:: c

        Router A: (A=0[local], B=4[South], C=3[South-East], D=10[West], E=8[South-East])
     
-
  .. code-block:: c

        Router C: (C=0[local], A=3[North-West], B=7[East], D=3[Noth-East], E=5[South-East])
     
-
  .. code-block:: c

        Router D: (D=0[West], A=6[South-West], C=3[South-West], B=8[South-West], E=8[South-West])
     


Question 3. Link state routing
-------------------------------

    Assume that the network from question 1 uses link state routing. After a certain time, all the routers have received all the information about all the routers. Which of these could be a LSP sent by one router of the network? The format of LSP messages is: LSP : [Sender Name] [Age] [Sequence Number] [List of Adjacent Active Links].

.. class:: positive

-
  .. code-block:: c

      LSP : A 60 31 [C:3];[D:10];[B:4]



-
  .. code-block:: c

      LSP : D 15 5 [C:3];[A:10];[E:10]


-
  .. code-block:: c

      LSP : C 24 26 [D:3];[A:3];[E:5]


-
  .. code-block:: c

      LSP : B 12 1 [A:4];[E:4]


-
  .. code-block:: c

      LSP : E 10 18 [C:5];[D:10];[B:4]


.. class:: negative

-
  .. code-block:: c

      LSP : A 15 24 [C:3];[D:6];[B:4];

  .. class:: comment

	 	 A LSP from a router contains informations about the links connected to him and to which neighbour they are connected. It does not compute a shortest path. The cost from A to D is thus 10 not 6.

-
  .. code-block:: c

      LSP : A 60 19 [C:3];[D:6];[B:4];[E:8]

  .. class:: comment

	 	 A LSP from a router contains informations about the links connected to him and to which neighbour they are connected. It does not give information about how he can reach other routers.

-
  .. code-block:: c

      LSP : D 21 60 [C:3];[A:6];[E:8]

  .. class:: comment

	  	A LSP from a router contains informations about the links connected to him and to which neighbour they are connected. It does not compute a shortest path. The cost from A to D is thus 10 not 6.


-
  .. code-block:: c

      LSP : D 15 63 [C:3];[A:6];[E:8];[B:10]

  .. class:: comment

	 	 A LSP from a router contains informations about the links connected to him and to which neighbour they are connected. It does not give information about how he can reach other routers.



-
  .. code-block:: c

      LSP : C 32 1 [D:3];[A:3];[E:5];[B:7]

  .. class:: comment

	 	 A LSP from a router contains informations about the links connected to him and to which neighbour they are connected. It does not give information about how he can reach other routers.

-
  .. code-block:: c

      LSP : B 47 62 [A:4];[E:4];[C:7];[D:10]

  .. class:: comment

	  	A LSP from a router contains informations about the links connected to him and to which neighbour they are connected. It does not give information about how he can reach other routers.


-
  .. code-block:: c

      LSP : E 25 25 [C:5];[D:8];[B:4]

  .. class:: comment

		  A LSP from a router contains informations about the links connected to him and to which neighbour they are connected. It does not compute a shortest path. The cost from E to D is thus 10 not 8.

-
  .. code-block:: c

      LSP : E 14 18 [C:5];[D:8];[B:4];[A:8]

  .. class:: comment

		  A LSP from a router contains informations about the links connected to him and to which neighbour they are connected. It does not give information about how he can reach other routers.



Question 4. Distance vector routing
------------------------------------

The routers from question 1 uses distance vector routing. They send their distance vector regularly over all their interfaces. 
Which one of these sequences of message could have been generated by the network from question 1?

  .. figure:: ../../png/network/qcm1-1-shortestPath.png
     :align: center
     :scale: 100

.. class:: positive

-
  .. code-block:: c

      - [D=0]
      - [A=0, D=10]
      - [B=0]
      - [C=0, A=3, D=3]
      - [E=0, A=8, B=4, C=5, D=8]
      - [D=0, A=6, B=14, C=3, E=10]
      - [B=0, A=4, C=9, E=4, D=14]
      - [A=0, B=4, C=3, D=6, E=8]


-
  .. code-block:: c

      - [C=0]
      - [A=0, C=3]
      - [D=0, C=3, A=10]
      - [E=0, A=20, C=5, D=10]
      - [B=0, A=4, E=4, C=7, D=14]
      - [C=0, A=3, D=3, E=5]
      - [E=0, A=8, C=5, D=8, B=4]
      - [A=0, B=4, C=3, D=6, E=8]


.. class:: negative

-
  .. code-block:: c

      - [B=0]
      - [C=0]
      - [D=0, C=3]
      - [A=0, B=4, C=3, D=10]
      - [E=0, C=5, B=4, D=10]
      - [D=0, A=6, B=14, C=3, E=10]
      - [B=0, A=4, C=7, E=4, D=14]
      - [A=0, B=4, C=3, D=6, E=8]
      - [C=0, A=3, D=3, E=5, B=7]

  .. class:: comment

	 	 At line 6: The router D can't know he can reach A with weight 6 until the router C sends its new vector.

-
  .. code-block:: c

      - [D=0]
      - [A=0, D=10]
      - [B=0, A=4]
      - [C=0, A=3, D=3, B=7]
      - [E=0, A=8, B=4, C=5, D=10]
      - [D=0, A=6, B=10, C=3, E=10]
      - [B=0, A=4, C=7, E=4, D=14]
      - [A=0, B=4, C=3, D=6, E=8]

  .. class:: comment

	 	 At line 4: The router C can't know how to reach B. Indeed B has sent his Vector to A and E, B will be reachable by C only when A or E send their Vector.
-
  .. code-block:: c

      - [C=0]
      - [A=0, C=3]
      - [D=0, C=3, A=6]
      - [E=0, A=8, C=5, D=10]
      - [B=0, A=4, E=4, C=9, D=14]
      - [C=0, A=3, D=3, E=5]
      - [E=0, A=8, C=5, D=5, B=4]
      - [A=0, B=4, C=3, D=6, E=8]

  .. class:: comment

	 	 At line 3: The router D know the route to A with weight 10. He learn later the route with weight 6.


Question 5. Failure with Distance Vector Routing
-------------------------------------------------

Consider that the network has reached a state where the router A, C, D have received
distance vectors from each of them. For an unknown reason, these routers have
never heard about B and E. Then, the link between the router A and D fail. What
will happen ?

 .. figure:: ../../png/network/qcm1-5-vectorRouting.png 
     :align: center
     :scale: 100
 
.. class:: positive

- Routers A and D notice after a sufficient delay (How much ?) that they own a route which
  is too old. The next distance vector for A will be [A=0, D=inf, C=3] and the next
  distance vector for D will be [ D=0, A=inf, C=3]. Then C share its distance vector
  to A and D and the failure is recovered.


.. class:: negative

- Routers A and D notice after a sufficient delay (How much ?) that they own a route which
  is too old. The next distance vector for A will be [A=0, C=3, D=inf B=inf, E=inf] and the next
  distance vector for D will be [D=0, A=inf, C=3, B=inf, E=inf].

  ..class:: comment 
      
      How can they know something about B and E ? They never sent any distance
      vector.



- Either router A or router D notice first the failure (let's say that A notice
  first) and sent its vector routing to the others with inside D=inf. When router C
  receive the distance vector, it updates its own distance vector and sent it
  to D. Thanks to that, D notice the failure and update its distance vector to
  [A=6, C=3, D=0]

  .. class:: comment

      It could be useful to read again the chapter Distance Vector Routing, where you will find a complete example about failure. The pseudo-code in this chapter could help you to understand correctly the algorithm. in the above affirmation, C has nothing to update from A about the A-D failure because the failure is not on its way to reach any routers. Also D doesn't learn a failure by someone else, D must see it by itself.


Question 6. The count to infinity problem
------------------------------------------

Consider that we have the following network where Distance Vector Routing run
and has reach a stable state where all the routers are known with the best
route. 
Which sequence of events must appear to cause a count to infinity probleme
between router B and E ?


(Which links must fail and which events must occur in order to have a
count to infinity problem between router B and E ?)

 .. figure:: ../../png/network/qcm1-6-vectorRouting.png 
     :align: center
     :scale: 120

.. class:: positive

- links A-B, C-E and D-E must fail, then E could notice the failures with the link
  C-E and D-E. E update its routing table and its vector to [E=0, B=4, A=8, C=inf, D=inf]
  and sent it to its neighbors (B here). But the vector is lost. B, which
  doesn't have noticed yet the failure with the link A-B, sent its vector 
  [B=0, A=4, E=4, C=7, D=10] to E. After have sent its vector, B notice the
  failure and update its table routing. The count to infinity appears when B
  and E start to exchange their vectors.

.. class:: negative

- The link between B and E and the link between C and E must fail, then
  consider that all message sending by B and E are lost. B and E will have the
  count to infinity problem when receiving distance vector by A and D
  respectively.

  .. class:: comment

        The link between D and E must also fail. without this fail, the network
        can eventually recover for any succesion of events.
 
- links A-B, C-E and D-E must fail then both B and E notice the failures
  exactely at the same time. The count to infinity problem begin when B and E
  start to exchange distance vector.

  .. class:: comment

        if B and E notice the failures at the same time, the count to infinity
        problem can't occur. The distance vector sent will have infinity value
        for unreachables routers.

  
Question 7. Link State Routing
------------------------------

Link state routing is an other type of routing protocols. When a router use link state routing, it sends message on the network. Only one of these affirmations is correct. Which one?

.. class:: positive

-
    A link state router sends periodically a ``HELLO`` message to all its neighbours.

-
    A link-state router sends link-state packets to its neighbours. If this lsp is newer than the one stored in the link state database of the neighbours, they forwards the lsp on all links except the one over which the LSP was received.

-
    The Link state packet send by a router contains information only about the neighbours of this router.

.. class:: negative

-
    A link state router sends periodically a ``HELLO`` message to all it's neighbours. This ``HELLO`` message is forwarded all over the network.
   
 	 .. class:: comment

	 	 The ``HELLO`` message are not forwarded all over the network.


-
    A link state router sends a ``HELLO`` message once when it boots.
    
 	 .. class:: comment

	 	 The ``HELLO`` message are send periodically.


-
  A link-state router sends link-state packets only to its neighbours. (They are not forwarded further)

 	 .. class:: comment

	 	 LSP are forwarded all over the network (if they are newer than the previously LSP received).


-
    When flooding is used on a network, there is a link state database containing the most recent LSP sent by each router shared between all routers.

  	.. class:: comment

	 	 Each router has his own LSDB. 


Question 8. Differencies between Distance Vector Routing and Link State Routing
--------------------------------------------------------------------------------

Distance Vector Routing and Link State Routing are two different protocols. Find the correct affirmations.


.. class:: positive

-
    The link state routing uses a shorthest path algorithm.

-
    Distance vector are never forwarded.

-
    Link state packets contains the state of directly connected links.
    



.. class:: negative

-
    The count to infinity problem is found in both Distance vector routing and Link state routing.

 	 .. class:: comment

	 	 You have not that problem in the Link state routing protocol.

-
    Distance vector are flooded on the entire network.
 
 	 .. class:: comment

	 	 Distance vector doesn't use the flood method. Flooding is used with link state routing.

-
    A router that implement distance vector routing has a database where distance vector are saved.

 	 .. class:: comment

	 	 Link state routing use database to store LSP, not distance vector.

-
    A link state packet contains information about the entire topology of the network.

  	.. class:: comment

	 	 Link state packet contains only information about the neighbours of the router who sends the LSP.

-
    The link state database eliminates the need of a routing table.


    

