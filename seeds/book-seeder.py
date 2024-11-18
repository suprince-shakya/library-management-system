from flask_seeder import Seeder
from app.models.book import Book
from app.models.author import Author
from app.models.category import Category
from werkzeug.utils import secure_filename
import os

categories=['Romance','Novel','Self-help','Friction','Fantasy','Horror','Action & Adventure','Science Fiction','Detective & Mystery','Thriller & Suspense']
authors=['Elle Marr','Emily Henry','Alastair Reynolds','Stephen Graham Jones','F. Scott Fitzgerald','Spencer Johnson','Jane Austen','Héctor García','Paulo Coelho','Robert Kiyosaki']

books=[
  {
    "name":"The Alone Time",
    "category":categories[9],
    "author":authors[0],
    "isbn":1414,
    "price":5,
    "quantity":3,
    "description":"For two sisters, confronting the past could come at a terrible price in a riveting novel about a family tragedy—and family secrets—by the #1 Amazon Charts bestselling author Elle Marr.Fiona and Violet Seng were just children when their family's Cessna crash-landed in the Washington wilderness, claiming the lives of their parents. For twelve harrowing weeks, the girls fended for themselves before being rescued.Twenty-five years later, they're still trying to move on from the trauma. Fiona repurposes it into controversial works of art. Violet has battled addiction and failed relationships to finally progress toward normalcy as a writer. The estranged sisters never speak about what they call their Alone Time in the wild. They wouldn't dare—until they become the subject of a documentary that renews public fascination with the “girl survivors” and questions their version of the events.When disturbing details about the Seng family are exposed, a strange woman claims to know the crash was deliberate. Fiona and Violet must come together to face the horrifying truth of what happened out there and what they learned about their parents and themselves. Before any other secrets emerge from the woods.",
    "picture":"./app/static/the-alone-time.jpg"
  },
  {
    "name":"Happy Place",
    "category":categories[0],
    "author":authors[1],
    "isbn":1313,
    "price":9,
    "quantity":3,
    "description":"Happy Place is a romantic comedy novel by Emily Henry about two friends who pretend to be in a relationship for one week. Harriet and Wyn have been best friends since college, and they've always been there for each other through thick and thin. They even got engaged at one point, but they broke up five months ago. They haven't told their friends about the breakup yet, because they don't want to ruin their annual weeklong vacation to a cottage in Maine.The cottage is a special place for Harriet and Wyn, and it's where they first fell in love. But this year, things are different. They're both still struggling with the breakup, and they're not sure how to act around each other.To make things even more complicated, Harriet's ex-boyfriend, Ford, shows up at the cottage. Ford is a famous actor, and he's everything that Wyn is not. He's confident, handsome, and successful. Harriet is immediately drawn to him, but she knows that she can't get involved with him again.Wyn is also feeling insecure about the situation. He's worried that Harriet will leave him for Ford, and he doesn't know how to compete with him.Get a FREE Audible copy of Happy Place by Emily Henry To make matters worse, Harriet and Wyn start to argue more and more. They disagree about everything, from what to do for dinner to how to decorate the cottage. It's clear that they're not on the same page, and they're both starting to question their relationship.One night, Harriet and Wyn get drunk and have a fight. They say things they don't mean, and they end up sleeping in separate rooms. The next morning, they both wake up feeling ashamed and regretful. They know that they need to talk, but they're both afraid of what the other person will say.Finally, Harriet and Wyn decide to have a heart-to-heart talk. They tell each other how they're feeling, and they finally start to communicate honestly. They realize that they still love each other, but they also realize that they need to make some changes if they want their relationship to work.Harriet and Wyn agree to give their relationship another try, but they know that it won't be easy. They have a lot of work to do, but they're both committed to making it work.Happy Place is a charming and heartwarming story about love, friendship, and second chances. It's a reminder that even when things are tough, there's always hope for a happy ending.Get a FREE Audible copy of Happy Place by Emily Henry Here are some additional details about the book: The book is set in Maine, and it captures the beauty of the New England coast. The characters are well-developed and relatable. Harriet and Wyn are both flawed characters, but they are also likable and sympathetic.The plot is engaging and unpredictable. The book takes unexpected turns, and it keeps the reader guessing until the end.The writing is witty and charming. Emily Henry has a gift for creating dialogue that is both funny and heartwarming.Overall, Happy Place is a delightful read that will leave you feeling happy and hopeful. It's a perfect book for fans of romantic comedies, or anyone who is looking for a feel-good story.",
    "picture":"./app/static/happy-place.jpg"
  },
  {
    "name":"Machine Vendetta",
    "category":categories[7],
    "author":authors[2],
    "isbn":1212,
    "price":23,
    "quantity":3,
    "description":"From the king of modern space opera comes a new adventure in the Prefect Dreyfus series— Machine Vendetta is a thrilling tale of deadly conspiracies and old enemies that refuse to die.Panoply is a small, efficient police force, dedicated to maintaining the rule of democracy among the ten thousand disparate city-states orbiting the planet Yellowstone.Ingvar Tench was one of Panoply's most experienced operatives. So why did she walk alone and unarmed into a habitat with a vicious grudge against her organization? As his colleagues pick up the pieces following her death, Prefect Tom Dreyfus must face his conscience. Four years ago, when an investigation linked to one of his most dangerous adversaries got a little too personal, Dreyfus arranged for Tench to continue the inquiry by proxy. In using her, did Dreyfus also put her in the line of fire? And what does Tench's attack tell him about an enemy he had hoped was dormant?",
    "picture":"./app/static/machine-vendetta.jpg"
  },
  {
    "name":"Don't Fear the Reape",
    "category":categories[5],
    "author":authors[3],
    "isbn":9999,
    "price":8,
    "quantity":9,
    "description":"December 12th, 2019, Jade returns to the rural lake town of Proofrock the same day as convicted Indigenous serial killer Dark Mill South escapes into town to complete his revenge killings, in this “superb” (Publishers Weekly) sequel to My Heart Is a Chainsaw from New York Times bestselling author Stephen Graham Jones.Four years after her tumultuous senior year, Jade Daniels is released from prison right before Christmas when her conviction is overturned. But life beyond bars takes a dangerous turn as soon as she returns to Proofrock. Convicted Serial Killer, Dark Mill South, seeking revenge for thirty-eight Dakota men hanged in 1862, escapes from his prison transfer due to a blizzard, just outside of Proofrock, Idaho.Dark Mill South's Reunion Tour began on December 12th, 2019, a Thursday.Thirty-six hours and twenty bodies later, on Friday the 13th, it would be over.",
    "picture":"./app/static/dont-fear-the-reaper.jpg"
  },
  {
    "name":"The Great Gatsby",
    "category":categories[1],
    "author":authors[4],
    "isbn":8888,
    "price":9,
    "quantity":5,
    "description":"The Great Gatsby, novel by American author F. Scott Fitzgerald, published in 1925. It tells the story of Jay Gatsby, a self-made millionaire, and his pursuit of Daisy Buchanan, a wealthy young woman whom he loved in his youth. Set in 1920s New York, the book is narrated by Nick Carraway. After moving to the fictional West Egg on Long Island, Nick comes to know Gatsby, who asks for his help in reconnecting with Daisy, now married to Tom Buchanan. Gatsby and Daisy rekindle their relationship. Tom discovers the affair and confronts Gatsby, revealing how Gatsby made his fortune selling illegal alcohol. While driving Gatsby's car, Daisy hits and kills Myrtle Wilson, Tom's mistress. Myrtle's husband later kills Gatsby and then himself. Initially given mixed reviews, The Great Gatsby gained popularity in the 1950s and is now considered a masterpiece of American literature. It has inspired several film adaptations.",
    "picture":"./app/static/the-great-gatsey.jpg"
  },
  {
    "name":"Rich Dad Poor Dad",
    "category":categories[2],
    "author":authors[9],
    "isbn":7777,
    "price":8,
    "quantity":8,
    "description":"Rich people don't work for money Before we get to the famous financial lessons, we're going tell you a story. The story of 9-year old Robert Kiyosaki. It begins in the 1950's. Robert and his friend Mike were curious boys with big ambitions: When they grew up, they wanted to become rich and make a lot of money. But just how they were going to accomplish that they didn't actually know. So, after a failed attempt to produce coins from melted toothpaste tubes, the boys decided to get some advice. They asked their dads how they could start becoming rich.You might be able to guess what Robert's own well-educated but “poor dad” replied: “Go to school, study, and find a good job.” It's familiar advice – but it's pretty misguided. If you follow guidance like this, you'll spend your entire life breaking your back to increase your pay, while others – the government, bill collectors, and your bosses – take most of the reward.In other words, Robert's poor dad might as well have said, “Go and join the rat race, the endless routine of working for everyone but yourself.” Now, lots of people still follow poor dad's mantra – but many do it out of a sense of fear, a powerful sense of distress at the idea of violating the expectations that society drills into us. A good job is what leads to wealth, we're told, so we study hard as kids and work even harder as adults. The result? We may be avoiding poverty, but we're certainly not growing any wealthier.But there are some people who don't teach that mantra to their kids – people who know how money is created, increased and maintained. Rich people, in other words – people like Mike's father, the rich dad who became a financial mentor to both boys. So what did Mike's dad suggest? At first, nothing. He made a deal with the young Kiyosaki, offering to teach him what he knew about money if the boy would work for him at the measly rate of 10 cents an hour. Robert agreed – but after a few weeks of being underpaid, the boy returned to his “rich” dad,  seething with anger and ready to quit. “You've exploited me long enough,” he said, “and you haven't even kept your promise. You taught me nothing about money in all those weeks!” But there it was: his first lesson, delivered by his new mentor with a slight smile. Robert Kiyosaki had just learned that life often pushes you around. And he'd learned that working for money does not make you rich. Which is why: Rich people don't work for money. So you might ask yourself: if the rich don't work for money, then how do they get wealthy? Through theft, maybe, or by winning the lotto?",
    "picture":"./app/static/rich-dad-poor-dad.jpg"
  },
  {
    "name":"Who moved my cheese",
    "category":categories[2],
    "author":authors[5],
    "isbn":6666,
    "price":15,
    "quantity":5,
    "description":"Your “cheese” or success in life may be paralyzing you.The two mice, Sniff and Scurry, don't think about things too much. They instead spend their time running up and down the corridors of their maze, in search of cheese.This seemingly “brainless” way in which these two mice set about achieving their goal is instructive, and is often the most effective method in reaching your own goals. In fact, acting without thinking too much can save you time and energy.If there's no cheese at the end of a path, for example, Sniff and Scurry simply turn around and scramble down another path – without wasting time being angry or frustrated.Hem and Haw were also searching for cheese in the maze, but not because they were hungry. Rather, they thought that finding cheese would make them feel happy and successful.With their more “complex” brains, Hem and Haw worked out strategies to find cheese, memorizing the maze's dark corners and blind alleys. Yet with all this planning, they still often got confused, and sometimes lost their way. And whenever the pair came up empty-handed, they became depressed, wondering if happiness would ever be attainable.",
    "picture":"./app/static/who-moved-my-cheese.jpg"
  },
  {
    "name":"Who took my money?",
    "category":categories[2],
    "author":authors[9],
    "isbn":5555,
    "price":10,
    "quantity":7,
    "description":"To avoid spending your old age in poverty, you need to act now.Whenever the author gives a talk about personal finance, someone in the audience is bound to ask him, “Why does money matter anyway? Isn't happiness more important?” In response, he smiles calmly and demonstrates why this attitude is so harmful. He'll begin with some alarming evidence. A survey for USA Today found that the number one fear for Americans is running out of money in old age. More than crime, nuclear war, or anything else, their greatest worry is living a long life with no money. After letting this sink in, the author tells his audience that one in three Americans over the age of 65 has no retirement plan at all. In other words, their greatest fear will likely come true. The key message here is: To avoid spending your old age in poverty, you need to act now. Many people want to put off their money worries until they're older. But we only have a limited time to get our finances in order. Without a decent pension, many of us will have to keep working long into old age. And with so many living expenses to consider – things like college debt, mortgage payments, car payments, taxes, and care for our elderly parents – retiring might not be an option at all. Sure, working into old age might be good for your physical and mental health, but working forever because you have to is a very different matter. The painful truth is that our money-earning lives are divided up into four quarters, just like a game of American football. The first quarter stretches roughly from the age of 25 to 35, the second from 35 to 45, the third from 45 to 55, and the last from 55 to the time we're expected to retire. If we can't afford to retire at that point, we go into overtime. Then, when we're too old to work but have no money left, we're out of time. Game over. Nobody wants to reach those final two stages without having their finances in order. So, at some point in those four quarters, we should work toward financial independence. But what exactly should we do? The standard advice is: save, invest in mutual funds, and hold these for the long term. However, the author argues, this isn't the way to reach financial independence – it's too slow and far too unreliable. In the following blinks, we'll explore what you can do instead.",
    "picture":"./app/static/who-took-my-money.jpg"
  },
  {
    "name":"Pride and Prejudice",
    "category":categories[0],
    "author":authors[6],
    "isbn":4444,
    "price":25,
    "quantity":2,
    "description":"The novel opens with one of the most famous lines in English literature: “It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.” The statement is seemingly what Mrs. Bennet thinks as she sets her sights on the newly arrived Bingley, who she is sure will make a suitable husband for one of her daughters. At a ball, Bingley takes an immediate interest in the beautiful and shy Jane. The encounter between his friend Darcy and Elizabeth is less cordial. Although Austen shows them intrigued by each other, she reverses the convention of first impressions: the pride of rank and fortune and prejudice against the social inferiority of Elizabeth's family hold Darcy aloof, while the pride of self-respect and prejudice against Darcy's snobbery hold Elizabeth equally aloof.The pompous Collins soon arrives, hoping to marry one of the Bennet sisters. Mrs. Bennet steers him toward Elizabeth, but the latter refuses his offer of marriage. He instead becomes engaged to her friend Charlotte. During this time, Elizabeth encounters the charming Wickham. There is a mutual attraction between the two, and he informs her that Darcy has denied him his inheritance.After Bingley abruptly departs for London, Elizabeth's dislike of Darcy mounts as she becomes convinced that he is discouraging Bingley's relationship with Jane. Darcy, however, has grown increasingly fond of Elizabeth, admiring her intelligence and vitality. While visiting the now-married Charlotte, Elizabeth sees Darcy, who professes his love for her and proposes. A surprised Elizabeth refuses his offer, and, when Darcy demands an explanation, she accuses him of breaking up Jane and Bingley and of denying Wickham his inheritance. Darcy subsequently writes Elizabeth a letter in which he explains that he separated the couple largely because he did not believe Jane returned Bingley's affection. He also discloses that Wickham, after squandering his inheritance, tried to marry Darcy's then 15-year-old sister in an attempt to gain possession of her fortune. With these revelations, Elizabeth begins to see Darcy in a new light.Shortly thereafter the youngest Bennet sister, Lydia, elopes with Wickham. The news is met with great alarm by Elizabeth, since the scandalous affair—which is unlikely to end in marriage—could ruin the reputation of the other Bennet sisters. When she tells Darcy, he persuades Wickham to marry Lydia, offering him money. Despite Darcy's attempt to keep his intervention a secret, Elizabeth learns of his actions. At the encouragement of Darcy, Bingley subsequently returns, and he and Jane become engaged. Finally, Darcy proposes again to Elizabeth, who this time accepts.",
    "picture":"./app/static/pride-prejudice.jpg"
  },
  {
    "name":"Ikigai",
    "category":categories[2],
    "author":authors[7],
    "isbn":3333,
    "price":15,
    "quantity":3,
    "description":"A deep purpose in life is the secret to longevity. Are you interested in living a long, healthy and fulfilling life? Who isn't? The secret to doing so just may be found on the island of Okinawa, in southern Japan, home to the highest concentration of centenarians in the world. And these island dwellers' secret to longevity may boil down to just one word: ikigai, which roughly translates to your reason for living or your inner motivation for a specific professional activity. It can also be described as an intersection between four different elements: what you're passionate about, where your skills lie, how you can earn a living and what the world needs. Many Japanese believe that everyone has an ikigai, or destiny, that they were born to fulfill.However, while some people find their ikigai quickly, others must seek it out over time. If you fall into this latter category, it's important to persist; after all, ikigai will ultimately be what motivates you to get out of bed in the morning. That's why Okinawans often attain a high degree of specialization and attention to detail in their daily work. For instance, in an Okinawan paintbrush factory, the authors met a skilled craftswoman who had spent her entire life perfecting the art of attaching individual hairs to a brush. At this stage in her career, she was able to do her job with stunning dexterity and skill. What's more, ikigai is also the key to longevity. So, if your ikigai is your job, you should never retire. And if your ikigai is a hobby that brings you meaning and joy, don't ever give it up. Okinawans abide by these rules and, as a result, remain active late into their lives. If they're forced into retirement, they still find ways to remain active, such as by doing gardening or other work in their communities. The benefits of this commitment are clear. Medical studies conducted on Okinawan centenarians have found extremely low rates of both heart disease and dementia. In the next blink, you'll learn how exactly an engaged mind enables a long life.",
    "picture":"./app/static/ikigai.jpg"
  },
  {
    "name":"The Alchemist",
    "category":categories[1],
    "author":authors[8],
    "isbn":2222,
    "price":20,
    "quantity":5,
    "description":"An Andalusian shepherd boy named Santiago dreams of a treasure while in a ruined church. He consults a Gypsy fortune-teller about the meaning of the recurring dream. The woman interprets it as a prophecy, telling the boy that he will discover a treasure at the Egyptian pyramids. After Santiago sets out, he meets an old king Melchizedek, or the king of Salem, who tells him to sell his sheep so as to travel to Egypt and accomplish his 'Personal Legend'. Early on his arrival in Africa, a man who claims to be able to take Santiago to the pyramids instead robs him of the money he had made from his flock. Santiago then has to work for a crystal merchant to earn enough to continue his journey. Along the way, the boy meets an Englishman who has come in search of an alchemist and continues his travels with his new companion. When they reach an oasis, Santiago meets and falls in love with an Arabian girl named Fatima, to whom he proposes marriage. She promises to marry him only after he completes his journey. Frustrated at first, he later learns that true love will not stop nor must one sacrifice one's destiny to it, since to do so robs it of truth. The Pyramids of Giza The boy then encounters a wise alchemist, who teaches him to realize his true self. Together, they risk a journey through the territory of warring tribes, where Santiago is forced to demonstrate his oneness with the 'Soul of the World' by turning himself into a dust storm before he is allowed to proceed. When he reaches the pyramids and begins digging, he is robbed by thieves, who ask him what he is digging for; he replies that a dream has led him to buried treasure. The thieves scoff, and the leader remarks about a dream he once had about treasure under a tree at a ruined church. Santiago realizes the treasure he sought was where he had his original dream all along.",
    "picture":"./app/static/alchemist.jpg"
  },
  {
    "name":"Eleven Minutes",
    "category":categories[1],
    "author":authors[8],
    "isbn":1111,
    "price":35,
    "quantity":5,
    "description":"Maria, a young girl from a remote village of Brazil, whose first encounters with love had left her heartbroken, goes to seek her fortune in Switzerland. She works for a time in a nightclub but soon becomes dissatisfied and after a heated discussion with her manager one night, she quits her job. She tries to become a model but is unsuccessful. Because she is running out of money, she accepts 1000 francs from an Arab man to spend the night with him. She then decides to become a prostitute and ends up in a brothel on Rue de Berne, the heart of Geneva's red-light district. There she befriends Nyah who gives her advice on her 'new profession' and after learning the tricks of the trade from Milan, the brothel owner, she enters the job with her body and mind shutting all doors for love and keeps her heart open only for her diary. Quickly she becomes quite successful and famous and her colleagues begin to envy her. Months pass and Maria grows into a professionally groomed prostitute who not only relaxes her clients' minds, but also calms their souls by talking to them about their problems. Her world turns upside down when she meets Ralf, a young Swiss painter, who sees her 'inner light'. Maria falls in love with him immediately and begins to experience what 'true love' is (according to the author, it is a sense of being for someone without actually possessing him/her). Maria is now split between her sexual fantasies and true love for Ralf. Eventually she decides that it is time for her to leave Geneva with her memory of Ralf, because she realizes that they are worlds apart. But before leaving, she decides to rekindle the dead sexual fire in Ralf and learns from him about the nature of Sacred Sex, sex which is mingled with true love and which involves the giving up of one's soul for the loved one.",
    "picture":"./app/static/eleven-minutes.jpg"
  },
]

class BookSeeder(Seeder):
  def run(self):
    for book in books:
      category=self.db.session.query(Category).filter(Category.title==book['category']).first()
      author=self.db.session.query(Author).filter(Author.name==book['author']).first()
      self.db.session.add(Book(name=book['name'],category_id=category.id,author_id=author.id,isbn=book['isbn'],quantity=book['quantity'],in_stock=book['quantity'],price=book['price'],description=book['description'],picture=book['picture']))
 