# Verified news for Monday 23 November 2026 — 50 stories.
# Sources verified from Reuters, AP, AFP, BBC, ESPN/Formula1 and wire
# pickups on the morning of 23 Nov 2026. Each story carries a region and
# a field so the header counts are honest and checkable.
# Regions: Middle East, Europe, North America, South Asia, East Asia,
# Africa, Oceania (7). Fields: climate, war, politics, sport, markets,
# tech, crime, health, entertainment, education, environment, transport,
# diplomacy, economy, energy, disaster, obituary, society (18).

MASTHEAD_NAME = "THE WORLD TODAY"
MASTHEAD_DATE = "MONDAY 23 NOVEMBER 2026"

LEADS = [
    {
        "headline": "COP31 COLLAPSES \u2014 NO DEAL",
        "deck": (
            "UN climate talks end in Antalya with no deal \u2014 the "
            "longest COP on record. The EU rejected a draft with no "
            "fossil-fuel mention; Guterres \u201cdeeply disappointed\u201d."
        ),
        "source": "Reuters",
        "region": "Europe",
        "field": "climate",
    },
    {
        "headline": "GULF WAR ESCALATES: 14 TANKERS SET TO BREAK BLOCKADE",
        "deck": (
            "Iran masses a tanker convoy at Kharg Island to run the US "
            "blockade; Bahrain counts two injured after Saturday\u2019s "
            "strikes on US bases."
        ),
        "source": "IRNA / Bahrain govt",
        "region": "Middle East",
        "field": "war",
    },
    {
        "headline": "DEMOCRATS WIN 258 HOUSE SEATS",
        "deck": (
            "Largest House majority since 1992 \u2014 Hubbard beats Foxx "
            "in North Carolina on Sunday to seal it."
        ),
        "source": "wire",
        "region": "North America",
        "field": "politics",
    },
    {
        "headline": "VERSTAPPEN WINS WILD VEGAS GP",
        "deck": (
            "35 lead changes under the lights; beats Norris by 0.639s, "
            "Piastri third after a 14-place fightback; Ferraris collide."
        ),
        "source": "Formula1/ESPN",
        "region": "North America",
        "field": "sport",
    },
]

EXPLAINER = {
    "label": "WHY THE GULF IS BURNING",
    "text": (
        "The US\u2013Iran war is in its ninth month: a US naval blockade "
        "on Iran, tanker attacks in the Strait of Hormuz, strikes on "
        "Qeshm Island, Bahrain and Kuwait \u2014 and Brent crude holding "
        "$92.57."
    ),
    "source": "Reuters",
}

# 46 grid stories: short bold headline, one short deck line, source tag.
GRID = [
    ("RUSSIAN SHIP STILL BURNING OFF FINLAND",
     "Cargo ship Sparta II ablaze in the Gulf of Finland after an attack.",
     "Reuters", "Europe", "war"),
    ("14 MISSING AFTER DRONE HITS KYIV FLATS",
     "Russian drone hits a building in the Kyiv region, Zelenskyy says.",
     "Reuters", "Europe", "war"),
    ("DRONE HITS KYIV SUPERMARKET",
     "3 killed, 15 wounded incl. 3 children in the Sunday-evening strike.",
     "Kyiv officials", "Europe", "war"),
    ("WOMAN KILLED IN DNIPROPETROVSK STRIKES",
     "9 injured in Russian attacks on the region.",
     "officials", "Europe", "war"),
    ("ZELENSKYY: GIVE US PATRIOTS",
     "Urges US to approve transfers as Russia fires 165 missiles in a week.",
     "wire", "Europe", "war"),
    ("RUSSIAN WARSHIP SUNK OFF LIBYA",
     "Explosion on a Russian ship follows a suspected Ukrainian drone attack.",
     "wire", "Africa", "war"),
    ("MYANMAR SLAMS ASEAN DECISION",
     "Army-backed govt calls it \u2018unfair and imbalanced\u2019.",
     "wire", "East Asia", "politics"),
    ("DRONE HITS UN BUILDING IN KHARTOUM",
     "UN reports an attack on a residential area in Sudan.",
     "UN", "Africa", "war"),
    ("INDONESIA FACTORY FIRE: SEARCH RESUMES TODAY",
     "24 body bags removed from the Java candy factory; 29 workers missing.",
     "Reuters", "East Asia", "disaster"),
    ("LISBON MARCHES ON LIVING COSTS",
     "Thousands protest as prices fuel anger.",
     "wire", "Europe", "society"),
    ("NEPAL PM MEETS MODI IN DELHI",
     "Balendra Shah on a state visit, 22\u201323 Nov; talks held Monday.",
     "wire", "South Asia", "diplomacy"),
    ("S. KOREA EDUCATION MINISTER QUITS",
     "Resigns amid an AI cheating scandal.",
     "wire", "East Asia", "education"),
    ("SAUDI COALITION DOWNS HOUTHI MISSILE",
     "Intercepted in the western region after a launch towards Riyadh.",
     "wire", "Middle East", "war"),
    ("INDIA POSTS RECORD 720/9 IN WELLINGTON",
     "Record Test total against New Zealand at the Basin Reserve.",
     "wire", "Oceania", "sport"),
    ("FBI PROBES BREACH OF CRIME DATABASE",
     "Trump confirms the hack in a Saturday TV interview.",
     "CNN/Al Jazeera", "North America", "crime"),
    ("NVIDIA CHIP-DIVERSION ROW DEEPENS",
     "Alice Huang linked to a secret network sending AI chips to China.",
     "wire", "North America", "tech"),
    ("EISENKOT: SETTLER ARSON IS \u2018JEWISH TERRORISM\u2019",
     "As Netanyahu stays silent; coalition talks fail a second round.",
     "wire", "Middle East", "politics"),
    ("GAZA\u2019S DIABETIC CHILDREN LACK INSULIN",
     "Struggle for life-saving medicine amid the siege.",
     "wire", "Middle East", "health"),
    ("US ARMY TO BLAST EXPLOSIVES IN IOWA",
     "Five tonnes to be detonated by 24 Nov despite a court-ordered pause.",
     "wire", "North America", "society"),
    ("TANKER INCIDENT EAST OF HORMUZ",
     "Reported amid Iranian threats to break the US blockade.",
     "UKMTO", "Middle East", "energy"),
    ("TWO TANKERS HIT IN HORMUZ",
     "UKMTO reports projectiles strike vessels leaving the Gulf.",
     "UKMTO", "Middle East", "energy"),
    ("WASHINGTON GOVERNOR: ICE \u2018OUT OF CONTROL\u2019",
     "After two people arrested at the airport.",
     "wire", "North America", "politics"),
    ("DELTA DELAYS IN ATLANTA",
     "Automation system issue disrupts flights.",
     "wire", "North America", "transport"),
    ("MILEY CYRUS MARRIES MAXX MORANDO",
     "California ceremony.",
     "wire", "North America", "entertainment"),
    ("TOM JACKSON DIES AT 75",
     "Ex-Broncos star and ESPN broadcaster.",
     "ESPN", "North America", "obituary"),
    ("3 KILLED AT OHIO BABY SHOWER",
     "Shooting; one man in custody.",
     "wire", "North America", "crime"),
    ("MAY TO BURNHAM: \u2018ACCEPT BREXIT\u2019",
     "Former PM\u2019s warning to the Labour challenger.",
     "wire", "Europe", "politics"),
    ("EU BUDGET PLAN KEEPS \u20ac100BN FOR UKRAINE",
     "European Council president unveils a reduced budget proposal.",
     "wire", "Europe", "diplomacy"),
    ("US SPY CHIEF: PUTIN \u2018NOT AMERICA\u2019S FRIEND\u2019",
     "On Ukraine.",
     "wire", "North America", "politics"),
    ("NHS \u2018WASTING BILLIONS\u2019, DATA SHOW",
     "UK health spending under fire.",
     "wire", "Europe", "health"),
    ("BRITON SWIMS STRAIT OF HORMUZ",
     "To highlight the environmental cost of the war.",
     "wire", "Middle East", "environment"),
    ("BRENT HOLDS $92.57",
     "Friday close; Bitcoin below $58,000, a seventh straight weekly loss.",
     "market data", "Middle East", "markets"),
    ("BJP MP WADKUTE DIES IN DELHI",
     "Rajya Sabha member, cardiac arrest.",
     "wire", "South Asia", "obituary"),
    ("AMIT SHAH\u2019S \u20b94,000 CR ARUNACHAL PUSH",
     "Infrastructure projects launched.",
     "wire", "South Asia", "economy"),
    ("MODI OPENS AI CENTRE AT IIT PATNA",
     "New centre for artificial intelligence research.",
     "wire", "South Asia", "tech"),
    ("INDIA, BULGARIA TALK IMEC, BLACK SEA",
     "Bilateral ties discussed.",
     "wire", "South Asia", "diplomacy"),
    ("TATA STEEL\u2019S \u20b928,000 CR APL APOLLO DEAL",
     "Steel deal worth \u20b928,000 crore.",
     "wire", "South Asia", "economy"),
    ("ANUPAMA KEEPS WORLD SNOOKER CROWN",
     "Defends the IBSF women\u2019s title.",
     "wire", "South Asia", "sport"),
    ("HYDERABAD STUDENTS PROTEST",
     "Demand action over casteist remarks.",
     "wire", "South Asia", "society"),
    ("9 PILGRIMS KILLED IN RAJASTHAN CRASH",
     "Vehicle rams a truck in Kota.",
     "wire", "South Asia", "transport"),
    ("SAFFRON FIELDS \u2018USED AS DUMPS\u2019",
     "Mehbooba Mufti on Kashmir.",
     "wire", "South Asia", "environment"),
    ("70% OF AUSSIE MPS SAY POLITICS HARMED MENTAL HEALTH",
     "Landmark study to be released in Parliament on Monday.",
     "wire", "Oceania", "health"),
    ("SIX SENT TO JUVENILE HOME AFTER MUMBAI ASSAULT",
     "Six sent to a juvenile home after the assault.",
     "wire", "South Asia", "crime"),
    ("CHINA \u2018DISAPPOINTED\u2019 AT COP31",
     "\u201cWe missed lots of things developing countries want,\u201d says Li Gao.",
     "Reuters", "East Asia", "climate"),
    ("EU REFUSES \u2018GREENWASH\u2019 DEAL",
     "\u201cWe will not accept a COP that greenwashes fossil fuel.\u201d",
     "Reuters", "Europe", "climate"),
    ("KURUM LEAVES STAGE MID-SPEECH",
     "COP31 president walks out during the closing plenary.",
     "edie/Reuters", "Europe", "climate"),
]

TIMELINE = [
    ("SAT 21 NOV ~18:00", "IRGC strikes US bases in Bahrain"),
    ("SAT 21 NOV EVENING", "Indonesia factory fire; 24 dead"),
    ("SUN 22 NOV ~07:00", "Verstappen wins the Las Vegas GP"),
    ("SUN 22 NOV AFTERNOON", "COP31 collapses with no deal"),
    ("SUN 22 NOV EVENING", "Democrats seal 258 House seats"),
    ("MON 23 NOV 00:00", "Search resumes at the Java factory"),
]

# Stories deliberately left out because they are older news.
DATE_CHECK = [
    ("KERCH BRIDGE SPAN COLLAPSES", "17 Nov"),
    ("ISRAEL ELECTS NEW SPEAKER", "17 Nov"),
    ("PERU 6.7 QUAKE", "21 Nov"),
    ("\u2018CHAPO ISIDRO\u2019 ARRESTED", "21 Nov"),
]

FOOTER = (
    "COP31 collapses with no deal \u2014 Gulf tanker convoy sets sail "
    "\u2014 Democrats take 258 House seats \u2014 Verstappen wins in Vegas "
    "\u2014 Brent $92.57."
)

# Numbered pins on the world map: (number, label, x fraction, y fraction)
MAP_PINS = [
    (1, "Antalya", 0.56, 0.42),
    (2, "Gulf", 0.63, 0.50),
    (3, "Washington", 0.22, 0.38),
    (4, "Las Vegas", 0.16, 0.44),
    (5, "Kyiv", 0.53, 0.18),
    (6, "Java", 0.79, 0.62),
    (7, "Delhi", 0.68, 0.50),
    (8, "Wellington", 0.93, 0.78),
]


def story_count():
    return len(LEADS) + len(GRID)


def region_count():
    regions = {s["region"] for s in LEADS}
    regions |= {g[3] for g in GRID}
    return len(regions)


def field_count():
    fields = {s["field"] for s in LEADS}
    fields |= {g[4] for g in GRID}
    return len(fields)
