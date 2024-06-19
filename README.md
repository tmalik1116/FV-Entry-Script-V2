# FV-Entry-Script-V2

Modified Python script for automation of adding deficiencies to Field View V2.0

V1.0 read Excel data from a .csv file and required more logic in order to convert a task to its subtrade,
and for correctly identifying and selecting the location of the deficiency within the building based on its description.

This version reads from a .txt file (which I had already converted from a pdf using different Python code),
and assigns all deficiencies to Chandos, due to the absence of the correct subtrade in the Field View list.

This is not a plug and play solution, it was designed to work with my specific computer setup. However it can be adapted 
quite easily to be much more broadly applicable.

Talha Malik, June 19, 2024
