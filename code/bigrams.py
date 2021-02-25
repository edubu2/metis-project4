bigrams = [
    (r"god bless america", "godblessamerica"),
    (r"corona ?virus", "covid"),
    (r"god bless", "godbless"),
    (r"do your part", "doyourpart"),
    (r"fake news media", "fakenewsmedia"),
    (r"trump lies?", "trumplies"),
    (r"biden lies?", "bidenlies"),
    (r"fake news", "fakenews"),
    (r"fake news network", "fakenewsnetwork"),
    (r"vote joe biden", "votejoebiden"),
    (r"trump supporters?", "trumpsupporter"),
    (r"biden supporters?", "bidensupporter"),
    (r"student loan debt", "studentloandebt"),
    (r"student loan", "studentloan"),
    (r"universal health ?care", "universalhealthcare"),
    (r"health ?care ?plan", "healthcareplan"),
    (r"health care", "healthcare"),
    (r"supreme courts?", "supremecourt"),
    (r"campaign trails?", "campaigntrail"),
    (r"pack the courts?", "packthecourt"),
    (r"cant stop", "cantstop"),
    (r"best case", "bestcase"),
    (r"worst case", "worstcase"),
    (r"cant wait", "cantwait"),
    (r"feel bad", "feelbad"),
    (r"love a?l?w?a?y?s? ?wins", "lovewins"),
    (r"worst week ever", "worstweekever"),
    (r"record_highs?", "recordhigh"),
    (r"record_lows?", "recordlow"),
    (r"worst year ever", "worstyearever"),
    (r"executive orders?", "executiveorder"),
    (r"white supremacy", "whitesupremacy"),
    (r"white supremacists?", "whitesupremacy"),
    (r"hispanic women", "hispanic_women"),
    (r"hispanic woman", "hispanic_woman"),
    (r"hispanic man", "hispanic_man"),
    (r"hispanic people", "hispanic_people"),
    (r"hispanic men", "hispanic_men"),
    (r"white women", "white_women"),
    (r"white woman", "white_woman"),
    (r"white man", "white_man"),
    (r"last four years", "lastfouryears"),    
    (r"african ?americans?", "africanamerican"),  
    (r"white people", "white_people"),    
    (r"black women", "black_women"),
    (r"white women", "white_women"),
    (r"black woman", "black_woman"),
    (r"white woman", "white_woman"),
    (r"black man", "black_man"),
    (r"white man", "white_man"),
    (r"black people", "black_people"),
    (r"white people", "white_people"),
    (r"hispanic people", "hispanic_people"),
    (r"national security", "nationalsecurity"),
    (r"fear campaign", "fear_campaign"),
    (r"black men", "black_men"),
    (r"white men", "white_men"),   
    (r"hate speech", "hatespeech"),
    (r"come together", "cometogether"),
    (r"climate change", "climatechange"),
    (r"global warming", "globalwarming"),
    (r"shits going down ?t?o?m?o?r?r?o?w?", "shitsgoingdowntomorrow"),
    (r"middle east", "middleeast"),
    (r"north korea", "northkorea"),
    (r"over the border", "overtheborder"),
    (r"supress the vote", "supressthevote"),
    (r"let them in", "letthemin"),
    (r"let them go", "letthemgo"),
    (r"fox news", "foxnews"),
    (r"fuck ?donald ?trump", "fxxktrump"),
    (r"fuck ?joe ?biden", "fxxkbiden"),
    (r"fuck trump", "fxxktrump"),
    (r"fuck biden", "fxxkbiden"),
    (r"gun rights", "gunrights"),
    (r"music fans?", "musicfan"),
    (r"take away our guns", "takeawayourguns"),
    (r"vote blue", "voteblue"),
    (r"vote ?f?o?r? donald trump", "votedonaldtrump"),
    (r"vote ?f?o?r? trump", "votedonaldtrump"),
    (r"vote ?f?o?r? joe biden", "votejoebiden"),
    (r"vote ?f?o?r? biden", "votejoebiden"),
    (r"vote red", "votered"),
    (r"voting red", "votered"),
    (r"voting blue", "voteblue"),
    (r'voter supression', 'votersupression'),
    (r'hispanic votes?', 'hispanicvote'),
    (r'white votes?', 'whitevote'),
    (r'hispanic votes?', 'hispanicvote'),
    (r'people of color', 'peopleofcolor'),
    (r'corrupt politicians?', 'corruptpolitician'),
    (r'whole world', 'wholeworld'),
    (r'last election', 'lastelection'),
    (r'stock market', 'stockmarket'),
    (r'orange man', 'orangeman'),
    (r'violent crimes?', 'violentcrime'),
    (r'defund the police', 'defundthepolice'),
    (r'campaign rally', 'campaignrally'),
    (r'violent protests?', 'violentprotest'),
    (r'cover ups?', 'coverup'),
    (r"vice presidents?", "vicepresident"),
    (r"domestic terrorism", "domesticterrorism"),
    (r"conspiracy theory", "conspiracytheory"),
    (r"go vote", "govote"),
    (r"get out there and vote", "getoutthereandvote"),
    (r"misinformation campaign", "misinformationcampagn"),
    (r"worst ?president ?ever", "worstpresidentever"),
    (r"best ?president ?ever", "bestpresidentever"),
    (r"go away", "goaway"),
    (r"far left", "farleft"),
    (r"far right", "farright"),
    (r"left wing", "leftwing"),
    (r"domestic terrorism", "domesticterrorism"),
    (r"conspiracy theory", "conspiracytheory"),
    (r"campaign stops?", "campaignstop"),
    (r"far left", "farleft"),
    (r"far right", "farright"),
    (r"left wing", "leftwing"),
    (r"right wing", "rightwing"),
    (r"electoral college", "electoralcollege"),
    (r"russian interference", "russianinteference"),
    (r"foreign interference", "foreigninteference"),    
    (r"social inequality", "socialinequality"),
    (r"hunter biden", "hunterbiden"),
    (r"ivanka trump", "ivankatrump"),
    (r"eric trump", "erictrump"),
    (r"trump crime family", "trumpcrimefamily"),
    (r"biden crime family", "bidencrimefamily"),
    (r"travel restrictions?", "travelrestriction"),
    (r"stay at home orders?", "stayathomeorder"),
    (r"lock downs?", "lockdown"),
    (r"tik tok", "tiktok"),
    (r"legal votes?", "legalvote"),
    (r"law enforcement", "lawenforcement"),
    (r"president trump", "donaldtrump"),
    (r"president donald trump", "donaldtrump"),
    (r"vice president mike pence", "mikepence"),
    (r"vice president pence", "mikepence"),
    (r"vice president kamala harris", "kamalaharris"),
    (r"vice president harris", "kamalaharris"),
    (r"vice president", "vicepresident"),
    (r"voting rights?", "votingrights"),
    (r"coronavirus outbreaks?", "coronavirusoutbreak"),
    (r"wwgwga", "wwg1wga"),
    (r"paris climate", "paris_climate"),
    (r"ag", "attorneygeneral"),
    (r"black hat", "blackhat"),
    (r"white hat", "whitehat"),
    (r"deathtoll", "deathtoll"),
    (r"heart and soul", "heartandsoul"),
    (r"covid hoax", "covidhoax"),
    (r"reality show hosts?", "realityshowhost"),
    (r"reality shows?", "realityshow"),
    (r"covid case", "covidcase"),
    (r"keep calm", "keepcalm"),
    (r"american dream", "americandream"),
    (r"cognitive ?problems?", "cognitiveproblem"),
    (r"where we go one we go all", "wwg1wga"),
    (r"anthony fauci", "anthonyfauci"),
    (r"flips? outcomes?", "flipoutcome"),
    (r"careful what you wish for", "carefulwhatyouwishfor"),
    (r"first black vp", "firstblackvp"),
    (r"first black vice president", "firstblackvp"),
    (r"do your research", "doyourresearch"),
    (r"united states of america", "usa"),
    (r"democratic presidential nominee", "democraticpresidentialnominee"),
    (r"republican presidential nominee", "republicanpresidentialnominee"),
    (r"farm country", "farmcountry"),
    (r"democratic party", "democraticparty"),
    (r"republican party", "republicanparty"),
    (r"red states?", "redstate"),
    (r"raise taxe?s?", "raisetax"),
    (r"increase taxe?s?", "raisetax"),
    (r"communications directors?", "communicationsdirector"),
    (r"lower taxe?s?", "reducetax"),
    (r"lower taxe?s?", "reducetax"),
    (r"reduce taxe?s?", "reducetax"),
    (r"american ?presidents?", "americanpresident"),
    (r"blue states?", "bluestate"),
    (r"be kind", "bekind"),
    (r"planned parenthoods?", "plannedparenthood"),
    (r"minimum wage", "minimumwage"),
    (r"four more years", "fourmoreyears"),
    (r"hope he dies", "hopehedies"),
    (r"hope you die", "hopeyoudie"),
    (r"absentee ballots?", "absenteeballot"),
    (r"draini?n?g?e?d? ?the ?swamps?", "draintheswamp"),
    (r"hillary clinton", "hillaryclinton"),
    (r"barack obama", "barackobama"),
    (r"decent man", "decentman"),
    (r"election eve", "electioneve"),
    (r"abortion rights?", "abortionrights"),
    (r"pro life", "prolife"),
    (r"ban abortion", "banabortion"),
    (r"legalize ?murder", "legalizemurder"),
    (r"medicare ?for ?all", "medicareforall"),
    (r"legalize ?cannabis", "legalizemarijuana"),
    (r"legalize ?weed", "legalizemarijuana"),
    (r"legalize ?it", "legalizemarijuana"),
    (r"held office", "heldoffice"),
    (r"ignore the polls", "ignorethepolls"),
    (r"mind games?", "mindgame"),
    (r"polls ?are ?rigged", "pollsarerigged"),
    (r"civil rights", "civilrights"),
    (r"social distancing", "socialdistancing"),
    (r"lock him up", "lockhimup"),
    (r"lock her up", "lockherup"),
    (r"lock them up", "lockthemup"),
    (r"invalidate votes", "invalidatevotes"),
    (r"cancel culture", "cancelculture"),
    (r"pro choice", "prochoice"),
    (r"come together", "cometogether"),
    (r"rise up", "riseup"),
    (r"lady gaga", "ladygaga"),
    (r"hate speech", "hatespeech"),
    (r"baby killers?", "babykiller"),
    (r"public health", "publichealth"),
    (r"go home", "gohome"),
    (r"first lady", "firstlady"),
    (r"black lives matter", "blacklivesmatter"),
    (r"blm", "blacklivesmatter"),
    (r"all lives matter", "alllivesmatter"),
    (r"blue lives matter", "bluelivesmatter"),
    (r"mailin ballots?", "mailinballot"),
    (r"mailins?", "mailinballot"),
    (r"steal speeche?s?", "stealspeech"),
    (r"stole speeche?s?", "stealspeech"),
    (r"united states", "usa"),
    (r"attorney generals?", "attorneygeneral"),
    (r"white house", "whitehouse"),
    (r"unite for a better america", "uniteforabetteramerica"),
    (r"commander and chief", "commanderandchief"),
    (r"make america great again", "maga"),
    (r"election fraud", "electionfraud"),
    (r"sleepy joe biden", "sleepyjoe"),
    (r"sleepy joe", "sleepyjoe"),
    (r"presidential elections?", "election"),
    (r"running mates?", "runningmate"),
    (r"voting machines?", "votingmachine"),
    (r"cast your ballots?", "castyourballot"),
    (r"foreign policy", "foreignpolicy"),
    (r"election days?", "electionday"),
    (r"allow abortions?", "allowabortion"),
    (r"voting booths?", "votingbooth"),
    (r"radical left", "radicalleft"),
    (r"free speech", "freespeech"),
    (r"first amendment", "firstamendment"),
    (r"joe biden", "joebiden"),
    (r"kamala harris", "kamalaharris"),
    (r"faithful followers?", "faithfulfollower"),
    (r"donald trump", "donaldtrump"),
    (r"mike pence", "mikepence"),
    (r"illegal aliens", "illegalaliens"),
    (r"illegal immigrants", "illegalimmigrants"),
    (r"nancy pelosi", "nancypelosi"),
    (r"mitch mcconnell", "mitchmcconnell"),
    (r"bernie sanders", "berniesanders"),
    (r"\bbernie\b", "berniesanders"),
    (r"\bobama\b", "barackobama"),
    (r"\bhillary\b", "hillaryclinton"),
    (r"\bdonald\b", "donaldtrump"),
    (r"\bbiden\b", "joebiden"),
    (r"\bpence\b", "mikepence"),
    (r"\bfauci\b", "anthonyfauci"),
    (r"\bjoe\b", "joebiden"),
    (r"\bkamala\b", "kamalaharris"),
    (r"\bharris\b", "kamalaharris"),
    (r"\btrump\b", "donaldtrump")
]