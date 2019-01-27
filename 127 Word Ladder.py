"""
Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to
end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
"""
__author__ = 'Danyang'


class Solution:
    def is_neighbor(self, p, q):
        diff = 0
        for a, b in zip(p, q):
            if a != b:
                diff += 1
            if diff > 1:
                return False
        return True

    def ladderLength(self, start, end, dct):
        """
        bfs
        """
        q = [start]
        visited = {start}
        lvl = 1
        while q:
            cur_q = []
            for a in q:
                if a == end:
                    return lvl
                for b in dct:
                    if b not in visited and self.is_neighbor(a, b):
                        visited.add(b)
                        cur_q.append(b)

            lvl += 1
            q = cur_q

        return 0

    def ladderLength_TLE(self, start, end, dict):
        """
        bfs
        :param start: a string
        :param end: a string
        :param dict: a set
        :return: integer
        """
        lst = [start]+list(dict)
        dp = [[-1 for _ in lst] for _ in lst]

        def diff_count(s1, s2):
            """
            s1 s2 are same length
            :param s1:
            :param s2:
            :return:
            """
            count = 0
            str1 = lst[s1]
            str2 = lst[s2]
            for i in xrange(len(str1)):
                if count>1:
                    return -1
                if str1[i]!=str2[i]:
                    count += 1
            return count

        for i in xrange(len(lst)):
            for j in xrange(i, len(lst)):
                dp[i][j] = diff_count(i, j)
                dp[j][i] = dp[i][j]

        visited = [False for _ in lst]  # avoid loop
        path_len = 0

        queue = [0]
        visited[0] = True
        while queue:
            path_len += 1
            length = len(queue)
            for i in xrange(length):  #O(V)
                if lst[queue[i]]==end:  # reached
                    return path_len
                for ind in xrange(1, len(lst)):  # O(k), add next level
                    if not visited[ind] and dp[ind][queue[i]]==1:
                        queue.append(ind)
                        visited[ind] = True
            queue = queue[length:]
        return path_len

    def ladderLength_TLE2(self, start, end, dict):
        """
        bfs
        :param start: a string
        :param end: a string
        :param dict: a set
        :return: integer
        """
        def diff_count(str1, str2):
            """
            s1 s2 are same length
            :param s1:
            :param s2:
            :return: 0 1 or -1
            """
            count = 0
            for i in xrange(len(str1)):
                if count>1:
                    return -1
                if str1[i]!=str2[i]:
                    count += 1
            return count

        path_len = 0

        queue = [start]
        while queue:
            path_len += 1
            length = len(queue)
            for i in xrange(length):  #O(V)
                if queue[i]==end:  # reached
                    return path_len

                remain_set = set(dict)
                for item in dict:  # O(k), add next level
                   if diff_count(item, queue[i])==1:
                        queue.append(item)
                        remain_set.remove(item)
                dict = remain_set

            queue = queue[length:]
        return path_len


    def ladderLength_complex(self, start, end, dict):
        """
        bfs

        Modify the current str by one char, and test whether it is in the set, rather than iterate through the dict and
        calculate the number of different chars. In other words, iterate through 'abcdefghijklmnopqrstuvwxyz' rather
        than dict


        :param start: a string
        :param end: a string
        :param dict: a set
        :return: integer, if impossible, return 0
        """
        path_len = 0
        lower_cases = [chr(i+ord('a')) for i in xrange(26)]

        queue = [start]
        dict.remove(start)
        while True:
            path_len += 1
            length_0 = len(queue)
            for i in xrange(length_0):  #O(V)
                current = queue[i]
                if current==end:  # reached
                    return path_len

                current = queue[i]
                for pos in xrange(len(current)):
                    lst = list(current)
                    for char in lower_cases:
                        lst[pos] = char
                        temp = "".join(lst)
                        if temp in dict:
                            queue.append(temp)
                            dict.remove(temp)

            queue = queue[length_0:]
            if not queue:
                return 0
        return path_len



if __name__=="__main__":
    assert Solution().ladderLength("sand", "acne", set(
        ["slit", "bunk", "wars", "ping", "viva", "wynn", "wows", "irks", "gang", "pool", "mock", "fort", "heel", "send",
         "ship", "cols", "alec", "foal", "nabs", "gaze", "giza", "mays", "dogs", "karo", "cums", "jedi", "webb", "lend",
         "mire", "jose", "catt", "grow", "toss", "magi", "leis", "bead", "kara", "hoof", "than", "ires", "baas", "vein",
         "kari", "riga", "oars", "gags", "thug", "yawn", "wive", "view", "germ", "flab", "july", "tuck", "rory", "bean",
         "feed", "rhee", "jeez", "gobs", "lath", "desk", "yoko", "cute", "zeus", "thus", "dims", "link", "dirt", "mara",
         "disc", "limy", "lewd", "maud", "duly", "elsa", "hart", "rays", "rues", "camp", "lack", "okra", "tome", "math",
         "plug", "monk", "orly", "friz", "hogs", "yoda", "poop", "tick", "plod", "cloy", "pees", "imps", "lead", "pope",
         "mall", "frey", "been", "plea", "poll", "male", "teak", "soho", "glob", "bell", "mary", "hail", "scan", "yips",
         "like", "mull", "kory", "odor", "byte", "kaye", "word", "honk", "asks", "slid", "hopi", "toke", "gore", "flew",
         "tins", "mown", "oise", "hall", "vega", "sing", "fool", "boat", "bobs", "lain", "soft", "hard", "rots", "sees",
         "apex", "chan", "told", "woos", "unit", "scow", "gilt", "beef", "jars", "tyre", "imus", "neon", "soap", "dabs",
         "rein", "ovid", "hose", "husk", "loll", "asia", "cope", "tail", "hazy", "clad", "lash", "sags", "moll", "eddy",
         "fuel", "lift", "flog", "land", "sigh", "saks", "sail", "hook", "visa", "tier", "maws", "roeg", "gila", "eyes",
         "noah", "hypo", "tore", "eggs", "rove", "chap", "room", "wait", "lurk", "race", "host", "dada", "lola", "gabs",
         "sobs", "joel", "keck", "axed", "mead", "gust", "laid", "ends", "oort", "nose", "peer", "kept", "abet", "iran",
         "mick", "dead", "hags", "tens", "gown", "sick", "odis", "miro", "bill", "fawn", "sumo", "kilt", "huge", "ores",
         "oran", "flag", "tost", "seth", "sift", "poet", "reds", "pips", "cape", "togo", "wale", "limn", "toll", "ploy",
         "inns", "snag", "hoes", "jerk", "flux", "fido", "zane", "arab", "gamy", "raze", "lank", "hurt", "rail", "hind",
         "hoot", "dogy", "away", "pest", "hoed", "pose", "lose", "pole", "alva", "dino", "kind", "clan", "dips", "soup",
         "veto", "edna", "damp", "gush", "amen", "wits", "pubs", "fuzz", "cash", "pine", "trod", "gunk", "nude", "lost",
         "rite", "cory", "walt", "mica", "cart", "avow", "wind", "book", "leon", "life", "bang", "draw", "leek", "skis",
         "dram", "ripe", "mine", "urea", "tiff", "over", "gale", "weir", "defy", "norm", "tull", "whiz", "gill", "ward",
         "crag", "when", "mill", "firs", "sans", "flue", "reid", "ekes", "jain", "mutt", "hems", "laps", "piss", "pall",
         "rowe", "prey", "cull", "knew", "size", "wets", "hurl", "wont", "suva", "girt", "prys", "prow", "warn", "naps",
         "gong", "thru", "livy", "boar", "sade", "amok", "vice", "slat", "emir", "jade", "karl", "loyd", "cerf", "bess",
         "loss", "rums", "lats", "bode", "subs", "muss", "maim", "kits", "thin", "york", "punt", "gays", "alpo", "aids",
         "drag", "eras", "mats", "pyre", "clot", "step", "oath", "lout", "wary", "carp", "hums", "tang", "pout", "whip",
         "fled", "omar", "such", "kano", "jake", "stan", "loop", "fuss", "mini", "byrd", "exit", "fizz", "lire", "emil",
         "prop", "noes", "awed", "gift", "soli", "sale", "gage", "orin", "slur", "limp", "saar", "arks", "mast", "gnat",
         "port", "into", "geed", "pave", "awls", "cent", "cunt", "full", "dint", "hank", "mate", "coin", "tars", "scud",
         "veer", "coax", "bops", "uris", "loom", "shod", "crib", "lids", "drys", "fish", "edit", "dick", "erna", "else",
         "hahs", "alga", "moho", "wire", "fora", "tums", "ruth", "bets", "duns", "mold", "mush", "swop", "ruby", "bolt",
         "nave", "kite", "ahem", "brad", "tern", "nips", "whew", "bait", "ooze", "gino", "yuck", "drum", "shoe", "lobe",
         "dusk", "cult", "paws", "anew", "dado", "nook", "half", "lams", "rich", "cato", "java", "kemp", "vain", "fees",
         "sham", "auks", "gish", "fire", "elam", "salt", "sour", "loth", "whit", "yogi", "shes", "scam", "yous", "lucy",
         "inez", "geld", "whig", "thee", "kelp", "loaf", "harm", "tomb", "ever", "airs", "page", "laud", "stun", "paid",
         "goop", "cobs", "judy", "grab", "doha", "crew", "item", "fogs", "tong", "blip", "vest", "bran", "wend", "bawl",
         "feel", "jets", "mixt", "tell", "dire", "devi", "milo", "deng", "yews", "weak", "mark", "doug", "fare", "rigs",
         "poke", "hies", "sian", "suez", "quip", "kens", "lass", "zips", "elva", "brat", "cosy", "teri", "hull", "spun",
         "russ", "pupa", "weed", "pulp", "main", "grim", "hone", "cord", "barf", "olav", "gaps", "rote", "wilt", "lars",
         "roll", "balm", "jana", "give", "eire", "faun", "suck", "kegs", "nita", "weer", "tush", "spry", "loge", "nays",
         "heir", "dope", "roar", "peep", "nags", "ates", "bane", "seas", "sign", "fred", "they", "lien", "kiev", "fops",
         "said", "lawn", "lind", "miff", "mass", "trig", "sins", "furl", "ruin", "sent", "cray", "maya", "clog", "puns",
         "silk", "axis", "grog", "jots", "dyer", "mope", "rand", "vend", "keen", "chou", "dose", "rain", "eats", "sped",
         "maui", "evan", "time", "todd", "skit", "lief", "sops", "outs", "moot", "faze", "biro", "gook", "fill", "oval",
         "skew", "veil", "born", "slob", "hyde", "twin", "eloy", "beat", "ergs", "sure", "kobe", "eggo", "hens", "jive",
         "flax", "mons", "dunk", "yest", "begs", "dial", "lodz", "burp", "pile", "much", "dock", "rene", "sago", "racy",
         "have", "yalu", "glow", "move", "peps", "hods", "kins", "salk", "hand", "cons", "dare", "myra", "sega", "type",
         "mari", "pelt", "hula", "gulf", "jugs", "flay", "fest", "spat", "toms", "zeno", "taps", "deny", "swag", "afro",
         "baud", "jabs", "smut", "egos", "lara", "toes", "song", "fray", "luis", "brut", "olen", "mere", "ruff", "slum",
         "glad", "buds", "silt", "rued", "gelt", "hive", "teem", "ides", "sink", "ands", "wisp", "omen", "lyre", "yuks",
         "curb", "loam", "darn", "liar", "pugs", "pane", "carl", "sang", "scar", "zeds", "claw", "berg", "hits", "mile",
         "lite", "khan", "erik", "slug", "loon", "dena", "ruse", "talk", "tusk", "gaol", "tads", "beds", "sock", "howe",
         "gave", "snob", "ahab", "part", "meir", "jell", "stir", "tels", "spit", "hash", "omit", "jinx", "lyra", "puck",
         "laue", "beep", "eros", "owed", "cede", "brew", "slue", "mitt", "jest", "lynx", "wads", "gena", "dank", "volt",
         "gray", "pony", "veld", "bask", "fens", "argo", "work", "taxi", "afar", "boon", "lube", "pass", "lazy", "mist",
         "blot", "mach", "poky", "rams", "sits", "rend", "dome", "pray", "duck", "hers", "lure", "keep", "gory", "chat",
         "runt", "jams", "lays", "posy", "bats", "hoff", "rock", "keri", "raul", "yves", "lama", "ramp", "vote", "jody",
         "pock", "gist", "sass", "iago", "coos", "rank", "lowe", "vows", "koch", "taco", "jinn", "juno", "rape", "band",
         "aces", "goal", "huck", "lila", "tuft", "swan", "blab", "leda", "gems", "hide", "tack", "porn", "scum", "frat",
         "plum", "duds", "shad", "arms", "pare", "chin", "gain", "knee", "foot", "line", "dove", "vera", "jays", "fund",
         "reno", "skid", "boys", "corn", "gwyn", "sash", "weld", "ruiz", "dior", "jess", "leaf", "pars", "cote", "zing",
         "scat", "nice", "dart", "only", "owls", "hike", "trey", "whys", "ding", "klan", "ross", "barb", "ants", "lean",
         "dopy", "hock", "tour", "grip", "aldo", "whim", "prom", "rear", "dins", "duff", "dell", "loch", "lava", "sung",
         "yank", "thar", "curl", "venn", "blow", "pomp", "heat", "trap", "dali", "nets", "seen", "gash", "twig", "dads",
         "emmy", "rhea", "navy", "haws", "mite", "bows", "alas", "ives", "play", "soon", "doll", "chum", "ajar", "foam",
         "call", "puke", "kris", "wily", "came", "ales", "reef", "raid", "diet", "prod", "prut", "loot", "soar", "coed",
         "celt", "seam", "dray", "lump", "jags", "nods", "sole", "kink", "peso", "howl", "cost", "tsar", "uric", "sore",
         "woes", "sewn", "sake", "cask", "caps", "burl", "tame", "bulk", "neva", "from", "meet", "webs", "spar", "fuck",
         "buoy", "wept", "west", "dual", "pica", "sold", "seed", "gads", "riff", "neck", "deed", "rudy", "drop", "vale",
         "flit", "romp", "peak", "jape", "jews", "fain", "dens", "hugo", "elba", "mink", "town", "clam", "feud", "fern",
         "dung", "newt", "mime", "deem", "inti", "gigs", "sosa", "lope", "lard", "cara", "smug", "lego", "flex", "doth",
         "paar", "moon", "wren", "tale", "kant", "eels", "muck", "toga", "zens", "lops", "duet", "coil", "gall", "teal",
         "glib", "muir", "ails", "boer", "them", "rake", "conn", "neat", "frog", "trip", "coma", "must", "mono", "lira",
         "craw", "sled", "wear", "toby", "reel", "hips", "nate", "pump", "mont", "died", "moss", "lair", "jibe", "oils",
         "pied", "hobs", "cads", "haze", "muse", "cogs", "figs", "cues", "roes", "whet", "boru", "cozy", "amos", "tans",
         "news", "hake", "cots", "boas", "tutu", "wavy", "pipe", "typo", "albs", "boom", "dyke", "wail", "woke", "ware",
         "rita", "fail", "slab", "owes", "jane", "rack", "hell", "lags", "mend", "mask", "hume", "wane", "acne", "team",
         "holy", "runs", "exes", "dole", "trim", "zola", "trek", "puma", "wacs", "veep", "yaps", "sums", "lush", "tubs",
         "most", "witt", "bong", "rule", "hear", "awry", "sots", "nils", "bash", "gasp", "inch", "pens", "fies", "juts",
         "pate", "vine", "zulu", "this", "bare", "veal", "josh", "reek", "ours", "cowl", "club", "farm", "teat", "coat",
         "dish", "fore", "weft", "exam", "vlad", "floe", "beak", "lane", "ella", "warp", "goth", "ming", "pits", "rent",
         "tito", "wish", "amps", "says", "hawk", "ways", "punk", "nark", "cagy", "east", "paul", "bose", "solo", "teed",
         "text", "hews", "snip", "lips", "emit", "orgy", "icon", "tuna", "soul", "kurd", "clod", "calk", "aunt", "bake",
         "copy", "acid", "duse", "kiln", "spec", "fans", "bani", "irma", "pads", "batu", "logo", "pack", "oder", "atop",
         "funk", "gide", "bede", "bibs", "taut", "guns", "dana", "puff", "lyme", "flat", "lake", "june", "sets", "gull",
         "hops", "earn", "clip", "fell", "kama", "seal", "diaz", "cite", "chew", "cuba", "bury", "yard", "bank", "byes",
         "apia", "cree", "nosh", "judo", "walk", "tape", "taro", "boot", "cods", "lade", "cong", "deft", "slim", "jeri",
         "rile", "park", "aeon", "fact", "slow", "goff", "cane", "earp", "tart", "does", "acts", "hope", "cant", "buts",
         "shin", "dude", "ergo", "mode", "gene", "lept", "chen", "beta", "eden", "pang", "saab", "fang", "whir", "cove",
         "perk", "fads", "rugs", "herb", "putt", "nous", "vane", "corm", "stay", "bids", "vela", "roof", "isms", "sics",
         "gone", "swum", "wiry", "cram", "rink", "pert", "heap", "sikh", "dais", "cell", "peel", "nuke", "buss", "rasp",
         "none", "slut", "bent", "dams", "serb", "dork", "bays", "kale", "cora", "wake", "welt", "rind", "trot", "sloe",
         "pity", "rout", "eves", "fats", "furs", "pogo", "beth", "hued", "edam", "iamb", "glee", "lute", "keel", "airy",
         "easy", "tire", "rube", "bogy", "sine", "chop", "rood", "elbe", "mike", "garb", "jill", "gaul", "chit", "dons",
         "bars", "ride", "beck", "toad", "make", "head", "suds", "pike", "snot", "swat", "peed", "same", "gaza", "lent",
         "gait", "gael", "elks", "hang", "nerf", "rosy", "shut", "glop", "pain", "dion", "deaf", "hero", "doer", "wost",
         "wage", "wash", "pats", "narc", "ions", "dice", "quay", "vied", "eons", "case", "pour", "urns", "reva", "rags",
         "aden", "bone", "rang", "aura", "iraq", "toot", "rome", "hals", "megs", "pond", "john", "yeps", "pawl", "warm",
         "bird", "tint", "jowl", "gibe", "come", "hold", "pail", "wipe", "bike", "rips", "eery", "kent", "hims", "inks",
         "fink", "mott", "ices", "macy", "serf", "keys", "tarp", "cops", "sods", "feet", "tear", "benz", "buys", "colo",
         "boil", "sews", "enos", "watt", "pull", "brag", "cork", "save", "mint", "feat", "jamb", "rubs", "roxy", "toys",
         "nosy", "yowl", "tamp", "lobs", "foul", "doom", "sown", "pigs", "hemp", "fame", "boor", "cube", "tops", "loco",
         "lads", "eyre", "alta", "aged", "flop", "pram", "lesa", "sawn", "plow", "aral", "load", "lied", "pled", "boob",
         "bert", "rows", "zits", "rick", "hint", "dido", "fist", "marc", "wuss", "node", "smog", "nora", "shim", "glut",
         "bale", "perl", "what", "tort", "meek", "brie", "bind", "cake", "psst", "dour", "jove", "tree", "chip", "stud",
         "thou", "mobs", "sows", "opts", "diva", "perm", "wise", "cuds", "sols", "alan", "mild", "pure", "gail", "wins",
         "offs", "nile", "yelp", "minn", "tors", "tran", "homy", "sadr", "erse", "nero", "scab", "finn", "mich", "turd",
         "then", "poem", "noun", "oxus", "brow", "door", "saws", "eben", "wart", "wand", "rosa", "left", "lina", "cabs",
         "rapt", "olin", "suet", "kalb", "mans", "dawn", "riel", "temp", "chug", "peal", "drew", "null", "hath", "many",
         "took", "fond", "gate", "sate", "leak", "zany", "vans", "mart", "hess", "home", "long", "dirk", "bile", "lace",
         "moog", "axes", "zone", "fork", "duct", "rico", "rife", "deep", "tiny", "hugh", "bilk", "waft", "swig", "pans",
         "with", "kern", "busy", "film", "lulu", "king", "lord", "veda", "tray", "legs", "soot", "ells", "wasp", "hunt",
         "earl", "ouch", "diem", "yell", "pegs", "blvd", "polk", "soda", "zorn", "liza", "slop", "week", "kill", "rusk",
         "eric", "sump", "haul", "rims", "crop", "blob", "face", "bins", "read", "care", "pele", "ritz", "beau", "golf",
         "drip", "dike", "stab", "jibs", "hove", "junk", "hoax", "tats", "fief", "quad", "peat", "ream", "hats", "root",
         "flak", "grit", "clap", "pugh", "bosh", "lock", "mute", "crow", "iced", "lisa", "bela", "fems", "oxes", "vies",
         "gybe", "huff", "bull", "cuss", "sunk", "pups", "fobs", "turf", "sect", "atom", "debt", "sane", "writ", "anon",
         "mayo", "aria", "seer", "thor", "brim", "gawk", "jack", "jazz", "menu", "yolk", "surf", "libs", "lets", "bans",
         "toil", "open", "aced", "poor", "mess", "wham", "fran", "gina", "dote", "love", "mood", "pale", "reps", "ines",
         "shot", "alar", "twit", "site", "dill", "yoga", "sear", "vamp", "abel", "lieu", "cuff", "orbs", "rose", "tank",
         "gape", "guam", "adar", "vole", "your", "dean", "dear", "hebe", "crab", "hump", "mole", "vase", "rode", "dash",
         "sera", "balk", "lela", "inca", "gaea", "bush", "loud", "pies", "aide", "blew", "mien", "side", "kerr", "ring",
         "tess", "prep", "rant", "lugs", "hobo", "joke", "odds", "yule", "aida", "true", "pone", "lode", "nona", "weep",
         "coda", "elmo", "skim", "wink", "bras", "pier", "bung", "pets", "tabs", "ryan", "jock", "body", "sofa", "joey",
         "zion", "mace", "kick", "vile", "leno", "bali", "fart", "that", "redo", "ills", "jogs", "pent", "drub", "slaw",
         "tide", "lena", "seep", "gyps", "wave", "amid", "fear", "ties", "flan", "wimp", "kali", "shun", "crap", "sage",
         "rune", "logs", "cain", "digs", "abut", "obit", "paps", "rids", "fair", "hack", "huns", "road", "caws", "curt",
         "jute", "fisk", "fowl", "duty", "holt", "miss", "rude", "vito", "baal", "ural", "mann", "mind", "belt", "clem",
         "last", "musk", "roam", "abed", "days", "bore", "fuze", "fall", "pict", "dump", "dies", "fiat", "vent", "pork",
         "eyed", "docs", "rive", "spas", "rope", "ariz", "tout", "game", "jump", "blur", "anti", "lisp", "turn", "sand",
         "food", "moos", "hoop", "saul", "arch", "fury", "rise", "diss", "hubs", "burs", "grid", "ilks", "suns", "flea",
         "soil", "lung", "want", "nola", "fins", "thud", "kidd", "juan", "heps", "nape", "rash", "burt", "bump", "tots",
         "brit", "mums", "bole", "shah", "tees", "skip", "limb", "umps", "ache", "arcs", "raft", "halo", "luce", "bahs",
         "leta", "conk", "duos", "siva", "went", "peek", "sulk", "reap", "free", "dubs", "lang", "toto", "hasp", "ball",
         "rats", "nair", "myst", "wang", "snug", "nash", "laos", "ante", "opal", "tina", "pore", "bite", "haas", "myth",
         "yugo", "foci", "dent", "bade", "pear", "mods", "auto", "shop", "etch", "lyly", "curs", "aron", "slew", "tyro",
         "sack", "wade", "clio", "gyro", "butt", "icky", "char", "itch", "halt", "gals", "yang", "tend", "pact", "bees",
         "suit", "puny", "hows", "nina", "brno", "oops", "lick", "sons", "kilo", "bust", "nome", "mona", "dull", "join",
         "hour", "papa", "stag", "bern", "wove", "lull", "slip", "laze", "roil", "alto", "bath", "buck", "alma", "anus",
         "evil", "dumb", "oreo", "rare", "near", "cure", "isis", "hill", "kyle", "pace", "comb", "nits", "flip", "clop",
         "mort", "thea", "wall", "kiel", "judd", "coop", "dave", "very", "amie", "blah", "flub", "talc", "bold", "fogy",
         "idea", "prof", "horn", "shoo", "aped", "pins", "helm", "wees", "beer", "womb", "clue", "alba", "aloe", "fine",
         "bard", "limo", "shaw", "pint", "swim", "dust", "indy", "hale", "cats", "troy", "wens", "luke", "vern", "deli",
         "both", "brig", "daub", "sara", "sued", "bier", "noel", "olga", "dupe", "look", "pisa", "knox", "murk", "dame",
         "matt", "gold", "jame", "toge", "luck", "peck", "tass", "calf", "pill", "wore", "wadi", "thur", "parr", "maul",
         "tzar", "ones", "lees", "dark", "fake", "bast", "zoom", "here", "moro", "wine", "bums", "cows", "jean", "palm",
         "fume", "plop", "help", "tuba", "leap", "cans", "back", "avid", "lice", "lust", "polo", "dory", "stew", "kate",
         "rama", "coke", "bled", "mugs", "ajax", "arts", "drug", "pena", "cody", "hole", "sean", "deck", "guts", "kong",
         "bate", "pitt", "como", "lyle", "siam", "rook", "baby", "jigs", "bret", "bark", "lori", "reba", "sups", "made",
         "buzz", "gnaw", "alps", "clay", "post", "viol", "dina", "card", "lana", "doff", "yups", "tons", "live", "kids",
         "pair", "yawl", "name", "oven", "sirs", "gyms", "prig", "down", "leos", "noon", "nibs", "cook", "safe", "cobb",
         "raja", "awes", "sari", "nerd", "fold", "lots", "pete", "deal", "bias", "zeal", "girl", "rage", "cool", "gout",
         "whey", "soak", "thaw", "bear", "wing", "nagy", "well", "oink", "sven", "kurt", "etna", "held", "wood", "high",
         "feta", "twee", "ford", "cave", "knot", "tory", "ibis", "yaks", "vets", "foxy", "sank", "cone", "pius", "tall",
         "seem", "wool", "flap", "gird", "lore", "coot", "mewl", "sere", "real", "puts", "sell", "nuts", "foil", "lilt",
         "saga", "heft", "dyed", "goat", "spew", "daze", "frye", "adds", "glen", "tojo", "pixy", "gobi", "stop", "tile",
         "hiss", "shed", "hahn", "baku", "ahas", "sill", "swap", "also", "carr", "manx", "lime", "debs", "moat", "eked",
         "bola", "pods", "coon", "lacy", "tube", "minx", "buff", "pres", "clew", "gaff", "flee", "burn", "whom", "cola",
         "fret", "purl", "wick", "wigs", "donn", "guys", "toni", "oxen", "wite", "vial", "spam", "huts", "vats", "lima",
         "core", "eula", "thad", "peon", "erie", "oats", "boyd", "cued", "olaf", "tams", "secs", "urey", "wile", "penn",
         "bred", "rill", "vary", "sues", "mail", "feds", "aves", "code", "beam", "reed", "neil", "hark", "pols", "gris",
         "gods", "mesa", "test", "coup", "heed", "dora", "hied", "tune", "doze", "pews", "oaks", "bloc", "tips", "maid",
         "goof", "four", "woof", "silo", "bray", "zest", "kiss", "yong", "file", "hilt", "iris", "tuns", "lily", "ears",
         "pant", "jury", "taft", "data", "gild", "pick", "kook", "colt", "bohr", "anal", "asps", "babe", "bach", "mash",
         "biko", "bowl", "huey", "jilt", "goes", "guff", "bend", "nike", "tami", "gosh", "tike", "gees", "urge", "path",
         "bony", "jude", "lynn", "lois", "teas", "dunn", "elul", "bonn", "moms", "bugs", "slay", "yeah", "loan", "hulk",
         "lows", "damn", "nell", "jung", "avis", "mane", "waco", "loin", "knob", "tyke", "anna", "hire", "luau", "tidy",
         "nuns", "pots", "quid", "exec", "hans", "hera", "hush", "shag", "scot", "moan", "wald", "ursa", "lorn", "hunk",
         "loft", "yore", "alum", "mows", "slog", "emma", "spud", "rice", "worn", "erma", "need", "bags", "lark", "kirk",
         "pooh", "dyes", "area", "dime", "luvs", "foch", "refs", "cast", "alit", "tugs", "even", "role", "toed", "caph",
         "nigh", "sony", "bide", "robs", "folk", "daft", "past", "blue", "flaw", "sana", "fits", "barr", "riot", "dots",
         "lamp", "cock", "fibs", "harp", "tent", "hate", "mali", "togs", "gear", "tues", "bass", "pros", "numb", "emus",
         "hare", "fate", "wife", "mean", "pink", "dune", "ares", "dine", "oily", "tony", "czar", "spay", "push", "glum",
         "till", "moth", "glue", "dive", "scad", "pops", "woks", "andy", "leah", "cusp", "hair", "alex", "vibe", "bulb",
         "boll", "firm", "joys", "tara", "cole", "levy", "owen", "chow", "rump", "jail", "lapp", "beet", "slap", "kith",
         "more", "maps", "bond", "hick", "opus", "rust", "wist", "shat", "phil", "snow", "lott", "lora", "cary", "mote",
         "rift", "oust", "klee", "goad", "pith", "heep", "lupe", "ivan", "mimi", "bald", "fuse", "cuts", "lens", "leer",
         "eyry", "know", "razz", "tare", "pals", "geek", "greg", "teen", "clef", "wags", "weal", "each", "haft", "nova",
         "waif", "rate", "katy", "yale", "dale", "leas", "axum", "quiz", "pawn", "fend", "capt", "laws", "city", "chad",
         "coal", "nail", "zaps", "sort", "loci", "less", "spur", "note", "foes", "fags", "gulp", "snap", "bogs", "wrap",
         "dane", "melt", "ease", "felt", "shea", "calm", "star", "swam", "aery", "year", "plan", "odin", "curd", "mira",
         "mops", "shit", "davy", "apes", "inky", "hues", "lome", "bits", "vila", "show", "best", "mice", "gins", "next",
         "roan", "ymir", "mars", "oman", "wild", "heal", "plus", "erin", "rave", "robe", "fast", "hutu", "aver", "jodi",
         "alms", "yams", "zero", "revs", "wean", "chic", "self", "jeep", "jobs", "waxy", "duel", "seek", "spot", "raps",
         "pimp", "adan", "slam", "tool", "morn", "futz", "ewes", "errs", "knit", "rung", "kans", "muff", "huhs", "tows",
         "lest", "meal", "azov", "gnus", "agar", "sips", "sway", "otis", "tone", "tate", "epic", "trio", "tics", "fade",
         "lear", "owns", "robt", "weds", "five", "lyon", "terr", "arno", "mama", "grey", "disk", "sept", "sire", "bart",
         "saps", "whoa", "turk", "stow", "pyle", "joni", "zinc", "negs", "task", "leif", "ribs", "malt", "nine", "bunt",
         "grin", "dona", "nope", "hams", "some", "molt", "smit", "sacs", "joan", "slav", "lady", "base", "heck", "list",
         "take", "herd", "will", "nubs", "burg", "hugs", "peru", "coif", "zoos", "nick", "idol", "levi", "grub", "roth",
         "adam", "elma", "tags", "tote", "yaws", "cali", "mete", "lula", "cubs", "prim", "luna", "jolt", "span", "pita",
         "dodo", "puss", "deer", "term", "dolt", "goon", "gary", "yarn", "aims", "just", "rena", "tine", "cyst", "meld",
         "loki", "wong", "were", "hung", "maze", "arid", "cars", "wolf", "marx", "faye", "eave", "raga", "flow", "neal",
         "lone", "anne", "cage", "tied", "tilt", "soto", "opel", "date", "buns", "dorm", "kane", "akin", "ewer", "drab",
         "thai", "jeer", "grad", "berm", "rods", "saki", "grus", "vast", "late", "lint", "mule", "risk", "labs", "snit",
         "gala", "find", "spin", "ired", "slot", "oafs", "lies", "mews", "wino", "milk", "bout", "onus", "tram", "jaws",
         "peas", "cleo", "seat", "gums", "cold", "vang", "dewy", "hood", "rush", "mack", "yuan", "odes", "boos", "jami",
         "mare", "plot", "swab", "borg", "hays", "form", "mesh", "mani", "fife", "good", "gram", "lion", "myna", "moor",
         "skin", "posh", "burr", "rime", "done", "ruts", "pays", "stem", "ting", "arty", "slag", "iron", "ayes", "stub",
         "oral", "gets", "chid", "yens", "snub", "ages", "wide", "bail", "verb", "lamb", "bomb", "army", "yoke", "gels",
         "tits", "bork", "mils", "nary", "barn", "hype", "odom", "avon", "hewn", "rios", "cams", "tact", "boss", "oleo",
         "duke", "eris", "gwen", "elms", "deon", "sims", "quit", "nest", "font", "dues", "yeas", "zeta", "bevy", "gent",
         "torn", "cups", "worm", "baum", "axon", "purr", "vise", "grew", "govs", "meat", "chef", "rest", "lame"])
    ) == 11
