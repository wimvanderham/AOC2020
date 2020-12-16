/*------------------------------------------------------------------------
    File        : day-15.p
    Purpose     : Solve AOC Day 15

    Syntax      :

    Description : 

    Author(s)   : Wim van der Ham
    Created     : Tue Dec 15 22:32:25 CET 2020
    Notes       :
  ----------------------------------------------------------------------*/

/* ***************************  Definitions  ************************** */

BLOCK-LEVEL ON ERROR UNDO, THROW.

DEFINE TEMP-TABLE ttNumber
   FIELD iNumber   AS INTEGER 
   FIELD iLastTurn AS INTEGER 
INDEX indNumber IS UNIQUE iNumber.

DEFINE VARIABLE cFileName  AS CHARACTER NO-UNDO.
DEFINE VARIABLE cStartList AS CHARACTER NO-UNDO.
DEFINE VARIABLE iTurn      AS INTEGER   NO-UNDO.
DEFINE VARIABLE iNumber    AS INTEGER   NO-UNDO.
DEFINE VARIABLE iNewNumber AS INTEGER   NO-UNDO.
DEFINE VARIABLE iP1        AS INTEGER   NO-UNDO.
DEFINE VARIABLE iP2        AS INTEGER   NO-UNDO.
DEFINE VARIABLE dtStart    AS DATETIME  NO-UNDO.
DEFINE VARIABLE dtP1       AS DATETIME  NO-UNDO.
DEFINE VARIABLE dtP2       AS DATETIME  NO-UNDO.

/* ********************  Preprocessor Definitions  ******************** */


/* ***************************  Main Block  *************************** */

ASSIGN 
   cFileName = "C:\Users\Wim\Documents\AOC\2020\input_15.txt"
.
FILE-INFO:FILE-NAME = cFileName.
IF FILE-INFO:FILE-TYPE EQ ? THEN DO:
   MESSAGE SUBSTITUTE ("Input file:~n~n'&1'~n~nnot found.", cFileName)
   VIEW-AS ALERT-BOX.
   RETURN.
END.

INPUT FROM VALUE (FILE-INFO:FULL-PATHNAME).
IMPORT UNFORMATTED 
   cStartList.
INPUT CLOSE.
  
MESSAGE SUBSTITUTE ("Start List: '&1'.", cStartList)
VIEW-AS ALERT-BOX.

dtStart = NOW.
iTurn = 1.
DO WHILE iTurn LE 30000000
WITH DOWN:
   IF iTurn LE NUM-ENTRIES (cStartList) THEN DO:
      /* First build the numbers called in the start list */
      /*
      ** In this game, the players take turns saying numbers. 
      ** They begin by taking turns reading from a list of starting numbers 
      ** (your puzzle input).
      */ 
      iNumber = INTEGER (ENTRY (iTurn, cStartList)).
      
      FIND  ttNumber
      WHERE ttNumber.iNumber EQ iNumber NO-ERROR.
      IF NOT AVAILABLE ttNumber THEN DO:
         CREATE ttNumber.
         ASSIGN 
            ttNumber.iNumber = iNumber
         .
      END.
      ASSIGN 
         ttNumber.iLastTurn   = iTurn
      .
   END.
   ELSE DO:
      /* Now determine new number based on the rules:
      ** Then, each turn consists of considering the most recently spoken number:
      ** If that was the first time the number has been spoken, 
      **   the current player says 0.
      ** Otherwise, the number had been spoken before; 
      **   the current player announces how many turns apart the number is 
      **   from when it was previously spoken.
      */
      IF iTurn - 1 EQ 2020 THEN DO:
         iP1  = iNumber.
         dtP1 = NOW.
      END.
      
      FIND  ttNumber
      WHERE ttNumber.iNumber EQ iNumber NO-ERROR.
      IF AVAILABLE ttNumber THEN DO:
         iNewNumber = iTurn - ttNumber.iLastTurn - 1.
      END.
      ELSE DO:
         CREATE ttNumber.
         ASSIGN 
            ttNumber.iNumber = iNumber
         .
         iNewNumber = 0.
      END.

      ASSIGN 
         ttNumber.iLastTurn = iTurn - 1
      .
      
      iNumber = iNewNumber.
   END.
   
/*    IF iTurn GE 30000000 - 10 THEN DO:  */
/*       /* Almost there */ */
/*       DISPLAY                          */
/*          iTurn iNumber                 */
/*       .                                */
/*    END.                                */
   iTurn = iTurn + 1.
END.

iP2 = iNumber.                            
dtP2 = NOW.
       
MESSAGE "Solutions:" SKIP (1)
SUBSTITUTE ("Part 1: &1. Found in &2 seconds.", iP1, INTERVAL(dtP1, dtStart, "seconds")) SKIP 
SUBSTITUTE ("Part 2: &1. Found in &2 minutes.", iP2, INTERVAL(dtP2, dtStart, "minutes"))
VIEW-AS ALERT-BOX INFORMATION.
