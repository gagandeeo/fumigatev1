from fumigate import Fumes
import re

test = [
            "hey amazon - my package never arrived \
            One of the other reviewers has mentioned that after watching just 1 Oz episode you'll be hooked. They "
            "are right, as this is exactly what happened with me.<br /><br /> ",
            "I sure would like to see a resurrection of a up dated Seahunt series with the tech they have today it "
            "would bring back the kid excitement in me.I grew up on black and white TV and Seahunt with Gunsmoke were "
            "my hero's every week.You have my vote for a comeback of a new sea hunt.We need a change of pace in TV "
            "and this would work for a world of under water adventure.Oh by the way thank you for an outlet like this "
            "to view many viewpoints about TV and the many movies.So any ole way I believe I've got what I wanna "
            "say.Would be nice to read some more plus points about sea hunt.If my rhymes would be 10 lines would you "
            "let me submit,or leave me out to be in doubt and have me to quit,If this is so then I must go so lets do "
            "it. ",
            " 😆 👨 https://www.amazon.com/gp/css/order-history?ref_=nav_orders_first please fix asap! @amazonhelp\
            hey amazon - my package never arrived ",
            "https://www.amazon.com/gp/css/or🧑‍🍼der-history?ref_=nav_orders_first please fix asap! @amazonhelp"
        ]
fumes = Fumes()
# text = fumes.clean("hey amazon - my package never arrived https://www.amazon.com/gp/css/order-history?ref_=nav_orders_first please fix asap! @amazonhelp ",
#                    methods=["url"], extract=True)
# print(text)
# print(re.findall(r'(\w+:\/\/\S+)|^rt|http.+?', test[2]))
# print(re.findall(r'\d+', "1234"))
# print([fumes.clean(x, methods=["url", "stopwords", "emo", "num"]) for x in test])
text = [fumes.purge(txt) for txt in test]
print([fumes.lemm(txt, pos='a') for txt in text])
