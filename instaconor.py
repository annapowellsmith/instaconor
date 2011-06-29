# Script to add the Atlantic's top 100 non-fiction articles of 2010
# to an Instapaper account. 
# Run as: "python instaconor.py"
# Articles taken from http://bit.ly/jHK3fZ and scraped using ScraperWiki.com: 
# http://scraperwiki.com/scrapers/100_best_non-fiction_articles_2010
import getpass 
import sys
import urllib 

ARTICLES = [   {   'category': 'The Art Of Storytelling',
        'link': 'http://www.washingtonmonthly.com/features/2010/1007.blake.html',
        'publication': 'Washington Monthly',
        'title': 'Dirty Medicine'},
    {   'category': 'The Art Of Storytelling',
        'link': 'http://www.texasmonthly.com/preview/2010-05-01/feature4',
        'publication': 'The Texas Monthly',
        'title': 'Last Days Of The Comanches'},
    {   'category': 'The Art Of Storytelling',
        'link': 'http://www.newyorker.com/arts/critics/atlarge/2010/05/10/100510crat_atlarge_gladwell?currentPage=all',
        'publication': 'The New Yorker',
        'title': "Pandora's Briefcase"},
    {   'category': 'The Art Of Storytelling',
        'link': 'http://www.newyorker.com/reporting/2010/04/05/100405fa_fact_goldberg?currentPage=all',
        'publication': 'The New Yorker',
        'title': 'The Hunted'},
    {   'category': 'The Art Of Storytelling',
        'link': 'http://www.themorningnews.org/archives/personal_essays/the_high_is_always_the_pain_and_the_pain_is_always_the_high.php',
        'publication': 'The Morning News',
        'title': 'The High Is Always The Pain And The Pain Is Always The High'},
    {   'category': 'The Art Of Storytelling',
        'link': 'http://www.thisamericanlife.org/radio-archives/episode/417/this-party-sucks',
        'publication': 'This American Life',
        'title': 'Patriot Games'},
    {   'category': 'The Art Of Storytelling',
        'link': 'http://www.esquire.com/print-this/ak-47-history-1110?page=all#',
        'publication': 'Esquire',
        'title': 'The Gun'},
    {   'category': 'The Art Of Storytelling',
        'link': 'http://joeposnanski.blogspot.com/2010/11/promise.html',
        'publication': 'Joe Blogs',
        'title': 'The Promise'},
    {   'category': 'The Art Of Storytelling',
        'link': 'http://www.vanityfair.com/culture/features/2010/12/vanishing-blonde-201012?printable=true&currentPage=1',
        'publication': 'Vanity Fair',
        'title': 'The Case Of The Vanishing Blonde'},
    {   'category': 'The Art Of Storytelling',
        'link': 'http://outsideonline.com/outside/culture/201007/killer-whale-behavior-trainer-death-seaworld.html',
        'publication': 'Outside',
        'title': 'The Killer In The Pool'},
    {   'category': 'The Art Of Storytelling',
        'link': 'http://www.newyorker.com/reporting/2010/07/12/100712fa_fact_grann',
        'publication': 'The New Yorker',
        'title': 'The Mark Of A Masterpiece'},
    {   'category': 'Crime & Punishment',
        'link': 'http://www.wired.com/magazine/2010/03/ff_masterthief_blanchard/all/1',
        'publication': 'Wired',
        'title': 'Art Of The Steal'},
    {   'category': 'Crime & Punishment',
        'link': 'http://outsideonline.com/outside/culture/201001/colton-harris-moore-plane-steal-1.html',
        'publication': 'Outside',
        'title': 'The Ballad Of Colton Harris-Moore'},
    {   'category': 'Crime & Punishment',
        'link': 'http://www.theatlantic.com/magazine/archive/2010/08/prison-without-walls/8195/',
        'publication': 'The Atlantic',
        'title': 'Prison Without Walls'},
    {   'category': 'Crime & Punishment',
        'link': 'http://www.nybooks.com/articles/archives/2010/mar/11/the-rape-of-american-prisoners/',
        'publication': 'The New York Review Of Books',
        'title': 'The Rape Of American Prisoners'},
    {   'category': 'Crime & Punishment',
        'link': 'http://online.wsj.com/article/SB10001424052702304023804575566201554448476.html',
        'publication': 'The Wall Street Journal',
        'title': 'A Solitary Jailhouse Lawyer Argues His Way Out Of Prison'},
    {   'category': 'Crime & Punishment',
        'link': 'http://www.thisamericanlife.org/radio-archives/episode/414/right-to-remain-silent',
        'publication': 'This American Life',
        'title': 'Is That A Tape Recorder In Your Pocket Or Are You Just Happy To See Me'},
    {   'category': 'Crime & Punishment',
        'link': 'http://www.theatlantic.com/magazine/archive/2010/05/the-wrong-man/8019/1/',
        'publication': 'The Atlantic',
        'title': 'The Wrong Man'},
    {   'category': 'Crime & Punishment',
        'link': 'http://www.slate.com/id/2245188/pagenum/all/#p2',
        'publication': 'Slate',
        'title': "The Chemist's War"},
    {   'category': 'Crime & Punishment',
        'link': 'http://www.gq.com/news-politics/politics/201012/eric-holder-attorney-general-rahm-emanuel-white-house-elections?printable=true&currentPage=1',
        'publication': 'Gq',
        'title': 'Hope. Change. Reality'},
    {   'category': 'Crime & Punishment',
        'link': 'http://www.newyorker.com/reporting/2010/10/18/101018fa_fact_finnegan?currentPage=all',
        'publication': 'The New Yorker',
        'title': 'In The Name Of The Law'},
    {   'category': 'Crime & Punishment',
        'link': 'http://www.governing.com/topics/public-justice-safety/courts-corrections/mississippi-correction-reform.html',
        'publication': 'Governing',
        'title': "Mississippi's Corrections Reform"},
    {   'category': 'Sports & Leisure',
        'link': 'http://www.tabletmag.com/news-and-politics/46897/smash/print/',
        'publication': 'Tablet',
        'title': 'Smash'},
    {   'category': 'Sports & Leisure',
        'link': 'http://sports.espn.go.com/espn/eticket/story?page=101201/Cleveland',
        'publication': 'Espn: Outside The Lines',
        'title': 'Believeland'},
    {   'category': 'Sports & Leisure',
        'link': 'http://www.nybooks.com/articles/archives/2010/feb/11/the-chess-master-and-the-computer/?pagination=false',
        'publication': 'The New York Review Of Books',
        'title': 'The Chess Master And The Supercomputer'},
    {   'category': 'Sports & Leisure',
        'link': 'http://www.nytimes.com/2010/06/20/magazine/20Computer-t.html?pagewanted=all',
        'publication': 'The New York Times Magazine',
        'title': "What Is I.B.M.'s Watson"},
    {   'category': 'Sports & Leisure',
        'link': 'http://www.guardian.co.uk/theobserver/2010/mar/21/tom-bissell-video-game-cocaine-addiction',
        'publication': 'The Observer',
        'title': 'Video Games: The Addiction'},
    {   'category': 'Sports & Leisure',
        'link': 'http://www.thestranger.com/seattle/Content?oid=4683741&mode=print',
        'publication': 'The Stranger',
        'title': 'The Mystery of the Tainted Cocaine'},
    {   'category': 'Sports & Leisure',
        'link': 'http://www.ediblegeography.com/a-cocktail-party-in-the-street-an-interview-with-alan-stillman/',
        'publication': 'Edible Geography',
        'title': 'A Cocktail Party In The Street: An Interview With Alan Stillman'},
    {   'category': 'Sports & Leisure',
        'link': 'http://www.slate.com/id/2277301/pagenum/all/#p2',
        'publication': 'Slate',
        'title': 'You Should Worship Kelly Slater'},
    {   'category': 'Science, Religion & Human Nature',
        'link': 'http://www.thenation.com/article/155400/postcard-palestine',
        'publication': 'The Nation',
        'title': 'Postcard From Palestine'},
    {   'category': 'Science, Religion & Human Nature',
        'link': 'http://online.wsj.com/article/SB10001424052748704779704575553943328901802.html',
        'publication': 'The Wall Street Journal',
        'title': 'In Chile, The Lessons Of Isolation'},
    {   'category': 'Science, Religion & Human Nature',
        'link': 'http://www.guardian.co.uk/society/2010/may/09/alcoholism-health-doctor-addiction-drug/print',
        'publication': 'The Observer',
        'title': 'The Little Pill That Could Cure Alcoholism'},
    {   'category': 'Science, Religion & Human Nature',
        'link': 'http://www.texasobserver.org/dateline/he-who-casts-the-first-stone',
        'publication': 'Texas Observer',
        'title': 'He Who Casts The First Stone'},
    {   'category': 'Science, Religion & Human Nature',
        'link': 'http://www.esquire.com/features/argentine-ant-control-0810',
        'publication': 'Esquire',
        'title': 'Invasion'},
    {   'category': 'Science, Religion & Human Nature',
        'link': 'http://www.theamericanscholar.org/solitude-and-leadership/print/',
        'publication': 'The American Scholar',
        'title': 'Solitude And Leadership'},
    {   'category': 'Science, Religion & Human Nature',
        'link': 'http://www.the-american-interest.com/article.cfm?piece=792',
        'publication': 'The American Interest',
        'title': 'Understanding Corruption'},
    {   'category': 'Science, Religion & Human Nature',
        'link': 'http://www.archaeology.org/1003/etc/neanderthals.html',
        'publication': 'Archaeology',
        'title': 'Should We Clone Neanderthals'},
    {   'category': 'Science, Religion & Human Nature',
        'link': 'http://www.historynet.com/holy-terror-the-rise-of-the-order-of-assassins.htm',
        'publication': 'Military History Quarterly',
        'title': 'Holy Terror: The Rise Of The Order Of The Assassins'},
    {   'category': 'Science, Religion & Human Nature',
        'link': 'http://www.nybooks.com/articles/archives/2010/jan/14/night/',
        'publication': 'The New York Review Of Books',
        'title': 'Night'},
    {   'category': 'Science, Religion & Human Nature',
        'link': 'http://www.vanityfair.com/culture/features/2010/01/hadron-collider-201001?printable=true',
        'publication': 'Vanity Fair',
        'title': 'The Genesis 2.0 Project'},
    {   'category': 'Science, Religion & Human Nature',
        'link': 'http://www.theatlantic.com/magazine/archive/2010/08/autism-8217-s-first-child/8227/',
        'publication': 'The Atlantic',
        'title': "Autism's First Child"},
    {   'category': 'On Birth, Death, & The Afterlife',
        'link': 'http://motherjones.com/politics/2010/02/surrogacy-tourism-india-nayna-patel?page=1',
        'publication': 'Mother Jones',
        'title': "Inside India's Rent-A-Womb Business"},
    {   'category': 'On Birth, Death, & The Afterlife',
        'link': 'http://www.theatlantic.com/magazine/archive/2010/04/letting-go-of-my-father/8001/1/',
        'publication': 'The Atlantic',
        'title': 'Letting Go of My Father'},
    {   'category': 'On Birth, Death, & The Afterlife',
        'link': 'http://www.newyorker.com/reporting/2010/08/02/100802fa_fact_gawande?currentPage=all',
        'publication': 'The New Yorker',
        'title': 'Letting Go'},
    {   'category': 'On Birth, Death, & The Afterlife',
        'link': 'http://www.gq.com/news-politics/newsmakers/201010/suicide-nurse-mark-drybrough-chatrooms-li-dao?printable=true',
        'publication': 'Gq',
        'title': 'Are You Sure You Want To Quit The World'},
    {   'category': 'On Birth, Death, & The Afterlife',
        'link': 'http://www.vanityfair.com/politics/features/2010/02/sniper-201002',
        'publication': 'Vanity Fair',
        'title': 'The Distant Executioner'},
    {   'category': 'On Birth, Death, & The Afterlife',
        'link': 'http://www.americanscientist.org/issues/id.9326,y.2010,no.3,content.true,page.1,css.print/issue.aspx',
        'publication': 'American Scientist',
        'title': "To See For One's Self"},
    {   'category': 'On Birth, Death, & The Afterlife',
        'link': 'http://nplusonemag.com/the-frozen-ladder',
        'publication': 'N+1',
        'title': 'The Frozen Ladder'},
    {   'category': 'On Birth, Death, & The Afterlife',
        'link': 'http://women.timesonline.co.uk/tol/life_and_style/women/the_way_we_live/article7039572.ece',
        'publication': 'The Times Of London',
        'title': 'The British POW Who Broke Into Auschwitz - And Survived'},
    {   'category': 'On Birth, Death, & The Afterlife',
        'link': 'http://www.nytimes.com/2010/07/11/magazine/11cryonics-t.html',
        'publication': 'The New York Times Magazine',
        'title': 'Until Cryonics Do Us Part'},
    {   'category': 'Multimedia Matters',
        'link': 'http://www.guardian.co.uk/books/2010/oct/09/howard-jacobson-comic-novels',
        'publication': 'The Guardian',
        'title': 'On Taking Comic Novels Seriously'},
    {   'category': 'Multimedia Matters',
        'link': 'http://www.theparisreview.org/interviews/5997/the-art-of-nonfiction-no-3-john-mcphee',
        'publication': 'The Paris Review',
        'title': 'The Art Of Non-Fiction Number 3: John McPhee'},
    {   'category': 'Multimedia Matters',
        'link': 'http://www.theawl.com/2010/08/seven-years-as-a-freelance-writer-or-how-to-make-vitamin-soup/2',
        'publication': 'The Awl',
        'title': 'Seven Years As A Freelance Writer'},
    {   'category': 'Multimedia Matters',
        'link': 'http://www.nytimes.com/2010/11/28/business/28borker.html',
        'publication': 'The New York Times',
        'title': 'A Bully Finds A Pulpit On The Web'},
    {   'category': 'Multimedia Matters',
        'link': 'http://conelrad.blogspot.com/2010/08/hiroshima-this-is-your-life.html',
        'publication': 'Conelrad Adjacent',
        'title': 'Hiroshima: This Is Your Life'},
    {   'category': 'Multimedia Matters',
        'link': 'http://www.nybooks.com/articles/archives/2010/nov/25/generation-why/?pagination=false',
        'publication': 'The New York Review Of Books',
        'title': 'Generation Why'},
    {   'category': 'Multimedia Matters',
        'link': 'http://www.nybooks.com/articles/archives/2010/dec/09/beck-revelation/?pagination=false',
        'publication': 'The New York Review Of Books',
        'title': 'The Beck Revelation'},
    {   'category': 'Multimedia Matters',
        'link': 'http://www.esquire.com/print-this/price-is-right-perfect-bid-0810?page=all',
        'publication': 'Esquire',
        'title': "TV's Crowning Moment Of Awesome"},
    {   'category': 'The Innovative & Creative',
        'link': 'http://mcsweeneys.net/links/panoramaexcerpts/Ali.html',
        'publication': 'The San Francisco Panorama',
        'title': 'Could It Be That the Best Chance to Save a Young Family From Foreclosure is a 28-Year-Old Pakistani American Playright-slash-Attorney who Learned Bankruptcy Law on the Internet? Wells Fargo, You Never Knew What Hit You'},
    {   'category': 'The Innovative & Creative',
        'link': 'http://www.defunctmag.com/Defunct/Monson.html',
        'publication': 'Defunct',
        'title': 'Long Live The Jart'},
    {   'category': 'The Innovative & Creative',
        'link': 'http://www.radiolab.org/2010/apr/05/',
        'publication': 'Radiolab',
        'title': 'Limits'},
    {   'category': 'The Innovative & Creative',
        'link': 'http://www.slate.com/id/2264784/',
        'publication': 'Slate',
        'title': 'Kanye West Has A Goblet'},
    {   'category': 'The Innovative & Creative',
        'link': 'http://www.slate.com/id/2273611/',
        'publication': 'Slate',
        'title': 'Please Allow Me To Correct A Few Things'},
    {   'category': 'The Innovative & Creative',
        'link': 'http://opinionator.blogs.nytimes.com/2010/06/20/the-anosognosics-dilemma-1/',
        'publication': 'The New York Times',
        'title': "The Anosognosic's Dilemma"},
    {   'category': 'The Innovative & Creative',
        'link': 'http://www.guardian.co.uk/science/the-lay-scientist/2010/sep/24/1',
        'publication': 'The Guardian',
        'title': 'This Is A News Website Article About A Scientific Paper'},
    {   'category': 'Food',
        'link': 'http://www.texasmonthly.com/preview/2010-04-01/feature2',
        'publication': 'Texas Monthly',
        'title': 'Consider The Oyster'},
    {   'category': 'Food',
        'link': 'http://money.cnn.com/2010/08/20/news/companies/inside_trader_joes_full_version.fortune/',
        'publication': 'Fortune',
        'title': 'Inside The Secret World Of Trader Joes'},
    {   'category': 'Food',
        'link': 'http://www.nytimes.com/2010/10/10/magazine/10dinner-t.html?_r=1&pagewanted=1',
        'publication': 'The New York Times',
        'title': 'The 36-Hour Dinner Party'},
    {   'category': 'Food',
        'link': 'http://www.nytimes.com/2010/06/27/magazine/27Tuna-t.html',
        'publication': 'The New York Times Magazine',
        'title': "Tuna's End"},
    {   'category': 'Food',
        'link': 'http://www.nytimes.com/2010/10/10/magazine/10Kosher-t.html?pagewanted=all',
        'publication': 'The New York Times Magazine',
        'title': 'Keeping It Kosher'},
    {   'category': 'Food',
        'link': 'http://live.gourmet.com/2010/11/app-exclusive-the-guiltless-pleasure/',
        'publication': 'Gourmet Live',
        'title': 'The Guiltless Pleasure'},
    {   'category': 'Profiles',
        'link': 'http://nymag.com/movies/profiles/67284/',
        'publication': 'New York Magazine',
        'title': 'The James Franco Project'},
    {   'category': 'Profiles',
        'link': 'http://www.details.com/culture-trends/news-and-politics/201008/interview-boxing-mike-tyson?printable=true',
        'publication': 'Details',
        'title': 'Everything You Know About Mike Tyson Is Wrong'},
    {   'category': 'Profiles',
        'link': 'http://www.slate.com/id/2247593/',
        'publication': 'Slate',
        'title': 'Big Breitbart'},
    {   'category': 'Profiles',
        'link': 'http://www.esquire.com/features/roger-ebert-0310',
        'publication': 'Esquire',
        'title': 'Roger Ebert: The Essential Man'},
    {   'category': 'Profiles',
        'link': 'http://www.newyorker.com/reporting/2010/09/13/100913fa_fact_boyer?currentPage=all',
        'publication': 'The New Yorker',
        'title': 'Frat House For Jesus'},
    {   'category': 'Profiles',
        'link': 'http://www.nytimes.com/2010/01/31/magazine/31Jihadist-t.html',
        'publication': 'The New York Times Magazine',
        'title': 'The Jihadist Next Door'},
    {   'category': 'Profiles',
        'link': 'http://www.nytimes.com/2010/04/25/magazine/25allen-t.html',
        'publication': 'The New York Times Magazine',
        'title': 'The Man The White House Wakes Up To'},
    {   'category': 'Profiles',
        'link': 'http://www.gq.com/entertainment/humor/201008/comedy-issue/comedy-issue-garry-shandling',
        'publication': 'Gq',
        'title': "The Comedian's Comedian's Comedian"},
    {   'category': 'Profiles',
        'link': 'http://www.guardian.co.uk/music/2010/oct/09/insane-clown-posse-christians-god',
        'publication': 'The Guardian',
        'title': 'Insane Clown Posse: And God Created Controversy'},
    {   'category': 'Profiles',
        'link': 'http://www.weeklystandard.com/articles/boy-yazoo-city_523551.html',
        'publication': 'The Weekly Standard',
        'title': 'The Boy From Yazoo City'},
    {   'category': 'This Is A Business',
        'link': 'http://www.npr.org/blogs/money/2010/02/podcast_dreaming_of_plastic_cr.html',
        'publication': 'Planet Money',
        'title': 'Dreaming of Plastic Crates in Haiti'},
    {   'category': 'This Is A Business',
        'link': 'http://www.texasmonthly.com/2010-04-01/feature3.php',
        'publication': 'Texas Monthly',
        'title': 'The Lost Girls'},
    {   'category': 'This Is A Business',
        'link': 'http://nymag.com/news/features/65238/',
        'publication': 'New York',
        'title': 'Rachel Uchitel Is Not A Madam'},
    {   'category': 'This Is A Business',
        'link': 'http://www.washingtonmonthly.com/features/2010/1011.gravois.html',
        'publication': 'The Washington Monthly',
        'title': 'The Closing Of The Marijuana Frontier'},
    {   'category': 'This Is A Business',
        'link': 'http://www.theawl.com/2010/11/my-summer-on-the-content-farm',
        'publication': 'The Awl',
        'title': 'My Summer On The Content Farm'},
    {   'category': 'This Is A Business',
        'link': 'http://places.designobserver.com/entry.html?entry=13598',
        'publication': 'Design Observer',
        'title': 'All Those Numbers: Logistics, Territory and Walmart'},
    {   'category': 'This Is A Business',
        'link': 'http://www.vanityfair.com/business/features/2010/10/greeks-bearing-bonds-201010',
        'publication': 'Vanity Fair',
        'title': 'Beware Of Greeks Bearing Bonds'},
    {   'category': 'This Is A Business',
        'link': 'http://www.theatlantic.com/magazine/archive/2010/12/-8220-god-help-you-you-39-re-on-dialysis-8221/8308/1/',
        'publication': 'The Atlantic',
        'title': "God Help You. You're On Dialysis"},
    {   'category': 'This Is A Business',
        'link': 'http://www.thisamericanlife.org/radio-archives/episode/403/nummi',
        'publication': 'This American Life',
        'title': 'NUMMI'},
    {   'category': 'This Is A Business',
        'link': 'http://www.nybooks.com/articles/archives/2010/oct/14/pirates-are-winning/?pagination=false',
        'publication': 'The New York Review Of Books',
        'title': 'The Pirates Are Winning'},
    {   'category': 'This Is A Business',
        'link': 'http://www.believermag.com/issues/201009/?read=article_young',
        'publication': 'The Believer',
        'title': 'Sweatpants in Paradise'},
    {   'category': 'This Is A Business',
        'link': 'http://www.theatlantic.com/magazine/archive/2010/05/gentrification-and-its-discontents/8092/',
        'publication': 'The Atlantic',
        'title': 'Gentrification And Its Discontents'},
    {   'category': 'This Is A Business',
        'link': 'http://www.thepointmag.com/archive/predatory-habits/',
        'publication': 'The Point',
        'title': 'Predatory Habits'},
    {   'category': 'This Is A Business',
        'link': 'http://www.city-journal.org/2010/20_4_urban-entrepreneurship.html',
        'publication': 'City Journal',
        'title': 'Start-Up City'},
    {   'category': 'This Is A Business',
        'link': 'http://www.slate.com/id/2276982/pagenum/all/#p2',
        'publication': 'Slate',
        'title': 'Tokyo Hooters Girls'}]

AUTHENTICATE_URL = 'https://www.instapaper.com/api/authenticate'
ADD_URL = 'https://www.instapaper.com/api/add'
 
username = raw_input("Enter your Instapaper email or username: ")
passwd = getpass.getpass("And password, if you have one: ")

# Check username + password is valid. 
print 'Checking your account details...'
user_data = urllib.urlencode({"username": username,"password": passwd})
validated = urllib.urlopen(AUTHENTICATE_URL, user_data)
status_code = validated.read()
if status_code!='200':
    if status_code=='403':
        print 'Sorry, invalid username or password! Please go to instapaper.com to retrieve your account details'
    elif status_code=="500":
        print 'Sorry, the Instapaper API is down. Please try again later.'
    else:
        print "Sorry, something went wrong - status code %s" % status_code
    sys.exit()

# Add articles. 
print 'Adding articles...'
for (i, a) in enumerate(ARTICLES):
    print "Adding '%s' from %s" % (a['title'], a['publication'])
    data = urllib.urlencode({ 
        'username': username,
        'password': passwd,
        'title': a['title'],
        'url': a['link'],
        'selection': "%s - Top 100 2010, %s" % (a['publication'], a['category'])
    })
    posted = urllib.urlopen(ADD_URL, data)
    status_code = posted.read()
    if status_code!='201':
        if status_code=="400":
            print 'Bad request or exceeded the rate limit'
        elif status_code=='403': 
            print "Invalid username or password"
        elif status_code=='500':  
            print "Sorry, the Instapaper API encountered an error. Please try again later"
        else:
            print "Sorry, something went wrong - status code %s" % status_code
