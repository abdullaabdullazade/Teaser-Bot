import discord
from discord.ext import commands

intents = discord.Intents(messages=True, guilds=True, members=True, reactions=True)

Bot = commands.Bot(command_prefix="/", intents=intents)


@Bot.event
async def on_ready():
    print("Hazıram!")





@Bot.command()
async def start(msg):
    await msg.send("""
Bot işləyir.Sizə kömək üçün burdayam.""")


@Bot.command()
async def thenounsuffixesandprefix(msg):
    await msg.send("""
1. Choose the correct line of the noun forming suffixes. 
A) ty, teen, ous, er B) ist, ism, ion, less  C) sness, hood, ess, ence   D) ldom, ify, ism, ist E) dage, ure, en, ive  
2. Choose the correct line of the noun forming suffixes. 
A) tion, or, ish, ful   B)  ent, ly, ible, ian C)  ıze, ate, en, ize  D) ar, al, an, ant E)  hood, ance, ship, less  
3. Which suffixes can be added to the word “act”? 
A) tion, ence  B)  ess, ist   C)  ant, y D) ese, tion  E)  tion, or  
4. Choose the correct suffix which forms nouns form the words “attend” and “resist”. 
A) ance B)  ence   C)  age  D) ess    E)  ese  
5. Which suffixes can be added to the word “invent”? 
A) ism, age  B)  ar, tion  C)  ian, or  D) or, ion   E)  er, an  
6. With which word doesn’t the suffix –ship make a new word? 
A) friend    B)  differ C)  leader D) member   E)  intern   
7. With which word doesn’t the suffix –ment make a new word? 
A) Pollute  B)  Agree  C)  Govern D) Develop  )  Punish  
8. With which word doesn’t the suffix –dom make a new word? 
A) free   B)  wise   C)  argue D) bore  E)  martyr  
9. With which word doesn’t the suffix –ence  make a new word? 
A) differ  B)  refer  C)  happy D) prefer  E)  exist  
10. With which word doesn’t the suffix –th make a new word? 
A)  clever  B)   wide C)   strong D)  long  E)  deep  
11. Choose the line of nouns with suffixes or prefixes. 
A) brother, community, meeting B)  self – criticism, musician, hopeless C)  happiness, election, beauty D) sadness, discussion, attendance E)  interesting, building, prewar   
12. Choose the line of nouns with suffixes or prefixes. 
A)  inaccuracy, supermarket, co-operation B)  development, package, careful C)  selfish, doctor, teacher D)  daughter, sailor, freedom E)  disadvantage, deep, dominant       
    """)


@Bot.command()
@commands.bot_has_role("admin")
async def thenounsuffixesandprefixcavab(msg):
    await msg.send("""
    1.C   
    2.D
    3.E
    4.A
    5.D
    6.B
    7.A
    8.C
    9.C
    10.A
    11.D
    12.A
    """)


@Bot.command()
@commands.bot_has_role("admin")
async def thenounsimplederivativeandcompoundnouns(msg):
    await msg.send("""
    1. Choose the line of derivative nouns. 
    A) ability, illness, barrel B)  childhood, classmate, bench C)  connection, weekend, lawyer D) pilgrimage, performance, proposal E)  betrayal, inventor, silver  
    2. Choose the line of compound nouns. 
    A) cameraman, german, cruelty B)  bathhouse, birthplace, mankind C)  comedy, novelist, fisherman D) birthday, look after, headache E)  copybook, landlady, stadium  
    3. Choose the line of compound nouns. 
    A) overall, tongue, oxen B)  reason, football, penknife C)  mother-in-law, sunset, norman D) seaman, reaction, sunrise E)  holdall, briefcase, statesman  
    4. Choose the line of derivative nouns. 
    A) approval, tradition, player B)  father-in-law, airmail, sunshine C)  housemaid, answer, magazine D) farmer, danger, monument E)  movement, freedom, gentleman  
    5. Choose the line of simple nouns. 
    A) bluebell, instrument, tale B)  bedroom, powerful, butterfly C)storm, reason, beard D) bench, scandal, proposal E)  toothbrush, tablecloth, computer
    6. Choose the line of simple nouns. 
    1. woodman   2. german 3. Englisman 4. norman 
    A) 2, 4     B) 1, 3   C) 1, 2    D) 2, 3  E) 1, 4  
    7. Choose the line of derivative nouns. 
    1. agreement  2. monument  3. parliament 4. Argument 
    A) 2, 4 B) 1, 3  C) 1, 2  D) 2, 3  E) 1, 4  
    8. Choose the line of compound nouns. 
    1. handwriting   2. dependence  3. armchair 4. dictation 
    A) 1, 4  B) 1, 3     C) 2, 4     D) 2, 3    E) 1, 2  
    9. Choose the line of compound nouns. 
    1. newspaper  2. language 3. mankind  4. creation 
    A) 1, 2  B) 2, 3 C) 1, 3   D) 1, 4   E) 2, 4  
    10. Choose the line of derivative nouns. 
    1. happiness   2. homeless  3. hopeless   4.  darkness 
    A) 2, 4   B) 1, 3 C) 2, 3     D) 1, 4    E) 1, 2  
    11. Choose the line of simple nouns. 
    A) melody, palace, event B)freedom, election, actress C)student, servant, sailor D) difference, phonetics, economy E)  baggage, middle, inkpot  
    """)


@Bot.command()
async def thenounsimplederivativeandcompoundnounscavab(msg):
    await msg.send("""
    1.C   
    2.D
    3.B
    4.E
    5.A
    6.C
    7.A
    8.E
    9.B
    10.C
    11.D
    """)


@Bot.command()
async def thenouncountableanduncountablenouns(msg):
    await msg.send("""
    1. Choose the correct line of uncountable nouns. 
    A)poetry,mosque, lamp B)music,song,help C)history,lamb, bee D)flood, garbage,wheat E)meat, cash, club 
    2. Choose the correct line of uncountable nouns. 
    A) bottle,door,butter  B)circle,example,bench C)pride,coal,thunder D)toast,scenery,inn E)cash,advice, job  
    3. Choose the correct line of countable nouns. 
    A) camera,baggage,damage B) actor,pencil,pea C) pleasure,lightning,water D)space,oil,literature E)evidence,fear, salt  
    4. Choose the correct uncountable nouns. 
    1. biology  2. ticket  3. music   4. feeling 
    A)1, 3 B)1, 2  C)1, 4   D)2, 3 E)2, 4  
    5. Choose the correct line of uncountable nouns. 
    A) storm, sandwich, idea  B) ımpression, potato, cow C) lie, feeling, idea D) chess, history, news E) art, childhood, advice  
    6. Choose the correct line of countable nouns. 
    A) anger, crime, idea B) view, sound, song C)justice,labour,enemy  D)spoon, cotton, sand E)speed,air,joy  
    7. Choose the correct line of countable nouns. 
    A) suggestion,tear,dream B) absence,alcohol,rice C)interest, honey, knowledge D) reality, petrol, decision E)progress, curd, blood  
    8. Choose the correct uncountable nouns. 
    1. respect  2. wish 3. opinion 4. permission 
    A)1, 2   B)2, 3 C)1, 3   D)1, 4 E)2, 4  
    9. Choose the correct countable nouns. 
    1. scenery  2. argument  3. difficulty 4. machinery 
    A)1, 2  B)2, 4  C)2, 3 D)1, 4 E)1, 3  
    10. Choose the correct line of uncountable nouns. 
    A) beef,furniture,housework B) wool,wood,storm C) ımpression,goose,air D) ice,room,office E)foot, part, paint  
    11. Choose the correct line of uncountable nouns. 
    A) ice, accommodation, rice  B) village, hand, country C) ocean, art, arm D) faith, advice, group E)cloud, wine, fear    
    12. Choose the correct line of countable nouns. 
    A) joke, biology, face   B) exam, event, flour C) power,wood,violence D)art,beef,research E)lady,rabbit,bear   
    """)


@Bot.command()
async def thenouncountableanduncountablenounscavab(msg):
    await msg.send("""
    1.D
    2.C
    3.B
    4.A
    5.D
    6.B
    7.A
    8.D
    9.C
    10.A
    11.A
    12.E
    """)


@Bot.command()
async def thenounpossesivecase(msg):
    await msg.send("""
1. Choose the correct variant. 
 1. The Black`s house 2. The manager`s advice 
 3. Moscow`s theatres  4. A months` holiday 
 A) 1,4  B) 2,3   C) 2,4 D) 3,4 E)  1,2  
2. Choose the correct variant.
A) All children` clothes are expensive.B)Mary`s been to Los Angeles ,and her friends`s too.C)The owl`s eyes are very large. D) Crist`s known as a short name. E)  Sevda`s invited a lot of guests to her henna party.  
3. Choose the correct variant. 
A) It`s alcohol, don`t use it.B) Tural`s neighbours have sold their car.C) My sister`s got some new books.D) Take the child to the childrens’ playground. E)  America`s the bulwark of democracy.  
4.Choose the correct variant. 
 1. These geese`s wings  2.Water`s edge 
 3. Three sheeps’ meal   4.Womens` rights 
 A) 1,2     B) 3,4       C) 2,3    D) 1,4     E) 2,4  
5. Choose the correct variant. 
1. Several day`s leave 3.The film`s merits
2. The company`s plans 4.Policemens` uniforms 
A) 2,4 B) 3,4  C) 1,2  D) 1,4  E)  2,3 
6. Choose the Incorrect variant. 
A) The child`s cry broke the stillness.B) I had a good time at my Uncle`s.C) Elgun hasn`t read J.Londons` stories at all. D) Tears came into the man`s eyes  and ran dawn his cheeks. E)Listen to the teacher`s explanation.  
7. Choose the correct variant. 
A) I`m these girls` English teacher.B) The child`s a high temperature.C) My friend`s lived in Italy.D) My mothers-in-laws` clothes is expensive. E)  State schools are free but private schools are not free.  
8. Choose the correct variant. 
1. A few deers` skin  2.Mice`s tails 
3.A minute`s break   4. A days` rest 
A) 2,3  B) 1,4 C) 1,2 D) 3,4 E) 2,4 
9. Choose the correct variant. 
A) My friend`s got a new office. B) Gunay and Fuad`s wedding party will be next month. C) That exercise`s very difficult. D) The road`s ten metres in width. E) What`s your occupation?  
10. Choose the correct variant. 
1. Those girls` dresses 2. Azerbaijans` banner  3. Two day`s rest  4. The world`s problems    
A) 2,4   B) 3,4 C) 1,4  D) 2,3 E) 1,2
    """)


@Bot.command()
async def thenounpossesivecasecavab(msg):
    await msg.send("""
    1.A
    2.C
    3.B
    4.E
    5.D
    6.C
    7.A
    8.D
    9.B
    10.B
    """)


@Bot.command()
async def thepronounpersonalandpossessivepronouns(msg):
    await msg.send("""
Choose the correct pronoun or pronouns.  
1. … are a good student. 
A) They    B) You   C) We    D) She    E)  He  
2. … doesn’t like tomatoes. 
A) You     B) We      C) She     D) I       E)  They  
3. My students and I always study together. 
A) I       B) They        C) He      D) She     E)  We  
4. … are nice. … like … .
A) They, I, them B) We, She, it C) They, We, it D) You, He, them E)  She, You, them  
5. … is a good actress in Azerbaijan. 
A) I        B) We       C) He D) You  E)  She  
6. Where is the newspaper? … ‘re sitting on … . 
A) We, them         B) She, it       C) They, them  D) You, it             E)  I, them  
7. Why are … looking at …? A) We, his      B) They, its      C) Her, them D) You, they    E)  You, them  
8. … wants the key. Can … give it to … ? 
A) She, you, her B) They, he, him C) He,  I, his D) We, she, them E)  It, you, our  
. … are going to invite all … friends. 
A) They, theirs B) We, our C) You, yours D) They, us E)  You, ours  
10. … is married. … husband works in a bank. 
A) He, you       B) It, they       C) She, her D) We, they       E)  You, are  
11. Listen to … brother! 
A) She and her       B) Her and he   C) She and he’s D) Her and her       E)  She and he  
12. Oxford is famous for … university. 
A) It      B) his     C) It’s    D) their    E)  its  
13. Are … going to wash … hands? 
A) you, your       B) He, him       C) We, us D) You, yours    E)  They, theirs  
14. … want to phone Sam. Do … know … phone number? 
A) We, they, him      B) I, you, his     C) She, he, his D) You, you, her       E)  They, you, him 
15. … are … books. Where are …? 
A) We, our, your   B) You, your, hers C) They, my, yours     D) We, their, their E)  He, his, his  
16. Is this book … or …? 
A) His, her    B) My, your   C) Her, ours D) Mine, yours  E)  Hers, their 
""")


@Bot.command()
async def thepronounpersonalandpossessivepronounscavab(msg):
    await msg.send("""
    1.B
    2.C
    3.E
    4.A
    5.E
    6.D
    7.E
    8.A
    9.B
    10.C
    11.D
    12.E
    13.A
    14.B
    15.C
    16.D  
    """)


@Bot.command()
async def thepronounpersonalpossessiveandreflexivepronouns(msg):
    await msg.send("""
1. Simon calmed ... with an effort.  
A) himselves   B) herself   C) himself D) itself E) themselves  
2. Several times ... reminded ... that he had not rung up Shucklewort yet.  
A) he, himself   B) he, herself  C) they, itself D) we, yourselves    E) she, himself   
3. ... could talk races with Hurstwood, tell interesting incidents concerning ...  . 
A) she, himself   B) she, herself    C) they, itself D) you, themselves   E) I, yourself  
4.  Mind ... own business and I’ll mind ... 
A) her, you   B) mine, his  C) your, my D) my, your  E) your, mine  
5. ... have made myself perfectly pleased here. 
A) she   B) I   C) mine  D) your E) itself  
6. Visitors admire not only Russia ... but also ... customs and historical places.  
A) itself, its  B) themselves, its C) themselves, it’s  D) itself, it’s E) itself, it 
7. Your doctor ... checked up me last month. 
1. himself 2. herself 3.themselves  4.myself 
A) 2,3    B) 3,4 C) 1,2 D) 1,3 E) 1,2,4  
8. ... went to the shops but ... didn’t buy anything. 
A) you, you    B) I, I  C) she, he    D) I, her  E) my, mine  
9.  He got up, washed, showed and dressed ... . 
A) himself  B) herself C) themselves D) - E) myself  
10.I don’t think Nana will get the job. Nana ... doesn’t think she’ll get it.  
A) herself    B) himself         C) themselves D) itself   E) ourselves  
11. ... is not our fault. ... can’t blame ... .  
A) it, our, you  B) they, you, it C) it, you, us D) it, you, she E) we, you, me  
12. Royale doesn’t need to borrow from ... . ... has got money.  
A) your, she  B) them, he C) they, she D) you, her   E) me, she  
13.  ... can give ... advice but ... won’t listen ... has got ideas. 
A) she, him, she, our  B) you, him, she, we C) you, him, he, he  D) he, us, we, we E) I, you, you, you  
14. Irene’s husband brought ... some beautiful shells from the South.  
A) me B) they C) he  D) herself E) their  
15. Children,  do it ... . 
A) themselves  B) yourself  C) yourselves D) itself  E) himself  
    """)


@Bot.command()
async def thepronounpersonalpossessiveandreflexivepronounscavab(msg):
    await msg.send("""
    1.C
    2.A
    3.B
    4.E
    5.B
    6.A
    7.C
    8.B
    9.D
    10.A
    11.C
    12.E
    13.C
    14.A
    15.C
    
    
    """)


@Bot.command()
async def reciprocalanddemonstrativepronouns(msg):
    await msg.send("""
1. Elizabeth and George talked and found ... delightful.  
A) one another B) each other C) each another  D) one another’s  E) each other’s  
2. We said good-bye to ... and arranged to meet in the autumn.  
A) each another  B) each other’s  C) one another  D) one another’s E) each others  
3.  ... cars are white, but ... cars are black. 
So they aren’t ... colour. 
A) these, those, the same   B) this, those, same C) this, that, the same   D) these, that, the same E) these, that, a same  
4. ... town is not a very interesting place to visit, so few tourists come here.  
A) those  B) the same  C) a same D) these    E) this  
5.  Do you like ... shoes? I bought them last week.  
A) these   B) that  C) this D) the same  E) such  
6.  What was the use even of loving, if love ... had to yield to death? (Galsworthy) 
A) your  B) yourself C) myself D) itself  E) themselves  
7.  They blamed ... for ... unlucky marriage. 
A) them, these  B) themselves, this C) their, this   D) yourselves, this E) themselves, these  
8. Sarah and Kate are good friends. They know ... well.  
A) each other B) them        C) themselves D) theirselves E) one another  
9. You must do three of ... exercises tomorrow.  
 1.they  2. these     3. those  4. that 
 A) 2,3,4  B) 1,4    C) 2,3  D) 1,3,5  E) 2,4  
10.  We can help ... . 
 1.one another  2. ourselves  3.one another’s  4. each other 5.yourself 
 A) 1,2,3  B) 1,5 C) 2,4   D) 1,2  E) 1,2,4  """)


@Bot.command()
async def reciprocalanddemonstrativepronouns(msg):
    await msg.send("""
    1.B
    2.C
    3.A
    4.E
    5.A
    6.D
    7.B
    8.A
    9.C
    10.E
    """)


@Bot.command()
async def indefinitepronouns(msg):
    await msg.send("""
Choose the correct pronoun or pronouns.  
1. The wounded were coming into the post, ... were carried on stretches, ... were walking and ... were brought on the bocks of men that came across the field. 
A) some, some, some B) some, any, somebody C) someone, someone, somebody D) any, some, anyone E) any, some, any  
2. - Couldn’t you find tomato sauce, Barto? - No, there wasn’t ... . - Aynur said.  
A) any   B) no   C) some   D) something  E) anyone 
3. Don’t let us have ... nonsense about the job.  
A) anyone    B) anything C) some D) any  E) something  
4. There isn’t ...  in the school. 
A) somebody B) anybody C) any D) some  E) some people  
5. Have you got ... friend?  
A) somebody B) anybody C) any D) some  E) anything  
6.  This evening I’m going out ... friends of mine.  
A) some  B) any   C) somebody D) anybody  E) someone  
7. Can I have ... milk in my coffee, please?   
A) any  B) some  C) anything D) anyone  E) something  
8.  If there are ... words you don’t understand, use a dictionary. 
A) anything  B) something C) anyone D) some  E) any  
9. Can you give me ... information about places of interesting in the town? 
A) something B) some  C) any D) anyone  E) anything  
10.  There is ... at the door. Can you go and see who it is? 
A) anything  B) anyone  C) someone D) anybody E) some  
11.  You must bu hungry. Would you like ... to eat? 
A) any  B) anything  C) any burgers  D) something   E) some  
12.  If there are ... letters for me, can you send them on to this address? 
A) any  B) some C) something D) anything E) anyone  
13. Last night I wrote ... letters to my family and friends. 
1. a few  2. few  3. a little 4.little 
A) 1,2  B) 3,5  C) 1,2,4 D) 1,2,3  E)  2,5  
14.  I’m going out for a walk. I need ... fresh air. 
A) few  B) a little C) a few D) any  E) anything  
15. . ... people in the office are very lazy. They do ... works. 
A) some, few  B) some, a few C) somebody, a little  D) some, little E) any, few 
    
    """)


@Bot.command()
async def indefinitepronounscavab(msg):
    await msg.send("""
1 .A
2 .A
3 .D
4 .B
5 .C
6 .A
7 .B
8 .E
9 .B
10 .C
11 .D
12 .A
13 .A
14 .B
15 .A
    """)


@Bot.command()
async def negativepronouns(ctx):
    await ctx.send("""
Choose the correct pronoun or pronouns.  
1. … of this money is mine. 
A) No  B) None  C) Nothing D) No one  E)  Nowhere  
2. … came to visit me while I was in hospital. 
A) No one  B) Every C) Nowhere D) Anybody  E)  Anyone  
3. … tells me …    . 
A) Everyone,Anything  B) Anybody,Anything C) Nobody,Nothing D) Nobody,Something E)  Nobody,Anything  
4. We had to walk home , because there was …  bus. 
A) None  B) Some  C) No D) Not  E)  A few  
5. I couldn`t make an omelette because there weren`t  …  eggs. 
A) Something B) Some  C) Not D) Any  E)  None  
6. We took a few photographs but …  of  them were very good 
A) None  B) No  C) Every D) Nothing  E)  Anything  
7. I don`t want …  to drink. I`m not thirty 
1. Nothing     2. Anything   3. Something 4. Any drinks 5. Some drinks 
A) 2,4      B) 1,2 C) 3,4     D) 1,4    E)  1,2  
8. The bus was completely empty.There was … on it. 
A) Someone     B) Anybody C) Nobody D) Anyone  E)  Somebody
9. Have you seen my watch? I have looked all over the house I can`t find it …. 
A) Nothing  B) Anything C) No one D) Nowhere  E)  Anywhere  
10. The accident looked serious but fortunately  …  was  injured.  
A) Nobody  B) Anybody C) Anyone D) Someone  E)  Something  
11. - What`s in that box ?  - …. . It`s empty 
A) No  B) Not  C) Anybody D) Nothing  E)  Something  
12. I don`t know  …  about  economics 
A) Nothing  B) Anything      C) Something D) Nowhere  E)  No  
13. I could answer …  of the questions they asked me. 
A) Something B) Every C) Any D) None  E)  No  
14. …  cars are allowed in the city centre. 
A) No  B) Note  C) Any D) Nothing  E)  Anything  
16. – Where are you going? -“ … ,  I`m staying here” 
A) Nobody B) Nowhere     C) Anywhere D) Somewhere E) Anyone  17. The exam was extremely difficult. … passed. 
A) Everybody B) Anybody C) Nobody  D) Any students E)  Nowhere  
18. She had … difficulty finding a job. 
A) Anything  B) Something C) Any D) No  E)  None 
    """)


@Bot.command()
async def negativepronounscavab(ctx):
    await ctx.send("""
1 .B  
2 .A
3 .E
4 .C
5 .D
6 .A
7 .A
8 .C
9 .E
10 .A
11 .D
12 .B
13 .D
14 .A
15 .B
16 .C
17 .D
18 .C
    
    """)


@Bot.command()
async def definingpronouns(ctx):
    await ctx.send("""
1. … summer we have a holiday by sea. 
A) All     B) Most      C) Both    D) Every    E)  Any  
2. … of students passes the exam in the class. 
A) All    B) Both     C) Each     D) Most    E)  Every 
3. … cars have wheels. 
A) Every     B) Neither C) Every D) Another  E)  All  
4. … of our students are clever. 
 1. Every       2. Most 3. All    4. Either  5. Each   
A) 1, 4, 5    B) 2, 3, 4     C) 1, 4    D) 2, 3  E)  1, 3, 5  
5. … of the children at this school is under 10 years old. 
 1. Every       2. Both  3. Most     4. Either 5. Each     
 A) 2, 3     B) 1, 4, 5    C) 2, 3, 5     D) 4, 5     E)  1, 4  6. 
… cities have the same problems. 
A) Either   B) All  C) Each D) Every  E)  Neither  
7. … of my parents are from Korea. 
A) Both  B) Each  C) Either D) Neither  E)  Every  
8. … of these book is very old. 
A) Either  B) Both  C) All D) Every  E)  Most  
9. Do… of you have English books? 
A) Each  B) All  C) Every D) Neither  E)  Either  
10. - Do you know those people? -… of them, not … of them. 
A)  every, all       B)  each, every C)  most, all D)  both, every E)  every, either  
11. Ann has two sisiters. … of them are married. 
A) Each  B) Every C) Any D) Both  E)  Neither  
12. … student has some skills. 
1. Every 2. Each  3. Both  4. All 
A) 1, 3    B) 2, 3 C) 1, 4  D) 2, 4  E)  1, 2  
13. What … books have you read before? 
A) Others    B) The other C) Another D) Other  E)  The others  
14. Is there … book by Bronte in your library? 
A) Other  B) Another   C) The others D) Others E)  The other 
15. There are only three students. I can’t see … . 
A) Others  B) Another ones C) Another  D) Other one E)  Other  
16. What … cities did you visit when you were in Korea? 
A) Others   B) The other C) Another D) The others E)  Other 
    
    """)


@Bot.command()
async def definingpronounscavab(ctx):
    await ctx.send("""
1 .D
2 .C
3 .E
4 .D
5 .D
6 .B
7 .A
8 .A
9 .B
10 .C
11 .D
12 .E
13 .D
14 .B
15 .A
16 .E
""")


@Bot.command()
async def interrogativerelativeandconjunctivepronouns(ctx):
    await ctx.send("""
Choose the correct pronoun or pronouns.  
1. … books have you read? 1. What 2. Whom  3. Which 4. What kind 
A) 1, 3     B) 2, 4     C) 1, 4     D) 2, 3     E) 1, 2  
2. - …  - She is a teacher 
  1. Who is she?     2. What is she?  3. What does she do? 4. How is she? 
  A) 1, 4  B) 2, 4 C) 1, 2  D) 2, 3  E) 1, 3  
3. … makes you sad? 
A) Whom  B) What  C) How D) What kind of E) Whose  
4. I don’t know these places. … of them do you know? 
A) Whose  B) What  C) Whom D) When   E) Which  
5. … lives in this house? 
A) Where  B) When C) Who D) Whom  E) How  
6. … does she live? 
A) Where  B) Who  C) What D) What kind of E) Whose  
7. -  … do you want? - I want coffee and sandwich. 
A) Whose  B) Whom C) What D) Who  E) When  
8. Everything … happened was my fault? 
A) What   B) Who  C) Whom D) That  E) Whose  
9. An architect is someone … designs buildings. 
 1. Who   2. What  3. Whom  4. That 
 A) 1, 4   B) 2, 3   C) 1, 3   D) 1, 2 E) 2, 4  
10. He told me … I wanted. 
A) Whose  B) What kind  C) What D) Which of E) Whose of  
11. The student … book is stolen has to tell her teacher. 
A) Who  B) Whom C) What D) Whose  E) What  
12.  Anyone … wants to do the exam must enter before next Friday. 
A) Whom  B) Who  C) Which D) What  E) Whose  
13. … is the cheese … was in the fridge? 
A) What, what  B) When, who   C) Where, whom  D) When, that  E) Where, which  
14. How  many  variants are correct? The woman … I saw was away. 
 1. Whom     2. Who   3. -  4. Whose     5. That  6. Which 
 A) 2   B) 3  C) 4  D) 5  E) 6     
15. Do you know the woman … next door? 
A) Who live     B) That live C) Which lives D) Who lives  E) Which live  
16. The bed … I wanted to buy was expensive.  
 1. Whom   2. Which 3. That   4. Who 
 A) 1, 2 B) 1, 3   C) 2, 4   D) 2, 3  E) 1, 4 
    
    """)


@Bot.command()
async def interrogativerelativeandconjunctivepronounscavab(ctx):
    await ctx.send("""
1 .A
2 .D
3 .B
4 .E
5 .C
6 .A
7 .C
8 .D
9 .A
10 .C
11 .D
12 .B
13 .E
14 .B
15 .D
16 .D
    
    """)


@Bot.command()
async def relativeandconjunctivepronouns(ctx):
    await ctx.send("""
Choose the correct pronoun or pronouns.  
1. The lady ... wallet was stolen was very anxious.
A) whose  B) who  C) which D) that E) whom  
2. This test is for students... native language is not English.  
A) whose  B) whom C) that  D) who  E) which   
3. In the morning he got two letters ... were answers to his advertisement. 
 1. which   2. what    3. that   4. who 5. Whom 
 A) 3, 4  B) 1, 3  C) 2, 5    D) 4, 5    E) 1, 2   
4. Sarah is very kind. She always does a favour to those... hurt you. 
 A) whom  B) what  C) who  D) whose  E) which   
5. Kate heard everything ... he said.  
 A) who  B) that C) what  D) whom   E) whose  
6. ... is the man ... leads the delegation from Tokio? 
 A) Whose, who  B) Whose, that C) Who, who   D) Who, which  E) Which, whose   
7. Those are the people.. . missed the train.    
 A) who  B) which C) what  D) whom   E) whose   
8. She didn't like the skirts... I wanted to buy.  
 A) what   B) that  C) who D) whose   E) whom   
9. ... was the man ... was waiting for the police?  
 A) Who, who  B) Who, whom  C) Which, what  D) Whom, who  E) Where, which   
10. The lady ... opened the window is my mother. 
 A) Which  B) Who  C) Whom D) What  E) Whose   
11. The woman ... car was stolen phoned the police. 
 A) whose   B) who C) that  D) which  E) whom   
12. ... was that man with... you were talking in the  yard?  
 A) Who, that   B) Whom, which  C) Where, who   D) Who, who E)Who, whom   
13.  My mother thanked the teacher... helped me. 
 A) who   B) whose C) what  D) whom   E) which   
14. This is the teacher ...  told me everything about my son.  
 1. whom 2. who 3. which 4. whose 5. that 
 A) 2, 4  B) 1, 4  C) 1,5   D) 3, 5 E) 2, 5   
15. A butcher is someone ... sells meat. 
 A) who   B) which C) whose  D) whom  E) what  
16. The girl.. . aunt is our doctor went to London. 
 A) whom  B) which C) that D) who E) whose   
17.  The police wanted to interview the man ... house was burnt. 
 A) who  B) that  C) which  D) who   E) whose 
    
    """)


@Bot.command()
async def relativeandconjunctivepronounscavab(ctx):
    await ctx.send("""
1 .A
2 .A
3 .B
4 .C
5 .B
6 .C
7 .A
8 .B
9 .A
10 .B
11 .A
12 .E
13 .A
14 .E
15 .A
16 .E
17 .E

    """)


@Bot.command()
async def allthepronouns(ctx):
    await ctx.send("""
Choose the correct pronoun(s).  
1. We went to the supermarket, but we bought.... .  
A) anything  B) any   C) nothing  D) every   E) everybody   
2. They are very hungry. But there is ... to eat.  
A) anything  B) something  C) any D) nothing   E) no  
3. There were two girls in the room. ... were reading ... .  
A) No, anything   B) Any, nothing  C) Both, something  D) All, anything  E) Each, something   
4.  ... is knocking at the door. Go and open it!  
A) Anybody  B) Nothing  C) Nobody  D) Somebody  E) Anything   
5. I think it's such a difficult exercise that ... can do it. 
A) nothing   B) anything  C) anyone   D) no one   E) somebody 
6. ...  are going out tonight. Why don 't you come with us?  
 1. Some of us   2. Any of them  3. None of us  4. Other 5. All of us 
 A) 2, 3     B) 3, 4, 5     C) 1, 5     D) 1,4     E) 1, 2, 3 
7.  I want to make ... cakes, but there isn`t... flour left in the cupboard. Will you go and buy some? 
A) some, any  B) little, few C)any,some  D) a little, any E) some, some  
8. Is... here, children?  
A) everybody  B) no one C) both  D) all   E) every 
9.  ... students think that Maths is difficult,.. don't think so. But most of them think it is useful. 
A) Some, any  B) Some, some  C) Some,anybody D) Many, somebody E) No, none   
10. You mustn 't say.. to ... about this secret. 
 1. anything, anybody 2. nothing, nobody 3. everything, everyone  4. something, somebody 
 A) 2, 3     B) 1, 3     C) 1, 2     D) 2, 4   E) 3, 4   
11. ... knows ... about yesterday's crime . 
1. Nobody, nothing  2. Nobody, anything  3. Nobody, something  4. Everybody, everything  
A) 3,4      B) 2, 4     C) 2, 3     D) 1,3     E) 1,4   
12. Some orphan children sleep in parks because ... have... place to go to at nights. 
A) they, some  B) they, any C) he, any  D) he, every  E) they, no   
13. Maria bought two magazines but she read ... of them. 
A) neither   B) either  C) no  D) any   E) every 
    
    """)


@Bot.command()
async def allthepronounscavab(ctx):
    await ctx.send("""
1 .C
2 .D
3 .C
4 .D
5 .D
6 .A
7 .A
8 .A
9 .B
10 .B
11 .B
12 .E
13 .A
    """)


@Bot.command()
async def theverbtest(ctx):
    await ctx.send("""
Choose the correct variant.  
1. Your shoes ... very dirty. 
A) am     B) is    C) are    D) has    E) does  
2. Look! There ... a nurse and some doctors in the hospital. 
A) are     B) is    C) were      D) do      E) will      
3. How much ... these postcards? 
A) has     B) is     C) will      D) does    E) are  
4. “Snow White and Seven Dwarfs” ... the best cartoon film I have ever seen. 
A) is  B) are  C) am   D) shall  E) do  
5. ... the Earth go round the Sun? 
A) is  B) do C) are D) does  E) has  
6. It ... a nice house but it ... have a garden. 
A) are, don’t   B) hasn’t, hasn’t C) is, doesn’t  D) has, don’t E) are, hasn’t  
7. Where ... my books?  - I ... no idea. 
A) am, do  B) are, am C) do, have D) has, haven’t E) are, have  
8. There ... any letters for me yesterday. 
A) was  B) are  C) is  D) were  E) will  
9. Why ... you late for meeting yesterday? 
A) are     B) have      C) were     D) do     E) did  
10. I feel fine this morning but I ... very tired last night. 
A) am  B) were   C) did D) had   E) was  
11. Choose the line of regular verbs. 
A) to start, to shut, to close B) to steal, to live, to stop C) to open, to want, to live,  D) to fly, to sing, to drink E) to feel, to teach, to hit  
12. Choose the line of irregular verbs. 
A) to sell, to wake, to study B) to see, to hear, to make C) to go, to catch, to save D) to promise, to lose, to arrive E) to understand, to stay, to raise  
13. Choose the line of regular verbs. 
A) to want, to found, to marry B) to try, to show, to write C) to drive, to put, to eat D) to rise, to water, to  think E) to hide, to run, to be 
14. Choose the line of irregular verbs. 
A) to send, to shut, to play B) to arrive, to promise, to do C) to have, to be, to do D) to stop, to give, to kill E) to beat, to watch, to ask  
15. Choose the line of regular verbs. 
A) to write, to book, to teach B) to go, to take, to clean C) to make, to tear, to drive D) to kill, to study, to try E) to sell, to like, to leave  
    
    """)


@Bot.command()
async def theverbtestcavab(ctx):
    await ctx.send("""
1 .C
2 .B
3 .E
4 .A
5 .D
6 .C
7 .E
8 .D
9 .C
10 .E
11 .C
12 .B
13 .A
14 .C
15 .D

    
    """)


@Bot.command()
async def theverbtest2(ctx):
    await ctx.send("""
Choose the correct variant.   
1. These postcards are nice. How much ... they? 
A) is      B) are       C) does     D) do      E) has  
2. Tony Blair ... approximately as old as Jakie Chan. 
A) is      B) has      C) does      D) are      E) have  
3. They ... rich. They ... got much money. 
A) are, haven’t  B) is, has  C) aren’t, have D) are, has  E) aren’t, haven’t  
4. “ ... on Sundays? “ “No, not usually” A) Do you work B) Do you working  C) Are you work D) Were you E) Have you work  
5. Sarah isn’t feeling well. She ... a headache. 
A) have     B) have got     C) has     D) do     E) is  
6. ... the weather good last week? 
A) Have    B) Are     C) Is    D) Were   E) Was  
7. She ... that window last week. A) broke  B) break  C) broken D) brokes  E) broked  
8. ... she cut her finger with a glass? 1. Are 2. Do   3. Does    4. Did    5. Is 
A) 3, 4, 5    B) 3, 4      C) 1, 2, 3     D) 2, 3     E) 3, 4  
9. There ... two posters and a calendar in my room. 
A) will     B) are     C) is      D) has      E) was  
10. There .. a big wardrobe and a mirror in my sister’sbedroom. 
A) is     B) are     C) will     D) were     E) have  
11. There ... a lot of traffic in the rush hour. 
A) have got B) has got      C) has    D) is     E) are  
12. “ ... New York and Los Angeles Spanish Cities?” “No, they aren`t Spanish cities” 
A) has     B) have     C) is     D) are     E) aren`t  1
3. My friend and I ... high school students. We aren’t primary school students. 
A) was    B) do      C) am     D) is     E) are  
14. My green pencil ... on the floor. 
A) is      B) were     C) are     D) have    E) has  
15. ... they leave without saying good bye last night. 
A) Do     B) Does   C) Did    D) Is     E) Was 
    
    """)


@Bot.command()
async def theverbtest2cavab(ctx):
    await ctx.send("""
1 .B
2 .A
3 .E
4 .A
5 .C
6 .E
7 .A
8 .E
9 .B
10 .A
11 .D
12 .D
13 .E
14 .A
15 .C
    
    
    """)


@Bot.command()
async def thepassivevoice(msg):
    await msg.send("""
    1. Someone repairs the machine. 
    A) The machine was repaired someone. B) The machine is repaired someone. C) Someone is repaired the machine. D) The machine repaires by someone. E) The machine is repaired by someone.  
    2. My mother took my camera yesterday. 
    A) My camera is taken by my mother. B) My camera was taken by her. C) My camera was took by my mother yesterday. D) My mother was taken my camera yesterday. E) My camera took by my mother yesterday.  
    3. They have cleaned all the windows this week. 
    A) All the windows have cleaned by them this week. B) All the windows has been cleaned. C) All the windows have been cleaned by them this week. D) They have been cleaned all the windows. E) All windows cleaned by them.  
    4. They sell cold drinks here. 
    A) They were sold cold drinks here. B) Cold drinks are sold by them. C) Cold drinks sell here. D) Cold drinks are sell here by them. E) Cold drinks were sold here.  
    5. When do they serve breakfast in this hotel? 
    A) When do breakfast serve in this hotel? B) When is breakfast served by them in this hotel? C) When breakfast sells in this hotel? D) When is breakfast serve by them? E) When are breakfast served in this hotel?  
    6. My father had paid the bill. 
    A) The bill had paid by my father. B) My father has been paid the bill. C) The bill had been paid by him. D) The bill have been paid by my father. E) The bill paid by my father.  
    7. They are mending the car now. 
    A) The car are mended by them now. B) The car is mending by them now. C) They were mended by them. D) The car is being mended now. E) The car is mended now.   
    8. You can see these mountains from a great distance. 
    A) These mountains can be seen by you. B) You can seen these mountains from a great distance. C) These mountains can seen from a great distance. D) These mountains can be saw from a great distance. E) You can be seen these mountains from a great distance.  
    9. She has packed the books. 
    A) The books has packed by her. B) The books have packed by her. C) She has been packed the books. D) The books have been packed. E) The books have been pack by her.  
    10. We will finish the job.
    A) The job will finish by us. B) The job will be finished by us. C) The job will be finished by we. D) We will be finished the job. E) The job will be finishing by us.  
    11. They were building it.
    A) It was being built by them. B) They were built it. C) It was built by them. D) It was being build by they. E) It was build by them.  
    """)


@Bot.command()
async def thepassivevoicecavab(msg):
    await msg.send("""
    1.E
    2.B
    3.C
    4.B
    5.B
    6.C
    7.D
    8.A
    9.D
    10.B
    11.A
    """)


@Bot.command()
async def test(msg):
    await msg.send("""
    1. My students ... more now. 
    A) is studying B) study        C) are studying D) studyes  E) will studied  
    2. My friends and I ... the boats on the sea at the moment.  
    A) am watching B) watches      C) is watching D) are watching E) will watched  
    3. Jane is busy. She ... on the phone. A) speaks  B) is speak   C) will spoke D) speaked  E) is speaking  
    4. A lot of people ... for the 6.30 bus at that time last night.  
    A) was speaking B) spoke  C) speak D) is speaking E) were speaking  
    5. He ... on the phone when I ... . 
    A)is speaking,arrived   B) was speaking,arrived C) was speaking, is arriving  D) is speaking, arriving E) is speaking, arrives  
    6. It was a sunny afternoon and people ... on the grass in the park. 
    A) is sitting  B) sits  C) were sitting D) has sat  E) are sitting  
    7. What ... you ... at seven o’clock last night? 
    A) are doing   B) was doing  C) were doing D) is doing   E) am doing  
    8. It ... when we ... home. 
    A) is raining, left B) was raining, left C) rains, are leaving D) rained, is rained E) rains, leaving  
    9. She entered the room where Jake ... for him at the supper table. 
    A) is waiting  B) are waiting C) waits D) was waiting E) were waiting  
    10. I ... you ... for a new house. 
    A) heard, were looking B) hears, is looking C) hear, was looking  D) heard, is looking E) hear, am looking  
    11. He can’t come, he ... dinner at the moment. 
    A) were having B) have  C) has had D) is having  E) was having  
    12. Look! The bus ... . 
    A) was coming      B) were coming    C) is coming D) are coming       E) am coming   
    Yazdıqdan sonra cavabları görmək üçün bu sözü yazın:/cavab
    """)


@Bot.command()
async def cavab(msg):
    await msg.send("""
1-C
2-D
3-E
4-E
5-B
6-C
7-C
8-B
9-D
10-A
11-D
12-C
""")


Bot.run('ODg5MDMwMDE5Mzk2MDI2NDI4.YUbTug.LzzBTW_GUzBhm2UIXjpT7eLOt2w')
