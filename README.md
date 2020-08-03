# CS1116-Lab4

insert_canidate.py
  this program implements a self-processing page:
  The program initially displays a form, which has a textfield, which allow the user to enter the name of a candidate.
  On submit, the program takes the name that the user entered and tries to insert that candidate into the database. If this 
  is successful, the program outputs the form again and a sentence that says that the insertion was successful.
  Your program should prevent the user from inserting a candidate who is already in the database.
 
update_vote.py
  The user will run my display_voting_form.py program that you downloaded in Step 1 to choose a candidate. On submit, 
  the user's choice will be sent to your update_vote.py program. Your program will increment the votes for the chosen candidate.
  Obviously, your program should guard againt a user who tries to vote for a non-existent candidate. Furthermore, your program should 
  use cookies to prevent a user from voting more than once. In this case, it does not matter what data is in the cookie, 
  since you are simply using it to detect whether this is a repeat visit or not. Just choose any sensible name and value
