Fumigate

A small demo library to help in NLP's most tedious task text cleaning.

Installation
pip install fumigate
#Get started
How to fumigate(clean) your text data

    1.  from fumigate import Fumes

    2. Instantiate a Fumes object
        fumes = Fumes()

    3. Call the purge method to clean everything.
        result = fumes.purge(<text>)
       
    4. Call the clean method to clean specific things from the methods available.
    
        ## methods is a list containing one or multiple methods available for fumigation.
        result = fumes.clean(<text>, methods=["url" | "sym" | "num" | "emo"], extract=False)
        
        # if extract=True returns tuple with removed characters/strings
        result, garbage = fumes.clean(<text>, methods=["url" | "sym" | "num" | "emo"], extract=True)
