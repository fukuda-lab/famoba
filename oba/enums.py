from enum import Enum
from typing import List, TypedDict


class OBACommandsSequencesFunctions(Enum):
    """These functions are the functions correspond to the functions defined in oba_commands_sequences.py"""

    def control_site_visit_sequence(
        control_site: str,
        next_site_rank: str = 0,
        clean_run: bool = False,
        cookie_banner_action: int = 0,
        _test_quick=True,
        youtube=False,
    ):
        pass

    def individual_training_visit_sequence(
        training_site: str,
        next_site_rank=None,
        sleep: int = 10,
        creation: bool = False,
        cookie_banner_action: int = 0,
        _test_quick=True,
    ):
        pass

    def training_visits_sequence(
        training_sites: List[str],
        next_site_rank: int,
        cookie_banner_action: int = 0,
    ):
        pass

    def get_cookie_banner_visit_sequences(
        training_pages: list,
        control_pages: list = [],
        time_for_user: int = 15,
    ):
        pass


class WebShrinkerCredentials(TypedDict):
    api_key: str
    secret_key: str


class TrancoPagesParams(TypedDict):
    updated: bool
    size: int


class CustomPagesParams(TypedDict):
    categorize_pages: bool
    custom_pages_list: int


class GenericQueries:
    """Stateless Queries"""

    GetBrowserIds = "SELECT DISTINCT(browser_id) FROM crawl ORDER BY start_time;"
    GetAmountOfVisits = "SELECT COUNT(*) FROM site_visits;"


class CleanBrowserQueries:
    """They need an instance to set the browser_ids first"""

    def __init__(self, browser_id):
        self.browser_id = browser_id

        self.CleanRunVisitsQuery = (
            "SELECT site_url, visit_id FROM site_visits WHERE browser_id ="
            f" '{self.browser_id}';"
        )


class OBABrowserQueries:
    """They need an instance to set the browser_ids first"""

    def __init__(self, browser_id):
        self.browser_id = browser_id

    def get_visit_rows_per_control_site_query(self, control_site_url: str):
        """Given a control site url, returns a list of tuples with (site_url, visit_id);"""
        return (
            "SELECT site_url, visit_id, site_rank FROM site_visits WHERE browser_id ="
            f" {self.browser_id} AND site_url = '{control_site_url}' ORDER BY"
            " site_rank;"
        )

    def get_unresolved_advertisements_query(self):
        """Returns a list of tuples with (ad_id, landing_page_url)"""
        return (
            "SELECT ad_id, landing_page_url FROM visit_advertisements WHERE visit_id = ?"
            f" AND browser_id = {self.browser_id} AND landing_page_url IS NULL"
        )


class ControlVisitsQueries:
    """Queries for the ControlVisits tables"""

    InsertControlVisit = (
        "INSERT INTO ControlVisits (visit_id, browser_id, site_url, site_rank) VALUES"
        " (?, ?, ?, ?)"
    )


class AdvertisementsQueries:
    """Queries for the Advertisements tables"""

    SelectAllAdIdsWithLandingPageURLQuery = (
        "SELECT ad_id FROM advertisements WHERE landing_page_url=:landing_page_url"
    )
    SelectResolvedAdvertisementsNotCategorizedFromVisitQuery = (
        "SELECT ad_id, landing_page_url FROM advertisements WHERE visit_id=:visit_id"
        " AND browser_id=:browser_id AND landing_page_url IS NOT NULL AND categorized = 0"
    )


class ControlVisitAdsQueries:
    """Queries for the Advertisements tables"""

    InsertControlVisitAdQuery = (
        "INSERT INTO ControlVisitAds (control_visit_id, control_site_url,"
        " control_site_rank, ad_id, landing_url, ad_href_url) VALUES (?, ?, ?, ?, ?, ?)"
    )


class AdCategoriesQueries:
    """Queries for the ad_categories tables"""

    InsertAdCategoryQuery = (
        "INSERT INTO ad_categories (ad_id, visit_id, landing_page_url, category_name,"
        " category_code, parent_category, confident) VALUES (?, ?, ?, ?, ?, ?, ?)"
    )

    SelectCategoriesFromLandingPageURLQuery = "SELECT category_name, category_code, parent_category, confident FROM ad_categories WHERE landing_page_url=:landing_page_url"


class TrainingPagesQueries:
    """Queries for the TrainingPages tables"""

    SelectIdQuery = "SELECT id FROM TrainingPages WHERE page_url=?"
    SelectTrainingPagesWithCategoryNoFilter = """
            WITH FilteredPages AS (
                SELECT 
                    RC.category,
                    TP.id,
                    TP.page_url,
                    ROW_NUMBER() OVER (PARTITION BY RC.category ORDER BY TP.id ASC) as rn
                FROM 
                    RetrievedCategories RC
                JOIN 
                    TrainingPages TP ON RC.training_page_id = TP.id
            )
            SELECT 
                category,
				GROUP_CONCAT(CASE WHEN rn <= :k THEN id END, ', ') AS top_page_ids,
                GROUP_CONCAT(CASE WHEN rn <= :k THEN page_url END, ', ') AS top_page_urls,
                COUNT(id) AS total_pages
            FROM 
                FilteredPages
            WHERE 
                rn <= :k
            GROUP BY 
                category
            ORDER BY
                COUNT(id) DESC;
            """

    SelectTrainingPagesWithCategoryConfidentFilter = """
            WITH FilteredPages AS (
                SELECT 
                    RC.category,
                    TP.id,
                    TP.page_url,
                    ROW_NUMBER() OVER (PARTITION BY RC.category ORDER BY TP.id ASC) as rn
                FROM 
                    RetrievedCategories RC
                JOIN 
                    TrainingPages TP ON RC.training_page_id = TP.id
                WHERE 
                    RC.confident = :confident
            )
            SELECT 
                category,
				GROUP_CONCAT(CASE WHEN rn <= :k THEN id END, ', ') AS top_page_ids,
                GROUP_CONCAT(CASE WHEN rn <= :k THEN page_url END, ', ') AS top_page_urls,
                COUNT(id) AS total_pages
            FROM 
                FilteredPages
            WHERE 
                rn <= :k
            GROUP BY 
                category
            ORDER BY
                COUNT(id) DESC;
            """

    SelectTrainingPagesWithCategoryCBCheckedFilter = """
            WITH FilteredPages AS (
                SELECT 
                    RC.category,
                    TP.id,
                    TP.page_url,
                    ROW_NUMBER() OVER (PARTITION BY RC.category ORDER BY TP.id ASC) as rn
                FROM 
                    RetrievedCategories RC
                JOIN 
                    TrainingPages TP ON RC.training_page_id = TP.id
                WHERE 
                    TP.cookie_banner_checked =  :cookie_banner_checked
            )
            SELECT 
                category,
				GROUP_CONCAT(CASE WHEN rn <= :k THEN id END, ', ') AS top_page_ids,
                GROUP_CONCAT(CASE WHEN rn <= :k THEN page_url END, ', ') AS top_page_urls,
                COUNT(id) AS total_pages
            FROM 
                FilteredPages
            WHERE 
                rn <= :k
            GROUP BY 
                category
            ORDER BY
                COUNT(id) DESC;
            """

    SelectTrainingPagesWithCategoryConfidentAndCBCheckedFilter = """
            WITH FilteredPages AS (
                SELECT 
                    RC.category,
                    TP.id,
                    TP.page_url,
                    ROW_NUMBER() OVER (PARTITION BY RC.category ORDER BY TP.id ASC) as rn
                FROM 
                    RetrievedCategories RC
                JOIN 
                    TrainingPages TP ON RC.training_page_id = TP.id
                WHERE 
                    RC.confident = :confident
                AND
                    TP.cookie_banner_checked =  :cookie_banner_checked
            )
            SELECT 
                category,
				GROUP_CONCAT(CASE WHEN rn <= :k THEN id END, ', ') AS top_page_ids,
                GROUP_CONCAT(CASE WHEN rn <= :k THEN page_url END, ', ') AS top_page_urls,
                COUNT(id) AS total_pages
            FROM 
                FilteredPages
            WHERE 
                rn <= :k
            GROUP BY 
                category
            ORDER BY
                COUNT(id) DESC;
            """

    SelectTrainingPagesWithCategoryCBCheckedAndPresenceFilter = """
            WITH FilteredPages AS (
                SELECT 
                    RC.category,
                    TP.id,
                    TP.page_url,
                    ROW_NUMBER() OVER (PARTITION BY RC.category ORDER BY TP.id ASC) as rn
                FROM 
                    RetrievedCategories RC
                JOIN 
                    TrainingPages TP ON RC.training_page_id = TP.id
                WHERE 
                    TP.cookie_banner_checked =  :cookie_banner_checked
                AND
                    TP.cookie_banner_presence =  :cookie_banner_presence
            )
            SELECT 
                category,
				GROUP_CONCAT(CASE WHEN rn <= :k THEN id END, ', ') AS top_page_ids,
                GROUP_CONCAT(CASE WHEN rn <= :k THEN page_url END, ', ') AS top_page_urls,
                COUNT(id) AS total_pages
            FROM 
                FilteredPages
            WHERE 
                rn <= :k
            GROUP BY 
                category
            ORDER BY
                COUNT(id) DESC;
            """

    SelectTrainingPagesWithCategoryAllFilters = """
            WITH FilteredPages AS (
                SELECT 
                    RC.category,
                    TP.id,
                    TP.page_url,
                    ROW_NUMBER() OVER (PARTITION BY RC.category ORDER BY TP.id ASC) as rn
                FROM 
                    RetrievedCategories RC
                JOIN 
                    TrainingPages TP ON RC.training_page_id = TP.id
                WHERE 
                    RC.confident = :confident
                AND
                    TP.cookie_banner_checked =  :cookie_banner_checked
                AND
                    TP.cookie_banner_presence =  :cookie_banner_presence
            )
            SELECT 
                category,
				GROUP_CONCAT(CASE WHEN rn <= :k THEN id END, ', ') AS top_page_ids,
                GROUP_CONCAT(CASE WHEN rn <= :k THEN page_url END, ', ') AS top_page_urls,
                COUNT(id) AS total_pages
            FROM 
                FilteredPages
            WHERE 
                rn <= :k
            GROUP BY 
                category
            ORDER BY
                COUNT(id) DESC;
            """


class RetrievedCategoriesQueries:
    """Queries for the TrainingPages tables"""

    InsertCategoryQuery = (
        "INSERT INTO RetrievedCategories (training_page_id, training_page_url,"
        " category, taxonomy, taxonomy_tier, taxonomy_id, confident) VALUES (?, ?, ?,"
        " ?, ?, ?, ?)"
    )


class CrawlDataQueries:
    """Queries for the Crawling Data"""

    SelectJavascriptsQuery = (
        "SELECT (id, frame_id, script_url, document_url, top_level_url, func_name,"
        " call_stack, symbol, operation, value, arguments, time_stamp) FROM javascript"
        " WHERE browser_id=? AND visit_id=?"
    )
    # TOO MANY THINGS
    # SelectJavascriptsQuery = "SELECT (id, window_id, tab_id, frame_id, script_url, func_name, script_loc_eval, document_url, top_level_url, call_stack, symbol, operation, value, arguments, time_stamp) FROM javascript WHERE browser_id=? AND visit_id=?"


NOTHING_GROUP = [
    "amklegal.co.uk",
    "autoexpress.co.uk",
    "besthearingaids.co.uk",
    "bestsearches.net",
    "channelweb.co.uk",
    "cio.com",
    "cliniccompare.com",
    "clubmed.co.uk",
    "cnn.com",
    "combatsiege.com",
    "csoonline.com",
    "curaprox.co.uk",
    "decanter.com",
    "desertorder.com",
    "digitalcameraworld.com",
    "drivingelectric.com",
    "ecoukhomes.com",
    "etoro.com",
    "exoticca.com",
    "flashtalking.com",
    "flexispot.co.uk",
    "forgeofempires.com",
    "fullnutritionsecrets.com",
    "getsmartinsights.com",
    "goodto.com",
    "haier-europe.com",
    "homeinsulationvoucher.co.uk",
    "interactivebrokers.co.uk",
    "investinyourfamily.co.uk",
    "kingswoodwills.co.uk",
    "lasik-eyes.co.uk",
    "legacywillsquote.com",
    "marieclaire.co.uk",
    "moneysavinghelp.co.uk",
    "mygenes.co.uk",
    "navy.quest",
    "newdogdiscovery.com",
    "newskindiscovery.com",
    "nostalgicreads.com",
    "panzer.quest",
    "planetcapture.io",
    "provacan.co.uk",
    "reassured.co.uk",
    "responsiblelife.co.uk",
    "sotrends.com",
    "standard.co.uk",
    "tapashkumar.com",
    "theweathernetwork.com",
    "theweek.com",
    "tips-and-tricks.co",
    "tradetracker.net",
    "vodafone.co.uk",
    "volvocars.com",
    "wallstreetviral.com",
    "whogivesacrap.org",
    "willfully.co.uk",
    "zarbi.com",
]

A_GROUP = [
    "creativecdn.com",
    "googleadservices.com",
    "googlesyndication.com",
    "doubleclick.net",
    "integralads.com",
    "onetag.com",
    "rtbhouse.com",
    "travelaudience.com",
    "clkmg.com",
]

M_GROUP = [
    "a-great-big-data-intl.fyi",  # anyrun
    "bestgadgetdiscounts.com",  # scamadviser trustscore 1
    "dailyactunews.com",  # scamdoc trustscore 1
    "hike-footwear.com",  # scamadviser trustscore 1
    "infoaday.com",  # gridinsoft trustscore 11
    "pzzqvpjlfkbmb.com",  # anyrun
    "theweeklyhub.com",  # scamdoc trustscore 1
    "llsdzktnxwnnr.com",  # anyrun
    "zbrjtstrclnm.com",  # anyrun
]

M_MINUS_GROUP = [
    "bsmsrch.com",  # scamadviser trustcore 52
    "flarequick.com",  # Scam-detector trustscore 58.9
    "ilius.net",  # ipqualityscore 65 suspicious
    "mrwisebuyer.com",  # webparanoid
    "ps.sbs",  # trustpilot reviews
    "savemoneymarket.co.uk",  # trustpilot reviews
    "solar-panels24-uk.com",  # scamadviser trustscore 46
    "stufftopics.com",  # webparanoid
    "suholtd.com",  # trustpilot reviews
    "thesearchgod.com",  # scam-detector trustscore 40.5
    "vyager.com",  # scam-detector trustscore 75.8
    "wwiqtest.com",  # trustpilot reviews
    "zajoltd.com",  # trustpilot reviews
]

U_GROUP = [
    "anlim.de",
    "beleepstooked.com",
    "bibinboxputhwagon.com",
    "carinsurance3m-uk.space",
    "carinsurance4d-uk.space",
    "claimstrk.com",
    "fertility-clinics.world",
    "gain-an-intl-best-online-mba-courses-usa-ace.fyi",
    "gain-intl-work-from-home.zone",
    "globalvisitclub.com",
    "ivf-treatments.world",
    "latellscoaddents.com",
    "lds.xyz",
    "linka.me",
    "mangstomsadding.com",
    "mobilestairliftuk.space",
    "mysearchesnow.com",
    "nsoftrack.com",
    "perpetual-track.com",
    "pix-trk.com",
    "quelancepitylus.com",
    "roinattrack.com",
    "searchlinksnow.com",
    "shefence-citional.com",
    "snzgdl.com",
    "stairlift24-uk.space",
    "strateg.is",
    "tclfplxhhh.com",
    "top7.today",
    "vsgzddj.com",
]


IAB_CATEGORIES = {
    "IAB1": {
        "IAB1": "Arts & Entertainment",
        "IAB1-1": "Books & Literature",
        "IAB1-2": "Celebrity Fan/Gossip",
        "IAB1-3": "Fine Art",
        "IAB1-4": "Humor",
        "IAB1-5": "Movies",
        "IAB1-6": "Music & Audio",
        "IAB1-7": "Television & Video",
    },
    "IAB10": {
        "IAB10": "Home & Garden",
        "IAB10-1": "Appliances",
        "IAB10-2": "Entertaining",
        "IAB10-3": "Environmental Safety",
        "IAB10-4": "Gardening",
        "IAB10-5": "Home Repair",
        "IAB10-6": "Home Theater",
        "IAB10-7": "Interior Decorating",
        "IAB10-8": "Landscaping",
        "IAB10-9": "Remodeling & Construction",
    },
    "IAB11": {
        "IAB11": "Law, Government, & Politics",
        "IAB11-1": "Immigration",
        "IAB11-2": "Legal Issues",
        "IAB11-3": "Government Resources",
        "IAB11-4": "Politics",
        "IAB11-5": "Commentary",
    },
    "IAB12": {
        "IAB12": "News / Weather / Information",
        "IAB12-1": "International News",
        "IAB12-2": "National News",
        "IAB12-3": "Local News",
    },
    "IAB13": {
        "IAB13": "Personal Finance",
        "IAB13-1": "Beginning Investing",
        "IAB13-10": "Retirement Planning",
        "IAB13-11": "Stocks",
        "IAB13-12": "Tax Planning / Accounting",
        "IAB13-2": "Credit / Debit & Loans",
        "IAB13-3": "Financial News",
        "IAB13-4": "Financial Planning",
        "IAB13-5": "Hedge Fund",
        "IAB13-6": "Insurance",
        "IAB13-7": "Investing",
        "IAB13-8": "Mutual Funds / ETFs",
        "IAB13-9": "Options",
    },
    "IAB14": {
        "IAB14": "Society",
        "IAB14-1": "Dating / Personals",
        "IAB14-2": "Divorce Support",
        "IAB14-3": "LGBTQ+",
        "IAB14-4": "Marriage",
        "IAB14-5": "Senior Living",
        "IAB14-6": "Teens",
        "IAB14-7": "Weddings",
        "IAB14-8": "Ethnic Specific",
        "IAB14-WS1": "Social Networking",
    },
    "IAB15": {
        "IAB15": "Science",
        "IAB15-1": "Astrology",
        "IAB15-10": "Weather",
        "IAB15-2": "Biology",
        "IAB15-3": "Chemistry",
        "IAB15-4": "Geology",
        "IAB15-5": "Paranormal Phenomena",
        "IAB15-6": "Physics",
        "IAB15-7": "Space / Astronomy",
        "IAB15-8": "Geography",
        "IAB15-9": "Botany",
    },
    "IAB16": {
        "IAB16": "Pets",
        "IAB16-1": "Aquariums",
        "IAB16-2": "Birds",
        "IAB16-3": "Cats",
        "IAB16-4": "Dogs",
        "IAB16-5": "Large Animals",
        "IAB16-6": "Reptiles",
        "IAB16-7": "Veterinary Medicine",
    },
    "IAB17": {
        "IAB17": "Sports",
        "IAB17-1": "Auto Racing",
        "IAB17-10": "Figure Skating",
        "IAB17-11": "Fly Fishing",
        "IAB17-12": "American Football",
        "IAB17-13": "Freshwater Fishing",
        "IAB17-14": "Game & Fish",
        "IAB17-15": "Golf",
        "IAB17-16": "Horse Racing",
        "IAB17-17": "Horses",
        "IAB17-18": "Hunting / Shooting",
        "IAB17-19": "Inline Skating",
        "IAB17-2": "Baseball / Softball",
        "IAB17-20": "Martial Arts",
        "IAB17-21": "Mountain Biking",
        "IAB17-22": "NASCAR Racing",
        "IAB17-23": "Olympics",
        "IAB17-24": "Paintball",
        "IAB17-25": "Power & Motorcycles",
        "IAB17-26": "Basketball",
        "IAB17-27": "Ice Hockey",
        "IAB17-28": "Rodeo",
        "IAB17-29": "Rugby",
        "IAB17-3": "Bicycling",
        "IAB17-30": "Running / Jogging",
        "IAB17-31": "Sailing / Boating",
        "IAB17-32": "Saltwater Fishing",
        "IAB17-33": "Scuba Diving",
        "IAB17-34": "Skateboarding",
        "IAB17-35": "Skiing",
        "IAB17-36": "Snowboarding",
        "IAB17-37": "Surfing / Body-Boarding",
        "IAB17-38": "Swimming",
        "IAB17-39": "Table Tennis / Ping-Pong",
        "IAB17-4": "Bodybuilding",
        "IAB17-40": "Tennis",
        "IAB17-41": "Volleyball",
        "IAB17-42": "Walking",
        "IAB17-43": "Waterski / Wakeboard",
        "IAB17-44": "World Football / Soccer",
        "IAB17-5": "Boxing",
        "IAB17-6": "Canoeing / Kayaking",
        "IAB17-7": "Cheerleading",
        "IAB17-8": "Climbing",
        "IAB17-9": "Cricket",
    },
    "IAB18": {
        "IAB18": "Style & Fashion",
        "IAB18-1": "Beauty",
        "IAB18-2": "Body Art",
        "IAB18-3": "Fashion",
        "IAB18-4": "Jewelry",
        "IAB18-5": "Clothing",
        "IAB18-6": "Accessories",
    },
    "IAB19": {
        "IAB19": "Technology & Computing",
        "IAB19-1": "3-D Graphics",
        "IAB19-10": "Computer Reviews",
        "IAB19-11": "Data Centers",
        "IAB19-12": "Databases",
        "IAB19-13": "Desktop Publishing",
        "IAB19-14": "Desktop Video",
        "IAB19-15": "Email / Chat / Messaging",
        "IAB19-16": "Graphics Software",
        "IAB19-17": "Home Video / DVD",
        "IAB19-18": "Internet Technology",
        "IAB19-19": "Java",
        "IAB19-2": "Animation",
        "IAB19-20": "JavaScript",
        "IAB19-21": "Mac Support",
        "IAB19-22": "MP3 / MIDI",
        "IAB19-23": "Net Conferencing",
        "IAB19-24": "Net for Beginners",
        "IAB19-25": "Network Security",
        "IAB19-26": "Palmtops / PDAs / Tablets",
        "IAB19-27": "PC Support",
        "IAB19-28": "Portable",
        "IAB19-29": "Entertainment / Virtual & Augmented Reality",
        "IAB19-3": "Antivirus Software",
        "IAB19-30": "Shareware / Freeware / Open Source",
        "IAB19-31": "Unix / Linux",
        "IAB19-32": "Visual Basic",
        "IAB19-33": "Web Clip Art",
        "IAB19-34": "Web Design / HTML",
        "IAB19-35": "Web Search",
        "IAB19-36": "Windows",
        "IAB19-4": "C / C++",
        "IAB19-5": "Cameras & Camcorders",
        "IAB19-6": "Cell Phones",
        "IAB19-7": "Computer Certification",
        "IAB19-8": "Computer Networking",
        "IAB19-9": "Computer Peripherals",
        "IAB19-WS1": "Hacking / Cracking",
        "IAB19-WS2": "VPNs / Proxies & Filter Avoidance",
        "IAB19-WS3": "Language Translation",
        "IAB19-WS4": "File Sharing",
    },
    "IAB2": {
        "IAB2": "Automotive",
        "IAB2-1": "Auto Parts",
        "IAB2-10": "Electric Vehicle",
        "IAB2-11": "Hatchback",
        "IAB2-12": "Hybrid",
        "IAB2-13": "Luxury",
        "IAB2-14": "Minivan",
        "IAB2-15": "Motorcycles",
        "IAB2-16": "Off-Road Vehicles",
        "IAB2-17": "Performance Vehicles",
        "IAB2-18": "Pickup",
        "IAB2-19": "Road-Side Assistance",
        "IAB2-2": "Auto Repair",
        "IAB2-20": "Sedan",
        "IAB2-21": "Trucks & Accessories",
        "IAB2-22": "Vintage Cars",
        "IAB2-23": "Wagon",
        "IAB2-3": "Buying/Selling Cars",
        "IAB2-4": "Car Culture",
        "IAB2-5": "Certified Pre-Owned",
        "IAB2-6": "Convertible",
        "IAB2-7": "Coupe",
        "IAB2-8": "Crossover",
        "IAB2-9": "Diesel",
    },
    "IAB20": {
        "IAB20": "Travel",
        "IAB20-1": "Adventure Travel",
        "IAB20-10": "Canada",
        "IAB20-11": "Caribbean",
        "IAB20-12": "Cruises",
        "IAB20-13": "Eastern Europe",
        "IAB20-14": "Europe",
        "IAB20-15": "France",
        "IAB20-16": "Greece",
        "IAB20-17": "Honeymoons / Getaways",
        "IAB20-18": "Hotels",
        "IAB20-19": "Italy",
        "IAB20-2": "Africa",
        "IAB20-20": "Japan / China",
        "IAB20-21": "Mexico & Central America",
        "IAB20-22": "National Parks",
        "IAB20-23": "South America",
        "IAB20-24": "Spas",
        "IAB20-25": "Theme Parks",
        "IAB20-26": "Traveling with Kids",
        "IAB20-27": "United Kingdom",
        "IAB20-3": "Air Travel",
        "IAB20-4": "Australia & New Zealand",
        "IAB20-5": "Bed & Breakfast",
        "IAB20-6": "Budget Travel",
        "IAB20-7": "Business Travel",
        "IAB20-8": "By US Locale",
        "IAB20-9": "Camping",
    },
    "IAB21": {
        "IAB21": "Real Estate",
        "IAB21-1": "Apartments",
        "IAB21-2": "Architects",
        "IAB21-3": "Buying / Selling Homes",
    },
    "IAB22": {
        "IAB22": "Shopping",
        "IAB22-1": "Contests & Freebies",
        "IAB22-2": "Couponing",
        "IAB22-3": "Comparison",
        "IAB22-4": "Engines",
    },
    "IAB23": {
        "IAB23": "Religion & Spirituality",
        "IAB23-1": "Alternative Religions",
        "IAB23-10": "Pagan / Wiccan",
        "IAB23-2": "Atheism / Agnosticism",
        "IAB23-3": "Buddhism",
        "IAB23-4": "Catholicism",
        "IAB23-5": "Christianity",
        "IAB23-6": "Hinduism",
        "IAB23-7": "Islam",
        "IAB23-8": "Judaism",
        "IAB23-9": "Latter-Day Saints",
    },
    "IAB24": {"IAB24": "Uncategorized"},
    "IAB25": {
        "IAB25": "Non-Standard Content",
        "IAB25-1": "Unmoderated UGC / Message Boards",
        "IAB25-2": "Extreme Graphic / Explicit Violence",
        "IAB25-3": "Adult Content",
        "IAB25-4": "Profane Content",
        "IAB25-5": "Hate Content",
        "IAB25-6": "Under Construction",
        "IAB25-7": "Incentivized",
        "IAB25-WS1": "Content Server",
        "IAB25-WS2": "Streaming Media",
        "IAB25-WS3": "Trackers",
    },
    "IAB26": {
        "IAB26": "Illegal Content",
        "IAB26-1": "Illegal Content",
        "IAB26-2": "Warez",
        "IAB26-3": "Spyware / Malware / Malicious",
        "IAB26-4": "Copyright Infringement",
        "IAB26-WS1": "Illegal Drugs & Paraphernalia",
        "IAB26-WS2": "Phishing",
    },
    "IAB3": {
        "IAB3": "Business",
        "IAB3-1": "Advertising",
        "IAB3-10": "Logistics",
        "IAB3-11": "Marketing",
        "IAB3-12": "Metals",
        "IAB3-2": "Agriculture",
        "IAB3-3": "Biotech/Biomedical",
        "IAB3-4": "Business Software",
        "IAB3-5": "Construction",
        "IAB3-6": "Forestry",
        "IAB3-7": "Government",
        "IAB3-8": "Green Solutions",
        "IAB3-9": "Human Resources",
    },
    "IAB4": {
        "IAB4": "Careers",
        "IAB4-1": "Career Planning",
        "IAB4-10": "Military",
        "IAB4-11": "Career Advice",
        "IAB4-2": "College",
        "IAB4-3": "Financial Aid",
        "IAB4-4": "Job Fairs",
        "IAB4-5": "Job Search",
        "IAB4-6": "Resume Writing/Advice",
        "IAB4-7": "Nursing",
        "IAB4-8": "Scholarships",
        "IAB4-9": "Telecommuting",
    },
    "IAB5": {
        "IAB5": "Education",
        "IAB5-1": "7-12 Education",
        "IAB5-10": "Homeschooling",
        "IAB5-11": "Homework/Study Tips",
        "IAB5-12": "K-6 Education",
        "IAB5-13": "Private School",
        "IAB5-14": "Special Education",
        "IAB5-15": "Studying Business",
        "IAB5-2": "Adult Education",
        "IAB5-3": "Art History",
        "IAB5-4": "College Administration",
        "IAB5-5": "College Life",
        "IAB5-6": "Distance Learning",
        "IAB5-7": "English as a 2nd Language",
        "IAB5-8": "Language Learning",
        "IAB5-9": "College / Graduate School",
    },
    "IAB6": {
        "IAB6": "Family & Parenting",
        "IAB6-1": "Adoption",
        "IAB6-2": "Babies & Toddlers",
        "IAB6-3": "Daycare/Pre School",
        "IAB6-4": "Family Internet",
        "IAB6-5": "Parenting - K-6 Kids",
        "IAB6-6": "Parenting teens",
        "IAB6-7": "Pregnancy",
        "IAB6-8": "Special Needs Kids",
        "IAB6-9": "Eldercare",
    },
    "IAB7": {
        "IAB7": "Health & Fitness",
        "IAB7-1": "Exercise / Weight Loss",
        "IAB7-10": "Brain Tumor",
        "IAB7-11": "Cancer",
        "IAB7-12": "Cholesterol",
        "IAB7-13": "Chronic Fatigue Syndrome",
        "IAB7-14": "Chronic Pain",
        "IAB7-15": "Cold & Flu",
        "IAB7-16": "Deafness",
        "IAB7-17": "Dental Care",
        "IAB7-18": "Depression",
        "IAB7-19": "Dermatology",
        "IAB7-2": "ADD",
        "IAB7-20": "Diabetes",
        "IAB7-21": "Epilepsy / Seizures",
        "IAB7-22": "GERD / Acid Reflux",
        "IAB7-23": "Headaches / Migraines / Fevers / Pain",
        "IAB7-24": "Heart Disease / Stroke",
        "IAB7-25": "Herbs for Health / Supplements / Vitamins",
        "IAB7-26": "Holistic Healing",
        "IAB7-27": "IBS / Crohn's / Celiac Disease",
        "IAB7-28": "Incest / Abuse Support",
        "IAB7-29": "Incontinence",
        "IAB7-3": "AIDS / HIV",
        "IAB7-30": "Infertility",
        "IAB7-31": "Men's Health",
        "IAB7-32": "Nutrition",
        "IAB7-33": "Orthopedics",
        "IAB7-34": "Panic / Anxiety Disorders",
        "IAB7-35": "Pediatrics",
        "IAB7-36": "Physical Therapy",
        "IAB7-37": "Psychology / Psychiatry / Therapy",
        "IAB7-38": "Senior Health",
        "IAB7-39": "Sexuality",
        "IAB7-4": "Allergies",
        "IAB7-40": "Sleep Disorders",
        "IAB7-41": "Smoking Cessation",
        "IAB7-42": "Substance Abuse",
        "IAB7-43": "Thyroid Disease / Endocrinology",
        "IAB7-44": "Weight Loss",
        "IAB7-45": "Women's Health",
        "IAB7-5": "Alternative Medicine / Holistic Healing",
        "IAB7-6": "Arthritis",
        "IAB7-7": "Asthma",
        "IAB7-8": "Autism / PDD / Asperger's Syndrome",
        "IAB7-9": "Bipolar Disorder",
        "IAB7-WS1": "Abortion",
    },
    "IAB8": {
        "IAB8": "Food & Drink",
        "IAB8-1": "American Cuisine",
        "IAB8-10": "Food Allergies",
        "IAB8-11": "French Cuisine",
        "IAB8-12": "Health / Low-Fat Cooking",
        "IAB8-13": "Italian Cuisine",
        "IAB8-14": "Japanese Cuisine",
        "IAB8-15": "Mexican Cuisine",
        "IAB8-16": "Vegan",
        "IAB8-17": "Vegetarian",
        "IAB8-18": "Wine",
        "IAB8-2": "Barbecues & Grilling",
        "IAB8-3": "Cajun / Creole",
        "IAB8-4": "Chinese Cuisine",
        "IAB8-5": "Cocktails / Beer",
        "IAB8-6": "Coffee / Tea",
        "IAB8-7": "Cuisine-Specific",
        "IAB8-8": "Desserts & Baking",
        "IAB8-9": "Dining Out",
    },
    "IAB9": {
        "IAB9": "Hobbies & Interests",
        "IAB9-1": "Art / Technology",
        "IAB9-10": "Collecting",
        "IAB9-11": "Comic Books / Anime / Manga",
        "IAB9-12": "Drawing / Sketching",
        "IAB9-13": "Freelance Writing / Getting Published",
        "IAB9-14": "Genealogy",
        "IAB9-15": "Getting Published",
        "IAB9-16": "Guitar / Keyboard / Drums",
        "IAB9-17": "Home Recording",
        "IAB9-18": "Investors / Inventors / Patents / Copyright",
        "IAB9-19": "Jewelry Making",
        "IAB9-2": "Arts & Crafts",
        "IAB9-20": "Magic & Illusion",
        "IAB9-21": "Needlework",
        "IAB9-22": "Painting",
        "IAB9-23": "Photography",
        "IAB9-24": "Radio",
        "IAB9-25": "Roleplaying Games",
        "IAB9-26": "Sci-Fi & Fantasy",
        "IAB9-27": "Scrapbooking",
        "IAB9-28": "Screenwriting",
        "IAB9-29": "Stamps & Coins",
        "IAB9-3": "Beadwork",
        "IAB9-30": "Video & Computer Games",
        "IAB9-31": "Woodworking",
        "IAB9-4": "Bird-Watching",
        "IAB9-5": "Board Games / Puzzles",
        "IAB9-6": "Candle & Soap Making",
        "IAB9-7": "Card Games",
        "IAB9-8": "Chess",
        "IAB9-9": "Cigars / Vaping / Tobacco & Accessories",
        "IAB9-WS1": "Gambling",
        "IAB9-WS2": "Weapons",
    },
}

TIER_1_CATEGORIES = [
    "Arts & Entertainment",
    "Home & Garden",
    "Law, Government, & Politics",
    "News / Weather / Information",
    "Personal Finance",
    "Society",
    "Science",
    "Pets",
    "Sports",
    "Style & Fashion",
    "Technology & Computing",
    "Automotive",
    "Travel",
    "Real Estate",
    "Shopping",
    "Religion & Spirituality",
    "Uncategorized",
    "Non-Standard Content",
    "Illegal Content",
    "Business",
    "Careers",
    "Education",
    "Family & Parenting",
    "Health & Fitness",
    "Food & Drink",
    "Hobbies & Interests",
]

WEBSHRINKER_CATEGORIES = {
    "abortion": "Abortion",
    "adult": "Adult",
    "advertising": "Advertising",
    "alcoholandtobacco": "Alcohol and Tobacco",
    "blogsandpersonal": "Blogs and Personal Sites",
    "business": "Business",
    "chatandmessaging": "Chat and Instant Messaging",
    "contentserver": "Content Server",
    "deceptive": "Deceptive",
    "drugs": "Drugs",
    "economyandfinance": "Economy and Finance",
    "education": "Education",
    "entertainment": "Entertainment",
    "foodandrecipes": "Food and Recipes",
    "gambling": "Gambling",
    "games": "Games",
    "government": "Government",
    "hacking": "Hacking",
    "hate": "Terrorism and Hate",
    "health": "Health",
    "humor": "Humor",
    "illegalcontent": "Illegal Content",
    "informationtech": "Information Technology",
    "jobrelated": "Job Related",
    "malicious": "Malicious",
    "mediasharing": "Media Sharing",
    "messageboardsandforums": "Messageboards and Forums",
    "newsandmedia": "News and Media",
    "parked": "Parked",
    "personals": "Dating and Personals",
    "proxyandfilteravoidance": "Proxy and Filter Avoidance",
    "realestate": "Real Estate",
    "religion": "Religion",
    "searchenginesandportals": "Search Engines and Portals",
    "shopping": "Shopping",
    "socialnetworking": "Social Networking",
    "sports": "Sports",
    "streamingmedia": "Streaming Media",
    "trackers": "Trackers",
    "translators": "Translation Sites",
    "travel": "Travel",
    "uncategorized": "Uncategorized",
    "vehicles": "Vehicles",
    "virtualreality": "Virtual Reality",
    "weapons": "Weapons",
}
