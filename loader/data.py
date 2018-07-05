#
# contains list of data used to generate various random data in real world examples
#
DAYS_IN_YEAR = 365
HOURS_IN_YEAR = DAYS_IN_YEAR * 24
MINUTES_IN_YEAR = HOURS_IN_YEAR * 60
MONTHS_IN_YEAR = 12
MAX_DIMENSION = 300
HUNDRED = 100.00
THOUSAND = 1000.00
TEN_THOUSAND = 10000.00
HUNDRED_THOUSAND = 100000.00
ONE_MILLION = 1000000.00

#
# taken from some of my favorite shows, if main character does not have a last name - the name is smith
# only first name and last name (array of arrays)
#
CAST_OF_CHARACTERS = [
    ['Dave', 'Nelson'],          ['Jimmy', 'James'],         ['Matthew', 'Brock'],    ['Lisa', 'Miller'],
    ['Joe', 'Garrelli'],         ['Beth', 'Smith'],          ['Bill', 'McNeal'],      ['Catherine', 'Duke'],
    ['Max', 'Lewis'],            ['Johnny', 'Johnson'],      ['Walt', 'Smith'],       ['Ed', 'Harlow'],
    ['Sandi', 'Angelini'],       ['Melanie', 'Sanders'],     ['Frank', 'Westford'],   ['Bob', 'Costas'],
    ['Don', 'Green'],            ['Jane', 'Robertson'],      ['Scott', 'Barker'],     ['Jerry', 'Seinfeld'],
    ['Ron', 'Jarek'],            ['Tom', 'Baxter'],          ['Marty', 'Jackson'],    ['Eddie', 'Chambers'],
    ['Steve', 'Johnson'],        ['Carl', 'Jackson'],        ['Kevin', 'Sparks'],     ['Adam', 'West'],
    ['John', 'Bush'],            ['James', 'Caan'],          ['Katie', 'Couric'],     ['Matt', 'Lauer'],
    ['Jack', 'Carter'],          ['Allison', 'Blake'],       ['Jo', 'Lupo'],          ['Douglas', 'Fargo'],
    ['Henry', 'Deacon'],         ['Vincent', 'Smith'],       ['Zoe', 'Carter'],       ['Zane', 'Donovan'],
    ['Nathan', 'Stark'],         ['Beverly', 'Barlowe'],     ['Grace', 'Monroe'],     ['Larry', 'Haberman'],
    ['Holly', 'Marten'],         ['Andy', 'Smith'],          ['Jim', 'Taggart'],      ['Kevin', 'Blake'],
    ['Eva', 'Thorne'],           ['Lexi', 'Carter'],         ['John', 'Mansfield'],   ['Michaela', 'Wen'],
    ['Spencer', 'Martin'],       ['Pilar', 'Smith'],         ['William', 'Shaw'],     ['Callie', 'Curie'],
    ['Seth', 'Osbourne'],        ['warren', 'Hughes'],       ['Jenna', 'Blake'],      ['Adam', 'Barlowe'],
    ['Abby', 'Carter'],          ['Noah', 'Drummer'],        ['Julia', 'Golden'],     ['Duncan', 'Smith'],
    ['Nick', 'Fowler'],          ['Walter', 'Perkins'],      ['Anne', 'Young'],       ['Susan', 'Perkins'],
    ['Carol', 'Taylor'],         ['Maria', 'Leonardo'],      ['Jasper', 'Cole'],      ['Brian', 'Perkins'],
    ['Doris', 'Gilmer'],         ['Bruce', 'Manlius'],       ['Irvin', 'Thatcher'],   ['Pierre', 'Fargo'],
    ['Claudia', 'Donovan'],      ['Marcus', 'Blake'],        ['Jason', 'Anderson'],   ['Callister', 'Raynes'],
    ['Jane', 'Harrington'],      ['Andre', 'Sandrov'],       ['Diane', 'Lancaster'],  ['Michael', 'Clark'],
    ['Carl', 'Carlson'],         ['Dylan', 'Hartwell'],      ['Pete', 'Puhlman'],     ['Emily', 'Glenn'],
    ['Christopher', 'Dactylos'], ['Ray', 'Darlton'],         ['Max', 'Dillon'],       ['William', 'Cobb'],
    ['Milton', 'Houk'],          ['Jake', 'Wyatt'],          ['Sam', 'Lovejoy'],      ['Wendy', 'Whiticus'],
    ['Leo', 'Weinbrenner'],      ['Tracy', 'Fox'],           ['Mary-Beth', 'Curtis'], ['Toby', 'Bismark'],
    ['Jacob', 'Stefano'],        ['Lisa', 'Wheeler'],        ['Louis', 'Glazer'],     ['Walter', 'Perkins'],
    ['Belle', 'St John'],        ['Paul', 'Suenos'],         ['Aaron', 'Finn'],       ['Steven', 'Whiticus'],
    ['Teri', 'Wallace'],         ['Sebastian', 'Marx'],      ['Ethan', 'Edison'],     ['Bella', 'Pagani'],
    ['Yuri', 'Gregor'],          ['H.J', 'Johnson'],         ['Norman', 'Gregor'],    ['Judy', 'Stone'],
    ['Derek', 'Bowers'],         ['Lily', 'Morgan'],         ['Ryan', 'Brock'],       ['Bob', 'Stone'],
    ['Eileen', 'Michaels'],      ['Rick', 'Wallace'],        ['Tanya', 'Zimmer'],     ['Kevin', 'Blake'],
    ['Bob', 'Nobb'],             ['Mark', 'Timmons'],        ['Neil', 'Baxter'],      ['Jessica', 'Lansky'],
    ['Pete', 'Lattimer'],        ['Myka', 'Bering'],         ['Artie', 'Nielson'],    ['Claudia', 'Donovan'],
    ['Leena', 'Smith'],          ['Steve', 'Jinks'],         ['Irene', 'Frederic'],   ['H.G', 'Wells'],
    ['Daniel', 'Dickenson'],     ['Adwin', 'Kosan'],         ['Marcus', 'Diamond'],   ['James', 'MacPherson'],
    ['Adrian', 'Smith'],         ['Kelly', 'Hernandez'],     ['Abigail', 'Chow'],     ['Jane', 'Lattimer'],
    ['Vanessa', 'Calder'],       ['Benedict', 'Valda'],      ['Joshua', 'Donovan'],   ['Walter', 'Sykes'],
    ['Chorlotte', 'Dupres'],     ['Sally', 'Stukowski'],     ['Hugo', 'Miller'],      ['Nick', 'Powell'],
    ['Sam', 'Martino'],          ['Claire', 'Donovan'],      ['Tyler', 'Struhl'],     ['Kate', 'Logan'],
    ['Rebecca', 'St Clair'],     ['Douglas', 'Fargo'],       ['Amanda', 'Lattimer'],  ['Jeannie', 'Bering'],
    ['Rebecca', 'St Claire'],    ['Walter', 'Sykes'],        ['Bonnie', 'Belski'],    ['Izzy', 'Weisfelt'],
    ['Lily', 'Abbott'],          ['Liam', 'Napier'],         ['Gary', 'Whitman'],     ['Gilbert', 'Radburn'],
    ['Jesslyn', 'Henjik'],       ['Larry', 'Newley'],        ['Lauren', 'Andrews'],   ['Mike', 'Madden'],
    ['Emma', 'Jinks'],           ['Jesse', 'Ashton'],        ['Autumn', 'Radnor'],    ['Arnold', 'Cassell'],
    ['Nana', 'Hernandez'],       ['Emily', 'Krueger'],       ['Jillian', 'Whitman'],  ['Eric', 'Marsden'],
    ['Jeff', 'Weaver'],          ['Warren', 'Bering'],       ['John', 'Hill'],        ['Kurt', 'Smoller'],
    ['Charlie', 'Martin'],       ['Michael', 'Martin'],      ['Dwayne', 'Maddox'],    ['Cody', 'Bell'],
    ['Ethan', 'Ellis'],          ['Judy', 'Giltoy'],         ['Joe', 'Barton'],       ['Evan', 'Smith'],
    ['Rebecca', 'Carson'],       ['Janice', 'Mallow'],       ['Diane', 'Hewlett'],    ['Scott', 'Mohr'],
    ['Alice', 'Liddell'],        ['Stephanie', 'Goodison'],  ['Reggie', 'Hinton'],    ['Corinne', 'Huggins'],
    ['Jonah', 'Raitt'],          ['Damian', 'Jardin'],       ['Garry', 'Gross'],      ['Lenny', 'Malone'],
    ['Amy', 'Gillian'],          ['Zach', 'Adanto'],         ['Lester', 'Holt'],      ['Brady', 'Miller'],
    ['Deb', 'Staley'],           ['Larry', 'Kemp'],          ['Anthony', 'Bishop'],   ['Thomas', 'Roberts'],
    ['Rick', 'Davis'],           ['Lisa', 'Da Vinci'],       ['Jed', 'Fissel'],       ['William', 'Freitag'],
    ['Beth', 'Raitt'],           ['Aaron', 'Sawyer'],        ['Gibson', 'Rice'],      ['Gil', 'Moorpark'],
    ['Ed', 'Schultz'],           ['Christina', 'Robertson'], ['Val', 'Preston'],      ['Terry', 'Chambers'],
    ['Ed', 'Marzotto'],          ['Bobby', 'Busecki'],       ['Jeff', 'Canning'],     ['Geoffery', 'Cedolia'],
    ['Manuel', 'Flores'],        ['Jerry', 'Hoffler'],       ['Nina', 'Golden'],      ['Hank', 'Siskel'],
    ['Joel', 'Lambeth'],         ['Ritchie', 'Purcell'],     ['Cody', 'Thomas'],      ['Tamara', 'Resnick'],
    ['Lee', 'Donaldson'],        ['Isabella', 'Fuentes'],    ['Buck', 'Mendell'],     ['Joe', 'Sweetwood'],
    ['Charles', 'Well'],         ['Kevin', 'Munroe'],        ['Colin', 'Shreve'],     ['Courtney', 'Moore'],
    ['Sam', 'Garity'],           ['Anja', 'Steinbruck'],     ['Barry', 'Byck'],       ['Rex', 'Simmons'],
    ['Haddon', 'Lockhart'],      ['Ricky', 'Johnson'],       ['Caspian', 'Barnabas'], ['Kyle', 'Barton'],
    ['Charlie', 'Battes'],       ['Regent', 'Gans'],         ['Choi', 'Pak'],         ['Jeff', 'Russell'],
    ['Will', 'Fox'],             ['John', 'Donley'],         ['Philo', 'Farnsworth'], ['Sutton', 'Harris'],
    ['Daniel', 'Varley'],        ['Halley', 'Newell'],       ['Eric', 'Bell'],        ['Lisa', 'Bernardo'],
    ['Johann', 'Steinbruck'],    ['Charlie', 'Bell'],        ['Jonah', 'Roth'],       ['Isaac', 'Weisfelt'],
    ['Liam', 'McShane'],         ['Jeff', 'McMasters'],      ['Daniel', 'Varley'],    ['Philip', 'Petrov'],
    ['Karl', 'Steinbruck'],      ['Tim', 'Watts'],           ['Anthony', 'Seklir'],   ['Laura', 'Roth'],
    ['Gavin', 'Tager'],          ['Greg', 'Permut'],         ['Minnie', 'Harris'],    ['Nora', 'Varley'],
    ['Monica', 'Hopper'],        ['Lenny', 'Bukowski'],      ['Karl', 'Irving'],      ['Donny', 'Shultz'],
    ['Charlie', 'Stanton'],      ['Jason', 'Kinser'],        ['Peg', 'Myer'],         ['Gwen', 'Ashton'],
    ['Karen', 'Miller'],         ['Owen', 'Larsen'],         ['Jordan', 'Tivoli'],    ['Gerry', 'Labelle'],
    ['Rose', 'Meyer'],           ['Hank', 'Conway'],         ['Adam', 'Griff'],       ['Doug', 'Varley'],
    ['Vincent', 'Crowley'],      ['Janet', 'Conway'],        ['Nancy', 'Malloy'],     ['Julia', 'Helmsworth'],
    ['Ralph', 'Brunsky'],        ['Jeff', 'Green'],          ['Justine', 'Pounder'],  ['Gordon', 'Letanik'],
    ['Chet', 'Greenfield'],      ['Lorna', 'Soliday'],       ['Grace', 'Ellen'],      ['Jake', 'Stone'],
    ['Cassandra', 'Cillian'],    ['Ezekiel', 'Jones'],       ['Eve', 'Baird'],        ['Flynn', 'Carsen'],
    ['Shawn', 'Spencer'],        ['Burton', 'Guster'],       ['Carlton', 'Lassiter'], ['Henry', 'Spencer'],
    ['Juliet', 'Ohara'],         ['Karen', 'Vick'],          ['Buzz', 'McNabb'],      ['Abigail', 'Lytar']
]

INTERNET_DOMAINS = [
    'google.com',   'gmail.com',     'yahoo.com',    'msn.com',     'microsoft.com', '10gen.com',
    'mongodb.com',  'aol.com',       'excite.com',   'lycos.com',   'usa.net',       'netscape.net',
    'hotmail.com',  'live.com',      'juno.com',     'netzero.com', 'fastmail.com',  'runbox.com',
    'postmark.com', 'planetall.com', 'poboxes.info', 'uunet.com',   'cern.ch',       'mail.com'
]

CITIES_STATES = [
    {
        's': 'AL',
        'n': 'Alabama',
        'c': ['Birmingham', 'Mobile', 'Montgomery', 'Gulf Shores', 'Huntsville', 'Auburn', 'Gadsden']
    }, {
        's': 'AK',
        'n': 'Alaska',
        'c': ['Anchorage', 'Fairbanks', 'Juneau', 'Kodiak', 'Kenai', 'Homer', 'Nome', 'Sitka', 'Wasilla']
    }, {
        's': 'AZ',
        'n': 'Arizona',
        'c': ['Phoenix', 'Tuscan', 'Scottsdale', 'Mesa', 'Tempe', 'Chandler', 'Flagstaff', 'Glendale']
    }, {
        's': 'AR',
        'n': 'Arkansas',
        'c': ['Little Rock', 'Fayetteville', 'Fort Smith', 'Hot Springs', 'Rogers', 'Springdale']
    }, {
        's': 'CA',
        'n': 'California',
        'c': ['Los Angeles', 'San Francisco', 'San Diego', 'Sacramento', 'San Jose', 'Sacramento']
    }, {
        's': 'CO',
        'n': 'Colorado',
        'c': ['Denver', 'Colorado Springs', 'Boulder', 'Aspen', 'Grand Junction', 'Pueblo', 'Durango']
    }, {
        's': 'CT',
        'n': 'Connecticut',
        'c': ['Hartford', 'New Haven', 'Stamford', 'Bridgeport', 'Greenwich', 'Milford']
    }, {
        's': 'DE',
        'n': 'Detroit',
        'c': ['Dover', 'Wimington', 'Newark', 'Milford', 'Middletown', 'Smyrna', 'Lewes']
    }, {
        's': 'FL',
        'n': 'Florida',
        'c': ['Tallahassee', 'Miami', 'Orlando', 'Tampa', 'Key West', 'Fort Myers', 'Naples', 'Sarasota']
    }, {
        's': 'GA',
        'n': 'Georgia',
        'c': ['Atlanta', 'Savannah', 'Augusta', 'Athens', 'Alpharetta', 'Macon', 'Kennesaw', 'Decatur']
    }, {
        's': 'HI',
        'n': 'Hawaii',
        'c': ['Honolulu', 'Kailua', 'Haleiwa', 'Kaneohe', 'Makaha', 'Waimea', 'Haiku', 'Kahuku', 'Kalapana']
    }, {
        's': 'ID',
        'n': 'Idaho',
        'c': ['Boise', 'Idaho Falls', 'Nampa', 'Twin Falls', 'Moscow', 'Eagle', 'Sandpoint' 'Pocatello']
    }, {
        's': 'IL',
        'n': 'Illinois',
        'c': ['Springfield', 'Chicago', 'Rockford', 'Evanston', 'Joliet', 'Elgin', 'Peoria', 'Naperville']
    }, {
        's': 'IN',
        'n': 'Indiana',
        'c': ['Indianapolis', 'Bloomington', 'South Bend', 'Gary', 'Fort Wayne', 'Carmel', 'Michigan City']
    }, {
        's': 'IA',
        'n': 'Iowa',
        'c': ['Des Moines', 'Iowa City', 'Cedar Rapids', 'Davenport', 'Waterloo', 'Ankeny', 'Siox City']
    }, {
        's': 'KS',
        'n': 'Kansas',
        'c': ['Topeka', 'Witchita', 'Kansas City', 'Shawnee', 'Manhattan', 'Salina', 'Hutchinson', 'Lenexa']
    }, {
        's': 'KY',
        'n': 'Kentucky',
        'c': ['Frankfort', 'Louisville', 'Lexington', 'Murray', 'Bowling Green', 'Owensboro', 'Nicholasville']
    }, {
        's': 'LA',
        'n': 'Louisiana',
        'c': ['Baton Rouge', 'New Orleans', 'Lafayette', 'Alexandria', 'Slidell', 'Kenner', 'Slidell']
    }, {
        's': 'ME',
        'n': 'Maine',
        'c': ['Augusta', 'Portland', 'Bangor', 'Bar Harbor', 'Camden', 'Lewiston', 'Rockland', 'Ogunquit']
    }, {
        's': 'MD',
        'n': 'Maryland',
        'c': ['Annapolis', 'Baltimore', 'Rockville', 'Silver Spring', 'College Park']
    }, {
        's': 'MA',
        'n': 'Massachusetts',
        'c': ['Boston', 'Cambridge', 'Worcester', 'Salem', 'Springfield', 'Waltham', 'Framingham']
    }, {
        's': 'MI',
        'n': 'Michigan',
        'c': ['Lansing', 'Detroit', 'Ann Arbor', 'Grand Rapids', 'Flint', 'Kalamazoo', 'Troy']
    }, {
        's': 'MN',
        'n': 'Minnesota',
        'c': ['St. Paul', 'Minneapolis', 'Duluth', 'St. Cloud', 'Mankato', 'Minnetonka', 'Eagan']
    }, {
        's': 'MS',
        'n': 'Mississippi',
        'c': ['Jackson', 'Biloxi', 'Gulfport', 'Tupelo', 'Oxford', 'Vicksburg', 'Ocean Springs']
    }, {
        's': 'MO',
        'n': 'Missouri',
        'c': ['Jefferson City', 'St. Louis', 'Kansas City', 'Jefferson City', 'Ozark', 'Joplin']
    }, {
        's': 'MT',
        'n': 'Montana',
        'c': ['Helena', 'Missoula', 'Billings', 'Bozeman', 'Great Falls', 'Butte', 'Whitefish']
    }, {
        's': 'NE',
        'n': 'Nebraska',
        'c': ['Lincoln', 'Omaha', 'Grand Island', 'Norfolk', 'Hastings', 'Fremont']
    }, {
        's': 'NV',
        'n': 'Nevada',
        'c': ['Carson City', 'Las Vegas', 'Reno', 'Henderson', 'Sparks', 'Elko', 'Boulder City']
    }, {
        's': 'NH',
        'n': 'New Hampshire',
        'c': ['Concord', 'Manchester', 'Portsmouth', 'Keene', 'Derry', 'Lebanon', 'Hanover']
    }, {
        's': 'NJ',
        'n': 'New Jersey',
        'c': ['Trenton', 'Newark', 'Atlantic City', 'Jersey City', 'Hoboken', 'Cape May', 'Toms River']
    }, {
        's': 'NM',
        'n': 'New Mexico',
        'c': ['Santa Fe', 'Alburquerque', 'Santa Fe', 'Taos', 'Roswell', 'Farmington']
    }, {
        's': 'NY',
        'n': 'New York',
        'c': ['Albany', 'Troy', 'New York City', 'Buffalo', 'Syracuse', 'Rochester', 'Ithaca', 'Yonkers']
    }, {
        's': 'NC',
        'n': 'North Carolina',
        'c': ['Raleigh', 'Charlotte', 'Durham', 'Greensboro', 'Wimington', 'Cary', 'High Point']
    }, {
        's': 'ND',
        'n': 'North Dakota',
        'c': ['Bismark', 'Fargo', 'Grand Forks', 'Minot', 'Mandan', 'Devils Lake', 'Wahpeton']
    }, {
        's': 'OH',
        'n': 'Ohio',
        'c': ['Columbus', 'Cleveland', 'Cincinnati', 'Dayton', 'Akron', 'Toledo', 'Canton', 'Kent']
    }, {
        's': 'OK',
        'n': 'Oklahoma',
        'c': ['Oklahoma City', 'Tulsa', 'Norman', 'Edmond', 'Broken Arrow', 'Stillwater', 'Moore']
    }, {
        's': 'OR',
        'n': 'Oregon',
        'c': ['Salem', 'Portland', 'Eugene', 'Bend', 'Beaverton', 'Medford', 'Oregon City', 'Corvallis']
    }, {
        's': 'PA',
        'n': 'Pennsylvania',
        'c': ['Harrisburg', 'Pittsburgh', 'Philadelphia', 'Lancaster', 'Allentown', 'Erie']
    }, {
        's': 'RI',
        'n': 'Rhode Island',
        'c': ['Providence', 'Newport', 'Warwick', 'Cranston', 'Narragansett', 'Westerly']
    }, {
        's': 'SC',
        'n': 'South Carolina',
        'c': ['Columbia', 'Charleston', 'Myrtle Beach', 'Greenville', 'Rock Hill', 'Clemson']
    }, {
        's': 'SD',
        'n': 'South Dakota',
        'c': ['Pierre', 'Sioux Falls', 'Rapid City', 'Aberdeen', 'Brookings', 'Sturgis', 'Deadwood']
    }, {
        's': 'TN',
        'n': 'Tennessee',
        'c': ['Nashville', 'Memphis', 'Knoxville', 'Gatlinburg', 'Franklin', 'Jackson', 'Cleveland']
    }, {
        's': 'TX',
        'n': 'Texas',
        'c': ['Austin', 'Houston', 'Dallas', 'San Antonio', 'Fort Worth', 'Galveston', 'Waco', 'Arlington']
    }, {
        's': 'UT',
        'n': 'Utah',
        'c': ['Salt Lake City', 'Provo', 'Ogden', 'Park City', 'Moab', 'Orem', 'Logan', 'Sandy', 'Layton']
    }, {
        's': 'VT',
        'n': 'Vermont',
        'c': ['Montpelier', 'Burlington', 'Rutland City', 'Brattleboro', 'Bennington', 'Stowe', 'Barre City']
    }, {
        's': 'VA',
        'n': 'Virginia',
        'c': ['Richmond', 'Charlottesville', 'Norfolk', 'Alexandria', 'Roanke', 'Fairfax', 'Jamestown']
    }, {
        's': 'WA',
        'n': 'Washington',
        'c': ['Olympia', 'Seattle', 'Spokane', 'Tacoma', 'Vancouver', 'Everett', 'Redmon', 'Renton']
    }, {
        's': 'WV',
        'n': 'West Virginia',
        'c': ['Charleston', 'Morgantwon', 'Beckley', 'Fairmont', 'Clarksburg', 'Huntington']
    }, {
        's': 'WI',
        'n': 'Wisconsin',
        'c': ['Madison', 'Milwaukee', 'Green Bay', 'Appleton', 'Kenosha', 'La Crosse', 'Racine']
    }, {
        's': 'WY',
        'n': 'Wyoming',
        'c': ['Cheyenne', 'Jackson', 'Cody', 'Casper', 'Rock Springs', 'Lander', 'Riverton', 'Evanston']
    }
]

LOREM_IPSUM_TAGS = [
    'accumsan', 'adipiscing', 'aenean', 'aliquam', 'aliquet', 'amet', 'ante', 'arcu', 'augue', 'blandit', 'commodo',
    'congue', 'consectetur', 'consequat', 'cras', 'curabitur', 'cursus', 'dapibus', 'dignissim', 'dolor', 'donec',
    'efficitur', 'eget', 'elit', 'elementum', 'enim', 'erat', 'eros', 'euismod', 'facilisi', 'fermentum', 'feugiat',
    'fringilla', 'gravida', 'iaculis', 'integer', 'interdum', 'ipsum', 'justo', 'lacinia', 'laoreet', 'lectus',
    'libero', 'lorem', 'luctus', 'malesuada', 'massa', 'mattis', 'mauris', 'maximus', 'metus', 'molestie', 'mollis',
    'morbi', 'nibh', 'nisi', 'nisl', 'nulla', 'nullam', 'odio', 'orci', 'ornare', 'pellentesque', 'pharetra',
    'placerat', 'porttitor', 'posuere', 'praesent', 'pretium', 'proin', 'pulvinar', 'purus', 'quam', 'quis', 'rhoncus',
    'risus', 'rutrum', 'sagittis', 'sapien', 'sed', 'semper', 'sit', 'sociosqu', 'sollicitudin', 'suscipit',
    'suspendisse', 'tellus', 'tincidunt', 'tortor', 'turpis', 'ullamcorper', 'urna', 'varius', 'vel', 'vehicula',
    'vestibulum', 'vitae', 'viverra', 'volutpat', 'vulputate'
]

# 5 paragraphs to use for various code generation
LOREM_IPSUM = {
    1: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque rutrum mi in suscipit malesuada. Donec '
       'maximus a arcu non sagittis. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris vitae risus id '
       'justo blandit placerat. Morbi rutrum ipsum dapibus orci pulvinar posuere. Donec id tellus lorem. Aenean ipsum '
       'enim, ullamcorper ac porttitor ut, vehicula non turpis. Aliquam erat volutpat. Integer ac augue dignissim odio '
       'dignissim cursus. Nulla facilisi. Proin eget lectus libero.',
    2: 'Praesent eu feugiat eros. Morbi viverra tortor placerat eros gravida, vel luctus arcu interdum. Sed interdum '
       'molestie iaculis. Aenean ac lorem pretium, congue nibh quis, lacinia nisl. Pellentesque libero metus, sagittis '
       'sed interdum a, aliquet sit amet dui. Aenean odio nisi, fermentum sit amet arcu non, fermentum ullamcorper '
       'lorem. Vestibulum ullamcorper justo et mollis dignissim.',
    3: 'Sed dolor quam, ornare sit amet aliquam a, sollicitudin ac massa. Sed eros tellus, accumsan eu enim a, '
       'dignissim semper enim. Integer sollicitudin ante purus, in pharetra lorem vestibulum vel. Praesent dapibus '
       'pretium rhoncus. Integer sit amet laoreet urna. Nulla vulputate ex. Cras vulputate eu sapien vitae accumsan. '
       'Proin elementum massa orci. Aliquam sapien augue, euismod id vulputate vitae, tincidunt et tortor. Praesent '
       'fringilla justo quis aliquet maximus. Cras interdum libero ac eros interdum, nec fermentum ex volutpat.',
    4: 'Donec sem turpis, accumsan sed turpis eget, volutpat interdum augue. Nullam eget dolor tellus. Curabitur metus '
       'massa, efficitur eu consequat vitae, varius arcu. Sed rutrum, massa vel commodo malesuada, augue eros auctor '
       'dolor, at lacinia metus massa tristique risus. Class aptent taciti sociosqu ad litora torquent per conubia '
       'nostra, per inceptos himenaeos. Nullam vitae metus varius, gravida augue ac, laoreet nibh. Nulla pulvinar odio '
       'dolor. Sed vestibulum mattis magna non venenatis.',
    5: 'Suspendisse in fermentum arcu. Aenean mattis euismod lorem, in pretium metus aliquet ac. Curabitur in felis '
       'facilisis, accumsan erat eu, mattis ex. Aenean ultrices nisi arcu, eget scelerisque libero consectetur nec. '
       'Nunc et porta nisi. Vestibulum in turpis imperdiet, fermentum mi in, rutrum nisi. Fusce accumsan nulla quis '
       'maximus dapibus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. '
       'Nam dolor purus, sagittis at diam a, volutpat malesuada enim. Duis a tristique est. Donec elementum, elit in '
       'condimentum dapibus, urna justo feugiat tellus, a sollicitudin lorem enim vitae velit. Duis sollicitudin ante '
       'nec massa auctor, sed semper nibh ornare. Mauris quis facilisis lectus, eget vulputate metus. Sed lobortis '
       'tristique turpis, eget volutpat libero tristique vulputate.'
}

# smaller 1 liners for comments and stuff
LOREM_IPSUM_COMMENTS = {
    1: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque rutrum mi in suscipit malesuada. Donec',
    2: 'maximus a arcu non sagittis. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris vitae risus id',
    3: 'justo blandit placerat. Morbi rutrum ipsum dapibus orci pulvinar posuere. Donec id tellus lorem. Aenean ipsum',
    4: 'enim, ullamcorper ac porttitor ut, vehicula non turpis. Aliquam erat volutpat. Integer ac augue dignissim odio',
    5: 'Praesent eu feugiat eros. Morbi viverra tortor placerat eros gravida, vel luctus arcu interdum. Sed interdum',
    6: 'molestie iaculis. Aenean ac lorem pretium, congue nibh quis, lacinia nisl. Pellentesque libero metus, sagittis',
    7: 'sed interdum, aliquet sit amet dui. Aenean odio nisi, fermentum sit amet arcu non, fermentum ullamcorper',
    8: 'Sed dolor quam, ornare sit amet aliquam a, sollicitudin ac massa. Sed eros tellus, accumsan eu enim a',
    9: 'dignissim semper enim. Integer sollicitudin ante purus, in pharetra lorem vestibulum vel. Praesent dapibus',
    10: 'pretium rhoncus. Integer sit amet laoreet urna. Nulla vulputate ex. Cras vulputate eu sapien vitae accumsan',
    11: 'Proin elementum massa orci. Aliquam sapien augue, euismod id vulputate vitae, tincidunt et tortor. Praesent',
    12: 'fringilla justo quis aliquet maximus. Cras interdum libero ac eros interdum, nec fermentum ex volutpat',
    13: 'Donec sem turpis, accumsan turpis eget, volutpat interdum augue. Nullam eget dolor tellus. Curabitur metus',
    14: 'massa, efficitur eu consequat vitae, varius at arcu. Sed rutrum, massa commodo malesuada, augue eros auctor',
    15: 'dolor, at lacinia metus massa tristique risus. Class aptent taciti sociosqu ad litora torquent per conubia',
    16: 'nostra, per inceptos himenaeos. Nullam vitae metus varius, gravida augue, laoreet nibh. Nulla pulvinar odio',
    17: 'Suspendisse in fermentum arcu. Aenean mattis euismod lorem, in pretium metus aliquet ac. Curabitur in felis',
    18: 'facilisis, accumsan erat eu, mattis ex. Aenean ultrices nisi arcu, eget scelerisque libero consectetur nec.',
    19: 'Nunc et porta nisi. Vestibulum in turpis imperdiet, fermentum mi in, rutrum nisi. Fusce accumsan nulla quis',
    20: 'maximus dapibus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos'
}
